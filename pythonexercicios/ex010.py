# Crie um programa que mostro quanto de dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar considere:
# 1 dolar = 3.27 reais

n=float(input("Digite o valor em reais:"))
n1=n/3.27
print("Você tem {:.2f} reais e pode comprar {:.2f} dólares".format(n,n1)) # :.2f mostra q auntidade de casas decimais que vai mostrar
