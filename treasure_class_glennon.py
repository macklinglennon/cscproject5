class Treasure():
    def __init__ (self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__ (self):
        return "" + self.name + ": " + self.description + " worth " + str(self.value) + " gold coins."




class Gold(Treasure):
    def __init__ (self, atm):
        self.atm = atm

    def __str__ (self):
        return "a pile of " + str(self.atm) + " gold coins"





class Weapon(Treasure):
    def __init__ (self, name, description, value, damage):
        self.damage = damage
        super(). __init__(name, description, value)
    def __str__ (self):
        return (Treasure.__str__(self)) + " Has " + str(self.damage) + " damage."
        
class GolfClub (Weapon):
    def __init__ (self):
        super(). __init__(name = "GolfClub", description = "A club \
        somtimes used for golfing and sometimes used for assault." , value = 50,
                          damage = 50)
class Pistol (Weapon):
    def __init__ (self):
        super(). __init__ (name = "Pistol", description = "A small handgun.",
                           value = 100, damage = 100)




class Food (Treasure):
    def __init__ (self, name, description, value, damage):
        self.damage = damage
        super(). __init__ (name, description, value)
    def __str__ (self):
        return (Treasure.__str__(self)) + " Has " + str(self.damage) + " damage."

class Pizza (Food):
    def __init__ (self):
        super(). __init__ (name = "Pizza", description = "A slice of pizza.",
                           value = 50, damage = -50)
class Soup (Food):
    def __init__ (self):
        super(). __init__ (name = "Soup", description = "A bowl of soup.",
                           value = 100, damage = -100)
        


class Armor (Treasure):
    def __init__ (self, name, description, value, strength):
        self.strength = strength
        super(). __init__ (name, description, value)
    def __str__ (self):
        return (Treasure.__str__(self)) + " Has " + str(self.strength) + "strength."
        
class Hat (Armor):
    def __init__ (self):
        super(). __inti__ (name =  "Hat", description = "A classic baseball \
        cap", value = 100, strength = 1)

class Jacket (Armor):
    def __init__ (self):
        super(). __init__ (name = "Jacket", description = "A nice warm \
        jacket", value = 200, strength = 100)


    
