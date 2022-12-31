## this is word based game 


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

    @property # character is Dead Or Alive
    def doa(self):
        if self.health > 0:
            return 1
        else: 
            return 0

class own_warrior(character):   # class of mate , subclass of CHARACTER

    own_character = 0

    def __init__(self):
        super().__init__()
        # self.atk = randint(15,25)
        self.atk = randint(50,55)
        
        self.dfn = randint(5,15)
        own_warrior.own_character += 1
        self.alias_num = self.own_character
        self.turn = 0

    def __repr__(self):
        return f'mate{self.alias_num}'

class foe_warrior(character):   #class of enemy , also subclass of CHARACTER

    foe_character = 0

    def __init__(self):
        super().__init__()
        self.atk = randint(40,45)
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


def get_doa(args):  ## player characters take turn to attack, don't use this, maybe will delete this

    doa_score = 0

    match args:

        case 'mate':

            for i in mateList:
                doa_score += i.doa


        case 'enemy':

            for i in enemyList:
                doa_score += i.doa

    # return f'{args} score is : {doa_score}'   this line is for debug purpose
    return doa_score


def targetInput():

    print('who to attack?: ')
    checkAvailableTarget()
    your_input = int(input())
    return your_input

def randomInput(start,end):   # for 'flip-coin' function and enemy deciding who to attack
    return randint(start,end)



def checkAvailableTarget():

    alive = []
    h_pt = []

    for i in enemyList:
        alive.append(i)
        h_pt.append(i.health)

    finList = list(enumerate(zip(alive,h_pt),0))

    for (num,(name,hp)) in finList:
        print(f'{num} - {name} - HP: {hp}')

def checkTeamHealth():

    alive = []
    h_pt = []

    for i in mateList:
        alive.append(i)
        h_pt.append(i.health)

    finList = list(enumerate(zip(alive,h_pt),0))

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


def get_dmg(atk,dfn):  # parse in get_tar_atk and get_tar_dfn as argument

    dmg = atk - dfn
    print(f'atk is {atk}')
    print(f'dfn is {dfn}')
    print(f'damage caused : {dmg} \n')
    
    return dmg



round = 0

while True:

    if get_doa('mate')!=0 and get_doa('enemy')!= 0:

        if round % 2 == 0:      ## round changer

            round += 1
            print('------------------player round start------------------')

            for i in mateList:

                if i.health > 0:
                    
                    print(f'Attacker of this round = {i}')

                    match targetInput():

                        case 0:
                            
                            if enemyList[0].health > 0:

                                print(i,'launched attack on',enemyList[0])
                                dmg = get_dmg(get_tar_atk(mateList,mateList.index(i)),get_tar_dfn(enemyList,0))
                                enemy1.health -= dmg
                                print(f'enemy1 received {dmg} damage! \n')

                            else:

                                print(f'this character is dead, attack not successful \n')


                        case 1:
                            
                            if enemyList[1].health > 0:

                                print(i,'launched attackon',enemyList[1])
                                dmg = get_dmg(get_tar_atk(mateList,mateList.index(i)),get_tar_dfn(enemyList,1))
                                enemy2.health -= dmg
                                print(f'enemy2 received {dmg} damage!')

                            else:

                                print(f'this character is dead, attack not successful \n')

                        case _:   # the _: mean matching any-other-else
                            print('--invalid input, wasted a chance to attack --')

                else:

                    continue
        
        else:

            round += 1
            print('------------------enemy round start------------------')

            for i in enemyList:

                if i.health > 0:
                    
                    print(f'Attacker of this round = {i}')

                    match randomInput(0,1):

                        case 0:
                            
                            if mateList[0].health > 0:

                                checkTeamHealth()
                                print(i,'launched attack on',mateList[0])
                                dmg = get_dmg(get_tar_atk(enemyList,enemyList.index(i)),get_tar_dfn(mateList,0))
                                mate1.health -= dmg
                                print(f'mate1 received {dmg} damage!')

                                checkTeamHealth()

                            else:

                                print(f'this character is dead, attack not successful \n')


                        case 1:
                            
                            if mateList[1].health > 0:

                                checkTeamHealth()
                                print(i,'launched attack on',mateList[1])
                                dmg = get_dmg(get_tar_atk(enemyList,enemyList.index(i)),get_tar_dfn(mateList,1))
                                mate2.health -= dmg
                                print(f'mate2 received {dmg} damage!')

                                checkTeamHealth()

                            else:

                                print(f'this character is dead, attack not successful \n')

                        
                        case _:   
                            print('--invalid input, wasted a chance to attack --')

                else:
                    continue
    
    else:

        if get_doa('mate')==0:
            print('-->> PLAYER character all dead, ENEMY win <<--')
        
        
        elif get_doa('enemy')==0:
            print('-->> ENEMY character all dead, PLAYER win <<--')

        break
