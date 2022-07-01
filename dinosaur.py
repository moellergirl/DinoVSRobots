
class Dinosaur:
    
    def __init__(self,name,attack_power):
        self.name='Dino Alexia Rose'
        self.health=100
        self.attack_power=40
    
    def attack(self,robot):
        print (f'{self.name} charged and attacked {self,robot}for{self.attack_power} dammage!\n How devistating,{self,robot} only has {self.health,robot - self.attack_power} of her health remaining!\n')

