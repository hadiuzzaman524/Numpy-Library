import numpy as np

# reshape the matrix
before=np.array([[1,2,3,4],[5,6,7,8]])
print(f"Before matrix{before}")
after=before.reshape((4,2))
print(f"After reshape matrix: {after}")
print(after.shape)

#vartically stacking vectors
v1=np.array([1,2,3,4,5])
v2=np.array([3,3,3,3,3])

x=np.vstack([v1,v2,v2])
print(f"shape of the new matrix is: {x.shape}")
print("The matrix is : ")
print(x)

#horizontal stacking vectors
r=np.ones((2,3))
print(r)
t=np.zeros((2,2))
print(t)
hs=np.hstack([r,t])
print(f"Horizontal stack: \n{hs}")
