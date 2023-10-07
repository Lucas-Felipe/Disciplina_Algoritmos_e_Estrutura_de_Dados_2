"""Arquivo de classe para a carta de cada peça do carro"""
class Carta:
    """Classe da carta"""
    def __init__(self, tipo, name, speed, power_unit, cornering, reliability, avg_pit_stop_time):
        self.tipo = tipo
        self.name = name
        self.speed = speed
        self.power_unit = power_unit
        self.cornering = cornering
        self.reliability = reliability
        self.avg_pit_stop_time = avg_pit_stop_time
