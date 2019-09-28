#!/bin/bash
#SBATCH --job-name=test_h36m
#SBATCH --mem=100Gb
#SBATCH --gres=gpu:k40m:1
#SBATCH --partition=gpu
#SBATCH --output=../output/test_h36m.%j.out
#SBATCH --error=../output/test_h36m.%j.err

cd ..
python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/hgreg-3d.pth 

echo '*************** S3_M on H36M ***************'
#python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_m/model_10.pth

echo '*************** S3_M_G on H36M ***************'
#python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_m_g/model_10.pth -gaussBlur

echo '*************** S3_S on H36M ***************'
#python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_s/model_10.pth

echo '*************** S3_S_G on H36M ***************'
#python2 main.py -expID H36M_test -ratio3D 1 -test -loadModel ../exp/Stage3_sg/model_10.pth -gaussBlur
# -loadModel /home/sehgal.n/3d_pose/pytorch-pose-hg-3d/exp/hgreg-3d.pth -test #/home/sehgal.n/3d_pose/pytorch-pose-hg-3d/exp/test_s3/model_5.pth -test # ../exp/Stage3_SYN_test_0/model_10.pth  -test -varWeight 0.01 -regWeight 0.01
# -ratio3D 1 
# -regWeigh 0.1 -varWeight 0.01 -loadModel ../exp/hgreg-3d.pth -LR 2.5e-5 -nEpochs 0 -test

