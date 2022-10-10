from random import randint
a=randint(0,999999999)
val=[0,0,0,0,0,0,0,0,0,0]
while a>0:
    val[a%10]+=1
    a//=10
for i in range(0,10):
    print("Cifra ",i," se repeta de ",val[i]," ori")