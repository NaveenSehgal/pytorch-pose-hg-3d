#!/bin/bash
#SBATCH --job-name=s1_S_G35
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_S_G35.%j.out
#SBATCH --error=../output/s1_S_G35.%j.err

cd ..
python2 main.py -expID S1_syn_gauss_35 -nEpochs 20 -loadModel ../exp/S1_syn_gauss_15/model_20.pth -allSYN -gaussBlur

