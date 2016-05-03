class Monster():
    def __init__ (self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0



class WildBoar(Monster):
    def __init__ (self):
        super(). __init__ (name = "Wild Boar", hp = 10, damage = 2)

class FrankCostanza (Monster):
    def __init__ (self):
        super(). __init__ (name = "Frank Costanza", hp = 100, damage = 1)

        



   
