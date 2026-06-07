print("Digite 0 para encerrar.\n")
print('Candidato 1: 1')
print('Candidato 2: 2 ')
print('Candidato 3: 3')
print('Nulos: 5')
print('Brancos: 6')
c1 = c2 = c3 = 0
nulos = 0
brancos = 0
total = 0

while True:
    voto = int(input("Digite o voto: "))

    if voto == 0:
        break

    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1


    total += 1


if total > 0:
    perc_nulos = (nulos / total) * 100
    perc_brancos = (brancos / total) * 100
else:
    perc_nulos = perc_brancos = 0

print("\nRESULTADOS:")
print("Candidato 1:", c1)
print("Candidato 2:", c2)
print("Candidato 3:", c3)
print("Nulos:", nulos)
print("Brancos:", brancos)
print("Percentual de nulos: ", perc_nulos,'%')
print("Percentual de brancos: ", perc_brancos, '%')
