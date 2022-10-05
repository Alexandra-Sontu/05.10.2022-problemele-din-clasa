from random import randint
n=int(input("Dati numarul de numere:"))    
Sp=0
Sn=0
for i in range(n):
    i=randint(-50,50)
    print(i)
    if i>0:
        Sp+=i
    if i<0:
        Sn+=i
print("Suma numerelor pozitive este:", Sp)
print("Suma numerelor negative este:", Sn)