import meshio
from graphics.plot_mesh import plot_mesh
from graphics.plot_path import plot_path
from algebra.compute_bd import compute_bd
# Load mesh and show the mesh
mesh = meshio.read('data/bunny.obj')
F = mesh.cells['triangle']
V = mesh.points
plot_mesh(F,V)

# compute the boundary vertices
bd = compute_bd(F)
plot_path(F, V, bd)

