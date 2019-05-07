#!/bin/bash
#SBATCH --job-name=s1_MP_G
#SBATCH --mem=50Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/s1_MP_G.%j.out
#SBATCH --error=../output/s1_MP_G.%j.err

cd ..
python2 main.py -expID S1_mpii_gauss -nEpochs 20 -useSyn -gaussBlur

