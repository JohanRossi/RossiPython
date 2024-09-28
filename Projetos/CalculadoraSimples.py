n1 = float(input("Digite numero 1: "))
n2 = float(input("Digite numero 2: "))

resposta = input("Escolha a sua Soma: \nSoma(+) \nSubtração(-) \nMultiplicação(*) \nDivisão(/)\n")

soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2

if (resposta == '+'):
    print(f'A soma é {soma}')
elif (resposta == '-'):
    print(f'A subtração é {sub}')
elif (resposta == '*'):
    print(f'A multiplicação é {multi}')
elif (resposta == '/'):
    if n1 == 0 or n2 == 0:
        print("O numero não pode ser divido por zero")
    else:
        print(f'A divisão é {div}')
else :
    print('Valor invalido, digite apenas as opções mostradas.')
    