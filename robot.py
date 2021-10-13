from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapons = []
        self.armory_populator()
        self.weapon = self.pick_weapon()

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power

    def armory_populator(self):
        weapon1 = Weapon('w1', 20)
        weapon2 = Weapon('w2', 15)
        weapon3 = Weapon('w3', 25)
        weapons.append(weapon1)
        weapons.append(weapon2)
        weapons.append(weapon3)

    def pick_weapon(self):
        user_weapon_choice = input("Which weapon? 1, 2, or 3.")
        if user_weapon_choice == "1":
            return self.weapons[0]
        elif user_weapon_choice == "2":
            return self.weapons[1]
        elif user_weapon_choice == "3":
            return self.weapons[2]

