from .questionOpener.questionOpener import openQuestionsJson

class Thinker:
    def __init__(self):
        self.puzzles = openQuestionsJson('./Thinker/questions.json')
        self.puzzlesAmount = len(self.puzzles)

    def getAnswer(self, puzzleId):
        answer = ''
        puzzle = self.puzzles[puzzleId]
        while answer not in puzzle['answers']:
            print('-----====== PUZZLE ======-----')
            print(puzzle['content'])
            print('Possible answers are:')
            print(*puzzle['answers'], sep='\n')
            answer = input('Your answer is: ')
            if answer in puzzle['answers']:
                if answer == puzzle['goodAnswer']:
                    return True
                return False
            print('You typed answer wrong!')

    @staticmethod
    def puzzleReward(player, healPower = 1):
        print("Congratulations! Your answer was a good answer!")
        if player.character.stats.lifePoints == player.character.stats.lifePointsMax:
            print("Anchorite can't heal you becouse you are on full health")
            print('You will be rewarded in XP instead!')
            player.character.experience += healPower * 2
            if player.character.isXpEnoughtForLvlup():
                player.character.levelUp()
        elif player.character.stats.lifePoints + healPower >= player.character.stats.lifePointsMax:
            player.character.stats.lifePoints = player.character.stats.lifePointsMax
            print('Anchorite healed you to full health!')
        else:
            player.character.stats.lifePoints += healPower
            print("Anchorite just healed you for %i life point" % healPower)

    def puzzlePenalty(self, player, attackDamage = 1):
        print("BAD BAD BAD! Your answer was wrong!")
        player.character.stats.lifePoints -= attackDamage
        if player.character.stats.lifePoints <= 0:
            player.die()
            print('Anchorite puzzle just killed you')
        else:
            print('Anchorite puzzle punished you!')
            print('You took %i damage' % attackDamage)

    def puzzleSolution(self, player, puzzleId):
        isAnswerGood = self.getAnswer(puzzleId)
        if isAnswerGood:
            self.puzzleReward(player)
        else:
            self.puzzlePenalty(player)