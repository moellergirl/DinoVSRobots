from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.battle=True
        self.robot=Robot()
        self.dinosaur=Dinosaur()


    def run_game (self):
        self.disply_welcome
        self.battle_phase
        self.disply_winner


    def disply_welcome(self):
        print('\ Welcome to the war of the of the Roses!\n There can be only one victor,who will it be?')


    def battle_phase(self):
        

        

    def disply_winner(self):
        pass