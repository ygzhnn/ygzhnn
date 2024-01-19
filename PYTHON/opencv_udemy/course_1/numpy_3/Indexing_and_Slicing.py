import numpy as np

array = np.array([1,2,3,4,5,6,7]) #vector dimension = 1

print(array[0:4])

reverse_array = array[::-1]
print(reverse_array)

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

"""print(array1[1,1])"""
print(array1[:,1])#2 tarafın 1 . indexteki elementi alır

print(array1[1,1:4])#2.satırın 3 elamnını bastırır
print(array1[-1,:])
print(array1[:,-1])
#virgülün sağında : olursa satır işlemi olur solunda : olursa stün işlemi