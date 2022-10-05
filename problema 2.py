from random import randint
n=int(input("Dati numarul de aruncari:"))
afisare=0
for i in range(n):
    i=randint(1,6)
    print(i)
    if i==6:
        afisare+=1
    else:
        afisare+=0
print("Numarul de afisari 6 este:", afisare)