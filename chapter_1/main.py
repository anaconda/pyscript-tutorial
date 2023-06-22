
# Adapted from https://numpy.org/doc/stable/user/quickstart.html#an-example
import numpy as np

a = np.arange(15).reshape(3, 5)
print(f"NDArray a: \n{a}")
# Expected:
# array([[ 0,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9],
#       [10, 11, 12, 13, 14]])
print(f"a.shape: {a.shape}")
# Expected:
# (3, 5)
print(f"a.ndim: {a.ndim}")
# Expected: 2
print(f"a.dtype.name: {a.dtype.name}")
# Expected: 'int64'
print(f"type(a): {type(a)}")
# Expected <class 'numpy.ndarray'>
b = np.array([6, 7, 8])
print(f"b: {b}")
# Expected: array([6, 7, 8])
print(f"type(b): {type(b)}")
# Expected: <class 'numpy.ndarray'>