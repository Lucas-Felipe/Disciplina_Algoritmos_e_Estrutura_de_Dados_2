"""Arquivo do programa principal"""
import itertools
from carta import Carta
import matplotlib.pyplot as plt

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

# Lista de todas as cartas disponíveis
todas_as_cartas = [cartas_breaks, cartas_gearbox, cartas_rear_wing, cartas_front_wing,
                   cartas_suspension, cartas_engine]
combinacoes = list(itertools.product(*todas_as_cartas))

# Calcule os team_scores de todas as combinações
team_scores = [calcular_team_score(comb) for comb in combinacoes]

team_scores_acima_de_750 = [score for score in team_scores if score >= 750]

# Determine as faixas desejadas para o histograma
faixas = list(range(400, int(max(team_scores_acima_de_750)) + 1, 25))

# Defina o ponto de corte
PONTO_DE_CORTE = 875

# Crie um histograma com base nas faixas de team_scores
n, bins, patches = plt.hist(team_scores_acima_de_750, bins=faixas, edgecolor='k', color='blue')

# Encontre as barras após o ponto de corte e defina a cor como vermelha
for i, bi in enumerate(bins):
    if bi >= PONTO_DE_CORTE:
        for patch in patches[i:]:
            patch.set_fc('red')  # Define a cor da barra como vermelha

# Adicione um ponto de corte na cor vermelha
plt.axvline(x=PONTO_DE_CORTE, color='red', linestyle='--',
            label=f'Ponto de Corte: {PONTO_DE_CORTE}')

# Configure rótulos e título
plt.xlabel('Team Score')
plt.ylabel('Número de Ocorrências')
plt.title('Distribuição dos Team Scores')
plt.legend()  # Adicione uma legenda para o ponto de corte

# Salve o gráfico
plt.savefig('team_score_hist_23')
valores_entre_425_450 = []
for valor in team_scores:
    if 890 <= valor <= 900:
        valores_entre_425_450.append(valor)
print("tamanho: ", len(valores_entre_425_450))
