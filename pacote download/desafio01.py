print ("====DESAFIO N°1====")
nome = input("Nome de usuário: ")
print ("Seja bem vindo(a)", nome)

print ("====DESAFIO N°2====")

dia = int(input("Dia de nascimento:"))
if (dia>31):
    print("erro, por favor digite novamente")
    
mes = input("Mês de nascimento:")
ano = input("Ano de nascimento:")
print(dia, "/", mes, "/", ano)

    

print ("====DESAFIO N°3====")

n1 = int(input("Insira o primeiro número a ser calculado:"))
n2 = int(input("Insira o segundo número a ser calculado:"))
total = (n1 + n2)
print("A soma de ", n1, "com ", n2, "é igual a ", total)
