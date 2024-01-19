import pandas as pd 

dictionary = {"Name":["Ali","Veli","Hilal","Evren","Ayse","Evren"],
              "Age":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.Age]
print(dataFrame1.list_comp)

def multiply(age):
    return age*2
print(dataFrame1)

dataFrame1["apply_metodu"] = dataFrame1.Age.apply(multiply)
print(dataFrame1)