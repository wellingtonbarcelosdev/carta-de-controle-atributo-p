amostra = int(input('Tamanho da amostra: '))
dados = cont = somadados = somadefeituosos = 0
while cont < amostra:
    cont += 1
    dados = float(input(f'Amostra {cont}: '))
    defeituosos = int(input('Defeituosos: '))
    porcentagem = (defeituosos * 100) / dados
    print(f'Porcentagem de defeituosos: {porcentagem:.2f}%')
    somadados += dados
    somadefeituosos += defeituosos
pmedia = (somadefeituosos / somadados) * 100
amostramedia = (somadados / amostra)
print(f'{pmedia:.2f}')
print(f'{amostramedia:.2f}')
