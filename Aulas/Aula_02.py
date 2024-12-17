# Video 26

# Execicio onde pede-se para o usuario digitar os valores de:
# largura, comprimento e preço do metro quadrado de um terreno.
# Apartir dos valores digitados, mostrar pro usuario:
# o total de metros quadrados e o preço total do terreno


'''
usuario prenche largura ->
se largura estiver vazia: 
    exibir mensagem de vazia
    pedir para cliente preencher de novo
se largura não for um numero:
    exibir mensagem de não numero
    pedir para cliente preencher dnv
se estiver tudo ok:
    pedir para o cliente preenhcer proximo campo
    repetir o processo até preencher todos os campos
em cada campo o usuario possui a opção de pedir para "SAIR"
'''

# Cria lista vazia para receber os campos preenchidos
campos_preenchidos = []

# Cria uma lista com o nome dos campos que serão solicitados
nome_campos = ['a Largura', 'o Comprimento', 'o Preço do m2']

# Define a quantidad de campos que está sendo pedido
# Servirá para movimentar o for e validar se todos os campos foram preenchidos
qtd_campos = len(nome_campos)

# Cria função para fazer as validações dos campos
def validar_campos(campo):
    # Se o campo não for preenchido retorna mensagem de vazio
    if not campo:
        return 'O valor não foi preenchido, vamos tentar de novo'
    # Caso o campo esteja preenchido
    else:
        # Tenta transformar o campo em float e retorna "OK" caso consiga
        try:
            campo = float(campo)
            return 'OK'
        # Caso não consiga, retorna mensagem de não numerico
        except:
            return 'O valor preenchido não é um numero, vamos tentar de novo'

# Define o primeiro campo a ser lido
n_campo = 0

# Lê cada um dos campos na lista, um por vez
while n_campo < qtd_campos:
    # Pede para o usuario digitar o campo especifico
    campo = input(f'Digite {nome_campos[n_campo]} do terreno: ')

    # Se for preeenchido "sair", encerra o código
    if campo.upper() == 'SAIR':
        print('Ok, vamos encerrar')
        break
    
    # Se a validação do campo não estiver ok, informa mensagem de acordo com o tipo de erro
    if validar_campos(campo) != 'OK':
        print(validar_campos(campo))
    # Se a valiudação estiver ok, adiciona o campo preenchido a lista para calculo, e redefine o campo a ser lido
    else:
        campos_preenchidos.append(float(campo))
        n_campo += 1

# Se a quantidade de campos preenchidos for a mesm de campos solicitados:
if len(campos_preenchidos) == len(nome_campos):
    # Calcula a metragem multiplicando a largura e o comprimento
    metragem = campos_preenchidos[0] * campos_preenchidos[1] 
    # Calcula o preço total multiplicando a metragem pelo preço do m2
    preco = metragem * campos_preenchidos[2]

    # Exibe a mensagem final com a metragem total e o preço do terreno
    print(f'O terreno possui {metragem}m2 e custará R${preco}')

