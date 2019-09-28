#!/bin/bash
#SBATCH --job-name=s3_s
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s3_s.%j.out
#SBATCH --error=../output/s3_s.%j.err

cd ..
python2 main.py -expID s3_s -ratio3D 1 -regWeight 0.1 -varWeight 0.01 -loadModel ../exp/s2_s_20/model_10.pth -LR 2.5e-5 -nEpochs 10 -allSYN -scaleMPJPE

