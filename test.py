import meshio
from algebra import  *
from parameterization import *
from graphics import *

import time
from power_diagram import power_diagram
from plot_power_diagram import *
mesh = meshio.read('data/bunny.obj')
F = mesh.cells['triangle']
V = mesh.points
#
# start_time = time.time()
# # compute the boundary vertices
bd = compute_bd(F)
# elapsed_time = time.time() - start_time
# print('compute bd' + str(elapsed_time))

#
# start_time = time.time()
# edge, eif = compute_edge(F)
# elapsed_time = time.time() - start_time
# print('compute edge' + str(elapsed_time))
#
#
# start_time = time.time()
# L= laplace_beltrami(F, V)
# elapsed_time = time.time() - start_time
# print('laplace_beltrami' + str(elapsed_time))
#
# start_time = time.time()
# uv = disk_harmonic_map(F, V)
# elapsed_time = time.time() - start_time
# print('disk_harmonic_map' + str(elapsed_time))
# # plot_mesh(F, uv)
#
#
# start_time = time.time()
vr = compute_vertex_ring(F, V, ordered=True)
# elapsed_time = time.time() - start_time
# print('compute_vertex_ring' + str(elapsed_time))
#
#
# start_time = time.time()
# plot_vertex_ring(F, uv, vr)
# elapsed_time = time.time() - start_time
# print('plot vertex ring' + str(elapsed_time))
# # vvif,nvif,pvif = compute_connectivity(F)
#


uv = disk_harmonic_map(F, V)

pd, h = power_diagram(F, uv)

# plot_power_diagram(pd)



from matplotlib import path
import numpy as np


def isinpolygon(polygon, xy):
    p = path.Path(polygon)
    flag = p.contains_points(xy)
    return flag


flag = isinpolygon(uv[bd,:], pd["dpe"])
print(flag)