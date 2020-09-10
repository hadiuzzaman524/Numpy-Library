import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)

#if we assign one array to another then
#when chenge the 2nd array then also automaticaly change
#first array its a big problem..
arr2=arr
arr2[0]=500
print(arr2)
print(arr)

#to avoid this problem we can use copy() function

arr3=arr.copy()
arr3[0]=2000
print(arr)
print(arr3)

#mathmatical operations...
arr+=100
print(arr)
# calculate angle..... same as cos tan etc.
arr=np.sin(arr)
print(arr)
