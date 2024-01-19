import matplotlib.pyplot as plt 
import pandas as pd 

dataFrame = pd.read_csv("Iris.csv")

dataFrame1 = dataFrame.drop(["Id"],axis=1)

setosa = dataFrame[dataFrame1.Species == "Iris-setosa"]
versicolor = dataFrame[dataFrame1.Species == "Iris-versicolor"]
virginica = dataFrame[dataFrame1.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color = "red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color = "green", label = "versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color = "blue", label = "virginica")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.legend()
plt.show()