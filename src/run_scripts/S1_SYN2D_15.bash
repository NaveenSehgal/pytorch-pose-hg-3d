#!/bin/bash
#SBATCH --job-name=s1_S_15
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_S_15.%j.out
#SBATCH --error=../output/s1_S_15.%j.err

cd ..
python2 main.py -expID S1_syn_15 -loadModel ../exp/S1_syn/model_15.pth -nEpochs 30 -allSYN 

