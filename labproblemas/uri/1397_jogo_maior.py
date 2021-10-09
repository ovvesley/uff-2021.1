n = int(input())

while n != 0:
    cont_a = 0
    cont_b = 0
    for _ in range(n):
        a, b = list(map(int, (input().split())))
        if a > b:
            cont_a += 1
        elif a < b:
            cont_b += 1
    print(cont_a, cont_b)

    n = int(input())

