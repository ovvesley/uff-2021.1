def generate_exp_add(add, exp):
    for _ in range(1, n+1):
        exp += add
        add = add + add
    return exp, add

n = int(input())
cont = 0

while n != -1:

    add = 1
    exp = 2
    exp, add = generate_exp_add(add, exp)

    cont +=1
    print(f"Teste {cont}")
    print(exp ** 2, end="\n\n")

    n = int(input())
