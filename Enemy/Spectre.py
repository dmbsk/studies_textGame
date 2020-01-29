from .Enemy import Enemy


class Spectre(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'Spectre')
        self.stats.strength = 20
        self.stats.vitality = 20
        self.xpReward = 4
        self.level = 4

        self.updateAllStats()

    def fullEnemyString(self):
        return super(Spectre, self).fullEnemyString()