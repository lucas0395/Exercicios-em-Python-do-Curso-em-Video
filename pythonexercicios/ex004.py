# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

a = input("Digite algo:")
print("O tipo primitivo desse valor é:", type(a))
print("Só tem espaços ?", a.isspace())
print("È um número ?", a.isnumeric())
print("È alfabético ?", a.isalpha())
print("È alfanumérico ?", a.isalnum())
print("Está em maiúsculo ?", a.isupper())
print("Está em minúsculo ?", a.islower())
print("Está capitalizada ?", a.istitle())