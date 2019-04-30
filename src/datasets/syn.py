import torch.utils.data as data
import numpy as np
import ref
import torch
from h5py import File
import cv2
from utils.utils import Rnd, Flip, ShuffleLR
from utils.img import Crop, DrawGaussian, Transform3D
import os


class Synthetic(data.Dataset):
    def __init__(self, opt, split):
        print '==> Initializing 3D synthetic {} data'.format(split)
        annot = {}
        f =	File('../data/synthetic/synthetic_annot.h5')
        tags = ['folder_name', 'id', 'image_name', 'istrain', 'joint_2d', 'joint_3d_mono']
        for tag in tags:
            annot[tag] = np.asarray(f[tag]).copy()

        self.folder = f.attrs['synthetic_folder'].decode('utf-8')
        f.close()
                
        num_pictures = len(annot['joint_2d'])
        self.split = split
        self.opt = opt
        self.annot = annot
        self.nSamples = len(self.annot['id'])      
        self.root = 7  # double check!
        self.nJoints = 16
        print 'Loaded 3D {} {} samples'.format(split, len(self.annot['id']))


    def LoadImage(self, index):
        sub_folder = self.annot['folder_name'][index][0].decode('utf-8') 
        image_name = self.annot['image_name'][index][0].decode('utf-8')
        image_path = os.path.join(os.path.join(os.path.join(self.folder, sub_folder), 'images'), image_name)
        #print image_path
        img = cv2.imread(image_path)  # TBD if need to resize images
        return img

    def GetPartInfo(self, index):
        pts = self.annot['joint_2d'][index].copy()
        pts_3d = self.annot['joint_3d_mono'][index].copy()
        
        if self.opt.mm:
            pts_3d = pts_3d * 1000

        pts_3d_mono = self.annot['joint_3d_mono'][index].copy()
        c = np.ones(2) * ref.synImgSize / 2
        s = ref.synImgSize * 1.0

        pts_3d = pts_3d - pts_3d[self.root]

        # Normalize 
        s2d, s3d = 0, 0
        for e in ref.edges:
            s2d += ((pts[e[0]] - pts[e[1]]) ** 2).sum() ** 0.5
            s3d += ((pts_3d[e[0], :2] - pts_3d[e[1], :2]) ** 2).sum() ** 0.5
        scale = s2d / s3d

        for j in range(self.nJoints):
            pts_3d[j, 0] = pts_3d[j, 0] * scale + pts[self.root, 0]
            pts_3d[j, 1] = pts_3d[j, 1] * scale + pts[self.root, 1]
            pts_3d[j, 2] = pts_3d[j, 2] * scale + ref.synImgSize / 2
    
        return pts, c, s, pts_3d, pts_3d_mono            

    def __getitem__(self, index):
        if self.split == 'train':
            index = np.random.randint(self.nSamples)

        img = self.LoadImage(index)
        pts, c, s, pts_3d, pts_3d_mono = self.GetPartInfo(index)
        pts_3d[7] = (pts_3d[12] + pts_3d[13]) / 2  # neck = average of shoulders

        inp = Crop(img, c, s, 0, ref.inputRes) / 256.  # crop image to input resolution
        outMap = np.zeros((ref.nJoints, ref.outputRes, ref.outputRes))  # nJoints x 64 x 64 heatmap for 2D
        outReg = np.zeros((ref.nJoints, 3))  # Regression target for 3D

        for i in range(ref.nJoints):
            pt = Transform3D(pts_3d[i], c, s, 0, ref.outputRes)
            if pts[i][0] > 1:
                outMap[i] = DrawGaussian(outMap[i], pt[:2], ref.hmGauss)  # Draw 2D heat map for detection

            outReg[i, 2] = pt[2] / ref.outputRes * 2 - 1

        inp = torch.from_numpy(inp)
        return inp, outMap, outReg, pts_3d_mono

    def __len__(self):
        return self.nSamples
