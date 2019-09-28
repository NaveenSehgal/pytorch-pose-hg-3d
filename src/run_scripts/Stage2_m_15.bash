#!/bin/bash
#SBATCH --job-name=s2_m_15
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_m_15.%j.out
#SBATCH --error=../output/s2_m_15.%j.err

cd ..

python2 main.py -expID Stage2_m_15 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage2_m/model_15.pth -nEpochs 15 -useSyn -dropLR 10

# python2 main.py -expID s2_m_15 -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/S1_mpii_50/model_10.pth -nEpochs 10 -useSyn
# python main.py -expID Stage2 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/Stage1/model_60.pth -nEpochs 30 -dropLR 25