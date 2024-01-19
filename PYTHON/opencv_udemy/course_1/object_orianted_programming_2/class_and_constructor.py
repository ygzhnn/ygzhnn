class Calisan:

    def __init__(self,isim,soyisim,maas): #constructor

        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@asd.com"

    def giveNameSurname(self):
        return self.isim + " " + self.soyisim


isci1 = Calisan("ali","veli",100)
print(isci1.isim)
print(isci1.email)

print(isci1.giveNameSurname())
print(isci1.maas)