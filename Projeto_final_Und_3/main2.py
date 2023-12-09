import osmnx as ox
import matplotlib.pyplot as plt

# Carrega o grafo da área a partir do arquivo .osm
graph = ox.graph_from_xml('map.osm', simplify=False)

# Plota o grafo
ox.plot_graph(ox.project_graph(graph))
plt.savefig("ruas_sta_cruz2.png", format="png")

# Conta o número de nós e arestas
num_nodes = ox.utils_graph.graph_to_gdfs(graph, edges=False).shape[0]
num_edges = ox.utils_graph.graph_to_gdfs(graph, nodes=False).shape[0]

print(f"Número de Nós: {num_nodes}")
print(f"Número de Arestas: {num_edges}")
