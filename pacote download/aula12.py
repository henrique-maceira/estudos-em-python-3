import random

#===exercicío01===
vc = float(input("Insira o valor da casa: R$ "))
sal = float(input("Insira o salário: R$ "))
anos = int(input("Em quantos anos o pagamento será efetuado: "))
ns = ((sal*30)/100)
pr = (vc/anos)
if(pr > ns):
    print("Infelizmente não é possível efetuar o empréstimo.")
else:
    print("Você está qualificado para este empréstimo.")

#===exercício02===

#===exercício03===
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
if(n1 > n2):
    print("O primeiro valor ({}) é maior.".format(n1))
elif(n1<n2):
    print("O segundo valor({}) é maior.".format(n2))
else:
    print("Não existe maior valor, ambos são iguais.")

#===exercício04===
id = int(input("Insira o ano de nascimento: "))
ano = (2020 - id) 
if(ano < 18):
    print("Você ainda não tem idade o suficiente para se alistar. Faltam {} ano(s).".format(18-ano))
elif(ano > 18):
    print("Você já se alistou (ou deveria ter se alistado) há {} ano(s).".format(ano - 18))
else:
    print("Você possui 18 anos e deve se alistar este ano.")

#===exercício05===
n1 = float(input("Insira o valor da primeira nota: "))
n2 = float(input("Insira o valor da segunda nota: "))
mf = ((n1 + n2)/2)
if(mf < 5):
    print("Nota: {}. REPROVADO.".format(mf))
elif(mf >= 5 and mf < 7):
    print("Nota: {}. RECUPERAÇÃO.".format(mf))
else:
    print("Nota: {}. APROVADO.".format(mf))

#===exercício06===
nome = str(input("Insira o nome do atleta: "))
ano = int(input("Insira o ano de nascimento: "))
id = (2020 - ano)
if(id <= 9):
    print("Atleta: {}, idade: {}, categoria MIRIM".format(nome,id))
elif(id <=14):
    print("Atleta: {}, idade: {}, categoria INFANTIL".format(nome,id))
elif(id <=19):
    print("Atleta: {}, idade: {}, categoria JÚNIOR".format(nome,id))
elif(id <=20):
    print("Atleta: {}, idade: {}, categoria SÊNIOR".format(nome,id))
else:
    print("Atleta: {}, idade: {}, categoria MASTER".format(nome,id))

#===exercício07===
peso = float(input("Insira o seu peso: "))
alt = float(input("Insira sua altura: "))
imc = (peso/(alt**2))
print(imc)
if(imc < 18.5):
    print("Abaixo do peso.")
elif(imc >= 18.5 and imc < 25):
    print("Peso ideal.")
elif(imc >= 125 and imc < 30):
    print("Sobrepeso.")
elif(imc >= 30 and imc < 40):
    print("Obesidade.")
else:
    print("Obesidade mórbita.")

#===exercício08===
val = float(input("Preço do produto: "))
pag = int(input("1 = à vista dinheiro; 2 = à vista cartão; 3 = 2x no cartão; 4 = 3x ou mais no cartão.\nO método de pagamento desejado:"))
if(pag == 1):
    desc = ((val*10)/100)
    print("Preço a ser pago é de: R$ {}".format(val-desc))
elif(pag == 2):
    desc = ((val*5)/100)
    print("Preço a ser pago é de: R$ {}".format(val-desc))
elif(pag == 3):
    print("Preço a ser pago é de: R$ {}".format(val))
else:
    jur = ((val*20)/100)
    print("Preço a ser pago é de: R$ {}".format(val + jur))

#===exercício09===
choo = int(input("OPÇÕES:\n1-PEDRA; 2-PAPEL; 3-TESOURA\nSUA ESCOLHA: "))
bot = random.randint(1,3)
if (choo == 1):
    if(bot == 1):
        print("ambos jogaram pedra. EMPATE.")
    elif(bot == 2):
        print("bot jogou papel e ganhou da sua pedra.")
    else:
        print("bot jogou tesoura e perdeu para sua pedra.")
elif(choo == 2):
    if(bot == 1):
        print("bot jogou pedra e perdeu para seu papel.")
    elif(bot == 2):
        print("ambos jogaram papel. EMPATE.")
    else:
        print("bot jogou tesoura e ganhou do seu papel.")
elif(choo == 3):
    if(bot == 1):
        print("bot jogou pedra e ganhou da sua tesoura.")
    elif(bot == 2):
        print("bot jogou papel e perdeu para sua tesoura.")
    else:
        print("ambos jogaram tesoura. EMPATE.")
