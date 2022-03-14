# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
a=input("Digite o nome do primeiro aluno:")
b=input("Digite o nome do segundo aluno:")
c=input("Digite o nome do terceiro aluno:")
d=input("Digite o nome do quarto aluno:")
lista=[a,b,c,d]
random.shuffle(lista)
print("O aluno escolhido foi {}".format(lista))