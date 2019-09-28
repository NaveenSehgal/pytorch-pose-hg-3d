#!/bin/bash
#SBATCH --job-name=s2_syn
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_syn.%j.out
#SBATCH --error=../output/s2_syn.%j.err

cd ..
python2 main.py -expID Stage2_s -ratio3D 1 -regWeight 0.1 -loadModel ../exp/S1_syn_50/model_10.pth -nEpochs 10 -allSYN 

