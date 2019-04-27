#!/bin/bash
#SBATCH --job-name=test_h36m
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/test_h36m.%j.out
#SBATCH --error=../output/test_h36m.%j.err

cd ..
python2 main.py -expID H36M_test -ratio3D 1 -loadModel ../exp/hgreg-3d.pth -test -varWeight 0.01 -regWeight 0.01
# -ratio3D 1 
# -regWeigh 0.1 -varWeight 0.01 -loadModel ../exp/hgreg-3d.pth -LR 2.5e-5 -nEpochs 0 -test

