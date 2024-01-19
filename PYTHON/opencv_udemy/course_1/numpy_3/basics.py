import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1*15 Vector

a = print(array.reshape(3,5))

print(array.dtype)
print(array.ndim)
print(array.size)
print(type(array))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
array.shape
zeros = np.zeros((3,4))
zeros[0,0] = 5
print(zeros)
np.ones((3,4))
np.empty(3,4)
         
a = np.arange(10,50,5)
print(a.ndim)