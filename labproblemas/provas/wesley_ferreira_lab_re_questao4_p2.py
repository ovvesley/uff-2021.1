import math

m, n = list(map(int, input().split()))

chocadeiras = list(map(int, input().split()))
cont = 0
data = {}
lista_all = [None] * m

chocadeiras.sort()

sum = 0

mmc = math.lcm(*chocadeiras)

for c in chocadeiras:
    sum+=c*n

print(sum//mmc)