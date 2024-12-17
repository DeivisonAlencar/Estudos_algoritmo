altura = input('Digite a altura da parede: ')
largura = input('Digite a largura da parede: ')

rendimento = 2

try:
    altura = float(altura)
    largura = float(largura)
    metragem = altura * largura
    tin_nesc = metragem / rendimento
    print(f'A parede com altura de {altura} e largura de {largura} possui {metragem}m2 e necessita de {tin_nesc} baldes de tinta')
except:
    print('Os valores digitados não são numeros')