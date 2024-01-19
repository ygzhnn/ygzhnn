# 1) Pandas hızlı ve etlili for dataframes
# 2) CSV ve text dosyalarına açıp inceleyip sonuçlarımızıda bu dosya tiplerine kayedebilriz
# 3) Pandas bizim işimizi kolaylaştırıyor for missing data
# 4) Reshape yapıp datayı daha etkili bir şekilde kullanabiliriz
# 5) Slicing ve indexing kolay
# 6) Time series data analizinde çok yardımcı
# 7) Ayrica her şeyden önemlisi hız. Pandas hız açısından optimize edilmiş hızlı bir kütüphane

import pandas as pd 

dictionary = {"Name:":["Ali","Veli","Hilal","Evren","Ayse","Evren"],
              "Age:":[15,16,17,33,45,66],
              "Maas":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head(6) #değer girmezsek ilk 5 i bastırır
print(head)

tail = dataFrame1.tail() # değer girmezsek son 5 i bastırır
print(tail)