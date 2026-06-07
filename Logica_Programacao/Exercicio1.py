print('DIGITE (0) para sair!')
somapar = 0
somaimpar = 0

numerospares = 0
numerosimpares = 0

while True:
    numero = int(input("Digite um numero inteiro: "))
    if numero == 0:
        break

    if numero % 2 == 0:
        numerospares = numerospares + 1
        somapar = somapar + numero
    else:
        numerosimpares = numerosimpares + 1
        somaimpar = somaimpar + numero


mediapar = somapar / numerospares
mediaimpar = somaimpar / numerosimpares

print('Média dos números pares digitados: ', mediapar)
print('Média dos números impares digitados: ', mediaimpar)



