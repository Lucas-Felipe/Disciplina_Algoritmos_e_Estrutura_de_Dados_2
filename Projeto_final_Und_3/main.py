import matplotlib.pyplot as plt
import osmnx as ox

# Seu código para gerar o gráfico com o OSMnx
place_name = "Santa Cruz, RN"
graph = ox.graph_from_place(place_name, network_type='all')
ox.plot_graph(ox.project_graph(graph))

# Salvar o gráfico como um arquivo PNG
plt.savefig("ruas_sta_cruz.png", format="png")

num_nodes = ox.utils_graph.graph_to_gdfs(graph, edges=False).shape[0]
num_edges = ox.utils_graph.graph_to_gdfs(graph, nodes=False).shape[0]

print(f"Número de Nós: {num_nodes}")
print(f"Número de Arestas: {num_edges}")

