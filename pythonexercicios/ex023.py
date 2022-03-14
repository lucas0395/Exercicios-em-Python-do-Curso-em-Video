# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um de seus digitos
# Ex: 1834   4 unidades 3 dezenas 8 centenas e 1 milhar

num = int(input("Digite um numero:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Unidade:{}".format(u))
print("Dezena:{}".format(d))
print("Centena:{}".format(c))
print("Milhar:{}".format(m))
