#!/bin/bash
#SBATCH --job-name=s3_sg
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s3_sg.%j.out
#SBATCH --error=../output/s3_sg.%j.err

cd ..

python2 main.py -expID Stage3_sg -ratio3D 1 -regWeight 0.1 -varWeight 0.01 -loadModel ../exp/Stage2_s_g_20/model_10.pth -nEpochs 10 -allSYN -scaleMPJPE -gaussBlur -LR 2.5e-5

# python2 main.py -expID Stage3_s -ratio3D 1 -regWeight 0.1 -varWeight 0.01 -loadModel ../exp/Stage2_s_20/model_10.pth -nEpochs 10 -allSYN -LR 2.5e-5 
