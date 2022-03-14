# Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando 0.50 centavos
# por km para viagens de ate 200km e 0.45 para viagens mais longas

d = int(input("Qual a distancia da viagem:"))
c = 0.5 * d
l = 0.45 * d
if d <= 200:
    print("A passagem vai custar {} reais".format(c))
else:
    print("A passagem vai custar {} reais".format(l))
