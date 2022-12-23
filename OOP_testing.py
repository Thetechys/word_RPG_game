from random import randint




friendList = []
foeList = []



class character():

    character_numer = 0

    def __init__(self):
        self.health = 100
        self.atk = 5 ##default value for all character
        self.dfn = 5
        character.character_numer += 1
        friendList

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
        self.health = 105
        self.atk = randint(15,25)
        self.dfn = randint(5,15)
        own_warrior.own_character += 1
        self.alias_num = self.own_character
        friendList.append(self)


class foe_warrior(character):

    foe_character = 0

    def __init__(self):
        super().__init__()
        self.health = 105
        self.atk = randint(15,25)
        self.dfn = randint(5,15)
        foe_warrior.foe_character += 1
        self.alias_num = self.foe_character
        foeList.append(self)


def player_input():
    your_input = input(str('do you want to attack enemy?[y/n]:  '))
    return your_input



asa = own_warrior()
suji = own_warrior()
''' --------------------'''
sumo = foe_warrior()
sapporo = foe_warrior()
genji = foe_warrior()


print(f'friend list: {friendList}')
print(f'foe list: {foeList}')

# print(asa.alias_num)
# print(suji.alias_num)
# print(sumo.alias_num)
# print(sapporo.alias_num)
# print(genji.alias_num)




round = 10

'''1 mod 2 == 0     ;   2 mod 2 == 1'''




# while round != 0:

#     if round % 2 == 0:

#         match player_input():

#             case 'y':

#                 print('attack')
#                 round -= 1
        
#             case 'n':

#                 print('pass this round')
#                 round -= 1

#     else:

#         print('enemy attack')
#         round -= 1