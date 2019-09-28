#!/bin/bash
#SBATCH --job-name=s2_s
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_s.%j.out
#SBATCH --error=../output/s2_s.%j.err

cd ..

python2 main.py -expID s2_s -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/S1_syn_50/model_10.pth -nEpochs 10 -allSYN -scaleMPJPE

