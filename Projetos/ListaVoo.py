nomes = [] 
destinos = []

continua = "s"
while continua == "s":
    nome = input("Faça sua reseva, falando seu nome: ")
    nomes.append(nome) 

    destino = input("Faça sua reseva, falando seu destino: ")
    destinos.append(destino)

    continua = input("Deseja continuar? (s/n): ")

for nome in nomes, destino in destinos:
    print(f"{nome} sua viagem foi reservada para {destino}")