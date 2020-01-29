from .Enemy import Enemy


class Undead(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'Undead')
        self.stats.vitality = 15
        self.stats.strength = 15
        self.xpReward = 3
        self.level = 3

        self.updateAllStats()

    def fullEnemyString(self):
        return super(Undead, self).fullEnemyString()
