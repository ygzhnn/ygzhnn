var1 = 10
var2 = 20

if (var1 > var2):
    print("var1 büyüktür var2 den")

elif (var1 == var2):
    print("var1 ve var2 eşittir")

else:
    print("var2 büyüktür var1")

liste = [1,2,3,4,5,6]

value = 3

if value in liste:
    print("evet {} değeri listenin içinde".format(value))

else:
    print("hayir")


dictionary = {"Ali":18,"Veli":19,"Ayşe":20}

keys = dictionary.keys()

if "Ali" in keys:
    print("evet")

else:
    print("hayır")


if "Can" in keys:
    print("evet")

else:
    print("hayır")

