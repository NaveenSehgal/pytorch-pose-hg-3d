import torch.utils.data as data
import numpy as np
import ref
import torch
from h5py import File
import cv2
from utils.utils import Rnd, Flip, ShuffleLR
from utils.img import Crop, DrawGaussian, Transform3D

class Synthetic(data.Dataset):
    def __init__(self, opt, split):
        print ('==> Initializing 3D synthetic {} data'.format(split))
        annot = {}
        f =	File('../data/synthetic/synthetic_annot.h5')
        for tag in tags:
            annot[tag] = np.asarray(f[tag]).copy()
        f.close()
                
        self.split = split
        self.opt = opt
        self.annot = annot
        self.nSamples = len(self.annot['id'])      

