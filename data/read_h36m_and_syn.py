import h5py
import numpy as np
 
f_syn = h5py.File('synthetic/synthetic_annot.h5')
f_h36m = h5py.File('h36m/annotSampleTest.h5', 'r')

jh = f_h36m['joint_3d_mono'].value
js = f_syn['joint_3d_mono'].value

