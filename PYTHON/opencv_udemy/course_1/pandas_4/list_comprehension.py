import numpy as np
import pandas as pd



dictionary = {"Name":["Ali","Veli","Hilal","Evren","Ayse","Evren"],
              "Age":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

ortalama_maas = np.mean(dataFrame1.Maas)

dataFrame1["maas_seviyesi"] = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.Maas]

"""for each in dataFrame1.Maas:
    if(ortalama_maas > each):
        print("dusuk")
    
    else:
        print("yuskek")"""

print(dataFrame1.maas_seviyesi)


dataFrame1.columns = [ each.lower() for each in dataFrame1.columns  ]

dataFrame1.columns = [each.split()[0] +"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]