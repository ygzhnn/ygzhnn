import matplotlib.pyplot as plt 
import pandas as pd 

dataFrame = pd.read_csv("Iris.csv")

dataFrame1 = dataFrame.drop(["Id"],axis=1)

setosa = dataFrame[dataFrame1.Species == "Iris-setosa"]
versicolor = dataFrame[dataFrame1.Species == "Iris-versicolor"]
virginica = dataFrame[dataFrame1.Species == "Iris-virginica"]

plt.hist(setosa.PetalLengthCm,bins = 10)
plt.xlabel("PetalLengthCm Values")
plt.ylabel("Frekans")
plt.title("Hist")
plt.show()