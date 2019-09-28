#!/bin/bash
#SBATCH --job-name=test
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/test.%j.out
#SBATCH --error=../output/test.%j.err

cd ..
python2 main.py -expID test_s2 -ratio3D 1 -regWeight 0.1 -loadModel ../exp/old/Stage1/model_60.pth -nEpochs 15 -useSyn -scaleMPJPE

