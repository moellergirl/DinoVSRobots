
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.battlefield_one=True
    
    def run_game (self):
        self.disply_welcome
        self.battle_phase
        self.disply_winner

    def disply_welcome(self):
        print('\ Welcome to the war of the of the Roses!\n There can be only one victor,who will it be?')


    def battle_phase(self):
        while self.battle==True:
            if Robot.health>0:
                Dinosaur()

            
        if Dinosaur.health>0:
            
                Robot( )
                
        else:
            self.battle==False

    def disply_winner(self):
        if Dinosaur.health<=0:
            print(f' Oh no! {Dinosaur.name} has been defeated.\n {Robot.name} is the victor!')
        elif Robot.health<=0:
            print(f'Ha! {Dinosaur.name} has schooled {Robot.name}.\n {Dinosaur.name} has won this war!')    
