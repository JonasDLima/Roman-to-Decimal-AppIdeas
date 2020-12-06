from conversores import *

print(f'Esse é um programa que faz a conversão de números romanos em decimais. \n')

convertido_milhar = ''
convertido_centena = ''
convertido_dezena = ''
convertido_unidade = ''

romano = ''

numero_decimal = input('Número decimal que deseja converter: \n')

try:
    if int(numero_decimal):
        pass
except Exception:
    print('Dado digitado incorreto, por favor digite um valor em notação decimal.')

    exit()


if int(numero_decimal) > 3999:
    print('O maior número que pode ser representado nesta notação é 3999')

    exit()

if len(numero_decimal) == 1:
    convertido_unidade = converte_unidade(numero_decimal)
    convertido = convertido_unidade

elif len(numero_decimal) == 2:
    convertido_dezena = converte_dezena(numero_decimal)
    convertido_unidade = converte_unidade(numero_decimal)
    convertido = convertido_dezena + convertido_unidade

elif len(numero_decimal) == 3:
    convertido_centena = converte_centena(numero_decimal)
    convertido_dezena = converte_dezena(numero_decimal)
    convertido_unidade = converte_unidade(numero_decimal)
    convertido = convertido_centena + convertido_dezena + convertido_unidade

else:
    convertido_milhar = converte_milhar(numero_decimal)
    convertido_centena = converte_centena(numero_decimal)
    convertido_dezena = converte_dezena(numero_decimal)
    convertido_unidade = converte_unidade(numero_decimal)
    convertido = convertido_milhar + convertido_centena + convertido_dezena + convertido_unidade

romano = romano.join(convertido)

print(romano)
