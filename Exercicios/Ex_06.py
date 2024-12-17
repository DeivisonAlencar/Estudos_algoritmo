numero = input('Digite um número inteiro ')

try:
    numero = int(numero)
    print(f'O antecessor de {numero} é {numero-1} \nO sucessor de {numero} é {numero+1}')
except:
    print('Não foi digitado um número inteiro')