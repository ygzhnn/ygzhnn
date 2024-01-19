"""i = 0

while (i < 4):
    print(i)
    i = i + 1"""

liste = [1,2,3,4,5,6]

sinir = len(liste)
each = 0
count = 0
while (each < sinir):
    count = count + liste[each]
    each = each + 1
    print(count)