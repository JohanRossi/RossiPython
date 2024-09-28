
nome = input("Digite seu nome: ")

print("Olá, "+ nome +"!")
print("Olá,", nome+ "!")
print("Olá, %s!" %nome)
print("Olá, {}!".format(nome))
print(f"Olá, {nome}!")

idade = int(input('Qual sua idade? \n'))

altura = float(input('Qual sua altura? \n'))
peso = int(input('Qual seu peso? \n'))

imc = peso / (altura * altura)
print(f"Prazer {nome} seu imc é {imc:.2f} você tem {idade} anos!")

if (idade < 18):

  print("Voce não pode entrar, tem q ter mais de 18 anos!")



