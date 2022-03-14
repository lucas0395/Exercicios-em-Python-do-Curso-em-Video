# Escreva um programa que pergunte o salario de uma pessoa e calcule o seu aumento
# pra salarios superiores a 1250 reais calcule um aumento de 10%
# pra salarios iferiores ou iguais aumento de 15%

s = float(input("Digite o salario:"))
a = s * 115 / 100
b = s * 110 / 100
if s > 1250:
    print("O salario era {:.2f} com o aumento de 10% foi para {:.2f}".format(s, b))
else:
    print("O salario era {:.2f} com o aumento de 15% foi para {:.2f}".format(s, a))
