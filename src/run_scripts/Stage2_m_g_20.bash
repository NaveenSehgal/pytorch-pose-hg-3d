#!/bin/bash
#SBATCH --job-name=s2_mg_20
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_mg_20.%j.out
#SBATCH --error=../output/s2_mg_20.%j.err

cd ..

python2 main.py -expID Stage2_m_g_20 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage2_m_g_15/model_5.pth -nEpochs 10 -useSyn -gaussBlur -dropLR 5

