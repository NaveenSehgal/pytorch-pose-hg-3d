import sys
from tqdm import tqdm
import h5py
import numpy as np

sys.path.append('/home/sehgal.n/3d_pose/pytorch-pose-hg-3d/src')
import ref

# Joint names
JOINTS = {
    0: 'right ankle',
    1: 'right knee',
    2: 'right hip', 
    3: 'left hip',
    4: 'left knee',
    5: 'left ankle',
    6: 'pelvis',
    7: 'thorax',
    8: 'upper neck',
    9: 'head',
    10: 'right wrist',
    11: 'right elbow',
    12: 'right shoulder',
    13: 'left shoulder',
    14: 'left elbow',
    15: 'left wrist'
}
 
LSHOULDER = 13
RHIP = 2


def get_torso_lengths(dataset):
    torsos = []

    for i, pose in tqdm(enumerate(dataset)):
        pts = dataset[i, :, :]
        torso_length = np.linalg.norm(pts[LSHOULDER] - pts[RHIP])
        torsos.append(torso_length)

    return torsos


def get_bone_lengths(dataset):
    bones = []

    for i, pose in tqdm(enumerate(dataset)):
        pts = dataset[i, :, :]
        pose = []
        for j1, j2 in ref.edges:
            bone_length = np.linalg.norm(pts[j1] - pts[j2])
            pose.append(bone_length)

        bones.append(pose)

    bones = np.array(bones)

    # print stats
    for i, edge in enumerate(ref.edges):
        print('{} - {}: {}'.format(JOINTS[edge[0]], JOINTS[edge[1]], round(bones.mean(axis=0)[i], 3)))

    return bones


f_syn = h5py.File('synthetic/synthetic_annot.h5')
f_h36m = h5py.File('h36m/annotSampleTest.h5', 'r')

jh = f_h36m['joint_3d_mono'].value
js = f_syn['joint_3d_mono'].value

bh = get_bone_lengths(jh)
print('\n\n')
bs = get_bone_lengths(js)

th = get_torso_lengths(jh)
ts = get_torso_lengths(js)
ratio = np.mean(ts) / np.mean(th)
print ('H36M to SYN: ', ratio)
print('SYN to H36M; ', 1/ratio)
