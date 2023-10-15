from boost import Boost
import networkx as nx
import matplotlib.pyplot as plt

# Defina os boosts
boosts = [
    Boost("Reindeer", 0, 0, 10, 20, 0, 0, 20, 0, 0),
    Boost("Eclipse", 25, 0, 0, 10, 0, 15, 0, 0, 0),
    Boost("Rainbow", 20, 0, 0, 0, 0, 0, 25, 5, 0),
    Boost("Grip", 0, 25, 0, 0, 15, 0, 0, 10, 0),
    Boost("Nazar", 0, 0, 0, 0, 15, 0, 0, 20, 15),
    Boost("Palm", 0, 0, 0, 0, 0, 0, 20, 10, 20),
    Boost("Movember", 0, 25, 0, 0, 0, 0, 15, 0, 10),
    Boost("Firework", 20, 0, 0, 0, 0, 15, 0, 15, 0),
    Boost("Skull", 25, 0, 10, 0, 0, 15, 0, 0, 0),
    Boost("Samba", 5, 0, 25, 20, 0, 0, 0, 0, 0),
    Boost("Taurus", 20, 0, 25, 0, 0, 5, 0, 0, 0),
    Boost("Merlion", 15, 25, 0, 10, 0, 0, 0, 0, 0)
]

# Crie um objeto de gráfico bipartido direcionado
G = nx.DiGraph()

# Defina os nós para as duas partições (boosts e características)
boosts = [boost for boost in boosts]
characteristics = [
    "speed", "power_unit", "cornering", "reliability", "avg_pit_stop_time",
    "overtaking", "defending", "race_start", "tyre_management"
]

# Adicione nós das duas partições ao gráfico
G.add_nodes_from(boosts, bipartite=0)
G.add_nodes_from(characteristics, bipartite=1)

# Crie as arestas direcionadas entre as características e os boosts
for boost in boosts:
    for characteristic in characteristics:
        weight = getattr(boost, characteristic)
        if weight > 0:
            G.add_edge(characteristic, boost, weight=weight)

# Crie um dicionário para mapear os nós para seus nomes
node_labels = {node: f"{node.name if isinstance(node, Boost) else node}" for node in G.nodes}
node_labels.update({node: f"{node}\nOut Degree: {G.out_degree(node, weight='weight')}" for node in characteristics})

# Defina cores diferentes para os grupos
node_colors = ['yellow' if isinstance(node, Boost) else 'lightblue' for node in G.nodes]

# Ajuste o tamanho dos nós com base no out degree, excluindo os nós Boost
node_sizes = [G.out_degree(node, weight='weight') * 50 if not isinstance(node, Boost) else 1000 for node in G.nodes]

# Posicione os nós usando um layout bipartido na vertical
pos = nx.bipartite_layout(G, boosts, align='vertical')

# Desenhe o gráfico bipartido com as arestas direcionadas, setas, out degree nas características, cores diferentes e tamanhos ajustados
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=node_sizes, font_size=10, node_color=node_colors, connectionstyle="arc3, rad = 0.1")
plt.title("Gráfico de Rede Bipartido dos Boosts e Características (Vertical) com Setas, Out Degree nas Características, Cores Diferentes e Tamanhos Ajustados")
# plt.show()
plt.savefig('grafico_bi_partido_boosts.png')
