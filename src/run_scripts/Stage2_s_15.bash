#!/bin/bash
#SBATCH --job-name=s2_s_15
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_s_15.%j.out
#SBATCH --error=../output/s2_s_15.%j.err

cd ..
python2 main.py -expID Stage2_s_10 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage2_s/model_10.pth -nEpochs 15 -allSYN

