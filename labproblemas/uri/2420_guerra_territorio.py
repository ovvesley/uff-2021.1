n = int(input())
secao = list(map(int, input().split()))
soma = sum(secao)

cont = 0
for i in range(len(secao)):
    cont+=secao[i]
    if cont == soma/2:
        print(i+1)
        break
