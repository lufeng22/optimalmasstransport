[F,V]=read_obj('bunny.obj');

 bd=compute_bd(F)

% [edge,eif] = compute_edge(F)
A = laplace_beltrami(F,V)