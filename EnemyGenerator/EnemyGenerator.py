from .AllEnemies import *
from random import randint


class EnemyGenerator:
    def __init__(self):
        self.enemiesRates = {
            range(0, 3): Rat,
            range(4, 7): Spider,
            range(8, 9): Undead,
            range(10, 10): Spectre
        }

    def getRandomEnemy(self):
        random = randint(0, 10)
        for enemyRange in self.enemiesRates:
            if enemyRange.start <= random <= enemyRange.stop:
                thatEnemy = self.enemiesRates[enemyRange]()
                return thatEnemy
