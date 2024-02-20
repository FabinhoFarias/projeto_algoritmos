import pandas as pd
from interface import rodar_interface

#Leitura do arquivo
dados_excel = pd.read_excel('anexo_16261_Coordenadas_Sedes_5565_Municípios_2010.xls')

grafo_cidades = {}


for _ , municipio in dados_excel.iterrows(): # preenchendo o grafo
    nome_municipio = municipio['NOME_MUNICIPIO']
    lat_municipio = municipio['LATITUDE']
    lon_municipio = municipio['LONGITUDE']
    grafo_cidades[nome_municipio] = {'latitude': lat_municipio, 'longitude': lon_municipio} # adição das coordenadas para os cálculos

for cidade, atributos in grafo_cidades.items():
    print(f'Cidade: {cidade}, Latitude: {atributos["latitude"]}, Longitude: {atributos["longitude"]}')

cidades_selecionadas = rodar_interface() # vai rodar e retornar uma lista
#print("Cidades selecionadas:", cidades_selecionadas)

ponto_de_partida,  ponto_de_chega = cidades_selecionadas[0], cidades_selecionadas[1]
