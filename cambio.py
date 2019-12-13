from os import system # Importar o método system da biblioteca os
from requests import get # Importar o método get da biblioteca requests
import json # Importar a biblioteca JSON
import pandas as pd # Importar biblioteca pandas - referindo ao pandas com pd
import decimal# Importar da biblioteca math o método round 


system("cls") # Limpar a tela antes de mostrar o resultado

# Precisa realizar o download da biblioteca request com o comando "python pip install requests ou  pip install requests"

url = "http://data.fixer.io/api/latest?access_key=15c3e81c27f68cff12b882f964c08046"
print("Acessando base de dados...")
resposta = get(url)

#Verifica o status code retornado da consulta a variavel url
if resposta.status_code == 200:
    print("Conseguiu acessar base de dados!")
    print("Buscando informações das moedas...")
    dados = resposta.json() # Transformar em JSON

    day = dados['date']
    print("Consulta realizada no dia %s/%s/%s" % (day[-2:], day[5:7], day[:4]))

    # Descobrir o valor em Real - Divide a taxa em real pela taxa da moeda que precisa
    euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'],2)
    dollar_real = round(dados['rates']['BRL'] / dados['rates']['USD'],2)
    btc_real = round(dados['rates']['BRL'] / dados['rates']['BTC'],2)

    print("Euro: %.2f" % euro_real)
    print("Dolar: %.2f" % dollar_real)
    print("Bitcoin: %.2f" % btc_real)

    df = pd.DataFrame({'Moedas': ['Euro','Dólar','Bitcoin'], 'Valores':[euro_real, dollar_real,btc_real]})
    df.index.name = 'Item' # Alterar o nome do campo do index
    df.to_csv('valores.csv', sep=';') # Exporta para CSV
    #df.to_csv('valores.csv', index=False sep=';') # Exportar para CSV sem o index

    print("Exportado com sucesso!")

else:
    print("Site com problema!")



