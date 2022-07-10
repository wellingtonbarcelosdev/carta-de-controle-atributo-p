amostra = int(input('Tamanho da amostra: '))
dados = cont = soma = 0
while cont < amostra:
    cont += 1
    dados = float(input(f'Amostra {cont}: '))
    soma += dados