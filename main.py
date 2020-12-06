print(f'Esse é um programa que faz a conversão de números romanos em decimais e vise versa. \n')

numero_decimal = input('Número decimal que deseja converter: \n')

convertido_milhar = ''
convertido_centena = ''
convertido_dezena = ''
convertido_unidade = ''

romano = ''

if int(numero_decimal) > 3999:
    print('O maior número que pode ser representado nesta notação é 3999')

    exit()


def converte_unidade(numero):
    romano = []
    unidade = ''
    if int(numero[len(numero) - 1]) < 5:
        unidade = 'I' * int(numero[len(numero) - 1])
    elif int(numero[len(numero) - 1]) < 9:
        unidade = 'V' + ('I' * (int(numero[len(numero) - 1]) - 5))
    elif int(numero[len(numero) - 1]) == 9:
        unidade = 'IX'
    romano.insert(int(numero[len(numero) - 1]), unidade)

    return romano


def converte_dezena(numero):
    romano = []
    dezena = ''
    if int(numero[len(numero) - 2]) < 4:
        dezena = 'X' * int(numero[len(numero) - 2])
    elif int(numero[len(numero) - 2]) < 5:
        dezena = 'XL'
    elif int(numero[len(numero) - 2]) == 5:
        dezena = 'L'
    elif int(numero[len(numero) - 2]) < 9:
        dezena = 'L' + ('X' * (int(numero[len(numero) - 2]) - 5))
    elif int(numero[len(numero) - 2]) == 9:
        dezena = 'XC'
    romano.insert(int(len(numero) - 2), dezena)

    return romano


def converte_centena(numero):
    romano = []
    centena = ''
    if int(numero[1]) < 4:
        centena = 'C' * int(numero[1])
    elif int(numero[1]) < 5:
        centena = 'CD'
    elif int(numero[1]) == 5:
        centena = 'D'
    elif int(numero[1]) < 9:
        centena = 'D' + ('C' * (int(numero[1]) - 5))
    elif int(numero[1]) == 9:
        centena = 'CM'
    romano.insert(1, centena)

    return romano


def converte_milhar(numero):
    romano = []
    milhar = ''
    if int(numero[0]) < 4:
        milhar = 'M' * int(numero[0])
    romano.insert(0, milhar)

    return romano


convertido_milhar = converte_milhar(numero_decimal)
print(convertido_milhar, numero_decimal[1:])
convertido_centena = converte_centena(numero_decimal)
print(convertido_milhar + convertido_centena, numero_decimal[2:])
convertido_dezena = converte_dezena(numero_decimal)
print(convertido_milhar + convertido_centena + convertido_dezena, numero_decimal[3:])
convertido_unidade = converte_unidade(numero_decimal)
print(convertido_milhar + convertido_centena + convertido_dezena, convertido_unidade, sep='')

convertido = convertido_milhar + convertido_centena + convertido_dezena + convertido_unidade

romano = romano.join(convertido)

print(romano)
