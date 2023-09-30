from .enum import Action
from deck import Card
from evaluator import evaluate_cards, _evaluate_cards


class Player:
    def __init__(self, name, chips=0):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.status = None
        self.next = None

    def __str__(self):
        return f"name : {self.name}, hand : {self.hand.cards}, chips : {self.chips}, status : {self.status}"

    def add_chips(self, amount):
        self.chips += amount

    def remove_chips(self, amount):
        self.chips -= amount


class Hand:
    def __init__(self):
        self.__cards = []
        self.strength = None

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def add_card(self, card):
        if not isinstance(card, Card):
            raise ValueError(
                "Only Card instances can be added to the array."
            )
        self.__cards.append(card)

    def reset_cards(self):
        self.__cards = []

    def update_strength(self):
        self.strength = evaluate_cards(self.cards)
