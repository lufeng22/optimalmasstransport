"""
[edge, eif] = compute_edge(face)
"""
import numpy as np
from algebra.compute_adjacent_matrix import compute_adjacency_matrix
import scipy
def xor(a, b):
    return np.logical_xor(a.todense(), b.todense())


def compute_edge(face):
    am, amd = compute_adjacency_matrix(face)
    IJ = np.argwhere(am)
    I = IJ[:, 0]
    J = IJ[:, 1]
    ind = I < J
    edge = np.array([I[ind], J[ind]])

    t1 = amd - xor(amd, am)
    V = t1[np.nonzero(t1)]
    V = np.squeeze(np.asarray(V))
    t2 = (amd - xor(amd, am)).transpose()
    V2 = t2[np.nonzero(t2)]
    V2 = np.squeeze(np.asarray(V2))

    eif = np.array([V[ind], V2[ind]])
    return edge.transpose(), eif.transpose()
