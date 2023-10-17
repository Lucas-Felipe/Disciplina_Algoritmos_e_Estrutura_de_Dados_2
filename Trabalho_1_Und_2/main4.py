"""Programa principal para o item 4"""
from itertools import combinations, product
from piloto import Piloto
from carta import Carta
from boost import Boost
from setup import Setup

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

pilotos = [
    Piloto("Max Verstappen", 97,86,99,89,94),
    Piloto("Charlhes Leclerc", 93,99,97,87,89),
    Piloto("Fernando Alonso", 99,92,89,97,88),
    Piloto("Lewis Hamilton", 81,86,89,94,90),
    Piloto("Lando Norris",99,95,99,99,99),
    Piloto("George Russel", 95,90,91,83,86),
    Piloto("Sergio Perez", 85,96,89,91,84),
    Piloto("Carlos Sainz", 84,85,95,90,91),
    Piloto("Lance Stroll", 92,83,87,94,89),
    Piloto("Pierre Gasly", 88,93,83,85,96),
]

cartas = [cartas_breaks, cartas_gearbox, cartas_rear_wing, cartas_front_wing, cartas_suspension,
          cartas_engine]

def team_score(piloto, setup, boost):
    """calculo do team score"""
    piloto_metrics = [piloto.overtaking, piloto.defending, piloto.qualifying,
                       piloto.race_start, piloto.tyre_management]
    setup_metrics = [setup.speed, setup.power_unit, setup.cornering,
                      setup.reliability,setup.avg_pit_stop_time / 0.02]
    boost_metrics = [getattr(boost, "speed"), getattr(boost, "cornering"),
                     getattr(boost, "power_unit"), getattr(boost, "reliability"),
                     getattr(boost, "avg_pit_stop_time") / 0.02, getattr(boost, "overtaking"), 
                     getattr(boost, "defending"), getattr(boost, "qualifying"),
                     getattr(boost, "race_start"), getattr(boost, "tyre_management")]
    return sum(piloto_metrics) + sum(setup_metrics) + sum(boost_metrics)

# Função para calcular a soma dos atributos de uma combinação de cartas
def calcular_soma_atributos(comb):
    soma_atributos = {
        "speed": 0,
        "power_unit": 0,
        "cornering": 0,
        "reliability": 0,
        "avg_pit_stop_time": 0
    }
    for carta in comb:
        soma_atributos["speed"] += carta.speed
        soma_atributos["power_unit"] += carta.power_unit
        soma_atributos["cornering"] += carta.cornering
        soma_atributos["reliability"] += carta.reliability
        soma_atributos["avg_pit_stop_time"] += carta.avg_pit_stop_time
    return soma_atributos

# Todas as combinações possíveis de 6 cartas
todas_combinacoes = list(combinations(
    cartas_breaks + cartas_gearbox + cartas_rear_wing + cartas_front_wing + cartas_suspension + cartas_engine, 6))

# Encontrar combinações com soma de atributos maior que 875
comb_validas = []
for comb in todas_combinacoes:
    soma = calcular_soma_atributos(comb)
    if all(val > 875 for val in soma.values()):
        comb_validas.append(comb)

# Imprimir combinações válidas
print(f"Total de combinações válidas: {len(comb_validas)}")
for i, comb in enumerate(comb_validas, 1):
    print(f"Combinação {i}: {comb}")