import meshio
from algebra import  *
from parameterization import *
from graphics import *
from power_diagram import power_diagram
mesh = meshio.read('data/bunny.obj')
F = mesh.cells['triangle']
V = mesh.points


# compute the boundary vertices
bd = compute_bd(F)
edge, eif = compute_edge(F)
L= laplace_beltrami(F, V)
uv = disk_harmonic_map(F, V)

# plot_mesh(F, uv)

vr = compute_vertex_ring(F, V, ordered=True)


power_diagram(F, uv)
