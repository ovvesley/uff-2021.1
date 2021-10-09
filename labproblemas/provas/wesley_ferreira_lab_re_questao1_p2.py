n = int(input())
for _ in range(n):
    password = "".join([word[0] for word in input().split()])
    print(password)