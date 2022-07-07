
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot=Robot('Robot David Rose')
        self.dino=Dinosaur('Dino Alexia Rose', 25)
    
    def run_game (self):
        self.disply_welcome()
        self.battle_phase()
        self.disply_winner()

    def disply_welcome(self):
        print('Welcome to the war of the of the Roses!\nThere can be only one victor,who will it be?')


    def battle_phase(self):
        while self.robot.health > 0 and self.dino.health > 0:
            self.robot.attack(self.dino)
            self.dino.attack(self.robot)
        

    def disply_winner(self):
        if self.dino.health <= 0:
            print(f' Oh no! {self.dino.name} has been defeated.\n{self.robot.name} is the victor!')
        elif self.robot.health <= 0:
            print(f'Ha! {self.robot.name} has been schooled by {self.dino.name}.\n{self.dino.name} has won the war!')    
