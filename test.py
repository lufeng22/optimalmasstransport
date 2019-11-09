import numpy as np
import trimesh
import pyrender
mesh = trimesh.load('data/face.obj')

# (press w in viewer to see triangles)
mesh.show()

## if you wish a better render, use following
# mesh_render = pyrender.Mesh.from_trimesh(mesh)
# scene = pyrender.Scene()
# scene.add(mesh_render)
# pl = pyrender.PointLight(color=[1.0, 1.0, 1.0], intensity=2.0)
#
# pyrender.Viewer(scene, use_raymond_lighting=True)

