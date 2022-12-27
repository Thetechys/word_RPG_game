from random import randint
import time
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

    def __repr__(self):
        return f'mate{self.alias_num}'

class foe_warrior(character):

    foe_character = 0

    def __init__(self):
        super().__init__()
        self.atk = randint(15,25)
        self.dfn = randint(5,15)
        foe_warrior.foe_character += 1
        self.alias_num = self.foe_character
        self.turn = 0

    def __repr__(self):
        return f'enemy{self.alias_num}'


'''--- friendly team instances ---'''
mate1 = own_warrior()
mate2 = own_warrior()
'''--- enemy team instances ---'''
enemy1 = foe_warrior()
enemy2 = foe_warrior()

mateList = [mate1,mate2]
enemyList = [enemy1,enemy2]


def player_input():  ## player characters take turn to attack, don't use this 

    print('which character to launch attack?: ')
    your_input = input(str('?:  '))
    return your_input


def targetInput():

    print('who to attack?: ')
    checkAvailableTarget()
    your_input = int(input())
    return your_input



def checkAvailableTarget():

    alive = []
    h_pt = []

    for i in enemyList:
        alive.append(i)
        h_pt.append(i.health)

    finList = list(enumerate(zip(alive,h_pt),1))

    for (num,(name,hp)) in finList:
        print(f'{num} - {name} - HP: {hp}')


def get_tar_dfn(list,tar):   # to be use in get_dmg

    if list == mateList:
        tget = mateList[tar]

    elif list == enemyList:
        tget = enemyList[tar]

    return tget.dfn


def get_tar_atk(list,tar):   # to be use in get_dmg

    if list == mateList:
        tget = mateList[tar]

    elif list == enemyList:
        tget = enemyList[tar]

    return tget.atk


def get_dmg(atk,dfn):

    dmg = atk - dfn
    print(f'atk is {atk}')
    print(f'dfn is {dfn}')
    print(f'damage caused : {dmg} \n')
    
    return dmg



round = 0

while True:

    if round % 2 == 0:      ## list changer

        round += 1
        print('------------------player round start------------------')

        for i in mateList:

            if i.health > 0:
                
                print(f'Attacker of this round = {i}')

                match targetInput():

                    case 1:
                        
                        print(i,'launched attack')
                        dmg = get_dmg(get_tar_atk(mateList,mateList.index(i)),get_tar_dfn(enemyList,1))
                        enemy1.health -= dmg


                    case 2:
                        
                        print(i,'launched attack')
                        dmg = get_dmg(get_tar_atk(mateList,mateList.index(i)),get_tar_dfn(enemyList,2))
                        enemy1.health -= dmg
                    
                    case 3:
                        print('--debug purpose --')
    
    
    elif round % 2 == 1:

        round += 1
        print('------------------enemy round start------------------')

        for i in enemyList:

            if i.health > 0:
                
                print(f'Attacker of this round = {i}')

                match targetInput():

                    case 1:
                        
                        print(i,'launched attack')
                        dmg = get_dmg(get_tar_atk(mateList,mateList.index(i)),get_tar_dfn(enemyList,1))
                        enemy1.health -= dmg
                        time.sleep(1)


                    case 2:
                        
                        print(i,'launched attack')
                        dmg = get_dmg(get_tar_atk(mateList,mateList.index(i)),get_tar_dfn(enemyList,2))
                        enemy1.health -= dmg
                        time.sleep(1)
                    
                    case 3:
                        print('--debug purpose --')


    else:

        print('debuggin purposes')
        break


# for i in mateList:

#     print(i)