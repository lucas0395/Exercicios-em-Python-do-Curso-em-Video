# Crie um programa que leia o nome de uma pessoa e diga se tem silva no nome

nome = str(input("Digite seu nome:")).strip().upper()
print("Seu nome tem Silva ? {}".format("SILVA" in nome))
