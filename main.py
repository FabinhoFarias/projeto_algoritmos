import pandas as pd
from interface import rodar_interface
from geopy.distance import geodesic

def calcular_distancia_entre_cidades(cidade1, cidade2, grafo_cidades):
    """Função para calcular as dicntâncias entre as cidades fornecidas pelo usuário"""
    coord_cidade1 = (grafo_cidades[cidade1]['latitude'], grafo_cidades[cidade1]['longitude'])
    coord_cidade2 = (grafo_cidades[cidade2]['latitude'], grafo_cidades[cidade2]['longitude'])
    distancia = geodesic(coord_cidade1, coord_cidade2).kilometers
    return distancia

#Leitura do arquivo
dados_excel = pd.read_excel('anexo_16261_Coordenadas_Sedes_5565_Municípios_2010.xls')
print(dados_excel)
grafo_cidades = {}

for _, municipio in dados_excel.iloc[1:].iterrows():  # preenchendo o grafo 
    nome_municipio = municipio['NOME_MUNICIPIO']
    lat_municipio = municipio['LATITUDE']
    lon_municipio = municipio['LONGITUDE']
    grafo_cidades[nome_municipio] = {'latitude': float(lat_municipio), 'longitude': float(lon_municipio)}# adição das coordenadas para os cálculos


#for cidade, atributos in grafo_cidades.items():
#    print(f'Cidade: {cidade}, Latitude: {atributos["latitude"]}, Longitude: {atributos["longitude"]}')

cidades_selecionadas = rodar_interface() # vai rodar e retornar uma lista
#print("Cidades selecionadas:", cidades_selecionadas)

ponto_de_partida,  ponto_de_chega = cidades_selecionadas[0], cidades_selecionadas[1]

distancia_entre_cidades = calcular_distancia_entre_cidades(ponto_de_partida, ponto_de_chega, grafo_cidades)

print(f"A distância entre {ponto_de_partida} e {ponto_de_chega} é de aproximadamente {distancia_entre_cidades:.2f} km.")


class Aresta:
    def __init__(self, cidade_origem, cidade_destino, distancia):
        self.cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino
        self.distancia = distancia

def encontrar_AGM(grafo, cidades):
    agm = [] 
    subconjuntos = {}

    def encontrar(subconjuntos, i):
        if subconjuntos[i] != i:
            subconjuntos[i] = encontrar(subconjuntos, subconjuntos[i])
        return subconjuntos[i]

    def unir(subconjuntos, x, y):
        raiz_x = encontrar(subconjuntos, x)
        raiz_y = encontrar(subconjuntos, y)
        subconjuntos[raiz_x] = raiz_y

    for cidade in cidades:
        subconjuntos[cidade] = cidade

    arestas = []
    for cidade_origem in grafo:
        for cidade_destino, distancia in grafo[cidade_origem].items():
            arestas.append(Aresta(cidade_origem, cidade_destino, distancia))

    arestas.sort(key=lambda x: x.distancia)

    for aresta in arestas:
        cidade_origem = aresta.cidade_origem
        cidade_destino = aresta.cidade_destino

        raiz_origem = encontrar(subconjuntos, cidade_origem)
        raiz_destino = encontrar(subconjuntos, cidade_destino)

        if raiz_origem != raiz_destino:
            agm.append(aresta)
            unir(subconjuntos, raiz_origem, raiz_destino)

    return agm

def encontrar_caminho(AGM, cidade_origem, cidade_destino):
    grafo = {}
    for aresta in AGM:
        if aresta.cidade_origem not in grafo:
            grafo[aresta.cidade_origem] = {}
        grafo[aresta.cidade_origem][aresta.cidade_destino] = aresta.distancia

    caminho = []
    atual = cidade_origem
    while atual != cidade_destino:
        caminho.append(atual)
        proxima = min(grafo[atual], key=grafo[atual].get)
        caminho.append(proxima)
        atual = proxima
    return caminho

# Árvore Geradora Mínima
AGM = encontrar_AGM(grafo_cidades, list(grafo_cidades.keys()))

# Encontrar o caminho entre as cidades selecionadas
caminho_entre_cidades = encontrar_caminho(AGM, ponto_de_partida, ponto_de_chega)
print("Melhor caminho entre as cidades:", caminho_entre_cidades)


