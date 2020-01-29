from .Enemy import Enemy


class Spider(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'Spider')
        self.stats.vitality = 10
        self.stats.strength = 10
        self.xpReward = 2
        self.level = 2

        self.updateAllStats()

    def fullEnemyString(self):
        return super(Spider, self).fullEnemyString()
