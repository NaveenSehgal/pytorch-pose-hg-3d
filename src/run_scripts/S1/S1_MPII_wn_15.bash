#!/bin/bash
#SBATCH --job-name=s1_MP_W15
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_MP_W15.%j.out
#SBATCH --error=../output/s1_MP_W15.%j.err

cd ..
python2 main.py -expID S1_mpii_wn_15 -nEpochs 15 -loadModel ../exp/S1_mpii_wn/model_15.pth -useSyn -whiteNoise
