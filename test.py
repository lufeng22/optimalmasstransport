import meshio
from graphics.plot_mesh import plot_mesh
from graphics.plot_path import plot_path
from algebra.compute_bd import compute_bd
from algebra.compute_adjacent_matrix import *
import numpy as np
# Load mesh and show the mesh
mesh = meshio.read('data/bunny.obj')
F = mesh.cells['triangle']

am, amd = compute_adjacency_matrix(F)
IJ = np.argwhere(am)
I = IJ[:, 0]
J = IJ[:, 1]
ind = I < J
edge = np.array([I[ind], J[ind]])

t1 = amd - np.logical_xor(amd, am)
V = t1[np.nonzero(t1)]
t2 = (amd - np.logical_xor(amd, am)).transpose()
V2 = t2[np.nonzero(t2)]
eif = np.array([V[ind], V2[ind]])

