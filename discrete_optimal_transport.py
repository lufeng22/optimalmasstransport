"""[pd2,h] = discrete_optimal_transport(disk,face,uv,sigma,area);
"""
from matplotlib import path
import numpy as np


def isinpolygon(polygon, xy):
    p = path.Path(polygon)
    flag = p.contains_points(xy)
    return flag



def calculate_gradient(cp,pd,sigma, more_accurate = False):
    nc = len(cp["cell"])
    D = np.zeros((nc, ))

    isin = np.ones((nc, )).astype(bool)
    isin2 = isin(cp, pd.dpe);
    % fisind
    out
    cells not isin cp
    completely
    for i = 1:nc
    ci = pd.cell
    {i};
    if ~all(isin2(ci))
        isin (i) = false;
    end


    end
    cp(end,:) = [];




def calculate_hessian(cp,pd,sigma):



def discrete_optimal_transport(disk,face,uv,sigma,area):



