n_1 = input('Digite um número inteiro: ')
n_2 = input('Digite outro número inteiro: ')

try:
    soma = int(n_1) + int(n_2)
    print(f'A soma de {n_1} e {n_2} é {soma}')
except:
    print('Um ou mais valores digitados não é um número inteiro')