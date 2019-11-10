import meshio
from algebra import  *
from parameterization import *
from graphics import *
mesh = meshio.read('data/bunny.obj')
F = mesh.cells['triangle']
V = mesh.points


# compute the boundary vertices
bd = compute_bd(F)
edge, eif = compute_edge(F)
L= laplace_beltrami(F, V)
uv = disk_harmonic_map(F, V)

plot_mesh(F, uv)
