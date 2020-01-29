from .Enemy import Enemy


class Rat(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'Rat')
        self.stats.vitality = 5
        self.stats.strength = 5
        self.xpReward = 1

        self.updateAllStats()

    def fullEnemyString(self):
        return super(Rat, self).fullEnemyString()
