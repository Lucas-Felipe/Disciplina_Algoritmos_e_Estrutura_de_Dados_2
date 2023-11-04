"""Arquivo principal para rede lasftm asia"""
import json
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar as arestas da rede a partir do arquivo CSV
EDGES_FILE = "drive/MyDrive/lasftm_asia/lastfm_asia_edges.csv"
edges_data = pd.read_csv(EDGES_FILE)

# Crie um objeto Graph vazio para representar a rede
G = nx.Graph()

# Adicione as arestas ao grafo
for index, row in edges_data.iterrows():
    source_node, target_node = row["node_1"], row["node_2"]
    G.add_edge(source_node, target_node)

# Carregar as características dos nós a partir do arquivo JSON
FEATURES_FILE = "drive/MyDrive/lasftm_asia/lastfm_asia_features.json"
with open(FEATURES_FILE, "r", encoding="utf-8") as json_file:
    features_data = json.load(json_file)

# Adicionar características aos nós do grafo
for node_id, node_features in features_data.items():
    G.nodes[int(node_id)]["features"] = node_features

# Carregar o alvo (target) dos nós a partir do arquivo CSV
TARGET_FILE = "drive/MyDrive/lasftm_asia/lastfm_asia_target.csv"
target_data = pd.read_csv(TARGET_FILE)

# Adicionar o alvo (target) aos nós do grafo
for index, row in target_data.iterrows():
    node_id, target_value = row["id"], row["target"]
    G.nodes[node_id]["target"] = target_value

# Calcule os graus dos nós e dos vizinhos
node_degrees = dict(G.degree())
neighbor_degrees = {node: sum(node_degrees[neighbor]
                              for neighbor in G.neighbors(node))
                              for node in G.nodes()}

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
