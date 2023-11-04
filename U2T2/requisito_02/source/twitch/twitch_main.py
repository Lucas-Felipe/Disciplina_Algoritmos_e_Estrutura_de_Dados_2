"""Arquivo principal para rede twitch"""
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar as arestas da rede a partir do arquivo CSV
EDGES_FILE = "drive/MyDrive/twitch/large_twitch_edges.csv"
edges_data = pd.read_csv(EDGES_FILE)

# Crie um objeto Graph vazio para representar a rede
G = nx.Graph()

# Adicione as arestas ao grafo
for index, row in edges_data.iterrows():
    source_node, target_node = row["numeric_id_1"], row["numeric_id_2"]
    G.add_edge(source_node, target_node)

# Carregar as características dos nós a partir do arquivo JSON
FEATURES_FILE = "drive/MyDrive/twitch/large_twitch_features.csv"
features_data = pd.read_csv(FEATURES_FILE)

# Adicionar características aos nós do grafo
for index, row in features_data.iterrows():
    node_id, target_value = row["numeric_id"], row["views"]
    G.nodes[node_id]["views"] = target_value

graudono, media_grau_vizinhos = zip(*nx.average_degree_connectivity(G).items())

# Ajuste de curva para encontrar a reta de interpolação
coefficients = np.polyfit(graudono, media_grau_vizinhos, 1)
polynomial = np.poly1d(coefficients)

# Crie um gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(graudono, media_grau_vizinhos, alpha=0.5)
plt.plot(graudono, polynomial(graudono), color='red', label='Reta de Interpolação')
plt.xlabel('Grau do Nó')
plt.ylabel('Média do Grau dos Vizinhos')
plt.title('Gráfico de Dispersão com Reta de Interpolação')
plt.grid(True)
plt.legend()
plt.show()
