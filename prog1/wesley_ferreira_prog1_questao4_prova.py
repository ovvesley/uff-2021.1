#TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I - E1
#QUESTAO 4
#Wesley Santos Ferreira

q = int(input())

for _ in range(q):
    #entrada informada no enunciado é 4,5  (Estando na mesma linha é inevitável o uso de lista para realizar o split do valor textual)

    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])

    cont_pares = 0
    sum_pares = 0
    current_value = m
    while cont_pares < n:
        if current_value % 2 == 0:
            cont_pares += 1
            sum_pares+=current_value
        current_value += 1

    print(sum_pares)

