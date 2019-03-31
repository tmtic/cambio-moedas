# Importar o método system da biblioteca os
from os import system

system("cls")

#Importar o método get da biblioteca requests
from requests import get

#Importar a biblioteca JSON
import json

# Precisa realizar o download da biblioteca request com o comando "python pip install requests ou  pip install requests"

url = "http://data.fixer.io/api/latest?access_key=15c3e81c27f68cff12b882f964c08046"
print("Acessando base de dados...")
resposta = get(url)

#Verifica o status code retornado da consulta a variavel url
if resposta.status_code == 200:
    print("Conseguiu acessar base de dados!")
    print("Buscando informações das moedas...")
    dados = resposta.json() # Transformar JSON

    day = dados['date']
    print("Consulta realizada no dia %s/%s/%s" % (day[-2:], day[5:7], day[:4]))

    # Descobrir o valor em Real - Divide a taxa em real pela taxa da moeda que precisa
    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
    btc_real = dados['rates']['BRL'] / dados['rates']['BTC']

    print("Euro: %.2f" % euro_real)
    print("Dólar: %.2f" % dollar_real)
    print("Bitcoin: %.2f" % btc_real)

else:
    print("Site com problemas!")



