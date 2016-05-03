import Player

class Action():
    def __init__ (self, method, name, hotkey):
        self.method = method
        self.name = name
        self.hotkey = hotkey

    def __str__ (self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__ (self):
        super(). __init__ (method = Player.move_north, name = "Move North",
                           hotkey = "n")

class MoveSouth (Action):
    def __init__ (self):
        super(). __init__ (method = Player.move_south, name = "Move South",
                           hotkey = "s")

class MoveEast (Action):
    def __init__ (self):
        super(). __init__ (method = Player.move_east, name = "Move East",
                           hotkey = "e")

class MoveWest (Action):
    def __init__ (self):
        super(). __init__ (method = Player.move_west, name = "Move West",
                           hotkey = "w")

class ViewInventory(Action):
    def __init__ (self):
        super(). __init__ (method = Player.print_inventory, name = "View \
                inventory", hotkey = "i")

class Attack(Action):
    def __init__ (self, enemy):
        super(). __init__ (method = PLayer.attack, name = "Attack",
                           hotkey = "a")
        
    
