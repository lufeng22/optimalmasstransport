""" compute_adjacency_matrix
 [am,amd] = compute_adjacency_matrix(face);
 face: double array, nf x 3, connectivity of mesh
 am : sparse matrix, nv x nv, undirected adjacency matrix
 amd: sparse matrix, nv x nv, directed adjacency matrix
"""
from scipy import sparse
from numpy import array
import numpy as np

def compute_adjacency_matrix(face):
    nf = face.shape[0]
    I = face.reshape((nf*3,1))
    facecopy = np.array([face[:,1],face[:,2], face[:,0]]).transpose()
    J = facecopy.reshape((nf*3,1))
    V = np.array([range(1,nf+1),range(1,nf+1),range(1,nf+1)]).reshape((nf*3,1),order='F')
    amd = sparse.coo_matrix((V.flatten(), (I.flatten(), J.flatten())))
    am = amd.copy().tocsr()
    am.data.fill(1)
    am = am + am.transpose()
    return am,amd.tocsr()

