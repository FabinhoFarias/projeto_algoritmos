import pandas as pd
from interface import rodar_interface , mostrar_lista
from geopy.distance import geodesic

def calcular_distancia_entre_cidades(coord_cidade1, coord_cidade2):
    """Função para calcular as distâncias entre as cidades fornecidas pelo usuário"""
    distancia = geodesic(coord_cidade1, coord_cidade2).kilometers
    print(f"Distância entre {coord_cidade1} e {coord_cidade2}: {distancia:.2f} km")
    return distancia

# Leitura do arquivo
dados_excel = pd.read_excel('anexo_16261_Coordenadas_Sedes_5565_Municípios_2010.xls')

cidades_de_pernambuco = [
    'Abreu e Lima', 'Afogados da Ingazeira', 'Afrânio', 'Agrestina', 'Água Preta', 'Águas Belas', 'Alagoinha',
    'Aliança', 'Altinho', 'Amaraji', 'Angelim', 'Araçoiaba', 'Araripina', 'Arcoverde', 'Barra de Guabiraba',
    'Barreiros', 'Belém de Maria', 'Belém do São Francisco', 'Belo Jardim', 'Betânia', 'Bezerros', 'Bodocó',
    'Bom Conselho', 'Bom Jardim', 'Bonito', 'Brejão', 'Brejinho', 'Brejo da Madre de Deus', 'Buenos Aires',
    'Buíque', 'Cabo de Santo Agostinho', 'Cabrobó', 'Cachoeirinha', 'Caetés', 'Calçado', 'Calumbi', 'Camaragibe',
    'Camocim de São Félix', 'Camutanga', 'Canhotinho', 'Capoeiras', 'Carnaíba', 'Carnaubeira da Penha', 'Carpina',
    'Caruaru', 'Casinhas', 'Catende', 'Cedro', 'Chã de Alegria', 'Chã Grande', 'Condado', 'Correntes', 'Cortês',
    'Cumaru', 'Cupira', 'Custódia', 'Dormentes', 'Escada', 'Exu', 'Feira Nova', 'Fernando de Noronha', 'Ferreiros',
    'Flores', 'Floresta', 'Frei Miguelinho', 'Gameleira', 'Garanhuns', 'Glória do Goitá', 'Goiana', 'Granito',
    'Gravatá', 'Iati', 'Ibimirim', 'Ibirajuba', 'Igarassu', 'Iguaraci', 'Ilha de Itamaracá', 'Inajá', 'Ingazeira',
    'Ipojuca', 'Ipubi', 'Itacuruba', 'Itaíba', 'Itambé', 'Itapetim', 'Itapissuma', 'Itaquitinga',
    'Jaboatão dos Guararapes', 'Jaqueira', 'Jataúba', 'Jatobá', 'João Alfredo', 'Joaquim Nabuco', 'Jucati', 'Jupi',
    'Jurema', 'Lagoa de Itaenga', 'Lagoa do Carro', 'Lagoa do Ouro', 'Lagoa dos Gatos', 'Lagoa Grande', 'Lajedo',
    'Limoeiro', 'Macaparana', 'Machados', 'Manari', 'Maraial', 'Mirandiba', 'Moreilândia', 'Moreno', 'Nazaré da Mata',
    'Olinda', 'Orobó', 'Orocó', 'Ouricuri', 'Palmares', 'Palmeirina', 'Panelas', 'Paranatama', 'Parnamirim', 'Passira',
    'Paudalho', 'Paulista', 'Pedra', 'Pesqueira', 'Petrolândia', 'Petrolina', 'Poção', 'Pombos', 'Primavera', 'Quipapá',
    'Quixaba', 'Recife', 'Riacho das Almas', 'Ribeirão', 'Rio Formoso', 'Sairé', 'Salgadinho', 'Salgueiro', 'Saloá',
    'Sanharó', 'Santa Cruz', 'Santa Cruz da Baixa Verde', 'Santa Cruz do Capibaribe', 'Santa Filomena',
    'Santa Maria da Boa Vista', 'Santa Maria do Cambucá', 'Santa Terezinha', 'São Benedito do Sul', 'São Bento do Una',
    'São Caetano', 'São João', 'São Joaquim do Monte', 'São José da Coroa Grande', 'São José do Belmonte',
    'São José do Egito', 'São Lourenço da Mata', 'São Vicente Férrer', 'Serra Talhada', 'Serrita', 'Sertânia',
    'Sirinhaém', 'Solidão', 'Surubim', 'Tabira', 'Tacaimbó', 'Tacaratu', 'Tamandaré', 'Taquaritinga do Norte',
    'Terezinha', 'Terra Nova', 'Timbaúba', 'Toritama', 'Tracunhaém', 'Trindade', 'Triunfo', 'Tupanatinga',
    'Tuparetama', 'Venturosa', 'Verdejante', 'Vertente do Lério', 'Vertentes', 'Vicência', 'Vitória de Santo Antão',
    'Xexéu'
]

cidades_de_pernambuco = [ cidade.upper() for cidade in cidades_de_pernambuco ]

# Filtrando os dados do Excel para incluir apenas as cidades de Pernambuco
dados_perbambuco = dados_excel[dados_excel['NOME_MUNICIPIO'].isin(cidades_de_pernambuco)]

# Criando o grafo apenas com as cidades de Pernambuco
grafo_cidades = {}

for _, municipio in dados_perbambuco.iterrows():
    nome_municipio = municipio['NOME_MUNICIPIO'].upper()  # Convertendo para maiúsculas
    lat_municipio = municipio['LATITUDE']
    lon_municipio = municipio['LONGITUDE']
    grafo_cidades[nome_municipio] = [float(lat_municipio), float(lon_municipio)]

cidades_selecionadas = rodar_interface()

ponto_de_partida, ponto_de_chegada = cidades_selecionadas[0], cidades_selecionadas[1]

class Aresta:
    def __init__(self, cidade_origem, cidade_destino, distancia):
        self.cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino
        self.distancia = distancia

def kruskal(grafo, cidades):
    # Algoritmo de kruskal para encontrar a AGM
    agm = {}  
    
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
        for cidade_destino in grafo:
            if cidade_origem != cidade_destino:
                distancia = calcular_distancia_entre_cidades(grafo[cidade_origem], grafo[cidade_destino])
                arestas.append(Aresta(cidade_origem, cidade_destino, distancia))

    arestas.sort(key=lambda x: x.distancia)

    for aresta in arestas:
        cidade_origem = aresta.cidade_origem
        cidade_destino = aresta.cidade_destino

        raiz_origem = encontrar(subconjuntos, cidade_origem)
        raiz_destino = encontrar(subconjuntos, cidade_destino)

        if raiz_origem != raiz_destino:
            if raiz_origem not in agm:  
                agm[raiz_origem] = []
            agm[raiz_origem].append(aresta)
            
            if raiz_destino not in agm:
                agm[raiz_destino] = []
            agm[raiz_destino].append(Aresta(cidade_destino, cidade_origem, aresta.distancia))

            unir(subconjuntos, raiz_origem, raiz_destino)
            print(f"Adicionada aresta: {aresta.cidade_origem} -> {aresta.cidade_destino}")

    return agm


def encontrar_caminho(AGM, cidade_origem, cidade_destino, caminho_atual=None):
    # Inicializar o caminho atual se não estiver definido
    if caminho_atual is None:
        caminho_atual = [cidade_origem]

    # Verificar se a cidade de destino foi alcançada
    if cidade_origem == cidade_destino:
        return caminho_atual

    # Verificar se todas as cidades adjacentes já foram visitadas
    cidades_adjacentes = [aresta.cidade_destino for aresta in AGM[cidade_origem]]
    cidades_restantes = [cidade for cidade in cidades_adjacentes if cidade not in caminho_atual]

    if not cidades_restantes:
        return None

    # Tentar encontrar um caminho para a cidade de destino a partir das cidades adjacentes
    for proxima_cidade in cidades_restantes:
        caminho_atual.append(proxima_cidade)
        resultado = encontrar_caminho(AGM, proxima_cidade, cidade_destino, caminho_atual)

        if resultado:
            return resultado

        # Se não há caminho a partir desta cidade, remove do caminho atual e tenta com a próxima
        caminho_atual.pop()

    # Se nenhum caminho válido foi encontrado, retorne None
    return None

# Encontrar a Árvore Geradora Mínima (AGM) do grafo
print("\nBuscando Árvore Geradora Mínima...")
AGM = kruskal(grafo_cidades, grafo_cidades.keys())

# Encontrar o caminho entre as cidades selecionadas
print("\nEncontrando o caminho entre as cidades selecionadas...")
caminho_entre_cidades = encontrar_caminho(AGM, ponto_de_partida, ponto_de_chegada)
print("\nMelhor caminho entre as cidades:", caminho_entre_cidades)

mostrar_lista(caminho_entre_cidades) # Mostrar lista d cidades geradas
