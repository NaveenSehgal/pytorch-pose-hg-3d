#!/bin/bash
#SBATCH --job-name=s3_m
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s3_m.%j.out
#SBATCH --error=../output/s3_m.%j.err

cd ..

python2 main.py -expID Stage3_m -ratio3D 1 -regWeight 0.1 -varWeight 0.01 -loadModel ../exp/Stage2_m_15/model_15.pth -nEpochs 10 -useSyn -LR 2.5e-5 

#python main.py -expID Stage3 -ratio3D 1 -regWeight 0.1 -varWeight 0.01 -loadModel ../exp/Stage2/model_30.pth -LR 2.5e-5 -nEpochs 10
