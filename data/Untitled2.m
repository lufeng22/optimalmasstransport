[F,V]=read_obj('bunny.obj');

uv = disk_harmonic_map(F,V);
plot_mesh(F,uv)


pd = power_diagram(face,uv);

plot_power_diagram(pd)