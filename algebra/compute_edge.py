"""
[edge, eif] = compute_edge(face)
"""
import numpy as np
from algebra.compute_adjacent_matrix import compute_adjacency_matrix


def compute_edge(face):
    am, amd = compute_adjacency_matrix(face)
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
    return edge, eif
