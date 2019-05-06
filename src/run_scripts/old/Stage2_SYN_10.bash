#!/bin/bash
#SBATCH --job-name=s2_syn
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_syn.%j.out
#SBATCH --error=../output/s2_syn.%j.err

cd ..
python2 main.py -expID Stage2_SYN_10 -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/Stage2_SYN/model_10.pth -nEpochs 10 -useSyn

