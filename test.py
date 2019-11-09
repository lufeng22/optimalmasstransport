import numpy as np
import trimesh
import pyrender
mesh = trimesh.load('data/alex.obj')

# (press w in viewer to see triangles)
# mesh.show()

mesh_render = pyrender.Mesh.from_trimesh(mesh)
scene = pyrender.Scene()
scene.add(mesh_render)
pyrender.Viewer(scene, use_raymond_lighting=True)