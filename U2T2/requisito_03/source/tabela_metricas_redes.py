import networkx as nx
import pandas as pd

# Função para calcular as métricas para uma rede
def calcular_metricas(nome_rede, G):
    num_vertices = len(G.nodes())
    num_arestas = len(G.edges())
    grau_assortatividade = nx.degree_assortativity_coefficient(G)
    num_componentes_conectados = nx.number_connected_components(G)

    # Encontre o maior componente conectado (Componente Gigante)
    componentes_conectados = list(nx.connected_components(G))
    maior_componente = max(componentes_conectados, key=len)
    tamanho_componente_gigante = len(maior_componente)

    coeficiente_agrupamento_medio = nx.average_clustering(G)

    return {
        "Rede": nome_rede,
        "Quantidade de Vértices": num_vertices,
        "Quantidade de Arestas": num_arestas,
        "Coeficiente de Grau de Assortatividade": grau_assortatividade,
        "Quantidade de Componentes Conectados": num_componentes_conectados,
        "Tamanho do Componente Gigante (GCC)": tamanho_componente_gigante,
        "Coeficiente de Clustering Médio": coeficiente_agrupamento_medio
    }

# Crie um dicionário com os dados de cada rede
dados_redes = {
#     "Deezer": deezer, #Código utilizado no Colab, onde cada rede estava já criada
#     "Facebook": facebook,
#     "GitHub": git,
#     "Twitch": twitch,
#     "Last FM": lastfm
}

# Inicialize uma lista para armazenar os resultados
resultados = []

# Calcule as métricas para cada rede
for nome_rede, grafo in dados_redes.items():
    metricas = calcular_metricas(nome_rede, grafo)
    resultados.append(metricas)

# Crie um DataFrame pandas com os resultados
tabela = pd.DataFrame(resultados)

# Exiba a tabela
print(tabela)
