# Faça um prgrama que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e
# mostre o comprimento da hipotenusa
import math

ca = float(input("Digite o cateto adjacente:"))
co = float(input("Digite o cateto oposto:"))
hip = math.hypot(ca, co)
a = ((ca**2)+(co**2))**(1/2)
print("O valor da hipotenusa é {:.2f}".format(hip))
