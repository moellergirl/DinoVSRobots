from weapon import Weapon
class Robot:

    def __init__(self,name):
        self.name=name     
        self.health=100
        self.active_weapon=Weapon('Anthrax Amaryllis', 25)
    

    def attack(self,dinosaur):
        dinosaur.health-= dinosaur.health-self.active_weapon.attack_power
        print(f'{self.name} riggered and doused {dinosaur.name} with the dreaded {self.active_weapon.name}!\n How mortifying, {dinosaur.name} has lost {dinosaur.health} of her health points. \n')
        robot=Robot('Robot David Rose')