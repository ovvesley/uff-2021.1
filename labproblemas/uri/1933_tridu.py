a, b = list(map(int, (input().split())))

response = ""
if a == b:
    response = a
elif a > b:
    response = a
elif a < b:
    response = b
print(response)