quantia_inicial, rodadas = list(map(int, (input().split())))

d = quantia_inicial
e = quantia_inicial
f = quantia_inicial
for _ in range(rodadas):
    input_split = input().split()

    acao = input_split[0]
    user = input_split[1]
    pagar_para = ""
    if len(input_split) == 4:
        pagar_para = input_split[2]
        dinheiro = int(input_split[3])
    else:
        dinheiro = int(input_split[2])


    if acao == "C":
        valor = (dinheiro * -1)
    elif acao == "V":
        valor = dinheiro
    elif acao == "A":
        valor = dinheiro

        if pagar_para == "D":
            d = d +( dinheiro * -1)
        elif pagar_para == "E":
            e = e + (dinheiro * -1)
        elif pagar_para == "F":
            f = f + (dinheiro * -1)

    if user == "D":
        d = d + valor
    elif user == "E":
        e = e + valor
    elif user == "F":
        f = f + valor


print(d,e,f)