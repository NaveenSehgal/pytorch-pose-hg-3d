#!/bin/bash
#SBATCH --job-name=s2_m_10
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_m_10.%j.out
#SBATCH --error=../output/s2_m_10.%j.err

cd ..

python2 main.py -expID Stage2_m_10 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage2_m/model_10.pth -nEpochs 10 -useSyn

# python2 main.py -expID s2_m_10 -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/S1_mpii_50/model_10.pth -nEpochs 10 -useSyn
# python main.py -expID Stage2 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage1/model_60.pth -nEpochs 30 -dropLR 25
