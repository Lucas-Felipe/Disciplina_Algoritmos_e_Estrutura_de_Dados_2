"""Arquivo de classe para representar o piloto"""
class Piloto:
    """Classe do piloto"""
    def __init__(self, name, overtaking, defending, qualifying, race_start, tyre_management):
        self.name = name
        self.overtaking = overtaking
        self.defending = defending
        self.qualifying = qualifying
        self.race_start = race_start
        self.tyre_management = tyre_management
