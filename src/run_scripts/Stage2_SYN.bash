#!/bin/bash
#SBATCH --job-name=s2_syn
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_syn.%j.out
#SBATCH --error=../output/s2_syn.%j.err

cd ..
python2 main.py -expID Stage2_SYN -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/Stage1_SYN_30/model_30.pth -nEpochs 10 -useSyn

