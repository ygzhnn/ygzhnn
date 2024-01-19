import matplotlib.pyplot as plt 
import pandas as pd 

dataFrame = pd.read_csv("Iris.csv")

#dataFrame.plot()
#plt.show()

dataFrame1 = dataFrame.drop(["Id"],axis=1)

setosa = dataFrame[dataFrame1.Species == "Iris-setosa"]
versicolor = dataFrame[dataFrame1.Species == "Iris-versicolor"]
virginica = dataFrame[dataFrame1.Species == "Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm, color = "red", label = "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm, color = "blue", label = "virginica")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

dataFrame1.plot(grid=True,alpha = 0.5) #linestyle = ":"
plt.show()

