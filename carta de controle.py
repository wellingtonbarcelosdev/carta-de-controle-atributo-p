from math import sqrt
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
lsc = pmedia + 3 * sqrt((pmedia * (100 - pmedia)) / amostramedia)
print(f'LSC: {lsc:.2f}')
lic = pmedia - 3 * sqrt((pmedia * (100 - pmedia)) / amostramedia)
print(f'LC: {pmedia}')
if lic >= 0.00:
    print(f'LIC: {lic:.2f}')
else:
    print('LIC: 0')
    