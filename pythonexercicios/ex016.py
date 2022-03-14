# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

import math
num=float(input("Digite um valor :"))
print("O valor digitado foi {} e a parte inteira é {}".format(num, math.trunc(num)))