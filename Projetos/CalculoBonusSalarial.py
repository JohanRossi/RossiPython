salario = float(input("Me diga o seu salario: "))
tempo = float(input("Me diga o tempo em anos: 1300"))

if tempo > 5:
    bonus = salario / 20 + salario

    print(f"Seu salario atual com 5% de bonus é {bonus}")
else:
    print(f"Seu salario atual é {salario}")