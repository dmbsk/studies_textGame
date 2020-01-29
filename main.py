from Player.Player import Player
from EnemyGenerator.EnemyGenerator import EnemyGenerator
from Map.Map import Map
from Thinker.Thinker import Thinker
from Menu.Menu import *

thinker = Thinker()
enemyGenerator = EnemyGenerator()
map = Map()
map.generateRandomMap()
player = Player(getPlayerName(), getPlayerCharacterClass())

for level in range(25):
    if player.isAlive:
        enemy = enemyGenerator.getRandomEnemy()
        direction = map.askPlayerForDirection()
        map.playerMove(direction, player, thinker, enemy)
