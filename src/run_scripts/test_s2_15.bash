#!/bin/bash
#SBATCH --job-name=test_15
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/test_15.%j.out
#SBATCH --error=../output/test_15.%j.err

cd ..
python2 main.py -expID test_s2_15 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/test_s2/model_15.pth -nEpochs 15 -useSyn -dropLR 10
