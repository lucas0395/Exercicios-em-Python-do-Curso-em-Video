# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais o dia e 0.15 reais por km rodado

d=int(input("Quantidade de dias alugados:"))
km=int(input("Quantidade de km rodados:"))
a=d*60
b=km*0.15
c=a+b
print("O carro foi alugado por {} dias e rodou {}km, entao o valor do aluguel é de {:.2f} reais".format(d,km,c))