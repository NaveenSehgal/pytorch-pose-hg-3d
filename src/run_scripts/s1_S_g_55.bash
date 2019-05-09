#!/bin/bash
#SBATCH --job-name=s1_S_G55
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_S_G55.%j.out
#SBATCH --error=../output/s1_S_G55.%j.err

cd ..
python2 main.py -expID S1_syn_gauss_55 -nEpochs 20 -loadModel ../exp/S1_syn_gauss_35/model_20.pth -allSYN -gaussBlur

