#cemberin cevre uzunlugu = 2 * pi * r


#DEFAULT
"""def cember_cevre_hesapla(r, pi = 3.14):
    
    Çember çevresi hesaplama
    input = r
    output = çemperin çevresi
    
    

    output = 2 * pi * r
    return output

cember_cevre_hesapla(2)"""

#FLEXIBLE
def hesapla(boy,kilo,*args): #*args daha sonradan daha fazla parametre ekleyebilmemizi sağlar
    output = boy*kilo
    return output


print(hesapla(1,2,2))
print(hesapla(1,2))