#!/bin/bash
#SBATCH --job-name=s3_syn
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s3_syn.%j.out
#SBATCH --error=../output/s3_syn.%j.err

cd ..
python2 main.py -expID Stage3_SYN_0 -ratio3D 1 -regWeigh 0.1 -varWeight 0.01 -loadModel ../exp/Stage2_SYN_20/model_10.pth -LR 2.5e-5 -nEpochs 10
