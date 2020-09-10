import numpy as np

stats=np.array([[2,2,3],[4,5,6]])
print(stats)
print("Minimum value: ")
print(np.min(stats))
print(f"maximum value: {np.max(stats)}")

print("Row wise minimum: ")
print(np.min(stats, axis=1))
#axis 1 mean every row wise calculations return
print("Column wise Minimum")
print(np.min(stats, axis=0))
#axis 0 means every column wise calculation return

print(f"The sum of all elements: {np.sum(stats)}")