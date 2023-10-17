"""Arquivo de classe para a carta de cada peça do carro"""
class Carta:
    """Classe da carta"""
    def __init__(self, tipo, name, speed, power_unit, cornering, reliability, avg_pit_stop_time):
        self.tipo = tipo
        self.name = name
        self.speed = speed
        self.cornering = cornering
        self.power_unit = power_unit
        self.reliability = reliability
        self.avg_pit_stop_time = avg_pit_stop_time

    def __str__(self):
        return f"{self.name} ({self.tipo})"

    def calcular_atributos(self):
        """Retorna um dicionário com os atributos da carta"""
        return {
            "speed": self.speed,
            "power_unit": self.power_unit,
            "cornering": self.cornering,
            "reliability": self.reliability,
            "avg_pit_stop_time": self.avg_pit_stop_time
        }
