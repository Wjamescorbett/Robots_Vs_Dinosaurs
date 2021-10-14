from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur_1 = Dinosaur("Dino 1", 30, 100)
        dinosaur_2 = Dinosaur("Dino 2", 50, 85)
        dinosaur_3 = Dinosaur("Dino 3", 80, 35)
        self.dinosaurs.append(dinosaur_1)
        self.dinosaurs.append(dinosaur_2)
        self.dinosaurs.append(dinosaur_3)
