#!/bin/bash
#SBATCH --job-name=s1_MP_G20
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_MP_G20.%j.out
#SBATCH --error=../output/s1_MP_G20.%j.err

cd ..
python2 main.py -expID S1_mpii_gauss_20 -nEpochs 30 -loadModel ../exp/S1_mpii_gauss/model_20.pth -useSyn -gaussBlur

