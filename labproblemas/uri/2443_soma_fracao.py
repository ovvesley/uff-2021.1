def func(x, y):
    val = x % y
    while val != 0:
        x = y
        y = val
        val = x % y

    return y

a,b,c,d = list(map(int, input().split()))

n = a*d + c*b
den = b*d

div = func(n, den)

num = n/div
den = den/div

print(int(num), int(den))