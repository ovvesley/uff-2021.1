#TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I - E1
#QUESTAO 2
#Wesley Santos Ferreira

TAM = 100
fabricadas_manha = 0
fabricadas_tarde = 0

media_mpecas = 0

maior_media = 0

menor_media = 0


for index in range(TAM):
    nome_torneiro = input("Informe o Nome do Torneiro: ")
    codigo_maquina = input("Informe o Codigo da Maquina") #nao informa que é inteiro,pode ser textual...

    dimencao_a = float(input("Informe a dimensão A "))
    dimencao_b = float(input("Informe a dimensão B"))
    dimencao_c = float(input("Informe a dimensão C"))

    data = input("Informe a Data")
    periodo = input("Informe o perido")

    media_dimensao = (dimencao_a + dimencao_b + dimencao_c)/3

    situacao = ""
    if media_dimensao <= 11.48:
        situacao = "Rejeitada"
    elif media_dimensao > 11.48 and media_dimensao <= 11.51:
        situacao = "Aprovada"
    else:
        situacao = "Reaproveitada"

    if index == 0:
        maior_media = media_dimensao
        menor_media = media_dimensao

    if media_dimensao > maior_media:
        maior_media = media_dimensao

    if media_dimensao < menor_media:
        menor_media = media_dimensao

    media_mpecas += media_dimensao

    if periodo.upper() == "TARDE":
        fabricadas_tarde += 1

    if periodo.upper() == "MANHA" or periodo.upper() == "MANHÃ":
        fabricadas_manha += 1
    print(f"Torneiro: {nome_torneiro}; Media Dimensoes: {media_dimensao}; Situacao:{situacao}")

media_mpecas = media_mpecas/TAM

print(f"MEDIA DE TODAS AS MEDIAS: {media_mpecas}")
print(f"MAIOR MEDIA: {maior_media}")
print(f"MENOR MEDIA: {menor_media}")
print(f"FABRICADAS MANHA: {fabricadas_manha}")
print(f"FABRICADAS TARDE: {fabricadas_tarde}")




