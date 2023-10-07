"""Arquivo de classe para representar o piloto"""
class Carta:
    """Classe do piloto"""
    def __init__(self, name, overtaking, qualifying, race_start, tyre_management):
        self.name = name
        self.overtaking = overtaking
        self.qualifying = qualifying
        self.race_start = race_start
        self.tyre_management = tyre_management
