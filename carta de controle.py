amostra = int(input('Tamanho da amostra: '))
dados = cont = soma = 0
while cont < amostra:
    cont += 1
    dados = float(input(f'Amostra {cont}: '))
    defeituosos = int(input('Defeituosos: '))
    porcentagem = (defeituosos * 100) / dados
    print(f'Porcentagem de defeituosos: {porcentagem:.2f}%')
    soma += dados
