from weapon import Weapon

class Robot:

    def __init__(self,name):
        self.name=" Robot Stevie Budd"        
        self.health=100
        self.active_weapon=Weapon
        


    def attack(self,dinosaur):
        dinosaur.health=dinosaur.health-Weapon
        print(f'{self.name} riggered and doused {dinosaur.name} with the dreaded {Weapon} in dammage!\n How mortifying,{dinosaur.name}only has {dinosaur.health} of her health remaining!\n')
