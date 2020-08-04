import random

#===exercício01===
se = "A"
while(se != "M" and se != "F"):
    se = str(input("Insira o sexo (M/F): ")).upper()
    if (se == "M"):
        print("O sexo inserido foi masculino.")
    elif(se == "F"):
        print("O sexo escolhido foi feminino.")

#===exercício02===
num= int(input("Seu palpite:"))
sor= random.randint(1,5)
c = 1
while(num != sor):
    num = int(input("Não foi dessa vez. Faça outro palpite: "))
    c = c + 1
    if (num == sor):
        print("O número sorteado foi {}.\nVocê levou {} tentativas para acertar".format(sor, c))

#===exercício03===
opc = 4
while(opc == 4):
    print("Bem vindo")
    val1 = int(input("Insira o primeiro valor: "))
    val2 = int(input("Insira o segundo valor: "))
    opc = int(input("Escolha a ação a ser feita:\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\n"))
    if(opc == 1):
        soma = (val1 + val2)
        print("Você escolheu soma, e o resultado é {}.".format(soma))
    elif (opc == 2):
        mult = (val1 * val2)
        print("Você escolheu multiplicação, e o resultado é {}.".format(mult))
    elif(opc == 3):
        if(val1> val2):
            print("O maior valor é {}.".format(val1))
        elif(val1 < val2):
            print("O maior valor é {}.".format(val2))
        else:
            print("Os valores são iguais.")
    elif(opc == 5):
        print("Até breve :) ")

#===exercício04===
val = int(input("Insira o valor: "))
fat = c = val
while (c != 2):
    fat = fat * (val- 1)    
    c = c - 1                     
    val = val - 1                 
print(fat) 

#===exercício05===
val = c = soma = 0
while( val!= 999):
    val= int(input("Insira o número: "))
    if(val != 999):
        c = c + 1 
        soma = soma + val
print("Você encerrou a contagem.\nVocê digitou {} números, e a soma deles é {}.".format(c, soma))

#===exercício06===
val = c = media = soma = 0
resp = "S"
lista = []
while(resp == "S"):
    val = int(input("Insira o número: "))
    resp = str(input("Deseja adicionar mais valores? [S/N]: ")).upper()
    lista.append(val)
    soma = soma + val
    c = c + 1
    media = (soma/c)
print("A média entre os valores digitados foi de {}\nO maior termo foi {}\nO menor termo foi {}".format(media, max(lista), min(lista)))
