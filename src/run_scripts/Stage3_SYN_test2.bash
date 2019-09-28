#!/bin/bash
#SBATCH --job-name=s2_syn_test
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_syn_test.%j.out
#SBATCH --error=../output/s2_syn_test.%j.err

cd ..
python2 main.py -expID Stage3_SYN_test2_0 -ratio3D 1 -regWeigh 0.1 -varWeight 0.01 -loadModel ../exp/old/Stage2_SYN_test_20/model_10.pth -LR 2.5e-5 -nEpochs 10 -useSyn
