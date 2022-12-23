from random import randint


class character():

    character_numer = 0

    def __init__(self):
        self.health = 100
        self.atk = 5 ##default value for all character
        self.dfn = 5
        character.character_numer += 1

    def attack(self):
        self.atk_pt = self.atk
        return self.atk_pt

    def defence(self):
        self.dfn_pt = self.dfn
        return self.dfn_pt


class own_warrior(character):

    own_character = 0

    def __init__(self):
        super().__init__()
        self.atk = randint(15,25)
        self.dfn = randint(5,15)
        own_warrior.own_character += 1
        self.alias_num = self.own_character
        self.turn = 0


class foe_warrior(character):

    foe_character = 0

    def __init__(self):
        super().__init__()
        self.atk = randint(15,25)
        self.dfn = randint(5,15)
        foe_warrior.foe_character += 1
        self.alias_num = self.foe_character
        self.turn = 0





mate1 = own_warrior()
mate2 = own_warrior()
# mate3 = own_warrior()
''' --------------------'''
enemy1 = foe_warrior()
enemy2 = foe_warrior()
# enemy3 = foe_warrior()

mateList = [mate1,mate2]
enemyList = [enemy1,enemy2]


def player_input():

    print('which character to launch attack?: ')
    print(mateBanner()[0]+'\n'+mateBanner()[1])
    your_input = input(str('?:  '))
    mateBanner()
    return your_input


def mateBanner():

    x = []

    for i in range(len(mateList)):
        x.append(f'{i+1} - mate{i+1}\n')
    return x

def enemyBanner():

    x = []

    for i in range(len(enemyList)):
        x.append(f'{i+1} - mate{i+1}')
    return x

round = 10
'''1 mod 2 == 0     ;   2 mod 2 == 1'''




while round != 0:

    if round % 2 == 0:

        match player_input():

            case 'y':

                print('attack')
                round -= 1
        
            case 'n':

                print('pass this round')
                round -= 1

    else:

        print('enemy attack')
        round -= 1