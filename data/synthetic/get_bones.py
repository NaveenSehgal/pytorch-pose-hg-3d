import sys
sys.path.append('/home/sehgal.n/3d_pose/pytorch-pose-hg-3d/src')
import ref
import h5py
import numpy as np
from tqdm import tqdm

def get_bone_length(pts):
    sum_bone_length = 0
    for e in ref.edges:
        sum_bone_length += ((pts[e[0]] -  pts[e[1]]) ** 2).sum() ** 0.5

    return sum_bone_length

data_file = '/home/sehgal.n/3d_pose/pytorch-pose-hg-3d/data/synthetic/synthetic_annot.h5'
f = h5py.File(data_file, 'r')
joints2d = f['joint_2d']
joints3d = f['joint_3d_mono'].value # (n, 16, 3)

joints3d *= 845.049574860222
ret = []
sum_bones = 0

for i, pose in tqdm(enumerate(joints3d)):
    sum_bones += get_bone_length(joints3d[i, :, :]) 
    ret.append(i)

print('Sum_bone_length', sum_bones / len(ret))

