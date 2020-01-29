from .AllCharacters import *
from Stats.Stats import Stats
from TextColor.TextColor import TextColor
c = TextColor()


class Character:
    def __init__(self, playerCharacterClass):
        self.stats = Stats()
        self.stats.vitality = 50
        self.stats.strength = 5
        self.characterClass = {
            'Warrior': self._createWarrior,
            'Rogue': self._createRogue,
            'Mage': self._createMage
        }[playerCharacterClass]()
        self._countClassBonuses()
        self.stats.countOtherstats()

        self.level = 1
        self.experience = 0
        self.experienceToLevel = self.level

    def _createWarrior(self):
        self.stats.countOtherstats()
        return Warrior()

    def _createRogue(self):
        self.stats.countOtherstats()
        return Rogue()

    def _createMage(self):
        self.stats.countOtherstats()
        return Mage()

    def _countClassBonuses(self):
        # Warrior bonuses
        self.stats.strengthMultiplier = self.characterClass.strengthMultiplier
        self.stats.vitalityMultiplier = self.characterClass.vitalityMultiplier

        # Rogue bonuses
        self.stats.agilityMultiplier = self.characterClass.agilityMultiplier

        # Mage bonuses
        self.stats.luck += self.characterClass.bonusLuck
        self.stats.luckyMultiplier = self.characterClass.luckMultiplier

    def levelUp(self):
        self.experience = self.experience - self.level
        self.level += 1
        self.experienceToLevel = self.level
        self.levelUpMenu() #adding stats
        self.stats.lifePoints = self.stats.lifePointsMax
        self.stats.countOtherstats()

    def levelUpMenu(self):
        statToUpgrade = ''
        print('%sCongratulations!' % c.level)
        print('You just leveled to %i!' % self.level)
        statList = ['Strength', 'Vitality', 'Agility', 'Luck']
        while statToUpgrade not in statList:
            print('Current stats:')
            print('Strength: %i' % self.stats.strength)
            print('Vitality: %i' % self.stats.vitality)
            print('Agility: %i' % self.stats.agility)
            print('Luck: %i' % self.stats.luck)
            statToUpgrade = input('Write stat name that you want to increase: ')
            if statToUpgrade not in statList:
                print("%s is not a stat from stat list" % statToUpgrade)
            else:
                {
                    'Strength': self.stats.increaseStrength,
                    'Vitality': self.stats.increaseVitality,
                    'Agility': self.stats.increaseAgility,
                    'Luck': self.stats.increaseLuck
                }[statToUpgrade]()

    def isXpEnoughtForLvlup(self):
        return self.experience >= self.experienceToLevel
