import random
#===exercício 01===
num= int(input("Seu palpite:"))
sor= random.randint(1,5)
if (num == sor):
    print("O número sorteado foi {}.\nVocê é o bichão mesmo hein".format(sor))
else:
    print("O número sorteado foi {}.\nTente novamente".format(sor))

#===exercício02===
vel= float(input("velocidade do automóvel: "))
if(vel > 80):
    mult = float((vel-80)*7)
    print("O veículo estava acima do limite de velocidade.\nO valor da multa é de: R$ {}. ".format(mult))
else:
    print("O veículo estava dentro do limite de velocidade.")

#===exercício03===
num= int(input("Insira o número: "))
if(num %2 == 0):
    print("O número digitado é par.")
else:
    print("O número digitado é impar.") 

#===exercício04===
dist= float(input("Insira a distância da viagem em km:"))
if(dist <=200):
    print("O preço da passagem é de R${}.".format(0.5*dist))
else:
    print("O preço da passagem é de R${}.".format(0.45*dist))

#===exercício05===
ano = int(input("Insira o ano em questão:"))
if(ano % 4 == 0):
    print("O ano de {} é um ano bissexto.".format(ano))
else:
    print("O ano de {} não é um ano bissexto.".format(ano))

#===exercício06===
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))
if(n1 > n2 and n1 > n3):
    print("{} é o maior número.\n".format(n1))
elif(n2 > n1 and n2 > n3):
    print("{} é o maior número.\n".format(n2))
else:
    print("{} é o maior número.\n".format(n3))
if(n1 < n2 and n1 < n3):
    print("{} é o menor número.\n".format(n1))
elif(n2 < n1 and n2 < n3):
    print("{} é o menor número.\n".format(n2))
else:
    print("{} é o menor número.\n".format(n3))

#==exercício07===
sal= float(input("Insira o valor do salário: "))
if(sal <= 1250.0):
    ns = ((15*sal)/100)
    print("O seu aumento será de R${}.\nTotalizando R${}.".format(ns, (sal+ns)))
else:
    ns = ((10*sal)/100)
    print("O seu aumento será de R${}.\nTotalizando R${}.".format(ns, (sal+ns)))

#===exercício08===
a = float(input("Insira a medida da primeira reta: "))
b = float(input("Insira a medida da segunda reta: "))
c = float(input("Insira a medida da terceira reta: "))
if((b-c) < a < (b+c) and (a-c) < b < (a+c) and (a-b) < c < (a+b)):
    print("Essas 3 retas são capazes de formar um triângulo.")
else:
    print("Essas 3 retas não formam um triângulo.")