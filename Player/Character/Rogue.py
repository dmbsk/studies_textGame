from .DefaultClass import DefaultClass


class Rogue(DefaultClass):
    def __init__(self):
        DefaultClass.__init__(self)
        self.name = 'Rogue'
        self.agilityMultiplier = 0.4
