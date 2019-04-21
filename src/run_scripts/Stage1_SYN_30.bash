#!/bin/bash
#SBATCH --job-name=s1_syn_30
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_syn_30.%j.out
#SBATCH --error=../output/s1_syn_30.%j.err

cd ..
python2 main.py -expID Stage1_SYN_30 -nEpochs 30 -useSyn -loadModel ../exp/Stage1_SYN/model_30.pth

