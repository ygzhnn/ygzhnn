import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

a = pd.concat([dataFrame1["NAME"],dataFrame1["MAAS"]],axis=0)
print(a)