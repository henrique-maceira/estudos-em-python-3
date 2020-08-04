print ("olá mundo")
num = int(input("Insira o RA:"))
n1 = int(input("Insira a nota da primeira prova:"))
n2 = int(input("Insira a nota da segunda prova:"))
total = ((n1 + n2)/2)
if (total>=5):
    print("O aluno de RA", num,"obteve", total, "como nota final e foi aprovado")
else:
    print("O aluno de RA", num, "obteve", total, "como nota final e não foi aprovado")