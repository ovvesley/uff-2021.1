n = int(input())
indice_teste = 1

while n != 0:

    senhas = []
    res = [[0 for x in range(10)] for y in range(6)]
    senha_final = []
    for _ in range(n):
        input_split = input().split()
        numbers = list(map(int, input_split[:10]))
        letras = input_split[10:]

        possibilidades = []
        for l in letras:
            if l == "A":
                possibilidades.append(numbers[0:2])
            elif l == "B":
                possibilidades.append(numbers[2:4])
            elif l == "C":
                possibilidades.append(numbers[4:6])
            elif l == "D":
                possibilidades.append(numbers[6:8])
            elif l == "E":
                possibilidades.append(numbers[8:10])



        senhas.append(possibilidades)

    for current_senha in senhas:
        for index_i in range(len(current_senha)):
            for i in current_senha[index_i]:
                res[index_i][i] += 1

    for index_i in range(len(res)):
        for index_j in range(len(res[index_i])):
            if res[index_i][index_j] == n:
                senha_final.append(index_j)

    senha = " ".join(map(str, senha_final))

    print(f"Teste {indice_teste}")
    print(f"{senha} ")
    print()
    indice_teste += 1
    n = int(input())
