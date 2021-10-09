a, g, ra, rg = list(map(float, input().split()))

preco_a = a / ra
preco_g = g / rg

if preco_g <= preco_a:
    print("G")
else:
    print("A")