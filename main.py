print(f'Esse é um programa que faz a conversão de números romanos em decimais e vise versa. \n')

numero_decimal = input('Número decimal que deseja converter: \n')

numeros_romanos = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

if int(numero_decimal) > 3999:
    print('O maior número que pode ser representado nesta notação é 3999')

    exit()


def converte_dezena(numero):
    pass


def converte_centena(numero):
    pass


def converte_milhar(numero):
    romano = []
    if numero[0] == '1':
        romano.insert(0, 'M')
    elif numero[0] == '2':
        romano.insert(0, 'MM')
    else:
        romano.insert(0, 'MMM')

    return romano


convertido = converte_milhar(numero_decimal)

convertido.extend(numero_decimal[1:])

print(convertido)
