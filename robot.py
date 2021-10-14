from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapons = []
        self.armory_populate()                   #REMOVED self. from armory_populate
        self.weapon = self.pick_weapon()         #REMOVED self. from pick_weapon

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power

    def armory_populate(self):
        self.weapon1 = Weapon('w1', 20)
        self.weapon2 = Weapon('w2', 15)
        self.weapon3 = Weapon('w3', 25)
        self.weapons.append(self.weapon1)
        self.weapons.append(self.weapon2)
        self.weapons.append(self.weapon3)

    def pick_weapon(self):
        user_weapon_choice = input("Which weapon? 1, 2, or 3.")
        if user_weapon_choice == "1":
            return self.weapons[0]
        elif user_weapon_choice == "2":
            return self.weapons[1]
        elif user_weapon_choice == "3":
            return self.weapons[2]

