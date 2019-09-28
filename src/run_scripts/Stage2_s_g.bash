#!/bin/bash
#SBATCH --job-name=s2_s_g
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_s_g.%j.out
#SBATCH --error=../output/s2_s_g.%j.err

cd ..

python2 main.py -expID Stage2_s_g -ratio3D 1 -regWeight 0.1 -loadModel ../exp/S1_syn_gauss_55/model_5.pth -nEpochs 10 -allSYN -scaleMPJPE -gaussBlur

