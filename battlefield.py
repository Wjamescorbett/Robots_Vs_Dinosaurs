from fleet import Fleet
from herd import Herd

fleet = Fleet()
fleet.robots()

herd = Herd()
herd.robots()

class Battlefield:
    def __init__(self):
        self.fleet = fleet
        self.herd = herd
    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print("Welcome robots and dinosaurs! Prepare to fight!")
        self.battle()

    def battle(self):
        print("Made it this far.")
        dino_turn(herd.dinosaur)

    def dino_turn(self, dinosaur):
        dinosaur.attack(fleet.robot)
        show_dino_opponent_options()

    def robo_turn(self, robot):
        robot.attack(herd.dinosaur)
        show_robo_opponent_options()

    def show_dino_opponent_options(self):

    def show_robo_opponent_options(self):

    def display_winners(self):
        if herd.health == 0:
            print("Robots win!")
        if  fleet.health == 0:
            print("Dinosaurs win!")
        else:
            battle()  
