# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tagente desse angulo

import math

a = int(input("Digite o angulo:"))
b = math.radians(a)
sen = math.sin(b)
cos = math.cos(b)
tan = math.tan(b)
print("O seno desse âgulo é {:.2f}".format(sen))
print("O cosseno desse âgulo é {:.2f}".format(cos))
print("a tangente desse âgulo é {:.2f}".format(tan))
