""""
power diagram
"""
import numpy as np
from scipy.linalg import norm

from scipy.spatial import ConvexHull
from calculate_face_normal import *
from algebra import *


def face_dual_uv(p):
    a = p[0, 1] * (p[1, 2] - p[2, 2]) + p[1, 1] * (p[2, 2] - p[0, 2]) + p[2, 1] * (p[0, 2] - p[1, 2])
    b = p[0, 2] * (p[1, 0] - p[2, 0]) + p[1, 2] * (p[2, 0] - p[0, 0]) + p[2, 2] * (p[0, 0] - p[1, 0])
    c = p[0, 0] * (p[1, 1] - p[2, 1]) + p[1, 0] * (p[2, 1] - p[0, 1]) + p[2, 0] * (p[0, 1] - p[1, 1])
    dp = [-a / c / 2, -b / c / 2]
    return dp


def power_diagram(face, uv, h=None, dh=None):
    if h is None:
        h = np.zeros((uv.shape[0], 1))

    if dh is None:
        dh = h * 0

    nf = face.shape[0]
    c = 1

    while True:
        h = h - c * dh
        pl = np.concatenate((uv, np.reshape(np.square(norm(uv, axis=1)), (-1, 1)) - h), axis=1)
        face = ConvexHull(pl).simplices
        fn = calculate_face_normal(face, pl)
        ind = fn[:, 2] < 0

        if np.sum(ind) < nf:
            h = h + c * dh
            c = c / 2
        else:
            break

        if np.max(abs(dh)) == 0:
            break

    fn = calculate_face_normal(face, pl)
    ind = fn[:, 2] < 0
    face = face[ind, :]
    pd = dict()
    pd['face'] = face
    vr = compute_vertex_ring(face, uv, ordered=True)
    pd['uv'] = uv
    pd['dp'] = np.zeros((face.shape[0], 2))
    pd['cell'] = [[] for i in range(pl.shape[0])]

    for i in range(face.shape[0]):
        dp = face_dual_uv(pl[face[i,:],:])
        pd['dp'][i,:] = dp
    pd['dp']



    # TOBECONTINUE
    return pd
