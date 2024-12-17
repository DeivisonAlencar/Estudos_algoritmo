saldo = input('Quanto você tem ? ')

cotacao = 3.45

try:
    saldo = float(saldo)
    dolar = saldo / cotacao
    print(f'Você pode trocar R${saldo:.2f} por U${dolar:.2f}')
except:
    print('Não foi digitado um numero')