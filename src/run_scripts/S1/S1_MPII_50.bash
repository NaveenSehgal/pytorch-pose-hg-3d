#!/bin/bash
#SBATCH --job-name=s1_MP50
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_MP50.%j.out
#SBATCH --error=../output/s1_MP50.%j.err

cd ..
python2 main.py -expID S1_mpii_50 -nEpochs 10 -loadModel ../exp/S1_mpii_20/model_30.pth -useSyn

