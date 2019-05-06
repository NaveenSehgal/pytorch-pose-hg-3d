import sys
import h5py
import numpy as np
import torch
import torch.utils.data

sys.path.append('/home/sehgal.n/3d_pose/pytorch-pose-hg-3d/src')
import ref
from datasets.syn import Synthetic
from opts import opts


''' Initialize models '''
opt = opts().parse()


# Run bad (beginning of stage 2 model) on N random SYN samples and print MPJPE



# Run finished model (after Stage 3) on N random SYN samples and print MPJPE
