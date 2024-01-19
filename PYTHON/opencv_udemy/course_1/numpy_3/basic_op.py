import numpy as np

"""a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))

print(a<2)
"""
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[1,2,3],[4,5,6]])

print(c*d)

#print(c.dot(d))
print(c.dot(d.T))
print(np.exp(c))

c = np.random.random((5,5))
print(c)
print(d.sum())
print(d.max())
print(d.min())

print(d.sum(axis=0))#stün toplamı
print(d.sum(axis=1))#satır toplamı

print(np.sqrt(d))
print(np.square(d))

print(np.add(d,d))