#!/bin/bash
#SBATCH --job-name=s2_m_g_15
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_m_g_15.%j.out
#SBATCH --error=../output/s2_m_g_15.%j.err

cd ..

python2 main.py -expID Stage2_m_g_15 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage2_m_g/model_15.pth -nEpochs 15 -useSyn -gaussBlur -dropLR 10

