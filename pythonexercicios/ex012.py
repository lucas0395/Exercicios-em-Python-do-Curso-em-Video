# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

p=float(input("Qual é o preço do produto:"))
d=p*95/100
print("O preço do produto é {} e com o desconto vai pra {}".format(p,d))