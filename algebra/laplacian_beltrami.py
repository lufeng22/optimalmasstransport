"""Laplace Beltrami operator on the mesh.
L = laplace_beltrami(face,vertex)
"""
import numpy as np

def cot2(pi, pj, pk):
    a = np.sqrt(np.dot(pj - pk, pj - pk))
    b = np.sqrt(np.dot(pk - pi, pk - pi))
    c = np.sqrt(np.dot(pi - pj, pi - pj))
    cs =np.divide((np.multiply(b,b) + np.multiply(c,c) - np.multiply(a,a)) , (2*np.multiply(b,c)) )
    ss2 = 1 - np.multiply(cs,cs)
    ss2[ss2 < 0] = 0
    ss2[ss2 > 1] = 1
    ss = np.sqrt(ss2)
    ct = np.divide(cs, ss)
    return ct



def laplace_beltrami(face,vertex):
    [edge, eif] = compute_edge(face)
    ne = size(edge, 1);
    ew = zeros(ne, 1);
    ind = eif(:, 1) > 0;
    ev1 = sum(face(eif(ind, 1),:), 2) - sum(edge(ind,:), 2);
    ct1 = cot2(vertex(ev1,:), vertex(edge(ind, 1),:), vertex(edge(ind, 2),:));
    ew(ind) = ew(ind) + ct1;
    ind = eif(:, 2) > 0;
    ev2 = sum(face(eif(ind, 2),:), 2) - sum(edge(ind,:), 2);
    ct2 = cot2(vertex(ev2,:), vertex(edge(ind, 1),:), vertex(edge(ind, 2),:));
    ew(ind) = ew(ind) + ct2;


    A = sparse([edge(:, 1);edge(:, 2)], [edge(:, 2);edge(:, 1)], [ew;    ew] / 2);
    sA = sum(A, 2);
    A = A - diag(sA);

