n, tam_pino = list(map(int, input().split()))
pinos = list(map(int, input().split()))
pinos_sum = pinos.copy()

aux = 0
for index_i in range(len(pinos)):
    if index_i + 1 >= len(pinos):
        continue
    diff = tam_pino - pinos_sum[index_i]
    pinos_sum[index_i]+= diff
    pinos_sum[index_i+1] += diff
    aux += abs(diff)
print(aux)