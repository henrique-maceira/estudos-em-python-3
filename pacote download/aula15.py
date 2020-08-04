import random
'''
#===exercício01===
c = soma = 0
while True:
    val = int(input("Insira o valor: "))
    if(val != 999):
        c += 1
        soma += val
    else:
        break
print(f"Você digitou {c} números e a soma deles é equivalente a {soma}.")

#===exercício02===
c = 0
while True:
    x = int(input("Insira o número: "))
    while ( x < 0):
        for c in range(0, 11):
            print(f"{x} x {c} = {(c*x)}")
            c += 1
        print("=====================================")
        x = int(input("Insira um novo número: "))
    else:
        print("Você encerrou o processo.")
        break

#===exercício03===
vit = soma = 0
while True:
    comp = random.randint(1, 10) 
    esc1 = int(input("Escolha um número de 0 a 10: "))
    esc2 = str(input("Escolha par ou ímpar [P/I]: ")).upper()
    soma = (esc1 + comp)
    print(f"o computador escolheu o número {comp} e a soma é {soma}")
    if (esc2 == "P" and soma % 2 == 0):
        vit += 1
    elif(esc2 == "I" and soma % 2 != 0):
        vit += 1
    else:
        print(f"Você ganhou {vit} vezes.")
        break

#===exercício04===
conti = conth = contm = 0
while True:
    idad = int(input("Insira sua idade: "))
    sex = str(input("Insira o sexo [M/F]: ")).upper()
    if(idad >= 18):
        conti += 1
    elif(sex == "M"):
        conth += 1
    elif(sex == "F" and idad < 20):
        contm += 1
    resp = str(input("      Deseja continuar? [S/N]: ")).upper()
    if(resp == "N"):
        print(f"O número de pessoas com mais de 18 anos é de {conti}.\nO número de homens cadastrados é de {conth}.\nO número de mulheres cadastradas com menos de 20 anos é de {contm}.")
        break
'''
#===exercício05===

    
    