from .Character.Character import Character as newCharacter
from Enemy.Enemy import Enemy
from TextColor.TextColor import TextColor
from random import Random
c = TextColor()


class Player:
    def __init__(self, playerName, playerCharacterClass):
        self.character = newCharacter(playerCharacterClass)
        self.name = '%s%s%s' % (c.bold, playerName, c.normal)
        self.isAlive = True
        self.nameAndHealth = '%s %s \033[1;0;32m/ %s' % (self.name,
                                                         self.character.stats.lifePoints_String,
                                                         self.character.stats.lifePointsMax_String)
    def battleOrDodge(self, enemy):
        if isinstance(enemy, Enemy):
            print('You found %s in the corridor' % enemy.fullEnemyString())
            print('Dodge chance is %.2f' % self.getDodgeChance(enemy) + "%")
            answer = ''
            goodAnswers = ['Dodge', 'Fight']
            while answer not in goodAnswers:
                print('If you want try dodging enemy type "Dodge" else type "Fight"')
                answer = input('What do you choose: ')
                if answer in goodAnswers:
                    {
                        'Dodge': self.tryDodge,
                        'Fight': self.battleAgainst
                    }[answer](enemy)

    def tryDodge(self, enemy):
        dodeChance = self.getDodgeChance(enemy)
        random = Random()
        randFloat = round(random.uniform(0, 100), 2)
        if randFloat <= dodeChance:
            print('You successfully dodge %s' % enemy.fullEnemyString())
            return True
        print('%s spotted you, you have to fight!' % enemy.fullEnemyString())
        self.battleAgainst(enemy)


    def battleAgainst(self, enemy):
        if isinstance(enemy, Enemy):
            print('%s starts battle against %s' % (self.name, enemy.fullEnemyString()))
            battleRound = 1
            while self.character.stats.lifePoints > 0 or enemy.stats.lifePoints > 0:

                print('\n\n-----===== %i =====-----' % battleRound)
                status = self.takeDamage(enemy)
                if status:
                    return False

                input('\nPress Enter to Attack enemy %s \n' % enemy.fullEnemyString())
                status = self.doDamage(enemy)
                if status:
                    return True

                battleRound += 1

    def takeDamage(self, enemy):
        self.character.stats.lifePoints = round(self.character.stats.lifePoints - enemy.stats.attackPower, 2)
        self.character.stats.recountStrings()
        print('%s attacked %s and dealt %s damage' % (enemy.fullEnemyString(), self.name, enemy.stats.attackPower_String))
        self.printCharacterLifeStatus()
        if self.character.stats.lifePoints <= 0:
            return self.die()
        return False

    def die(self):
        print('! You died !')
        self.isAlive = False
        return True

    def doDamage(self, enemy):
        damage = self.character.stats.attackPower
        random = Random()
        randFloat = round(random.uniform(0, 100), 2)
        if randFloat <= self.character.stats.criticalChance:
            print("Your hit is critical!")
            damage *= 2.5
        enemy.stats.lifePoints = round(enemy.stats.lifePoints - damage, 2)
        enemy.stats.recountStrings()
        print('You dealt %s%.2f%s damage to enemy %s' % (c.damage, damage, c.normal, enemy.fullEnemyString()))
        if enemy.stats.lifePoints <= 0:
            self.enemyDie(enemy)
            return True
        return False

    def enemyDie(self, enemy):
        print('%s died!' % enemy.fullEnemyString())
        print('Your reward for battle: %i exp' % enemy.xpReward)
        self.character.experience += enemy.xpReward
        if self.character.isXpEnoughtForLvlup():
            self.character.levelUp()
            return True
        return False

    def printCharacterLifeStatus(self):
        print('Your life is %s \033[1;0;32m/ %s' % (self.character.stats.lifePoints_String, self.character.stats.lifePointsMax_String))

    def getDodgeChance(self, enemy):
        return round((self.character.stats.dodgeFight * (1 / enemy.level)) * 100, 2)

