import sys
import h5py
import numpy as np
import torch
import torch.utils.data
from train import train, val
import ref
from datasets.syn import Synthetic
from opts import opts


def estimate_mpjpe(model_path):
    model = torch.load(model_path).cuda()
    val_loader = torch.utils.data.DataLoader(Synthetic(opt, 'val'), batch_size=1, shuffle=False,
                                             num_workers=int(ref.nThreads))
    criterion = torch.nn.MSELoss().cuda()
    # loss_val, acc_val, mpjpe_val, loss3d_val = val(0, opt, val_loader, model, criterion)

    dataset = Synthetic(opt, 'val')
    sample = dataset.__getitem__(0)
    inp, outMap, outReg, pts_3d_mono = sample

    import pdb; pdb.set_trace()


''' Constants / Configurations '''
N_SAMPLES = 100  # Number of SYN samples to use for estimating MPJPE
stage2_model_path = '../exp/Stage2_SYN_10/model_10.pth'
stage3_model_path = '../exp/Stage3_SYN_0/model_10.pth'


''' Initialize models '''
opt = opts().parse()

''' Run '''
estimate_mpjpe(stage3_model_path)
