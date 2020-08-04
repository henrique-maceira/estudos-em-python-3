# ===exercicio01===
n= int(input("Insira o valor de n: "))
print("{} , {} , {}".format((n-1),(n),(n+1)))

# ===exercicio02===
n= float(input("Insira o valor de n: "))
print("{}, {}, {}".format((n*2), (n*3), (n**(1/2))))

# ===exercicios03===
n1= float(input("Valor da nota 1: "))
n2= float(input("Valor da nota 2: "))
m= float((n1+n2)/2)
print("O valor da média é {}".format(m))

# ===exercicio04===
m= float(input("Insira o valor em metros: "))
c= float(m*100)
mi= float(m*1000) 
print("{} metros equivalem a {} centímetros e {} milímetros".format(m, c, mi))

# ===exercicio06===
n= float(input("Insira a quantidade em reais que você possui: "))
print("Com {} reais, você é capaz de comprar {} dólares.".format(n, (n/3.27)))

# ===exercicio07===
lar= float(input("Insira a largura da parede: "))
alt= float(input("Insira a altura da parede: "))
area= float(lar*alt)
print("São necessários {} litros de tinta para pintar {} m²".format((area*2), area))

# ===exercicio08===
p= float(input("Insira o preço do produto: "))
d= float((5*p/100))
print("Com o desconto de R${}, o preço vai de R${} para R${}".format(d, p, (p-d)))

# ===exercicio09===
s= float(input("Insira o valor do salário: "))
a= float((15*s/100))
print("Com um aumento de 15%, seu salário vai de R${}, para R${}".format(s, (s+a)))

