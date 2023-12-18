import osmnx as ox
import networkx as nx
import folium
from folium import plugins

# Carrega o grafo da área a partir do arquivo .osm
graph = ox.graph_from_xml('map.osm', simplify=False)

# Converter multigrafo para grafo simples
graph = nx.Graph(graph)

# Métricas do grafo
eccentricity = nx.eccentricity(graph)
diameter = nx.diameter(graph)
periphery = nx.periphery(graph)
radius = nx.radius(graph)
center = nx.center(graph)

# Calcular a média das coordenadas para definir o ponto central do mapa
mean_latitude = sum(graph.nodes[node]['y'] for node in graph.nodes) / len(graph.nodes)
mean_longitude = sum(graph.nodes[node]['x'] for node in graph.nodes) / len(graph.nodes)

# Criar um mapa interativo usando folium
m = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=12)

# Adicionar nós relevantes ao mapa
for node_id in periphery:
    node = graph.nodes[node_id]
    folium.CircleMarker(
        location=(node['y'], node['x']),
        radius=5,
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(m)

for node_id in center:
    node = graph.nodes[node_id]
    folium.CircleMarker(
        location=(node['y'], node['x']),
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

# Adicionar arestas ao mapa
for edge in graph.edges():
    folium.PolyLine(
        locations=[(graph.nodes[edge[0]]['y'], graph.nodes[edge[0]]['x']),
                   (graph.nodes[edge[1]]['y'], graph.nodes[edge[1]]['x'])],
        color='black',
        weight=2
    ).add_to(m)

# Salvar o mapa interativo como um arquivo HTML
m.save('mapa_interativo.html')
