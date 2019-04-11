import h5py
f = h5py.File('synthetic_annot.h5')
print('Keys: {}'.format(list(f.keys())))
print('Synthetic Folder: {}'.format(f.attrs['synthetic_folder']))
