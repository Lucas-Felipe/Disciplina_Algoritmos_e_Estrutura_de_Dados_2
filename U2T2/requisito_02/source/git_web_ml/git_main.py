"""Arquivo principal para rede deezer"""
import json
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar as arestas da rede a partir do arquivo CSV
EDGES_FILE = "drive/MyDrive/git_web_ml/musae_git_edges.csv"
edges_data = pd.read_csv(EDGES_FILE)

# Crie um objeto Graph vazio para representar a rede
G = nx.Graph()

# Adicione as arestas ao grafo
for index, row in edges_data.iterrows():
    source_node, target_node = row["id_1"], row["id_2"]
    G.add_edge(source_node, target_node)

# Carregar as características dos nós a partir do arquivo JSON
FEATURES_FILE = "drive/MyDrive/git_web_ml/musae_git_features.json"
with open(FEATURES_FILE, "r", encoding="utf-8") as json_file:
    features_data = json.load(json_file)

# Adicionar características aos nós do grafo
for node_id, node_features in features_data.items():
    G.nodes[int(node_id)]["features"] = node_features

# Carregar o alvo (target) dos nós a partir do arquivo CSV
TARGET_FILE = "drive/MyDrive/git_web_ml/musae_git_target.csv"
target_data = pd.read_csv(TARGET_FILE)

# Adicionar o alvo (target) aos nós do grafo
for index, row in target_data.iterrows():
    node_id, target_value = row["id"], row["ml_target"]
    G.nodes[node_id]["ml_target"] = target_value

# Calcule os graus dos nós e dos vizinhos
node_degrees = dict(G.degree())
neighbor_degrees = {node: sum(node_degrees[neighbor]
                              for neighbor in G.neighbors(node))
                              for node in G.nodes()}

# Crie um gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(list(node_degrees.values()), list(neighbor_degrees.values()), alpha=0.5)
plt.xlabel('Grau dos Nós')
plt.ylabel('Grau dos Vizinhos')
plt.title('Gráfico de Dispersão: Grau dos Nós vs. Grau dos Vizinhos')
plt.grid(True)

# Calcule a reta de melhor ajuste (linear) usando a função polyfit do NumPy
x = np.array(list(node_degrees.values()))
y = np.array(list(neighbor_degrees.values()))
slope, intercept = np.polyfit(x, y, 1)

# Crie a reta linear a partir dos coeficientes
line = slope * x + intercept

# Adicione a reta linear ao gráfico
plt.plot(x, line, color='red', label='Reta Linear de Melhor Ajuste')

plt.legend()
plt.show()
