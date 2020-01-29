from Stats.Stats import Stats
from TextColor.TextColor import TextColor
c = TextColor()


class Enemy:
    def __init__(self, enemyName):
        self.name = '%s%s%s' % (c.bold, enemyName, c.normal)
        self.level = 1
        self.xpReward = 1

        self.stats = Stats()

    def fullEnemyString(self):
        return '%s %sLv%i %s' % (self.name, c.level, self.level, self.stats.lifePoints_String)

    def updateAllStats(self):
        self.stats.countOtherstats()
        self.stats.recountStrings()
