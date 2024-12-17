numero = input('Digite um numero ')

try:
    numero = float(numero)
    dobro = numero * 2
    terca = numero / 3
    print(f'O dobro de {numero:.1f} é {dobro:.1f} \nA terça parte de {numero:.1f} é {terca:.5f}')
except:
    print('Ñão foi preenchido um numero')