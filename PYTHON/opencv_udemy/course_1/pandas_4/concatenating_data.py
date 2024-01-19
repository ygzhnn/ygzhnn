import pandas as pd 

dictionary = {"Name":["Ali","Veli","Hilal","Evren","Ayse","Evren"],
              "Age":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.yeni_feature)

dataFrame1.drop(["yeni_feature"],axis=1,inplace=True)
# dataFrame1 = dataFrame1.drop(["yeni_feature"],axis=1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical
data_concat = pd.concat([data1,data2],axis=0)
print(data_concat)

#horizontal

maas = dataFrame1.Maas
age = dataFrame1.Age

data_h_concat = pd.concat([maas,age],axis=1)
print(data_h_concat)
