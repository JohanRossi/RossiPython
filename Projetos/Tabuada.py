numero = int(input("Fale o numero que queira saber a tabuada: "))
i = 0

while i < 11:
    vezes = numero * i
    print(f"{numero} x {i} = {vezes}")
    i = i + 1