import osmnx as ox
import networkx as nx
import folium

# Carrega o grafo da área a partir do arquivo .osm
graph = ox.graph_from_xml('map (3).osm', simplify=False)

# Converter multigrafo para grafo simples
graph = nx.Graph(graph)

# Métricas de Grafo
degree = dict(nx.degree(graph))
clustering = nx.clustering(graph)
closeness = nx.closeness_centrality(graph)
betweenness = nx.betweenness_centrality(graph)
eigenvector = nx.eigenvector_centrality(graph, max_iter=500)

# Encontrar nós relevantes para cada métrica
relevant_nodes = set([
    max(degree, key=degree.get),
    max(clustering, key=clustering.get),
    max(closeness, key=closeness.get),
    max(betweenness, key=betweenness.get),
    max(eigenvector, key=eigenvector.get)
])

# Criar um mapa interativo usando folium
m = folium.Map(location=[-6.1957818, -35.0153689], zoom_start=12)

# Adicionar nós relevantes ao mapa
for node in relevant_nodes:
    info = f'Node: {node}<br> Degree: {degree[node]}<br> Clustering: {clustering[node]:.4f}<br> Closeness: {closeness[node]:.4f}<br> Betweenness: {betweenness[node]:.4f}<br> Eigenvector: {eigenvector[node]:.4f}'
    folium.CircleMarker(location=(graph.nodes[node]['y'], graph.nodes[node]['x']),
                        radius=5, color='red', fill=True, popup=folium.Popup(info, max_width=300)).add_to(m)

# Salvar o mapa interativo em um arquivo HTML
m.save('interactive_map_relevant_nodes_3_smaller_santa.html')
