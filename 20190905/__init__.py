import numpy as np

m = np.array([[1, 5, 2],
              [4, 7, 4],
              [2, 0, 9]])
u, s, v = np.linalg.svd(m)
print(np.round(np.abs(u.dot(np.linalg.inv(u)))))
print(s)
i = v.dot(np.linalg.inv(v))
print(np.round(np.abs(i)))

A = np.arange(27).reshape((3, 3, 3))
print(A)
print(A[:,:,2])
print(A[...,2])

arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[[0,1,2],[1,0,0]])