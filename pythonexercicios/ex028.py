# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar
# descobrir qual foi o numero escolhido pelo computador
# o programa devera escrever na tela se o usuario venceu ou perdeu

import random

n = int(input("Digite um numero de 0 a 5:"))
lista = [0, 1, 2, 3, 4, 5]
d = random.choice(lista)
if n == d:
    print("Parabens vc acertou")
else:
    print("Voce errou o numero escolhido foi {} e vc digitou {}".format(d, n))
