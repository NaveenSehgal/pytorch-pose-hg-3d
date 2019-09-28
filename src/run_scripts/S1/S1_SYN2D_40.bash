#!/bin/bash
#SBATCH --job-name=s1_S_40
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_S_40.%j.out
#SBATCH --error=../output/s1_S_40.%j.err

cd ..
python2 main.py -expID S1_syn_40 -loadModel ../exp/S1_syn_15/model_25.pth -nEpochs 10 -allSYN 

