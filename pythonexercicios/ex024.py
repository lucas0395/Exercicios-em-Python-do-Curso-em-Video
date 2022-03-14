# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome santo

c=str(input("Digite o nome da cidade:")).strip()
print(c[:5].upper() == "SANTO")
