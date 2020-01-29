from random import randint


class Map:
    def __init__(self, size=25):
        self.size = size
        self.corridorsAmount = 3
        self.map = [[0 for i in range(self.corridorsAmount)]for j in range(self.size)]
        self.playerPosition = 0
        self.directionsToChoose = ['Left', 'Top', 'Right', 'Up']
        self.isPlayerAlive = True

    def generateRandomMap(self):
        for i in range(0, len(self.map)):
            poll = ['Enemy', 'Thinker', 'Nothing']
            for j in range(self.corridorsAmount):
                randomTurn = randint(0, len(poll) - 1)
                self.map[i][j] = poll[randomTurn]
                del poll[randomTurn]

    def askPlayerForDirection(self):
        direction = ''
        while direction not in self.directionsToChoose:
            direction = input('Select direction (possible directions Left, Top, Right): ')
            print('You choose to move to the %s' % direction)
            if direction in self.directionsToChoose:
                return direction

    def playerMove(self, direction, player, thinker, enemy):
        numericDirection = {
            'Left': 0,
            'Top': 1,
            'Up': 1,
            'Right': 2,
        }[direction]
        {
            'Nothing': self._emptyCorridor,
            'Enemy': (lambda: self._enemyCorridor(player, enemy)),
            'Thinker': (lambda: self._thinkerCorridor(player, thinker))
        }[self.map[self.playerPosition][numericDirection]]()

    def _emptyCorridor(self):
        print('You pass the corridor without any problems')
        self.playerPosition += 1

    def _enemyCorridor(self, player, enemy):
        print('You meet enemy in the corridor!')
        player.battleOrDodge(enemy)
        self.playerPosition += 1

    def _thinkerCorridor(self, player, thinker):
        print('You meet Anchorite with special puzzle!')
        thinker.puzzleSolution(player, randint(0, thinker.puzzlesAmount - 1))
        self.playerPosition += 1