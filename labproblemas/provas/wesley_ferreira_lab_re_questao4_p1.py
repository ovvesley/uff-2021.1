na = int(input())
nb = int(input())
nc = int(input())

cidades = [na, nb, nc]
custo_cidade = [0, 0, 0]
for idx_i in range(len(cidades)):
    cidade_destino = cidades.copy()
    cidade_destino[idx_i] = None

    for idx_j in range(len(cidade_destino)):
        if cidade_destino[idx_j]:
            passagem = abs(idx_j - idx_i)
            custo = cidades[idx_j] * passagem * 2
            custo_cidade[idx_i] += custo

custo_cidade.sort()
print(custo_cidade[0])