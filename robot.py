from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapons = []
        self.armory_populate()

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power

    def armory_populate(self):
        self.weapon1 = Weapon('w1', 20)
        self.weapon2 = Weapon('w2', 15)
        self.weapon3 = Weapon('w3', 25)
        self.weapons.append(self.weapon1)
        self.weapons.append(self.weapon2)
        self.weapons.append(self.weapon3)


