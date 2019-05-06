#!/bin/bash
#SBATCH --job-name=stage1_syn
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/stage1_syn.%j.out
#SBATCH --error=../output/stage1_syn.%j.err

cd ..
python2 main.py -expID Stage1_SYN -nEpochs 30 -useSyn 

