#TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I - E1
#QUESTAO 1
#Wesley Santos Ferreira

sum_positivo = 0
sum_negativo = 0
cont_positivo = 0
cont_negativo = 0
cont_nulo = 0
for _ in range(5):
    valor = int(input())
    if valor == 0:
        cont_nulo += 1
    elif valor < 0:
        cont_negativo += 1
        sum_negativo += valor
    elif valor > 0:
        cont_positivo += 1
        sum_positivo += valor
print(f"Positivos: {cont_positivo}; Negativos: {cont_negativo}; Nulos: {cont_nulo}")
print(f"Media Positivo: {sum_positivo / cont_positivo}; Media Negativa: {sum_negativo / cont_negativo}")



