# Crie um progarama que leia o nome completo de uma pessoa e mostre
# o nome com tdas as letras maiusculas e minusculas
# quantas letras ao tdo sem contar os espacos
# quantas letras tem o primeiro nome

nome = str(input("Digite seu nome:")).strip()
print("Seu nome em maiusucula é: {}".format(nome.upper()))
print("Seu nome em minuscula é: {}".format(nome.lower()))
print("Seu nome possui {} letras".format(len(nome) - nome.count(" ")))
print("eu primeiro nome tem {} letras".format(nome.find(' ')))
