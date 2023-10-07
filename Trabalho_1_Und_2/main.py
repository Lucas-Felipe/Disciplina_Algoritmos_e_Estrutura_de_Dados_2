# team_score = speed + cornering + power_unit + reliability + (avg_pit_stop_time/0.02)
from carta import Carta

# Lista de cartas para os freios
cartas_breaks = [
    Carta("Breaks", "wildcore", 5, 3, 4, 7, 2),
    Carta("Breaks", "suspense", 4, 4, 3, 6, 2),
    Carta("Breaks", "the warden", 3, 5, 4, 5, 3),
    Carta("Breaks", "onyx", 4, 3, 5, 6, 2),
    Carta("Breaks", "axiom", 6, 2, 3, 5, 4),
    Carta("Breaks", "crisis sl", 5, 3, 4, 7, 3),
    Carta("Breaks", "essence", 3, 4, 5, 5, 3),
    Carta("Breaks", "starter", 4, 2, 6, 6, 2)
]

# Lista de cartas para a caixa de câmbio
cartas_gearbox = [
    Carta("Gearbox", "voyage", 5, 4, 4, 6, 2),
    Carta("Gearbox", "vector", 4, 5, 3, 5, 3),
    Carta("Gearbox", "kick shift", 3, 4, 5, 6, 2),
    Carta("Gearbox", "verdict", 4, 3, 4, 7, 3),
    Carta("Gearbox", "spectrum", 6, 3, 3, 5, 4),
    Carta("Gearbox", "swiftcharge", 5, 4, 4, 6, 3),
    Carta("Gearbox", "switch-r-00", 3, 5, 5, 5, 2),
    Carta("Gearbox", "starter", 4, 4, 6, 6, 2)
]

# Lista de cartas para a asa traseira
cartas_rear_wing = [
    Carta("Rear Wing", "typhoon", 5, 4, 4, 7, 2),
    Carta("Rear Wing", "transcendence", 4, 5, 3, 6, 3),
    Carta("Rear Wing", "freeflare", 3, 4, 5, 5, 2),
    Carta("Rear Wing", "the patron", 4, 3, 4, 6, 2),
    Carta("Rear Wing", "the wasp", 6, 3, 3, 7, 3),
    Carta("Rear Wing", "the matador", 5, 4, 4, 5, 4),
    Carta("Rear Wing", "phantom-x", 3, 5, 5, 6, 2),
    Carta("Rear Wing", "starter", 4, 4, 6, 5, 3)
]

# Lista de cartas para a asa dianteira
cartas_front_wing = [
    Carta("Front Wing", "virtue", 5, 4, 4, 6, 3),
    Carta("Front Wing", "thunderclap", 4, 5, 3, 5, 2),
    Carta("Front Wing", "trailblazer", 3, 4, 5, 7, 3),
    Carta("Front Wing", "zeno", 4, 3, 4, 6, 2),
    Carta("Front Wing", "the vagabond", 6, 3, 3, 5, 4),
    Carta("Front Wing", "feral punch", 5, 4, 4, 7, 2),
    Carta("Front Wing", "the scout", 3, 5, 5, 6, 2),
    Carta("Front Wing", "starter", 4, 4, 6, 5, 3)
]

# Lista de cartas para a suspensão
cartas_suspension = [
    Carta("Suspension", "sigma", 5, 4, 4, 6, 3),
    Carta("Suspension", "presence", 4, 5, 3, 5, 2),
    Carta("Suspension", "horizon", 3, 4, 5, 7, 3),
    Carta("Suspension", "radiance", 4, 3, 4, 6, 2),
    Carta("Suspension", "icon v3", 6, 3, 3, 5, 4),
    Carta("Suspension", "rodeo", 5, 4, 4, 7, 2),
    Carta("Suspension", "the equator", 3, 5, 5, 6, 2),
    Carta("Suspension", "starter", 4, 4, 6, 5, 3)
]

# Lista de cartas para o motor
cartas_engine = [
    Carta("Engine", "cloudroar", 5, 4, 4, 6, 3),
    Carta("Engine", "avalanche", 4, 5, 3, 5, 2),
    Carta("Engine", "the rover", 3, 4, 5, 7, 3),
    Carta("Engine", "twinburst", 4, 3, 4, 6, 2),
    Carta("Engine", "enigma", 6, 3, 3, 5, 4),
    Carta("Engine", "nova", 5, 4, 4, 7, 2),
    Carta("Engine", "brute force", 3, 5, 5, 6, 2),
    Carta("Engine", "starter", 4, 4, 6, 5, 3)
]
