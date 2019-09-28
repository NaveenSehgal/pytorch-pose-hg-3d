#!/bin/bash
#SBATCH --job-name=s1_MP_W30
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_M_W30.%j.out
#SBATCH --error=../output/s1_M_W30.%j.err

cd ..
python2 main.py -expID S1_mpii_wn_30 -nEpochs 15 -loadModel ../exp/S1_mpii_wn_15/model_15.pth -useSyn -whiteNoise

