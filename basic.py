import numpy as np

n=np.array([2,3,4,5] ,dtype='int32')

print("Two dimentional: ")
m=np.array([[1,2,3],[3,4,5],[4,5,6]])
print(m)

print("One Dimentional: ")
print(n)

#ndim function return dimention of array...
print(f"Dimention of n is: {n.ndim}")
print(f"Dimention of m is: {m.ndim}")

# shape function return how many row and column are
#there ......
print(n.shape)
print(m.shape)

#return data type with dtype
print(n.dtype)

#reutn the dimention of array...
print(n.ndim)

#return size of item used of memory
print(n.itemsize)

#numberbytes return total uses memory
print(n.nbytes)
