from TextColor.TextColor import TextColor
c = TextColor()

class Stats:
    def __init__(self):
        self.vitality = 1
        self.agility = 1
        self.strength = 1
        self.luck = 1

        self.vitalityMultiplier = 0.2
        self.agilityMultiplier = 0.2
        self.strengthMultiplier = 0.2
        self.luckMultiplier = 7

        self.lifePoints = None
        self.lifePointsMax = None
        self.attackPower = None
        self.dodgeFight = None
        self.criticalChance = None

        self.attackPower_String = ''
        self.lifePoints_String = ''
        self.lifePointsMax_String = ''
        self.dodgeFight_String = ''
        self.criticalChance_String = ''

    def countOtherstats(self):
        self.lifePoints = round(self.vitality * self.vitalityMultiplier, 2)
        self.lifePointsMax = self.lifePoints
        self.attackPower = round(self.strength * self.strengthMultiplier, 2)
        self.dodgeFight = round(self.agility * self.agilityMultiplier, 2)
        self.criticalChance = round(self.luck * self.luckMultiplier, 2)

    def recountStrings(self):
        self.attackPower_String = '%s%.2f%s' % (c.damage, self.attackPower, c.normal)  # red
        self.lifePoints_String = '%s%.2f%s' % (c.life, self.lifePoints, c.normal)  # green
        self.lifePointsMax_String = '%s%.2f%s' % (c.life, self.lifePointsMax, c.normal)  # green
        self.dodgeFight_String = '%s%.2f%s' % (c.dodge, self.dodgeFight, c.normal)  # green
        self.criticalChance_String = '%s%.2f%s' % (c.critical, self.criticalChance, c.normal)  # yellow

    def increaseStrength(self, increaseBy = 1):
        self.strength += increaseBy
        self.countOtherstats()
        self.recountStrings()
        print('Strength increased by %i.' % increaseBy)
        print('Current stats:')
        print('Strength points: %i' % self.strength)
        print('Attack power is now %s' % self.attackPower_String)

    def increaseVitality(self, increaseBy = 1):
        self.vitality += increaseBy
        self.countOtherstats()
        self.recountStrings()
        print('Vitality increased by %i.' % increaseBy)
        print('Current stats:')
        print('Vitality points: %i' % self.vitality)
        print('Max Life points is now %s' % self.lifePoints_String)

    def increaseAgility(self, increaseBy = 1):
        self.agility += increaseBy
        self.countOtherstats()
        self.recountStrings()
        print('Agility increased by %i.' % increaseBy)
        print('Current stats:')
        print('Agility points: %i' % self.agility)
        print('Dodge chance is now %s' % self.dodgeFight_String)

    def increaseLuck(self, increaseBy = 1):
        self.luck += increaseBy
        self.countOtherstats()
        self.recountStrings()
        print('Strength increased by %i.' % increaseBy)
        print('Current stats:')
        print('Luck points: %i' % self.luck)
        print('Crit chance is now %s' % self.criticalChance_String + "%")
