"""Arquivo de classe para o setup do carro"""
from carta import Carta

class Setup:
    """Classe do carro/setup"""
    def __init__(self):
        self.front_wing = None  # Carta de asa dianteira
        self.rear_wing = None   # Carta de asa traseira
        self.suspension = None  # Carta de suspensão
        self.gearbox = None     # Carta de caixa de câmbio
        self.engine = None      # Carta de motor
        self.breaks = None      # Carta de freios
        self.team_score = 0

    def __str__(self):
        return f"Team Score: {self.team_score}"

    # Métodos para definir as cartas em cada atributo
    def definir_front_wing(self, carta):
        if self.front_wing is None:
            self.front_wing = carta
        else:
            print("A asa dianteira já possui uma carta. Não é possível adicionar mais cartas.")

    def definir_rear_wing(self, carta):
        if self.rear_wing is None:
            self.rear_wing = carta
        else:
            print("A asa traseira já possui uma carta. Não é possível adicionar mais cartas.")

    def definir_suspension(self, carta):
        if self.suspension is None:
            self.suspension = carta
        else:
            print("A suspensão já possui uma carta. Não é possível adicionar mais cartas.")

    def definir_gearbox(self, carta):
        if self.gearbox is None:
            self.gearbox = carta
        else:
            print("A suspensão já possui uma carta. Não é possível adicionar mais cartas.")

    def definir_engine(self, carta):
        if self.engine is None:
            self.engine = carta
        else:
            print("A suspensão já possui uma carta. Não é possível adicionar mais cartas.")

    def definir_breaks(self, carta):
        if self.breaks is None:
            self.breaks = carta
        else:
            print("A suspensão já possui uma carta. Não é possível adicionar mais cartas.")

    # Método para calcular a soma dos atributos
    def calcular_soma_atributos(self):
        soma_atributos = {
            "speed": 0,
            "power_unit": 0,
            "cornering": 0,
            "reliability": 0,
            "avg_pit_stop_time": 0
        }

        if self.front_wing:
            soma_atributos["speed"] += self.front_wing.speed
            soma_atributos["power_unit"] += self.front_wing.power_unit
            soma_atributos["cornering"] += self.front_wing.cornering
            soma_atributos["reliability"] += self.front_wing.reliability
            soma_atributos["avg_pit_stop_time"] += self.front_wing.avg_pit_stop_time

        if self.rear_wing:
            soma_atributos["speed"] += self.rear_wing.speed
            soma_atributos["power_unit"] += self.rear_wing.power_unit
            soma_atributos["cornering"] += self.rear_wing.cornering
            soma_atributos["reliability"] += self.rear_wing.reliability
            soma_atributos["avg_pit_stop_time"] += self.rear_wing.avg_pit_stop_time

        if self.suspension:
            soma_atributos["speed"] += self.suspension.speed
            soma_atributos["power_unit"] += self.suspension.power_unit
            soma_atributos["cornering"] += self.suspension.cornering
            soma_atributos["reliability"] += self.suspension.reliability
            soma_atributos["avg_pit_stop_time"] += self.suspension.avg_pit_stop_time

        if self.gearbox:
            soma_atributos["speed"] += self.gearbox.speed
            soma_atributos["power_unit"] += self.gearbox.power_unit
            soma_atributos["cornering"] += self.gearbox.cornering
            soma_atributos["reliability"] += self.gearbox.reliability
            soma_atributos["avg_pit_stop_time"] += self.gearbox.avg_pit_stop_time

        if self.engine:
            soma_atributos["speed"] += self.engine.speed
            soma_atributos["power_unit"] += self.engine.power_unit
            soma_atributos["cornering"] += self.engine.cornering
            soma_atributos["reliability"] += self.engine.reliability
            soma_atributos["avg_pit_stop_time"] += self.engine.avg_pit_stop_time

        if self.breaks:
            soma_atributos["speed"] += self.breaks.speed
            soma_atributos["power_unit"] += self.breaks.power_unit
            soma_atributos["cornering"] += self.breaks.cornering
            soma_atributos["reliability"] += self.breaks.reliability
            soma_atributos["avg_pit_stop_time"] += self.breaks.avg_pit_stop_time

        return soma_atributos
    