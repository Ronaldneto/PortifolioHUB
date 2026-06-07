print("Digite 0 para encerrar.\n")

valor = float(input("Digite um valor: "))

if valor == 0:
    print("Nenhum valor foi digitado.")
else:
    quantidade = 1
    soma = valor
    maior = valor
    menor = valor
    maior_ou_igual_50 = 1 if valor >= 50 else 0

    while True:
        valor = float(input("Digite um valor: "))

        if valor == 0:
            break

        quantidade += 1
        soma += valor

        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

        if valor >= 50:
            maior_ou_igual_50 += 1

    media = soma / quantidade

    print("\nRESULTADOS:")
    print("Quantidade:", quantidade)
    print("Soma:", soma)
    print("Média:", media)
    print("Maior valor:", maior)
    print("Menor valor:", menor)
    print("Valores maiores ou iguais a 50:", maior_ou_igual_50)
