# Escreva um provrama que converta .uma temperatura digitada em ºC e converta para ºF

c=float(input("Digite a temperatura em ºC:"))
f=((9*c)/5)+32
print("A temperatura de {}ºC conrresponde a {:.1f}ºF".format(c,f))