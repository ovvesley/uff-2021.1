#TCC00308 - PROGRAMAÇÃO DE COMPUTADORES I - E1
#QUESTAO 1
#Wesley Santos Ferreira

def open_file(path):
    return open(path, 'r')

def write_file(path, data):
    file = open(path, 'a')
    file.write(data)
    file.close()

def generate_line(number):
    return f'{number}\n'

file = open_file('inteiros.txt')

for line in file:
    n = int(line.strip())
    line_to_file = generate_line(n)
    if n % 2 == 0:
        write_file('pares.txt', line_to_file)
    else:
        write_file('impares.txt', line_to_file)
file.close()