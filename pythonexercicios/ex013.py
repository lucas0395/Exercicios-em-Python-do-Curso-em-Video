# Faça um algoritmo que leia o salário de um funcionário ee mostre o seu novo salário, com 15% de aumento

s = float(input("Digite o salário:"))
a = s * 115 / 100
print("O antigo salário é {} e com o aumento de 15% vai para {:.2f}".format(s, a))
