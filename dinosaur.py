


class Dinosaur:
    
    def __init__(self,name,attack_power):
        self.name='Dino Alexia Rose'
        self.health=100
        self.attack_power=35
        
    def attack(self,robot):
        robot.health = robot.health - self.attack_power
        print (f'{self.name} charged and attacked {robot.name}for{self.attack_power} in dammage!\n How devistating,{robot.name} only has {robot.health} of her health remaining!\n')
        

