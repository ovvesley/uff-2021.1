n = int(input())

copos = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a > b:
        copos +=b

print(copos)