"""Arquivo de classe para boost de vantagem"""
class Boost:
    """Classe dos boosts"""
    def __init__(self, name, speed, power_unit, cornering, reliability, avg_pit_stop_time,
                 overtaking, defending, race_start, tyre_management):
        self.name = name
        self.speed = speed
        self.power_unit = power_unit
        self.cornering = cornering
        self.reliability = reliability
        self.avg_pit_stop_time = avg_pit_stop_time
        self.overtaking = overtaking
        self.defending = defending
        self.race_start = race_start
        self.tyre_management = tyre_management
