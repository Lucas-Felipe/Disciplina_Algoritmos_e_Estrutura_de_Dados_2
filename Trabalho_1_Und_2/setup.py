"""Arquivo de classe para o setup do carro"""
class Setup:
    """Classe do carro/setup"""
    def __init__(self, speed, power_unit, cornering, reliability, avg_pit_stop_time, configuracao, team_score):
        self.speed = speed
        self.power_unit = power_unit
        self.cornering = cornering
        self.reliability = reliability
        self.avg_pit_stop_time = avg_pit_stop_time
        self.configuracao = configuracao
        self.team_score = team_score

    def valida_atributos_max_220(self):
        """valida os valores dos atributos, máximo de 220"""
        if self.speed>220:
            self.speed = 220
        if self.power_unit>220:
            self.power_unit=220
        if self.cornering>220:
            self.cornering=220
        if self.reliability>220:
            self.reliability=220
