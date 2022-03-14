# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma area de 2m²

n=float(input("Largura da parede:"))
n1=float(input("Altura da parede:"))
a=n*n1
print("Sua parede tem a dimenção de {} x {} e sua área é de {}m²".format(n,n1,a))
t=a/2
print("Para pintar essa parede vc vai gastar {} litros de tinta".format(t))