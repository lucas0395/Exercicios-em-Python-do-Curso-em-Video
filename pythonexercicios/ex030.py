# Crie um programa que leia um numero inteiro e diga se ele e par ou impar

n = int(input("Digite um numero:"))
m = n % 2
if m == 0:
    print("O numero {} é par".format(n))
else:
    print("O número {} e impar".format(n))
