n = int(input())
indice_teste = 1

while n != 0:
    saida = ""

    input_split = list(map(int, input().split()))
    cont = 1
    for index_i in range(len(input_split)):
        val = input_split[index_i]
        if val == cont:
            saida = str(val)
        cont += 1

    print(f"Teste {indice_teste}")
    print(f"{saida}")
    print()
    indice_teste += 1
    n = int(input())
