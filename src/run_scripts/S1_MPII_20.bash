#!/bin/bash
#SBATCH --job-name=s1_MP20
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_MP20.%j.out
#SBATCH --error=../output/s1_MP20.%j.err

cd ..
python2 main.py -expID S1_mpii_20 -nEpochs 30 -loadModel ../exp/S1_mpii/model_20.pth -useSyn

