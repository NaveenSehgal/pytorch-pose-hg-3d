#!/bin/bash
#SBATCH --job-name=s2_s_20
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_s_20.%j.out
#SBATCH --error=../output/s2_s_20.%j.err

cd ..

python2 main.py -expID s2_s_20 -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/s2_s_10/model_10.pth -nEpochs 10 -allSYN -scaleMPJPE

