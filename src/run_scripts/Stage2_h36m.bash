#!/bin/bash
#SBATCH --job-name=s2_H36M
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_H36M.%j.out
#SBATCH --error=../output/s2_H36M.%j.err

cd ..
python2 main.py -expID Stage2_H36M_0 -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/Stage1/model_60.pth -nEpochs 10 

