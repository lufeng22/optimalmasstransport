clear all;
[F,V]=read_obj('bunny.obj');


% plot_mesh(F,uv)
% 
% 

% 
% plot_power_diagram(pd)

 
% vr=compute_vertex_ring(F,V, [], 1)
%  [vvif,nvif,pvif] = compute_connectivity(F) 
uv = disk_harmonic_map(F,V);
pd = power_diagram(F,uv)