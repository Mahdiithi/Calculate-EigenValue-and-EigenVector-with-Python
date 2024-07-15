import numpy as np
from numpy.linalg import eig

a = np.array([[[2, 3, 4],[0, 0, 1],[3, 6, 2]]])
w, v = eig(a)
print("E-Value: ", w)
print("E-Vector: ", v)