import numpy as np 

liste = [1,2,3,4] #list

array = np.array(liste) #numpy array

list2 = list(array) 

a = np.array([1,2,3])

b=a
c=a

b[0] = 5
print(a)
print(b)
print(c)
#np array memory de depolanırken değer olark değil ala olarak depolanır a b c ye aynı alanı ayırdığımız için hepsi değişir

d = np.array([1,2,3])
e = d.copy()
f = d.copy()
f[0] = 5
e[0] = 6
print(d)
print(f)
print(e)