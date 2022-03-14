# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra A
# em que posição ela aparece pela primeira vez
# em que posicao ela aparece na ultima vez

f = str(input("Digite a frase:")).strip().upper()
print("A letra A aparece {} vezes na frase".format(f.count("A")))
print("A letra A aparece pela primera vez na posição {}".format(f.find("A")+1))
print("A letra A aparece pela ultima vez na posição {}".format(f.rfind("A")+1))
