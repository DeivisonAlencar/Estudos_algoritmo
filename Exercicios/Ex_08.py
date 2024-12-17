distancia = input('Digite uma distancia em metros')

try:
    distancia = float(distancia)
    km = distancia / 1000
    hm = distancia / 100
    dam = distancia / 10
    dm = distancia / 0.10
    cm = distancia / 0.010
    mm = distancia / 0.0010

    print(f'A Distancia de {distancia} metros corresponde a \n{km}Km \n{hm}Hm \n{dam}Dam \n{dm}dm \n{cm}cm \n{mm}mm')
except:
    print('O valor não preenchido não é um número')