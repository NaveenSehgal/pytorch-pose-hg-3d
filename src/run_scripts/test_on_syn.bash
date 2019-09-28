#!/bin/bash
#SBATCH --job-name=test_syn
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/test_syn.%j.out
#SBATCH --error=../output/test_syn.%j.err

cd ..
echo '*************** S3_M on SYN ***************'
python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_m/model_10.pth -useSyn -scaleMPJPE

echo '*************** S3_M_G on SYN ***************'
python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_m_g/model_10.pth -gaussBlur -useSyn -scaleMPJPE

echo '*************** hgreg-3d on SYN ***************'
python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/hgreg-3d.pth -useSyn -scaleMPJPE

echo '*************** S3_S on H36M ***************'
python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_s/model_10.pth -useSyn -scaleMPJPE

echo '*************** S3_S_G on H36M ***************'
python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_sg/model_10.pth -useSyn -gaussBlur -scaleMPJPE


# -ratio3D 1 
# -regWeigh 0.1 -varWeight 0.01 -loadModel ../exp/hgreg-3d.pth -LR 2.5e-5 -nEpochs 0 -test

