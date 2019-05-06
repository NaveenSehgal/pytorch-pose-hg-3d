import h5py
import numpy as np

f = h5py.File('annot.h5', 'r')
print('Keys: {}'.format(list(f.keys())))

