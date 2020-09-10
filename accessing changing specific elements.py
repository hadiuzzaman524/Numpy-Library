import numpy as np

a=np.array([[1,2,3,4,5],[5,4,3,2,4]])
print(a)
print(a.shape) #return how many row and column
print(a[0,0]) #return specific row column value
print(a[0, :]) # return row 0 all elements
print(a[:,2]) #return all row's 2nb column

#getting a little more fancy [startindex:endindex:stepsize]
print(a[0,1:4:2])
print(a)
#change the value of 0,1 position
a[0,1]=20
print(a)

#change the entire series.
a[:,2]=10
print(a)
