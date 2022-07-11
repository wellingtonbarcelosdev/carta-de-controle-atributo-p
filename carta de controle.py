from math import sqrt
amostra = int(input('Tamanho da amostra: '))
meta = float(input('Meta gerencial de NÃO CONFORMES (em %): '))
dados = cont = somadados = somadefeituosos = 0
while cont < amostra:
    cont += 1
    dados = float(input(f'Amostra {cont}: '))
    defeituosos = int(input('Defeituosos: '))
    porcentagem = (defeituosos * 100) / dados
    print(f'Porcentagem de defeituosos amostra {cont}: {porcentagem:.2f}%')
    somadados += dados
    somadefeituosos += defeituosos
pmedia = somadefeituosos / amostra
amostramedia = (somadados / amostra)
print('-=' * 20)
lsc = pmedia + 3 * sqrt((pmedia * (100 - pmedia)) / amostramedia)
print(f'LSC: {lsc:.2f}')
lic = pmedia - 3 * sqrt((pmedia * (100 - pmedia)) / amostramedia)
print(f'LC: {pmedia:.2f}')
if lic >= 0.00:
    print(f'LIC: {lic:.2f}')
else:
    print('LIC: 0')
capacidade = (1-pmedia) * 100
print(f'Capacidade do processo: {capacidade:.2f}%')
if capacidade < 100 - meta:
    print(f'Processo acima da meta gerencial de {meta}% NÃO CONFORMES')
else:
    print(f'Processo dentro do limite gerencial de {meta}%')
indicecp = meta / pmedia
print(f'Indice cp: {indicecp:.3f}')
