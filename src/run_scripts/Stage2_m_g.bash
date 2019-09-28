#!/bin/bash
#SBATCH --job-name=s2_m_g
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_m_g.%j.out
#SBATCH --error=../output/s2_m_g.%j.err

cd ..

python2 main.py -expID Stage2_m_g -ratio3D 1 -regWeight 0.1 -loadModel ../exp/S1_mpii_gauss_45/model_15.pth -nEpochs 15 -useSyn -gaussBlur

