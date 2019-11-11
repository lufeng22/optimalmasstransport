""""
power diagram
"""
import numpy as np
from scipy.linalg import norm

from scipy.spatial import ConvexHull
from calculate_face_normal import *
from algebra import *
from intersectRayPolygon import *

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

    K =  ConvexHull(uv).vertices
    K = np.append(K,K[0])
    vb = np.zeros((K.shape[0] - 1, 2))
    mindp = np.min(pd["dp"], axis=0) - 1
    maxdp = np.max(pd["dp"], axis=0) + 1
    minx = mindp[0]
    miny = mindp[1]
    maxx = maxdp[0]
    maxy = maxdp[1]
    box = np.array([minx, miny, maxx, miny, maxx, maxy, minx, maxy, minx, miny]).reshape((-1,2))

    for i in range(K.shape[0]- 1):
        i1 = K[i]
        i2 = K[i + 1]
        vec = uv[i2,:] - uv[i1,:]
        vec = np.array([vec[1], -vec[0]])
        mid = (uv[i2,:] + uv[i1,:]) / 2.0
        intersects = intersectRayPolygon(mid, vec, box)
        vb[i,:] = intersects

    pd["dpe"] = np.concatenate((pd["dp"], vb), axis=0)

    vvif, _, _= compute_connectivity(face)

    for i in range(uv.shape[0]):
        vri = vr[i]
        pb = np.argwhere(K==i)
        if pb.size > 0 :
            pb = pb[0]
            fr = np.zeros((len(vri) + 1,1))
            fr[-1] = face.shape[0] + pb
            if pb == 0:
                fr[0] = face.shape[0] + K.shape[0]-1
            else:
                fr[0] = face.shape[0] + pb - 1
            for j in range(len(vri) - 1):
                fr[j+1] = vvif[i, vri[j]]
        else:
            fr = np.zeros((len(vri),1))
            for j in range(len(vri)):
                fr[j] = vvif[i, vri[j]]
        pd["cell"][i] = np.flip(fr)

    return pd, h
