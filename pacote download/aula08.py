import math
import random

#===exercício 01===
num= float(input("Insira o número: "))
num1= math.floor(num)
print("O número {} tem a parte inteira {}".format(num, num1))

#===exercício 02===

co= float(input("Insira o comprimento do cateto oposto: "))
ca= float(input("Insira o comprimento do cateto adjacente: "))
hip= math.sqrt(co**2 + ca**2)
print("O valor da hipotenusa é de: {} m.".format(hip))

#===exercício 03===

ang= int(input("Insira o valor do ângulo: "))
sen= math.sin(ang)
cos= math.cos(ang)
tg= math.tan(ang)
print("Seno: {}, Cosseno: {}, Tagente: {}.".format(sen,cos,tg))

#===exercício 04===

num= random.randint(1,4)
print("O número sorteado foi {}".format(num))
if(num == 1):
    print("Jorginho foi o escolhido")
elif(num == 2):
    print("Clebinho foi o escolhido")
elif(num == 3):
    print("juninho foi o escolhido")
else:
    print("joãozinho foi o escolhido")

#===exercício 05===

a1 = str(input("Nome do aluno 1: "))
a2 = str(input("Nome do aluno 2: "))
a3 = str(input("Nome do aluno 3: "))
a4 = str(input("Nome do aluno 4: "))
lista= (a1, a2, a3, a4)
random.shuffle(lista)
print("A ordem de apresentação será:")
print(lista)