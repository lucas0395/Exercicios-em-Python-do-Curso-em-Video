# Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome da pessoa

nome = str(input("Digite seu nome:")).strip()
n = nome.split()
print("Seu primeiro nome é {}".format(n[0]))
print("Seu ultimo nome é {}".format(n[(len(n) - 1)]))
