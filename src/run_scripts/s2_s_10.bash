#!/bin/bash
#SBATCH --job-name=s2_s_10
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_s_10.%j.out
#SBATCH --error=../output/s2_s_10.%j.err

cd ..

python2 main.py -expID s2_s_10 -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/s2_s/model_10.pth -nEpochs 10 -allSYN -scaleMPJPE

