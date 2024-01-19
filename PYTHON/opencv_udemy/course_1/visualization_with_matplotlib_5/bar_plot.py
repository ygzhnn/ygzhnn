import numpy as np 
import matplotlib.pylab as plt

"""x = np.array([1,2,3,4,5,6,7])
y = x*2+5

plt.bar(x,y)

plt.title("Bar Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()"""

x = np.array([1,2,3,4,5,6,7])
a = ["Turkey","Usa","a","b","c","d","e",]
y = x*2+5

plt.bar(a,y)

plt.title("Bar Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()