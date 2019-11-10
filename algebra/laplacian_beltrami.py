"""Laplace Beltrami operator on the mesh.
L = laplace_beltrami(face,vertex)
"""
import numpy as np
from algebra.compute_edge import *
from scipy.linalg import norm

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


def laplace_beltrami(face,vertex):
    edge, eif = compute_edge(face)
    ne = edge.shape[0]
    ew = np.zeros((ne, 1))
    ind = eif[:,0] > 0

    ev1 = np.sum(face[eif[ind,0],:], axis=1) - np.sum(edge[ind,:],axis = 1)

    ct1 = cot2(vertex[ev1,:], vertex[edge[ind, 0],:], vertex[edge[ind, 1],:])
    ew[ind] = ew[ind] + ct1
    ind = eif[:, 1] > 0
    ev2 = np.sum(face[eif[ind, 1],:], axis=1) - np.sum(edge[ind,:], axis = 1)
    ct2 = cot2(vertex[ev2,:], vertex[edge[ind, 0],:], vertex[edge[ind, 1],:])
    ew[ind] = ew[ind] + ct2

    A = sparse([edge(:, 1);edge(:, 2)], [edge(:, 2);edge(:, 1)], [ew;    ew] / 2);
    sA = sum(A, 2);
    A = A - diag(sA);

