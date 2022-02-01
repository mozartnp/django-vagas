import json
import random
import string
import datetime

def openJson(filename):
    with open(filename, 'r') as f:
        todosDados = json.load(f)
    return todosDados

def dumpJson(filename, temp):
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)

def geradorEmail():
    nome = ''
    contador = 6
    while contador >= 0:
        letra = random.choice(list(string.ascii_lowercase))
        nome = nome + letra
        contador -= 1
    arroba = ''    
    contador = 6
    while contador >= 0:
        letra = random.choice(list(string.ascii_lowercase))
        arroba = arroba + letra
        contador -= 1
    email = (nome + '@' +arroba + '.com')
    return email

def geradorSenha():
    #Tamanho da senha
    contador = random.randrange(start=8, stop=128)
    #Tipos de caracter da senha
    lista_caracter = ['especial', 'letras', 'numeros']

    senha = ''
    while contador >= 0:
        escolha_caracter = random.choice(lista_caracter)
        if escolha_caracter == 'especial':
            caracter = random.choice(list(string.punctuation))
        elif escolha_caracter == 'letras':
            caracter = random.choice(list(string.ascii_letters))
        elif escolha_caracter == 'numeros':
            caracter = random.choice(list(string.digits))
        senha = senha + caracter
        contador -= 1
    return senha

def geradorDatas():
    # Ano em que começa a contar o tempo aleatorio
    ano_comeco = 2010
    # Ano atual ( que é o fim aleatorio)
    data_hoje = datetime.datetime.now()

    ano_final = data_hoje.year
    comeco = datetime.datetime(ano_comeco, 1, 1, 00, 00, 00)
    anos = ano_final - ano_comeco + 1
    fim = comeco + datetime.timedelta(days=365 * anos)
    data = comeco + (fim -comeco) * random.random()
    if data > data_hoje:
        data = geradorDatas()
    return data

def insertDados(destino):
    # A quantidade de usuario, por padrão será algo entre 50 e 100
    qnt_User = random.randrange(start=50, stop=100)

    json = openJson(destino)
    novoItem = {}
    pk = 1
    lista_escolha = [True, False]
    lista_tipo_user = ['EMPR', 'CAND']

    for x in range(qnt_User): 
        email = geradorEmail()
        senha = geradorSenha()
        timestamp = str(geradorDatas())

        novoItem["pk"] = pk
        novoItem["model"] = "user.User"
        novoItem["fields"] = {}
        novoItem["fields"]["password"] = senha
        novoItem["fields"]["email"] = email
        novoItem["fields"]["tipo_user"] = random.choice(list(lista_tipo_user))
        novoItem["fields"]["date_joined"] = timestamp
        novoItem["fields"]["last_login"] = timestamp
        novoItem["fields"]["is_active"] = random.choice(list(lista_escolha))
        novoItem["fields"]["is_admin"] = random.choice(list(lista_escolha))
        novoItem["fields"]["is_staff"] = random.choice(list(lista_escolha))
        novoItem["fields"]["is_superuser"] = random.choice(list(lista_escolha))
        
        json.append(novoItem)
        novoItem = {}
        pk += 1
    dumpJson(destino, json)

jsonDestino = "./test_user.json"
insertDados(jsonDestino)