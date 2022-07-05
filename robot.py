from weapon import Weapon
class Robot:

    def __init__(self,name):
        self.name='Robot David Rose'       
        self.health=100
        self.active_weapon=Weapon
    

    def attack(self,dinosaur):
        dinosaur.health=dinosaur.health-self.active_weapon
        print(f'{self.name} riggered and doused {dinosaur.name} with the dreaded {self.active_weapon} in dammage!\n How mortifying,{dinosaur.name}only has {dinosaur.health} of his health remaining!\n')
