class Calisan:

    zam_orani = 1.8
    counter = 0

    def __init__(self,isim,soyisim,maas): #constructor

        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@asd.com"
        Calisan.counter = Calisan.counter + 1

    def giveNameSurname(self):
        return self.isim + " " + self.soyisim   
    
    def zam_yap(self):
        self.maas = self.maas + self.maas * self.zam_orani
    
calisan1 = Calisan("ali","veli",100.0)
print("ilk maas:",calisan1.maas)
calisan1.zam_yap()
print("son maaş:",calisan1.maas)
print(calisan1.counter)

calisan2 = Calisan("ayşe","hatice",200.0)
print(calisan2.counter)