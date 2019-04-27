#!/bin/bash
#SBATCH --job-name=test_syn
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/test_syn.%j.out
#SBATCH --error=../output/test_syn.%j.err

cd ..
python2 main.py -expID SYN_test -loadModel ../exp/hgreg-3d.pth -test -useSyn -ratio3D 1  -nosynsum
# -ratio3D 1 
# -regWeigh 0.1 -varWeight 0.01 -loadModel ../exp/hgreg-3d.pth -LR 2.5e-5 -nEpochs 0 -test

