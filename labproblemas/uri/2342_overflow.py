max = int(input())
a, sinal, b = input().split()

n = int(a)
b = int(b)

if (sinal== "+"):
    if n + b <= max:
        print("OK")
    else:
        print("OVERFLOW")

else:
    if n * b <= max:
        print("OK")
    else:
        print("OVERFLOW")



