class Player:
    def __init__(self, name, chips=0):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.next_player = None

    def add_chips(self, amount):
        self.chips += amount

    def remove_chips(self, amount):
        self.chips -= amount
        
class Hand:
    def __init__(self):
        self.cards = []
        self.strength = None

    def show_strength(self):
        return self.strength
    
    def check_strength(self):
        self.
        