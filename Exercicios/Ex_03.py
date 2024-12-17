nome = input('Qual o seu nome? ')
salario = input('Qual foi o seu salário de junho? ')

try:
    salario = float(salario)
    print(f'O funcionario {nome} tem um salario de R${salario:.2f} em junho')
except:
    print('O valor digitado não é um número')

# Precisei de auxilio do curso de python para validar como trazer duas casas decimais
# Porém sabia em que aula ir pois sabia que estava relacionado a f-string

