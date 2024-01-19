yas = 10
name = "ali"
soyisim = "veli"

def func_quiz(yas ,name , *args, ayakkabi_num = 35):
    print("Cocugun ismi:", name, " yasi:", yas," ayak numarasi:", ayakkabi_num)
    print(type(name))
    print(float(yas))

    output = args[0]*yas

    return output

sonuc = func_quiz(yas, name,soyisim)
print("args[0]*yas: ",sonuc)