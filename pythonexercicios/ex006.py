# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a raiz quadrada

n = int(input("Digite um numero:"))
a = n * 2
b = n * 3
c = pow(n,1/2) # ou utilizar a funcao **
print("O dobro do número é {}\n O triplo é {}\nE a raiz quadrada é {}".format(a, b, c))
