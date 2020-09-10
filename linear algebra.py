import numpy as np

a=np.ones((2,3))
print(a)
b=np.full((3,2),2)
print(b)

print("Multiplication of a b is: ")
print(np.matmul(a,b)) # matrix multiply

#find determinant
print("Itentity matrix: ")
c=np.identity(3)
print(c)
print(np.linalg.det(c))
