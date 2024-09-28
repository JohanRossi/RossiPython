import os

nome = input("Digite seu nome: ")


idade = int(input('Qual sua idade: '))
os.system('cls')

print('======================================')
altura = float(input('Qual sua altura: '))

print('\n')
peso = int(input('Qual seu peso: '))
print('======================================')
print('\n')
os.system('cls')

imc = peso / (altura * altura)
print(f"Prazer {nome} seu imc é {imc:.2f} e você tem {idade} anos!")




