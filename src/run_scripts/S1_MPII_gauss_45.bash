#!/bin/bash
#SBATCH --job-name=s1_MP_G45
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_MP_G45.%j.out
#SBATCH --error=../output/s1_MP_G45.%j.err

cd ..
python2 main.py -expID S1_mpii_gauss_45 -nEpochs 15 -loadModel ../exp/S1_mpii_gauss_20/model_25.pth -useSyn -gaussBlur

