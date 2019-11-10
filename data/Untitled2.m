[F,V]=read_obj('bunny.obj');

uv = disk_harmonic_map(F,V);
plot_mesh(F,uv)