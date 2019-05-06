#!/bin/bash
#SBATCH --job-name=s2B0
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2B0.%j.out
#SBATCH --error=../output/s2B0.%j.err

cd ..
python2 main.py -expID Stage2_SYN_bone -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/Stage1_SYN_30/model_30.pth -nEpochs 10 -useSyn -nosynsum -mm

