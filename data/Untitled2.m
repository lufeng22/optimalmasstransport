clear all;
dbstop if error
[F,V]=read_obj('bunny.obj');

bd = compute_bd(F);
uv = disk_harmonic_map(F,V);
disk = uv(bd, :);
pd = power_diagram(F,uv);


in2 = isinpolygon(disk,pd.dpe);
% 
% nc = size(uv,1);
% 
% [pd2,h] = discrete_optimal_transport(disk,face,uv,sigma,area);