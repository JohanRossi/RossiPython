valor = float(input("Informe o valor da compra: "))
formadepagar = input(" A vista ou deseja financiar (Vista/Financiar): ")

x = 0
while formadepagar == "Vista":
    if valor < 500:
        vistafinal1 = valor - valor / 10 
        print(f"O valor final da sua compra é: {vistafinal1:.2f}")
    if valor < 1000:
        vistafinal1 = valor - valor / 6.66
        print(f"O valor final da sua compra é: {vistafinal1:.2f}") 
    else:
        vistafinal1 = valor - valor / 5
        print(f"O valor final da sua compra é: {vistafinal1:.2f}")
while  formadepagar == "Financiar":
    parcelas = int(input("Quantas parcelas você gostaria de aplicar: "))

    if valor > 800 and parcelas < 5:
        mensal = valor / parcelas
        print(f"Você pagara R${mensal:.2f} por {parcelas} meses até o valor final R${valor} ser pago.")

    if parcelas >= 19:
            print("O numero maximo de parcelas é 18!")

    if valor > 800 and parcelas > 10:
        if parcelas == 11:
            financiarfinal1 = valor / 20 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break

        if parcelas == 12:
            financiarfinal1 = valor / 15.38 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break

        if parcelas == 13:
            financiarfinal1 = valor / 14.28 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break

        if parcelas == 14:
            financiarfinal1 = valor / 11.11 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break

        if parcelas == 15:
            financiarfinal1 = valor / 10.52 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break

        if parcelas == 16:
            financiarfinal1 = valor / 10 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break

        if parcelas == 17:
            financiarfinal1 = valor / 8.84 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break

        if parcelas == 18:
            financiarfinal1 = valor / 8,33 + valor
            valor2 = financiarfinal1 / parcelas
            print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")
            break
            
        print(f"Você pagara R${valor2:.2f} por {parcelas} meses até o valor final R${financiarfinal1:.2f} ser pago.")

    else:
        print("Apenas compras com mais de 800 reais podem aceitar mais de 5 parcelas.")

                
