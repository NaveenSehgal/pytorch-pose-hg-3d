#!/bin/bash
#SBATCH --job-name=test_s3
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/test3.%j.out
#SBATCH --error=../output/test3.%j.err

cd ..
python2 main.py -expID test_s3 -ratio3D 1 -regWeight 0.1 -varWeight 0.01 -loadModel ../exp/test_s2_15/model_15.pth -LR 2.5e-5 -nEpochs 10 -useSyn
