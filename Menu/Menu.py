def getPlayerName():
        return input(u'Enter player name: ')


def getPlayerCharacterClass():
    characterClass = ''
    characterClassList = ['Warrior', 'Rogue', 'Mage']
    while characterClass not in characterClassList:
        print('Select your character from Warrior, Rogue, Mage')
        characterClass = input('Your choose: ')
        if characterClass in characterClassList:
            return characterClass
