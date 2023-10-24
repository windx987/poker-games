from myenum import Action
from deck import Card
from evaluator import evaluate_cards, _evaluate_cards


class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.status = None
        self.bet = 0
        self.next = None

    def __str__(self):
        return f"name : {self.name}, hand : {self.hand.cards}, chips : {self.chips - self.bet}, bet : {self.bet}, status : {self.status}"

    def add_chips(self, amount):
        self.chips += amount

    def remove_chips(self, amount):
        self.chips -= amount

    def get_chips(self):
        return self.chips

    def add_bet(self, amount):
        self.bet = amount

    def reset_bet(self):
        self.remove_chips(self.bet)
        self.bet = 0


class Hand:
    def __init__(self):
        self.cards = []
        self.strength = 0

    def get_cards(self):
        return self.cards

    def add_card(self, card):
        if not isinstance(card, Card):
            raise ValueError(
                "Only Card instances can be added to the array."
            )
        self.cards.append(card)

    def reset_cards(self):
        self.cards = []

    def update_strength(self, cards):
        self.strength = evaluate_cards(*cards)
