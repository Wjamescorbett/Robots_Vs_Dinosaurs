from fleet import Fleet
from herd import Herd

fleet = Fleet()
herd = Herd()



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
        round_number = 1
        print("Made it this far.")
        print(f"Start of turn {round_number}! Dino's turn. ")
        self.dino_turn(self.herd.dinosaurs[0])
        print("Dino's turn over, robots go. ")
        self.robot_turn()
        round_number += 1

    def dino_turn(self, dinosaur):
        self.herd.dinosaurs[0].attack(self.fleet.robots[0])


    # def robot_turn(self, robot):


    # def show_dino_opponent_options(self):


    # def show_robo_opponent_options(self):


    # def display_winners(self):
    #     if herd.health == 0:
    #         print("Robots win!")
    #     if  fleet.health == 0:
    #         print("Dinosaurs win!")
    #     else:
    #         battle()  







# self.dino_turn(self.herd.dinosaurs[0])
# self.fleet.robot_list[0].attack(self.herd.dino_list[0])