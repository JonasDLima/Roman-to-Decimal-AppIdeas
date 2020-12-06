def converte_unidade(numero):
    romano = []
    unidade = ''
    if int(numero[len(numero) - 1]) < 4:
        unidade = 'I' * int(numero[len(numero) - 1])
    elif int(numero[len(numero) - 1]) == 4:
        unidade = 'IV'
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
    if int(numero[len(numero) - 3]) < 4:
        centena = 'C' * int(numero[len(numero) - 3])
    elif int(numero[len(numero) - 3]) == 4:
        centena = 'CD'
    elif int(numero[len(numero) - 3]) == 5:
        centena = 'D'
    elif int(numero[len(numero) - 3]) < 9:
        centena = 'D' + ('C' * (int(numero[len(numero) - 3]) - 5))
    elif int(numero[len(numero) - 3]) == 9:
        centena = 'CM'
    romano.insert(int(numero[len(numero) - 3]), centena)

    return romano


def converte_milhar(numero):
    romano = []
    milhar = ''
    if int(numero[int(numero[len(numero) - 3])]) < 4:
        milhar = 'M' * int(numero[int(numero[len(numero) - 3])])
    romano.insert(int(numero[len(numero) - 3]), milhar)

    return romano
