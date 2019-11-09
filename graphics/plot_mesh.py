"""
Plot_mesh
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import axes3d, Axes3D  # <-- Note the capitalization!

def plot_mesh(F=None, V=None):
    if (F is None)   and (V is None):  # show a example
        # Make parameter spaces radii and angles.
        n_angles = 36
        n_radii = 8
        min_radius = 0.25
        radii = np.linspace(min_radius, 0.95, n_radii)
        angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
        angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
        angles[:, 1::2] += np.pi / n_angles
        # Map radius, angle pairs to x, y, z points.
        x = (radii * np.cos(angles)).flatten()
        y = (radii * np.sin(angles)).flatten()
        z = (np.cos(radii) * np.cos(3 * angles)).flatten()

        # Create the Triangulation; no triangles so Delaunay triangulation created.
        triang = mtri.Triangulation(x, y)

        # Mask off unwanted triangles.
        xmid = x[triang.triangles].mean(axis=1)
        ymid = y[triang.triangles].mean(axis=1)
        mask = xmid ** 2 + ymid ** 2 < min_radius ** 2
        triang.set_mask(mask)


        fig = plt.figure()

        ax = Axes3D(fig)  # <-- Note the difference from your original code...
        ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
        # Draw now
        plt.show()
