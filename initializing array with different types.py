import numpy as np

#all zeros method fill all element with zero

print(np.zeros((2,2))) # here (2,2) is array dimention

print(np.ones((3,4),dtype='int32')) # here (3,4) is array dimention
#fill full array with one

a=np.full((2,2),99,dtype='float32')
#np.full function fill up the full array with any values

print(a)
#random number
print(np.random.rand(4,3))

#random integer number
#print random number between 0-9
print(np.random.randint(9))

#int random number array
print(np.random.randint(7 , size=(3,3)))
#this line choose random number between 0-7 and fill the (3,3) dimention array

print(np.random.randint(3,7 , size=(3,3)))
#this line fill random number between 3-7

#itentity matrix
print(np.identity(5))

#repeat an array
print('repeat array')
arr=np.array([[1,2,3]])
r=np.repeat(arr,3, axis=0)
print(r)

#make a specific matrix with some operation

output=np.ones((5,5),dtype='int32')
print("Output Matrix is: ")
print(output)

print("Print matrix with zero value: ")
z=np.zeros((3,3),dtype='int32')
print(z)

z[1,1]=9
print("modified z:")
print(z)

#now replace some value with z matrix
output[1:4,1:4]=z
print(output)




