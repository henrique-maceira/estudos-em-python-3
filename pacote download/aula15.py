import random

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

#===exercício05===
mil = soma = produto = barato = 0
barato = 5000000000
name = str
while True:
        prod = str(input("Insira o nome do produto: "))
        val = float(input("Insira o preço do produto: "))
        soma += val
        if (val > 1000):
            mil += 1
        if (val < barato):
            barato = val
            name = prod
        resp = str(input("Deseja inserir outro produto? [S/N]: ")).upper()
        if (resp == "N"):
            print(f"Você gastou R$ {soma}.\n{mil} produtos custam mais que mil reais e o item mais barato é o (a): {name}.")
            break

#===exercício06=== *A SER FINALIZADO*
op1 = cont2 = cont3 = cont4 = cont5 = 0
while True:
    sac = int(input("Insira o valor a ser sacado: "))
    if((sac/50)%2 == 0):
        op1 = (sac/50)
        print(f"Você receberá {op1} notas de R$50.")
        break
    else:
        while ((sac - 50)>50):
            sac = sac - 50
            cont2 += 1
        while ((sac - 20)<50 and (sac - 20)>=20):
            sac = sac - 20
            cont3 += 1
        while ((sac - 10)<20 and (sac - 10)>=10):
            sac = sac - 10
            cont4 += 1
        while ((sac - 1)<10):
            sac = sac - 1 
            cont5 += 1
        print(f"Você receberá {cont2} notas de R$50.\n{cont3} notas de R$20.\n{cont4} notas de R$10.\n{cont5} notas de R$1,00.")
        break
        
    