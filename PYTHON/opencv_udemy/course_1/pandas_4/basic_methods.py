import pandas as pd 

dictionary = {"Name:":["Ali","Veli","Hilal","Evren","Ayse","Evren"],
              "Age:":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1.columns)
print(dataFrame1.info()) #pandas string yerine object yazar
print(dataFrame1.dtypes)
print(dataFrame1.describe()) #numeric feature = columns (age,maas)