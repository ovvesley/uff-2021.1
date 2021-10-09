n = int(input())
pesos = list(map(int, input().split()))

pesos.sort(reverse=True)
res = "S"
for index_i in range(len(pesos)):

    if index_i + 1 >= len(pesos):
        val_next = 0
    else:
        val_next = pesos[index_i + 1]

    diff = abs(pesos[index_i] - val_next)

    if diff > 8:
        res = "N"

print(res)