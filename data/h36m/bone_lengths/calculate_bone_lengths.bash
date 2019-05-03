#!/bin/bash
#SBATCH --job-name=bones
#SBATCH --mem=20Gb
#SBATCH --partition=general
#SBATCH --output=bones.%j.out
#SBATCH --error=bones.%j.err

python3 calc_bone_lengths.py 

