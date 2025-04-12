vetLido = [0.0] * 10
vetPar = [0.0] * 10
vetImpar = [0.0] * 10

for x in range(10):
    vetLido[x] = int(input(f'Numero{x + 1}: '))

P = 0
I = 0
for x in range(10):
    if vetLido[x] % 2 == 0:
        vetPar[P] = vetLido[x]
        P += 1
else:
    vetImpar[I] = vetLido[x]
    I += 1
print(f'vetor lido:{vetLido}')
print(f'vetor PAR, TAMANHO {P}:{vetPar[0:P]}')