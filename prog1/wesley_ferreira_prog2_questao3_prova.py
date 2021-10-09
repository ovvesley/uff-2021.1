#TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I - E1
#QUESTAO 3
#Wesley Santos Ferreira

def generate_string_first_letter(frase):
    return "".join([word[0] for word in frase.split()])

frase = "O segundo periodo letivo termina em dezembro"
new_frase = generate_string_first_letter(frase)
print(new_frase)