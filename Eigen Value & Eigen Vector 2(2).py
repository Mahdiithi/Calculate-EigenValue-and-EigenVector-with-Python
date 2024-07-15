import numpy as np
from numpy.linalg import eig

a = np.array([[3, 4],[2, 0]])
w, v = eig(a)
print("E-Value: ", w)
print("E-Vector: ", v)