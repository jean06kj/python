vetLido = [0] * 10
vetPar = [0] * 10
vetImpar = [0] * 10

P = 0  # Contador de pares
I = 0  # Contador de ímpares

# Leitura dos números
for x in range(10):
    vetLido[x] = int(input(f'Número {x + 1}: '))

# Separação de pares e ímpares
for x in range(10):
    if vetLido[x] % 2 == 0:
        vetPar[P] = vetLido[x]
        P += 1
    else:
        vetImpar[I] = vetLido[x]
        I += 1

# Impressão dos resultados
print(f'\nVetor lido: {vetLido}')
print(f'Vetor PAR (tamanho {P}): {vetPar[:P]}')
print(f'Vetor ÍMPAR (tamanho {I}): {vetImpar[:I]}')
