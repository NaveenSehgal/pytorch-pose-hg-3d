'''
Takes in path of synthetic data folder and converts labels to h5 file

structure your data as follows:

SYNTHETIC_FOLDER:
    -> SYN_RR_amir_....
    -> SYN_RR_naveen_...
        -> images
        -> joints_gt.mat
        -> joints_gt3d.mat
        ... 
    ..
    ..
    ..
    -> SYN_RR_sarah_...

This file will then output the h5 file to datasets/synthetic.
This file is analogous to GetH36M.py
'''

import numpy as np
import h5py
import os
import scipy.io as sio

def convert(syn_joints):
    ''' input format 14 x 2 '''
    mpii_shape = list(syn_joints.shape)
    if syn_joints.shape[0] != 14:
        print('INCORRECT INPUT SHAPE INTO CONVERSION FUNCTION FROM SYN TO MPII')
        exit(0)

    mpii_shape[0] = 16
    mpii = np.zeros(mpii_shape)
    mpii[[0,1,2,3,4,5,7, 9, 10, 11,12,13,14, 15]] = syn_joints[[0,1,2,3,4,5, 12, 13, 6, 7, 8, 9, 10, 11]]
    mpii[6] = np.mean(syn_joints[2:4, :], axis=0)
    mpii[8] = syn_joints[12] + (syn_joints[13] - syn_joints[12]) / 3

    return mpii
 

SYNTHETIC_FOLDER = '/scratch/sehgal.n/datasets/synthetic'
SAVE_PATH = '../../data/synthetic/'
sub_folders = [os.path.join(SYNTHETIC_FOLDER, folder) for folder in os.listdir(SYNTHETIC_FOLDER) if os.path.isdir(os.path.join(SYNTHETIC_FOLDER, folder))]
FRAC_TRAIN = 0.8  # Make this proportion of samples designated for training

print('Loading the following folders: ')
for fold in sub_folders:
    print(fold)

n_images = 0
joints2d, joints3d, image_names, folder_names = np.array([]), np.array([]), np.array([]), np.array([])  # initialize empty arrays
istrain = np.array([])
ids = np.array([]) 
i = 0
for folder in sub_folders:
    folder_path = os.path.join(SYNTHETIC_FOLDER, folder)
    j2d_file, j3d_file, image_dir = [os.path.join(folder_path, x) for x in ['joints_gt.mat', 'joints_gt3d.mat', 'images']]
    j2d = np.array([convert(x) for x in np.swapaxes(sio.loadmat(j2d_file)['joints_gt'], 2, 0)])
    j3d = np.array([convert(x) for x in np.swapaxes(sio.loadmat(j3d_file)['joints_gt3d'], 2, 0)])

    im_names = os.listdir(image_dir)
    im_names.sort()  # Make sure going in increasing order
    im_names = np.reshape(im_names, (len(im_names), 1))
    fold_name = np.reshape([folder,] * len(im_names), (len(im_names), 1))
    
    if ids.size == 0:
        max_ids = 0
    max_ids = [-1 if ids.size == 0 else max(ids)][0]
    start_id = max_ids + 1
    stop_id = start_id + len(j2d)
    id_list = np.arange(start_id, stop_id)
    ids = np.append(ids, id_list)
    is_train_0 = np.reshape((np.random.rand(len(j2d)) < FRAC_TRAIN).astype(int), (len(j2d), 1))
    istrain = [np.vstack((istrain, is_train_0)) if istrain.size != 0 else is_train_0][0]

    # Append to grand list
    joints2d = [np.vstack((joints2d, j2d)) if joints2d.size != 0 else j2d][0]
    joints3d = [np.vstack((joints3d, j3d)) if joints3d.size != 0 else j3d][0]   
    image_names = [np.vstack((image_names, im_names)) if image_names.size != 0 else im_names][0]
    folder_names = [np.vstack((folder_names, fold_name)) if folder_names.size != 0 else fold_name][0]

# Correct encoding for string arrays
image_names = np.chararray.encode(image_names, encoding='utf8')
folder_names = np.chararray.encode(folder_names, encoding='utf8')

# Store to h5
h5name = os.path.join(SAVE_PATH, 'synthetic_annot.h5')
f = h5py.File(h5name, 'w')
f['joint_2d'] = joints2d
f['joint_3d_mono'] = joints3d
f['image_name'] = image_names
f['folder_name'] = folder_names
f['id'] = ids
f['istrain'] = istrain
f.attrs['synthetic_folder'] = np.string_(SYNTHETIC_FOLDER)
f.close()

