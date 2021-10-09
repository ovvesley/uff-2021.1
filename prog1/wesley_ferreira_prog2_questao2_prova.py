# TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I - E1
# QUESTAO 2
# Wesley Santos Ferreira
def fib(n):
    last = last_one = val = 1
    if n in [1, 2]:
        return last
    else:
        for i in range(2, n):
            val = last + last_one
            last_one = last
            last = val
        return val


def field_array_with_fib(tam, array):
    for t in range(1, tam + 1):
        val_fib = fib(t)
        index_arr = t - 1
        array[index_arr] = val_fib


def contains_in_array(array1, array2):
    is_contain = True
    for val in array2:
        if val not in array1:
            is_contain = False

    if is_contain:
        print(f"O ARRAY {array2} está contido no ARRAY {array1}")
    else:
        print(f"O ARRAY {array2} NÃO está contido no ARRAY {array1}")


TAM = 200
fibbarray = [None] * 200

outro_array = [1, 2, 3]

field_array_with_fib(TAM, fibbarray)
print(f"`{len(fibbarray)}` FIB: {fibbarray}")

contains_in_array(fibbarray, outro_array)
