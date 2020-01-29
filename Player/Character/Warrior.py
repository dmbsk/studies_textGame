from .DefaultClass import DefaultClass


class Warrior(DefaultClass):
    def __init__(self):
        DefaultClass.__init__(self)
        self.name = 'Warrior'
        self.strengthMultiplier = 0.3
        self.vitalityMultiplier = 0.3
