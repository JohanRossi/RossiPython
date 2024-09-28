import random

sorteado = random.randint(0, 100)

tentativa = 0
maxtentativas = 3

while tentativa < maxtentativas:
    print("Digite um numero de 0 a 100: ")
    entrada = input()

    if entrada.isdigit():
        palpite = int(entrada)
        
        if palpite < 0 or palpite > 100:
            print("Por favor, digite um número entre 0 e 100.")
            continue

        if palpite == sorteado:
            print("Parabéns! Você acertou o número!")
            break
        else:
            tentativa += 1

            if palpite < sorteado:
                print("O número é maior.")
            else:
                print("O número é menor.")
            print(f"Tentativas restantes: {maxtentativas - tentativa}")
    else:
        print("Entrada inválida. Por favor, digite um número válido.")

if tentativa >= maxtentativas:
    print(f"Errou AAKAKKAKAKAKA o numero era: {sorteado}")

