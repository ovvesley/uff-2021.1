TAM = 500 + 1
n = int(input())

matriz = []
for i in range(TAM):
    matriz.append([])
    for j in range(TAM):
        matriz[i].append(0)

msm_lugar = 0
for _ in range(n):
    x, y = list(map(int, input().split()))
    matriz[x][y] += 1
    if matriz[x][y] > 1:
        msm_lugar = 1
        break


print(msm_lugar)
