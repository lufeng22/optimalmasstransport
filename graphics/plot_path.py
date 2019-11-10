"""
Plot_path
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D  # <-- Note the capitalization!

def plot_path(F, V, path):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_trisurf(V[:,0], V[:,1], V[:,2], triangles=F,  cmap=plt.cm.Spectral, edgecolor=[0.2, 0.2, 0.2] , linewidth = 0.5, alpha=0.7)

    ax.plot(V[path, 0], V[path, 1], V[path, 2], 'r-', linewidth=3)
    # Draw now
    plt.draw()

    plt.show()
