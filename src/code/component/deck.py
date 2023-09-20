from .utils import ListNode, random
from .card import Card

RANK = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUIT = ['C', 'D', 'H', 'S']

"""
            |      |    C |    D |    H |    S |
            | ---: | ---: | ---: | ---: | ---: |
            |    2 |    0 |    1 |    2 |    3 |
            |    3 |    4 |    5 |    6 |    7 |
            |    4 |    8 |    9 |   10 |   11 |
            |    5 |   12 |   13 |   14 |   15 |
            |    6 |   16 |   17 |   18 |   19 |
            |    7 |   20 |   21 |   22 |   23 |
            |    8 |   24 |   25 |   26 |   27 |
            |    9 |   28 |   29 |   30 |   31 |
            |    T |   32 |   33 |   34 |   35 |
            |    J |   36 |   37 |   38 |   39 |
            |    Q |   40 |   41 |   42 |   43 |
            |    K |   44 |   45 |   46 |   47 |
            |    A |   48 |   49 |   50 |   51 |
"""

class Deck:
    def __init__(self):
        self.cards = [Card(rank+suit) for rank in RANK for suit in SUIT]
        random.shuffle(self.cards)

        self.head = None

        for card in self.cards:
            new_node = ListNode(card)
            new_node.next = self.head
            self.head = new_node
            
    def deal_card(self):
        card = self.head
        self.head = self.head.next
        return card
    