# Faca um programa que leia 3 numeros e fale qual o maior e o menor deles

a = int(input("Digite um numero:"))
b = int(input("Digite um numero:"))
c = int(input("Digite um numero:"))
# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior numero
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
