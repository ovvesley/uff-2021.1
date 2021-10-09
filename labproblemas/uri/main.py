import sys

n = int(input())

menor_esforco = sys.maxsize
indice_menor_esforco = 0
for index in range(n):
    trilha = list(map(int, input().split()))
    m = trilha[0]
    hs = trilha[1:]

    last_esforco = hs[0]
    som_ida = 0
    for h in hs:
        calc = h - last_esforco
        if calc >= 0:
            som_ida += calc
        last_esforco = h

    hs = hs[::-1]
    last_esforco = hs[0]
    som_volta = 0
    for h in hs:
        calc = h - last_esforco
        if calc >= 0:
            som_volta += calc
        last_esforco = h

    if som_ida < menor_esforco:
        menor_esforco = som_ida
        indice_menor_esforco = index
    if som_volta < menor_esforco:
        menor_esforco = som_volta
        indice_menor_esforco = index


print(indice_menor_esforco+1)




