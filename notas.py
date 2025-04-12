vetLido = [0.0] * 10
vetDes = [0.0] * 10

# Leitura dos valores
for x in range(10):
    vetLido[x] = float(input(f'Valor {x+1}: '))

# Cálculo da média dos valores lidos
mediaLido = sum(vetLido) / 10

# Cálculo da distância de cada valor até a média
for x in range(10):
    vetDes[x] = abs(vetLido[x] - mediaLido)

# Cálculo da média das distâncias
mediaDesvio = sum(vetDes) / 10

# Exibindo resultados
print(f'Média dos valores lidos: {mediaLido:.2f}')
print(f'Média dos desvios: {mediaDesvio:.2f}')
