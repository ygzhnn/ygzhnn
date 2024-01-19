import pandas as pd 

dictionary = {"Name":["Ali","Veli","Hilal","Evren","Ayse","Evren"],
              "Age":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

"""print(dataFrame1["Name"])
print(dataFrame1.Age)

dataFrame1["Yeni_Feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.Yeni_Feature)

print(dataFrame1.loc[:3,"Age"]) #pandasta 3 yazdığımızda 3. elemanı da bastırır"""

print(dataFrame1.loc[:3, ["Age","Name"]])

print(dataFrame1.loc[::-1])

print(dataFrame1.loc[:,:"Name"])

print(dataFrame1.iloc[:,2])