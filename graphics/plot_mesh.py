"""
Plot_mesh
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import axes3d, Axes3D  # <-- Note the capitalization!

def plot_mesh(F=None, V=None):
    if (F is None)   and (V is None):  # show a example
        u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
        v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
        u, v = np.meshgrid(u, v)
        u, v = u.flatten(), v.flatten()
        x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
        y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
        z = 0.5 * v * np.sin(u / 2.0)
        tri = mtri.Triangulation(u, v)
        fig = plt.figure()
        ax = Axes3D(fig)
        print(tri.triangles)
        ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)

    else:

        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot_trisurf(V[:,0], V[:,1], V[:,2], triangles=F, cmap=plt.cm.Spectral)
        # Draw now
        plt.draw()
