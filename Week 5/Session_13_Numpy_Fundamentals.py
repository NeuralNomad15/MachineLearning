#Creating Numpy Arrays
# np.array
import numpy as np

a = np.array([1,2,3])
print(a)

# 2D and 3D
b = np.array([[1,2,3],[4,5,6]])
print(b)

# dtype
np.array([1,2,3],dtype=float)

# np.arange
np.arange(1,11,2)

# with reshape
np.arange(16).reshape(2,2,2,2)

# np.ones and np.zeros
np.ones((3,4))

np.zeros((3,4))

# np.random
np.random.random((3,4))

# np.linspace
np.linspace(-10,10,10,dtype=int)

# np.identity
np.identity(3)

a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
a3

# ndim
a3.ndim

# shape
print(a3.shape)
a3

# size
print(a2.size)
a2

# dtype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# dtype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# astype
a3.astype(np.int32)

