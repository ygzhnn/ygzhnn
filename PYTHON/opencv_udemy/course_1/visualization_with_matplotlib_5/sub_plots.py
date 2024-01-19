import matplotlib.pyplot as plt 
import pandas as pd 

dataFrame = pd.read_csv("Iris.csv")

#dataFrame.plot()
#plt.show()

dataFrame1 = dataFrame.drop(["Id"],axis=1)

setosa = dataFrame[dataFrame1.Species == "Iris-setosa"]
versicolor = dataFrame[dataFrame1.Species == "Iris-versicolor"]
virginica = dataFrame[dataFrame1.Species == "Iris-virginica"]



"""dataFrame1.plot(grid=True,alpha = 0.9,subplots=True) #linestyle = ":"
plt.show()"""

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm, color = "red", label = "setosa")
plt.ylabel("setosa - PetalLengthCm")

plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.ylabel("versicolor - PetalLengthCm")

plt.show()