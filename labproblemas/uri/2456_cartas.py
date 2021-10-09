serie = list(map(int, input().split()))

ordenada_c = serie.copy()
ordenada_c.sort()

ordenada_d = serie.copy()
ordenada_d.sort(reverse=True)

response = ""
if ordenada_d == serie:
    response= "D"
elif ordenada_c == serie:
    response = "C"
else:
    response ="N"
print(response)

