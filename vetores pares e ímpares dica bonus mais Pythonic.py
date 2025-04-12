# Criando os vetores com 10 posições, inicialmente preenchidos com 0
vetLido = [0] * 10        # Vai armazenar os números digitados
vetPar = [0] * 10         # Vai armazenar os números pares
vetImpar = [0] * 10       # Vai armazenar os números ímpares

P = 0  # Contador para controlar a posição no vetor de pares
I = 0  # Contador para controlar a posição no vetor de ímpares

# Leitura de 10 números inteiros do usuário
for x in range(10):
    vetLido[x] = int(input(f'Número {x + 1}: '))  # Armazena cada número no vetor vetLido

# Laço para separar os números em pares e ímpares
for x in range(10):
    if vetLido[x] % 2 == 0:       # Verifica se o número é par
        vetPar[P] = vetLido[x]    # Armazena o número no vetor de pares
        P += 1                    # Incrementa o contador de pares
    else:
        vetImpar[I] = vetLido[x]  # Armazena o número no vetor de ímpares
        I += 1                    # Incrementa o contador de ímpares

# Impressão dos resultados
print(f'\nVetor lido: {vetLido}')               # Mostra todos os números digitados
print(f'Vetor PAR (tamanho {P}): {vetPar[:P]}') # Mostra apenas os pares armazenados (fatiado até P)
print(f'Vetor ÍMPAR (tamanho {I}): {vetImpar[:I]}') # Mostra os ímpares (fatiado até I)

# Você lê 10 números e armazena no vetor vetLido.
# Depois percorre esse vetor e verifica se cada número é par ou ímpar.
# Dependendo da verificação, o número vai para vetPar ou vetImpar.
#O uso de P e I serve para controlar quantos números realmente foram armazenados em cada vetor.
#No final, os vetores são fatiados com [:P] e [:I] para mostrar apenas os valores válidos (evita exibir os zeros que sobraram).




