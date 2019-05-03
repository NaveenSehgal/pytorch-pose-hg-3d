import sys
sys.path.append('/home/sehgal.n/3d_pose/pytorch-pose-hg-3d/src')
import ref
from tqdm import tqdm
import h5py
import numpy as np

'''
joint id (0 - r ankle, 1 - r knee, 2 - r hip, 3 - l hip, 4 - l knee, 5 - l ankle, 6 - pelvis, 7 - thorax, 8 - upper neck, 9 - head top, 10 - r wrist, 11 - r elbow, 12 - r shoulder, 13 - l shoulder, 14 - l elbow, 15 - l wrist)
'''
 
LSHOULDER = 13
RHIP = 2

f_syn = h5py.File('synthetic/synthetic_annot.h5')
f_h36m = h5py.File('h36m/annotSampleTest.h5', 'r')

jh = f_h36m['joint_3d_mono'].value
js = f_syn['joint_3d_mono'].value

def get_torso_lengths(dataset):
    torsos = []

    for i, pose in tqdm(enumerate(dataset)):
        pts = dataset[i, :, :]
        torso_length = np.linalg.norm(pts[LSHOULDER] - pts[RHIP]) 
        torsos.append(torso_length)

    return torsos

th = get_torso_lengths(jh)
ts = get_torso_lengths(js)
ratio = np.mean(ts) / np.mean(th)
print ('H36M to SYN: ', ratio)
print('SYN to H36M; ', 1/ratio)

