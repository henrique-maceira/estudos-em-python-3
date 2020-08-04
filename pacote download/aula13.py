
#===exercício01===
for c in range(10, -1, -1,):
    print (c)

#===exercício02===
for c in range(1, 51):
    if (c%2 == 0):
        print(c)

#===exercício03===
s = 0
for c in range (1, 501):
    if(c%2 != 0 and c%3 == 0):
        s = s + c
print(s)

#===exercício04===
s = 0
for c in range (1, 7):
    a = int(input("Insira o número: "))
    if (a%2 == 0):
        s = s + a
print(s)

#===exercício05===
term = int(input("Insira o primeiro termo: "))
raz = int(input("Insira a razão da PA: "))
t = term
print(term)
for c in range (1, 10):
    t = t + raz 
    print(t)

#===exercício06===
n = int(input("Insira um número: "))
d = 0
for c in range(1, 11):
    if(n%c==0):
        d = (d + 1) 
if(d > 2): 
    print("{} não é um número primo.".format(n))
elif(d <= 2):
    print("{} é um número primo.".format(n))

#===exercício07===
d = 0
n = 0
for c in range(1,8):
    a = int(input("Ano de nascimento: "))
    if((2020 - a) >= 18):
        d = d + 1
    else:
        n = n + 1
print("{} pessoas já atingiram a maioridade.\n{} pessoas ainda não atingiram a maioridade.".format(d, n))

#===exercício08===
maip = 0
menp = 110
for c in range(1, 6):
    pes = float(input("Insira seu peso: "))
    if(pes > maip):
        maip = pes
    elif(pes < menp):
        menp = pes
print ("{} é o maior peso e {} é o menor peso.".format(maip, menp)) 

#===exercício09===
med = 0
maip = 0
mul = 0
name = 0
for c in range(1,5):
    nom = str(input("Insira o nome: "))
    idad = int(input("Insira a idade: "))
    sex = str(input("M/F: "))
    med = med + idad
    if(sex == "M" or sex == "m" and idad > maip):
        name = nom
        maip = idad
    elif(sex == "F" or sex == "f" and idad <20):
        mul = mul + 1
print("A média de idade do grupo é {}.\nO homem mais velho é {} e possui {} anos.\nHá {} mulheres com menos de 20 anos.".format((med/4),name, maip, mul))