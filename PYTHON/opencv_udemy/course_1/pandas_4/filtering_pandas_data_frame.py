import pandas as pd 

dictionary = {"Name":["Ali","Veli","Hilal","Evren","Ayse","Evren"],
              "Age":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

filtre1 = dataFrame1.Maas > 200
print(filtre1)

filtrelenmis_data = dataFrame1[filtre1]

print(filtrelenmis_data)

filtre2 = dataFrame1.Age < 20

print(dataFrame1[filtre1 & filtre2])

print(dataFrame1[dataFrame1.Age > 60])
