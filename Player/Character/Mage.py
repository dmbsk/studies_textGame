from .DefaultClass import DefaultClass


class Mage(DefaultClass):
    def __init__(self):
        DefaultClass.__init__(self)
        self.name = 'Mage'
        self.bonusLuck = 4
