# Criação do vetor de 10 posições reais
vetClasse = [0.0] * 10

# Inicialização das variáveis simples
soma = 0
notaAcima = 0

# Loop de leitura de notas
for x in range(10):
    vetClasse[x] = float(input(f'Nota {x + 1}: '))

# Loop para calcular a soma das notas
for x in range(10):
    soma += vetClasse[x]

# Cálculo da média
media = soma / 10

# Loop para contar as notas acima da média
for x in range(10):
    if vetClasse[x] > media:
        notaAcima += 1

# Exibição do resultado
print(f'Média das notas: {media}')
print(f'Número de notas acima da média: {notaAcima}')
