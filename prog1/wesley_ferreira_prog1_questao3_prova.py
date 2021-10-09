#TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I - E1
#QUESTAO 3
#Wesley Santos Ferreira

n = int(input())
x = int(input())

direcao = 1
cont_fat = 0
soma = 0

for index_i in range(1, n+1):

    cont_fat += direcao
    if cont_fat == 4:
        direcao= -1
    if cont_fat == 1:
        direcao= 1

    calc_fat = 1
    for f in range(cont_fat+1):
        if f == 0:
            calc_fat *= 1
        else:
            calc_fat *= f

    expo = index_i + 1
    termo = (x ** expo) / calc_fat

    if index_i % 2 != 0:
        termo = termo * -1

    soma += termo
    print(f"x={x} fat={cont_fat}! expo={expo} termo={termo}")

print(f"SOMA: {soma}")