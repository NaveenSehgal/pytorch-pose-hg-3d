#!/bin/bash
#SBATCH --job-name=s2_syn_test
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s2_syn_test.%j.out
#SBATCH --error=../output/s2_syn_test.%j.err

cd ..
python2 main.py -expID Stage2_SYN_test_20 -ratio3D 1 -regWeigh 0.1 -loadModel ../exp/Stage2_SYN_test_10/model_10.pth -nEpochs 10 -useSyn -dropLR 5

