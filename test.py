import meshio
from graphics.plot_mesh import plot_mesh
from graphics.plot_path import plot_path
from algebra.compute_bd import compute_bd
from algebra.compute_edge import *
from scipy.linalg import norm
# Load mesh and show the mesh
mesh = meshio.read('data/bunny.obj')
F = mesh.cells['triangle']
V = mesh.points
# plot_mesh(F,V)

# compute the boundary vertices
bd = compute_bd(F)
# plot_path(F, V, bd)

from algebra.compute_edge import *
def cot2(pi, pj, pk):
    a = norm(pj - pk, axis=1)
    b = norm(pk - pi, axis=1)
    c = norm(pi - pj, axis=1)
    cs =np.divide((np.multiply(b,b) + np.multiply(c,c) - np.multiply(a,a)) , (2*np.multiply(b,c)) )
    ss2 = 1 - np.multiply(cs,cs)
    ss2[ss2 < 0] = 0
    ss2[ss2 > 1] = 1
    ss = np.sqrt(ss2)
    ct = np.divide(cs, ss)
    return ct



face = F
vertex = V
edge, eif = compute_edge(face)

ne = edge.shape[0]
ew = np.zeros((ne, 1))
ind = eif[:, 0] > 0



ev1 = np.sum(face[eif[ind, 0], :], axis=1) - np.sum(edge[ind, :], axis=1)
ct1 = cot2(vertex[ev1, :], vertex[edge[ind, 0], :], vertex[edge[ind, 1], :])
ew[ind] = ew[ind] + ct1
ind = eif[:, 1] > 0
ev2 = np.sum(face[eif[ind, 1], :], axis=1) - np.sum(edge[ind, :], axis=1)
ct2 = cot2(vertex[ev2, :], vertex[edge[ind, 0], :], vertex[edge[ind, 1], :])
ew[ind] = ew[ind] + ct2