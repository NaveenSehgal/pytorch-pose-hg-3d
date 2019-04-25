import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import numpy as np

EDGES = [[0, 1], [1, 2], [2, 6], [6, 3], [3, 4], [4, 5], 
		 [10, 11], [11, 12], [12, 8], [8, 13], [13, 14], [14, 15], 
         [6, 8], [8, 9]]


def plot_pose3d(pose_joints):
	''' pose (16, 3) '''

	fig = plt.figure()
	ax = Axes3D(fig)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	# Scatter joints
	xs = pose_joints[:, 0]
	ys = pose_joints[:, 1]
	zs = pose_joints[:, 2]
	ax.scatter(xs, ys, zs)

	# Draw bones
	for edge in EDGES:
		joint1, joint2 = edge[0], edge[1]
		x_start, y_start, z_start = pose_joints[joint1, :]
		x_end, y_end, z_end = pose_joints[joint2, :]

		xs = np.linspace(x_start, x_end)
		ys = np.linspace(y_start, y_end)
		zs = np.linspace(z_start, z_end)

		ax.plot3D(xs, ys, zs, 'blue')

	plt.show()


if __name__ == '__main__':
	f = h5py.File('synthetic_annot.h5')
	print('Keys: {}'.format(list(f.keys())))
	print('Synthetic Folder: {}'.format(f.attrs['synthetic_folder']))

	joints3d = f['joint_3d_mono'].value  # (N, 16, 3)

	plot_pose3d(joints3d[0])
