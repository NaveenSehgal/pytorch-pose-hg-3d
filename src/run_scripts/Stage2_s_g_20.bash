#!/bin/bash
#SBATCH --job-name=s2_sg_20
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_sg_20.%j.out
#SBATCH --error=../output/s2_sg_20.%j.err

cd ..

python2 main.py -expID Stage2_s_g_20 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage2_s_g_10/model_10.pth -nEpochs 10 -allSYN -scaleMPJPE -gaussBlur -dropLR 5

