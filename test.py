from disk_omt import *
from meshio import *
from parameterization import *
import numpy as np

F, V = read_obj('data/bunny.obj')

vr = compute_vertex_ring(F, V, ordered=True)

bd = compute_bd(F)
uv = disk_harmonic_map(F, V)

disk = uv[bd, :]


def sigma(x):
    x = x.reshape((-1, 2))
    return np.ones((x.shape[0],))


nc = uv.shape[0]
area = 4 / nc * np.ones((nc,))
pd2, h, maxdh = discrete_optimal_transport(disk, F, uv, sigma, area)
