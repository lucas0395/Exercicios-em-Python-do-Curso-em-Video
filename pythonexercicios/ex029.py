# Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80km/hr, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar 7 reais por kda km acima do limite

v = int(input("Qual a velocidade do carro:"))
m = (v - 80) * 7
if v <= 80:
    print("Voce esta dentro do limite de velocidade")
else:
    print("Voce ultrapassou o limite e sua multa é de {} reais".format(m))
