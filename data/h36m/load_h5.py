import h5py
import numpy as np

f = h5py.File('annotSampleTest.h5', 'r')
joints2d = f['joint_2d']
joints3d = f['joint_3d_mono'] # (n, 16, 3)

A = joints2d[0, 0, :]
B = joints3d[0, 0, :]
