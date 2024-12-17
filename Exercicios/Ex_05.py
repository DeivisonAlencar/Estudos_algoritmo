nota_01 = input('Digite a primeira nota ')
nota_02 = input('Digite a segunda nota ')

try:
    nota_01 = float(nota_01)
    nota_02 = float(nota_02)
    media = (nota_01 + nota_02)/2
    print(f'A média entre {nota_01:.1f} e {nota_02:.1f} é igual a {media:.1f}')
except:
    print('Um dos valores prenchidos não é um numero')

# Precisei pesquisar como se calcula média em python
# E descobri que só é possivel através da soma e divisão "manual" ou via funções em bibliotecas