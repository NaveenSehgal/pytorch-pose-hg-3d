import torch.utils.data as data
import numpy as np
import ref
import torch
from h5py import File
import cv2
from utils.utils import Rnd, Flip, ShuffleLR
from utils.img import Crop, DrawGaussian, Transform
from utils.noise import gaussian_blur, white_noise
import os

class Syn2D(data.Dataset):
  def __init__(self, opt, split, returnMeta = False):
    print '==> initializing 2D SYN {} data.'.format(split)

    # Load annotations
    annot = {}
    tags = ['folder_name', 'id', 'image_name', 'istrain', 'part']
    f = File('../data/syn2D/annot.h5')

    for tag in tags:
      annot[tag] = np.asarray(f[tag]).copy()
    
    self.folder = f.attrs['synthetic_folder'].decode('utf-8')
    f.close()

    # Choose only samples for the split (train or test)
    in_split = np.ravel(annot['istrain'] == (1 if split == 'train' else 0))
    ids = np.arange(annot['id'].shape[0])[in_split]
    for tag in tags:
        annot[tag] = annot[tag][ids]

    print 'Loaded SYN2D {} {} samples'.format(split, len(annot['part']))
    
    self.split = split
    self.opt = opt
    self.annot = annot
    self.returnMeta = returnMeta
  
  def LoadImage(self, index):
    sub_folder = self.annot['folder_name'][index][0].decode('utf-8') 
    image_name = self.annot['image_name'][index][0].decode('utf-8')
    image_path = os.path.join(os.path.join(os.path.join(self.folder, sub_folder), 'images'), image_name)
    img = cv2.imread(image_path)

    # Preprocessing 
    if self.opt.gaussBlur:
        img = gaussian_blur(img)
    elif self.opt.whiteNoise:
        img = white_noise(img)

    return img
  
  def GetPartInfo(self, index):
    pts = self.annot['part'][index].copy()
    c = np.ones(2) * ref.h36mImgSize / 2
    s = ref.h36mImgSize * 1.0
    return pts, c, s
      
  def __getitem__(self, index):
    img = self.LoadImage(index)
    pts, c, s = self.GetPartInfo(index)
    r = 0
    
    if self.split == 'train':
      s = s * (2 ** Rnd(ref.scale))
      r = 0 if np.random.random() < 0.6 else Rnd(ref.rotate)
    inp = Crop(img, c, s, r, ref.inputRes) / 256.
    out = np.zeros((ref.nJoints, ref.outputRes, ref.outputRes))
    Reg = np.zeros((ref.nJoints, 3))
    for i in range(ref.nJoints):
      if pts[i][0] > 1:
        pt = Transform(pts[i], c, s, r, ref.outputRes)
        out[i] = DrawGaussian(out[i], pt, ref.hmGauss) 
        Reg[i, :2] = pt
        Reg[i, 2] = 1
    if self.split == 'train':
      if np.random.random() < 0.5:
        inp = Flip(inp)
        out = ShuffleLR(Flip(out))
        Reg[:, 1] = Reg[:, 1] * -1
        Reg = ShuffleLR(Reg)
      #print 'before', inp[0].max(), inp[0].mean()
      inp[0] = np.clip(inp[0] * (np.random.random() * (0.4) + 0.6), 0, 1)
      inp[1] = np.clip(inp[1] * (np.random.random() * (0.4) + 0.6), 0, 1)
      inp[2] = np.clip(inp[2] * (np.random.random() * (0.4) + 0.6), 0, 1)
      #print 'after', inp[0].max(), inp[0].mean()
      
    inp = torch.from_numpy(inp)
    if self.returnMeta:
      return inp, out, Reg, np.zeros((ref.nJoints, 3))
    else:
      return inp, out
    
  def __len__(self):
    return len(self.annot['part'])

