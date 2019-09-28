#!/bin/bash
#SBATCH --job-name=s2_m_wn
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_m_wn.%j.out
#SBATCH --error=../output/s2_m_wn.%j.err

cd ..

python2 main.py -expID s2_m_wn -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/S1_mpii_wn_45/model_15.pth -nEpochs 10 -useSyn -whiteNoise -scaleMPJPE
