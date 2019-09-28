#!/bin/bash
#SBATCH --job-name=s1_S_G15
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_S_G15.%j.out
#SBATCH --error=../output/s1_S_G15.%j.err

cd ..
python2 main.py -expID S1_syn_gauss_15 -nEpochs 20 -loadModel ../exp/S1_syn_gauss/model_15.pth -allSYN -gaussBlur

