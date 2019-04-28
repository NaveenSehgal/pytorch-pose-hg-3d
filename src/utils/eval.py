import numpy as np
import ref

def getPreds(hm):
  assert len(hm.shape) == 4, 'Input must be a 4-D tensor'
  res = hm.shape[2]
  hm = hm.reshape(hm.shape[0], hm.shape[1], hm.shape[2] * hm.shape[3])
  idx = np.argmax(hm, axis = 2)
  preds = np.zeros((hm.shape[0], hm.shape[1], 2))
  for i in range(hm.shape[0]):
    for j in range(hm.shape[1]):
      preds[i, j, 0], preds[i, j, 1] = idx[i, j] % res, idx[i, j] / res
  
  return preds

def calcDists(preds, gt, normalize):
  dists = np.zeros((preds.shape[1], preds.shape[0]))
  for i in range(preds.shape[0]):
    for j in range(preds.shape[1]):
      if gt[i, j, 0] > 0 and gt[i, j, 1] > 0:
        dists[j][i] = ((gt[i][j] - preds[i][j]) ** 2).sum() ** 0.5 / normalize[i]
      else:
        dists[j][i] = -1
  return dists

def distAccuracy(dist, thr = 0.5):
  dist = dist[dist != -1]
  if len(dist) > 0:
    return 1.0 * (dist < thr).sum() / len(dist)
  else:
    return -1

def Accuracy(output, target):
  preds = getPreds(output)
  gt = getPreds(target)
  dists = calcDists(preds, gt, np.ones(preds.shape[0]) * ref.outputRes / 10)
  acc = np.zeros(len(ref.accIdxs))
  avgAcc = 0
  badIdxCount = 0
  
  for i in range(len(ref.accIdxs)):
    acc[i] = distAccuracy(dists[ref.accIdxs[i]])
    if acc[i] >= 0:
      avgAcc = avgAcc + acc[i]
    else:
      badIdxCount = badIdxCount + 1
  
  if badIdxCount == len(ref.accIdxs):
    return 0
  else:
    return avgAcc / (len(ref.accIdxs) - badIdxCount)

def MPJPE(output2D, output3D, meta, opt):
  '''
  Params
  ------
  output2D: np.ndarray (batch_size, n_joints, output_res, output_res)  (6x16x64x64)
	2D output heatmap

  output3D: np.ndarray (batch_size, n_joints) (6x16)
	3D predictions

  opt: argparse.Namespace 
  meta: torch.DoubleTensor (batch_size, n_joints, 3) (6x16x3)
  '''

  meta = meta.numpy()
  p = np.zeros((output2D.shape[0], ref.nJoints, 3))  # (batch_size, n_joints, 3)

  # Get predictions from the heatmap
  p[:, :, :2] = getPreds(output2D).copy()  # getPreds(output2D) returns (batch_size, n_joints, 2)
  
  # Heatmap is shape (batch_size, n_joints, output_res, output_res)
  hm = output2D.reshape(output2D.shape[0], output2D.shape[1], ref.outputRes, ref.outputRes)
  
  # Loop through each sample in the batch
  for i in range(hm.shape[0]):

  	# Loop through each joint
    for j in range(hm.shape[1]):

      # Get the x, y prediction for the specific sample and joint
      pX, pY = int(p[i, j, 0]), int(p[i, j, 1])
      scores = hm[i, j, pX, pY]  # heat map score for that prediction

      # If the pX and pY are valid (not at the edge of the image)
      if pX > 0 and pX < ref.outputRes - 1 and pY > 0 and pY < ref.outputRes - 1:
      	# Get the difference of the heatmap between 1+ and 1- the predictionp oint
        diffY = hm[i, j, pX, pY + 1] - hm[i, j, pX, pY - 1]
        diffX = hm[i, j, pX + 1, pY] - hm[i, j, pX - 1, pY]

        # Add or subtract 0.25 to the prediction coordinates depending on the sign 
        # of the derivative in that direction.  
        # If diff >= 0 (the heatmap is increasing from right to left), then add 0.25
        p[i, j, 0] = p[i, j, 0] + 0.25 * (1 if diffX >=0 else -1)
        p[i, j, 1] = p[i, j, 1] + 0.25 * (1 if diffY >=0 else -1)

  p = p + 0.5  # Why add 0.5 to the pixel positions? 
  # Scale the depth coordinate to be half the depth multiplied by the outputRes (64)
  p[:, :, 2] = (output3D.copy() + 1) / 2 * ref.outputRes

  # Average sum of bone lengths for a person in the dataset
  h36mSumLen = 4296.99233013
  synSumLen = 4.140971735214678

  # Flags for testing out this function 
  if opt.nosynsum:
    synSumLen = h36mSumLen
  if opt.mm:
    #h36mSumLen *= 1000
    synSumLen *= 1000
  
  # Initialize index of root joint, and err, num3D to 0
  root = 6
  err = 0  # Contain sum of mpjpe errors 
  num3D = 0  # Number of 3D samples 
  
  # For each sample in the batch
  for i in range(p.shape[0]):  
    s = meta[i].sum()  # Sum of all coordinates in the pose
    
    # Check if the sum of coordinates is outside some range 
    if not (s > - ref.eps and s < ref.eps):
   	  # if so, consider it a valid 3D sample
      num3D += 1
      lenPred = 0  # Length of the predicted bones
      
      # For each edge
      for e in ref.edges:
      	# Calculate the sqrt ( sum ( bone_edge_length ^ ^2 ) ) 
        lenPred += ((p[i, e[0]] - p[i, e[1]]) ** 2).sum() ** 0.5 
      
      pRoot = p[i, root].copy()  # Prediction for the root bone
      
      # For each joint
      for j in range(ref.nJoints):
      	'''
		1. Subtract predicted coordinates of that joint by the predicted root coords
			to get relative location 
		2. Divide the above number by lenPred, which is the square root of the sum of square
			bone lengths of the person
		3. Multiply by the average sum of bone lengths for a person
		4. Add the ground truth joint location 
      	'''
      	if opt.useSyn == True:
            p[i, j] = (p[i, j] - pRoot) / lenPred * synSumLen + meta[i, root]
        else:
            p[i, j] = (p[i, j] - pRoot) / lenPred * h36mSumLen + meta[i, root]
      
      p[i, 7] = (p[i, 6] + p[i, 8]) / 2  # TODO: neck is average of shoulders?
      
      # For each joint
      for j in range(ref.nJoints):
      	# Calculate the sqrt. of the sum of squared distances
        dis = ((p[i, j] - meta[i, j]) ** 2).sum() ** 0.5

        # Add the average error per joint to the err variable
        err += dis / ref.nJoints

  if num3D > 0:
    return err / num3D, num3D  # Return the average error per joint, and the number of 3D samples
  else:
    return 0, 0
