"""Arquivo do programa principal para a rede"""
import itertools
from carta import Carta
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Função para calcular a soma dos atributos de um setup
def calcular_soma_atributos(setup):
    """Calcula a soma de cada atributo advindo de cada carta"""
    soma_speed = sum(carta.speed for carta in setup)
    soma_power_unit = sum(carta.power_unit for carta in setup)
    soma_cornering = sum(carta.cornering for carta in setup)
    soma_reliability = sum(carta.reliability for carta in setup)
    soma_avg_pit_stop_time = sum(carta.avg_pit_stop_time for carta in setup)
    return soma_speed, soma_power_unit, soma_cornering, soma_reliability, soma_avg_pit_stop_time

def calcular_team_score(setup):
    """calcula o team score de cada setup"""
    (soma_speed, soma_power_unit, soma_cornering, soma_reliability,
     soma_avg_pit_stop_time) = calcular_soma_atributos(setup)
    team_score = (soma_speed + soma_cornering + soma_power_unit + soma_reliability +
                  (soma_avg_pit_stop_time / 0.02))
    return team_score

# Crie um novo grafo direcionado
G = nx.DiGraph()

# Lista de cartas para os freios
cartas_breaks = [
    Carta("Breaks", "wildcore", 36,23,33,22,0.59),
    Carta("Breaks", "suspense", 20, 32, 23,21, 0.37),
    Carta("Breaks", "the warden", 26,28,27,25,0.43),
    Carta("Breaks", "onyx", 26,23,25,50,0.49),
    Carta("Breaks", "axiom", 14,34,18,15,0.67),
    Carta("Breaks", "crisis sl", 27,16,18,19,0.51),
    Carta("Breaks", "essence", 14,13,12, 25, 0.76),
    Carta("Breaks", "starter", 1,1,1,1,1)
]

# Lista de cartas para a caixa de câmbio
cartas_gearbox = [
    Carta("Gearbox", "voyage", 25, 28, 22, 27, 0),
    Carta("Gearbox", "vector", 24, 38, 22, 36, 0.55),
    Carta("Gearbox", "kick shift", 18, 19, 29, 19, 0.45),
    Carta("Gearbox", "verdict", 33, 18, 20, 30, 0.63),
    Carta("Gearbox", "spectrum", 20, 25, 21, 23, 0.53),
    Carta("Gearbox", "swiftcharge", 14, 23, 22, 16, 0.71),
    Carta("Gearbox", "switch-r-00", 12, 13, 11, 14, 0.47),
    Carta("Gearbox", "starter", 1,1,1,1,1)
]

# Lista de cartas para a asa traseira
cartas_rear_wing = [
    Carta("Rear Wing", "typhoon", 50, 27, 26, 23, 0.53),
    Carta("Rear Wing", "transcendence", 24, 22, 36, 37, 0.53),
    Carta("Rear Wing", "freeflare", 21, 33, 20, 22, 0.37),
    Carta("Rear Wing", "the patron", 23, 21, 19, 37, 0.61),
    Carta("Rear Wing", "the wasp", 16, 24, 23, 14, 0.69),
    Carta("Rear Wing", "the matador", 19, 16, 18, 17, 0.72),
    Carta("Rear Wing", "phantom-x", 26, 15, 12, 11, 0.76),
    Carta("Rear Wing", "starter", 1,1,1,1,1)
]

# Lista de cartas para a asa dianteira
cartas_front_wing = [
    Carta("Front Wing", "virtue", 23, 50, 27, 24, 0.49),
    Carta("Front Wing", "thunderclap", 35, 23, 21, 33, 0.55),
    Carta("Front Wing", "trailblazer", 21, 23, 42, 20, 0.57),
    Carta("Front Wing", "zeno", 25, 23, 22, 26, 0.53),
    Carta("Front Wing", "the vagabond", 31, 20, 23, 21, 0.35),
    Carta("Front Wing", "feral punch", 13, 15, 22, 21, 0.73),
    Carta("Front Wing", "the scout", 13, 27, 15, 14, 0.73),
    Carta("Front Wing", "starter", 1,1,1,1,1)
]

# Lista de cartas para a suspensão
cartas_suspension = [
    Carta("Suspension", "sigma", 32, 28, 30, 29, 0.39),
    Carta("Suspension", "presence", 23, 26, 24, 22, 0.2),
    Carta("Suspension", "horizon", 22, 36, 24, 37, 0.53),
    Carta("Suspension", "radiance", 25, 17, 26, 19, 0.65),
    Carta("Suspension", "icon v3", 17, 13, 16, 23, 0.54),
    Carta("Suspension", "rodeo", 23, 22, 15, 14, 0.69),
    Carta("Suspension", "the equator", 20, 19, 18, 21, 0.61),
    Carta("Suspension", "starter", 1,1,1,1,1)
]

# Lista de cartas para o motor
cartas_engine = [
    Carta("Engine", "cloudroar", 26, 24, 50, 27, 0.55),
    Carta("Engine", "avalanche", 34, 22, 25, 21, 0.35),
    Carta("Engine", "the rover", 27, 25, 28, 24, 0.53),
    Carta("Engine", "twinburst", 16, 29, 18, 17, 0.51),
    Carta("Engine", "enigma", 16, 13, 23, 25, 0.69),
    Carta("Engine", "nova", 31, 13, 15, 16, 0.71),
    Carta("Engine", "brute force", 21, 19, 36, 18, 0.63),
    Carta("Engine", "starter", 1,1,1,1,1)
]

# Crie uma lista com todas as cartas disponíveis
todas_as_cartas = [cartas_breaks, cartas_gearbox, cartas_rear_wing, cartas_front_wing,
                   cartas_suspension, cartas_engine]
TEAM_SCORE_MAXIMO = 890
# Crie nós para cada setup e adicione as cartas usadas em cada setup
setups = list(itertools.product(cartas_breaks, cartas_gearbox, cartas_rear_wing, cartas_front_wing, cartas_suspension, cartas_engine))
setup_nodes = {}
setup_cards_used = {}

for setup in setups:
    team_score = calcular_team_score(setup)
    if team_score >= TEAM_SCORE_MAXIMO:
        setup_nodes[setup] = team_score
        G.add_node(setup, team_score=team_score, node_type="setup")
        setup_cards_used[setup] = [carta for carta in setup]

# Contagem da frequência de uso das cartas
carta_usage_count = {}
for setup, cards_used in setup_cards_used.items():
    for carta in cards_used:
        if carta in carta_usage_count:
            carta_usage_count[carta] += 1
        else:
            carta_usage_count[carta] = 1

# Adicione nós para as cartas usadas em setups
for setup, cards_used in setup_cards_used.items():
    for carta in cards_used:
        G.add_node(carta, node_type="carta")

# Adicione arestas que representam as cartas usadas em cada setup
for setup in setup_nodes:
    for carta in setup_cards_used[setup]:
        G.add_edge(setup, carta)

# Inverta as direções das arestas
G = G.reverse()

# Crie grupos de nós para separar os nós de setup e cartas
node_groups = {}
for node in G.nodes():
    node_groups[node] = 0 if G.nodes[node]["node_type"] == "setup" else 1

# Defina o layout com shell_layout para posicionar os nós de setup no centro
# e os nós de carta ao redor
pos = nx.shell_layout(G, [list(setup_nodes.keys()), list(G.nodes())])

# Rótulos dos nós (nomes das cartas ou Team Score)
node_labels = {node: f"{setup_nodes[node]}" if G.nodes[node]["node_type"] == "setup" else str(node) for node in G.nodes()}

# Calcula os tamanhos das bolas com base na frequência de uso das cartas
node_sizes = [carta_usage_count[node] * 700 if G.nodes[node]["node_type"] == "carta" else 700 for node in G.nodes()]

# Defina as cores dos nós e rótulos
node_colors = ["lightcoral" if G.nodes[node]["node_type"] == "setup" else "lightblue" for node in G.nodes()]

# Desenhe o grafo com rótulos, tamanhos e cores personalizadas
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=node_sizes, font_size=8, node_color=node_colors, font_color="black", font_weight="bold", edge_color="black")

# Exiba o gráfico
plt.savefig('rede_setups_e_cartas_com_rotulos_e_cores.png')

# Função de densidade de probabilidade para a propriedade "Out Degree" dos vértices de cartas
def plot_out_degree_prob_density(graph):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    
    # Calcula o "Out Degree" (número de conexões) para cada vértice de carta
    out_degrees = [val for (node, val) in graph.out_degree if graph.nodes[node]["node_type"] == "carta"]
    sns.kdeplot(out_degrees, shade=True, color="lightcoral")
    
    plt.xlabel("Out Degree (Número de Cartas por Setup)")
    plt.ylabel("Density")
    plt.title("PDF of Out Degree for Cards in Setups")
    
    plt.savefig('out_degree_prob_density.png')

# Crie a função de densidade de probabilidade para o "Out Degree" das cartas
plot_out_degree_prob_density(G)