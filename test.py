import meshio
from graphics.plot_mesh import plot_mesh
from graphics.plot_path import plot_path
from algebra.compute_bd import compute_bd
from algebra.compute_edge import *
from algebra.laplacian_beltrami import *
from scipy.linalg import norm
# Load mesh and show the mesh
mesh = meshio.read('data/bunny.obj')
F = mesh.cells['triangle']
V = mesh.points
# plot_mesh(F,V)

# compute the boundary vertices
bd = compute_bd(F)

edge, eif = compute_edge(F)


# plot_path(F, V, bd)
L= laplace_beltrami(F, V)
