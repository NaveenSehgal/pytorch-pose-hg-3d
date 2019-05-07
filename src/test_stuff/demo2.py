import sys
import torch
from opts import opts
import ref
from utils.eval import getPreds
import cv2
import numpy as np
import os
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_pose3d(img, pred, reg):
  # pred (16, 2)
  # reg (16, 1)

  fig = plt.figure()
  ax = Axes3D(fig)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

  xs = pred[:, 0]
  ys = pred[:, 1]
  zs = reg

  ax.scatter(xs, ys, zs)

  # draw bones
  for edge in ref.edges:
    j1, j2 = edge[0], edge[1]
    x_start, y_start = pred[j1, :]
    z_start = reg[j1][0]
    x_end, y_end = pred[j2, :]
    z_end = reg[j2][0]

    xs = np.linspace(x_start, x_end)
    ys = np.linspace(y_start, y_end)
    zs = np.linspace(z_start, z_end)

    ax.plot3D(xs, ys, zs, 'blue')


  plt.savefig('test.png', dpi=300) 

def main():
  opt = opts().parse()
  if opt.loadModel != 'none':
    model = torch.load(opt.loadModel).cuda()
  else:
    model = torch.load('/home/sehgal.n/3d_pose/pytorch-pose-hg-3d/exp/hgreg-3d.pth').cuda()
  opt.demo = '/scratch/sehgal.n/datasets/synthetic/SYN_RR_amir_180329_0624_G20190212_1843_P2000_A00/images/image_000001.png'
  img = cv2.imread(opt.demo)
  input = torch.from_numpy(img.transpose(2, 0, 1)).float() / 256.
  input = input.view(1, input.size(0), input.size(1), input.size(2))
  input_var = torch.autograd.Variable(input).float().cuda()
  output = model(input_var)
  pred = getPreds((output[-2].data).cpu().numpy())[0] * 4
  reg = (output[-1].data).cpu().numpy().reshape(pred.shape[0], 1)

  plot_pose3d(img, pred, reg)
  #  debugger = Debugger()
  #debugger.addImg((input[0].numpy().transpose(1, 2, 0)*256).astype(np.uint8))
  #debugger.addPoint2D(pred, (255, 0, 0))
  #:wqdebugger.addPoint3D(np.concatenate([pred, (reg + 1) / 2. * 256], axis = 1))
  #debugger.showImg(pause = True)
  #debugger.show3D()

if __name__ == '__main__':
  main()
