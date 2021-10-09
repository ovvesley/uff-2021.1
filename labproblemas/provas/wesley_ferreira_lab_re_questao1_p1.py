n, t = list(map(int, input().split()))
jogadas = list(map(int, input().split()))

pontuacao = [0 for _ in range(n)]

maior_pont = 0
maior_som = 0
indice_vencedor = 0
for index in range(len(jogadas)):
    idx_jogador = index % n
    pontuacao[idx_jogador] += jogadas[index]

    if jogadas[index] >= maior_pont:
        maior_pont = jogadas[index]
        if pontuacao[idx_jogador] >= maior_som:
            maior_som = pontuacao[idx_jogador]
            indice_vencedor = idx_jogador
    elif pontuacao[idx_jogador] >= maior_som:
         indice_vencedor = idx_jogador
         maior_som = pontuacao[idx_jogador]

print(indice_vencedor + 1)
