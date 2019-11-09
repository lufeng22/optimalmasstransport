"""
Harmoni  map a single patch mesh to a rectangle 
uv = rect_harmonic_map(face, vertex, corner)
corner specify four corner indices, of the vertex.
"""
import numpy as np

def rect_harmonic_map(face, vertex, corner):

    nv = vertex.shape[0]
    bd = compute_bd(face)  #  boundary vertex list
    nbd = bd.shape[0]


    i = np.where(bd == corner[0])
    bd = np.array(bd[i:-1], bd[0:i])
    corner = corner([1:end, 1],:);

    ck = zeros(size(corner, 1), 1);
    k = 1;
    for i = 1:length(bd)
    if (bd(i) == corner(k))
        ck(k) = i;
        k = k + 1;
    end
    end

    uvbd = zeros(nbd, 2);
    if size(corner, 2) == 2 | | size(corner, 2) == 3
        if size(corner, 2) == 3
            zc = corner(:, 2)+1
            i * corner(:, 3);
            else
            zc = corner;
        end
        zbd = zeros(nbd, 1);

        zbd(ck(1): ck(2)) = linspace(zc(1), zc(2), ck(2) - ck(1) + 1);
        zbd(ck(2): ck(3)) = linspace(zc(2), zc(3), ck(3) - ck(2) + 1);
        zbd(ck(3): ck(4)) = linspace(zc(3), zc(4), ck(4) - ck(3) + 1);
        zbd(ck(4): ck(5)) = linspace(zc(4), zc(5), ck(5) - ck(4) + 1);
        uvbd = [real(zbd), imag(zbd)];
    else
        uvbd(ck(1): ck(2), 1) = linspace(0, 1, ck(2) - ck(1) + 1)
        ';
        uvbd(ck(1): ck(2), 2) = 0;
        uvbd(ck(2): ck(3), 1) = 1;
        uvbd(ck(2): ck(3), 2) = linspace(0, 1, ck(3) - ck(2) + 1)
        ';
        uvbd(ck(3): ck(4), 1) = linspace(1, 0, ck(4) - ck(3) + 1)
        ';
        uvbd(ck(3): ck(4), 2) = 1;
        uvbd(ck(4): ck(5), 1) = 0;
        uvbd(ck(4): ck(5), 2) = linspace(1, 0, ck(5) - ck(4) + 1)
        ';
    end
    uvbd(end,:) = [];
    bd(end) = [];
    uv = zeros(nv, 2);
    uv(bd,:) = uvbd;
    in = true(nv, 1);
    in (bd) = false;
    A = laplace_beltrami(face, vertex);
    Ain = A( in, in );
    rhs = -A( in, bd)*uvbd;
    uvin = Ain\rhs;
    uv( in,:) = uvin;
