# from __future__ import annotations
from typing import Any, Union

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
rank_map = {
    "2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7,
    "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12,
}
suit_map = {
    "C": 0, "D": 1, "H": 2, "S": 3,
    "c": 0, "d": 1, "h": 2, "s": 3
}

rank_reverse_map = {value: key for key, value in rank_map.items()}
suit_reverse_map = {value: key for key, value in suit_map.items() if key.islower()}

class Card:
    def __init__(self, other: Union[int, str, Card]):
        self.__slots__ = ["__id"]
        self.__id = int 
          
class Player:
    def __init__(self, name, chips=0):
        self.name = name
        self.chips = chips
        self.hand_head = None
        self.next_player = None

    def add_chips(self, amount):
        self.chips += amount

    def remove_chips(self, amount):
        self.chips -= amount

    def add_to_hand(self, card):
        new_node = ListNode(card)
        new_node.next = self.hand_head
        self.hand_head = new_node

    def clear_hand(self):
        self.hand_head = None

    def hand_display(self):
        current = self.hand_head
        print(f"name: {self.name}, chips: {self.chips}, hands", end=": " )
        while current:
            print(current.data, end=", " if current.next else "\n")
            current = current.next

class PokerTable:
    def __init__(self):
        self.community_head = None
        self.player_head = None
        self.deck = Deck()

    def reset_deck(self):
        self.deck = Deck()

    def add_community_card(self, card):
        new_node = ListNode(card)
        new_node.next = self.community_head
        self.community_head = new_node

    def clear_community_cards(self):
        self.community_head = None

    def cards_display(self):
        current = self.community_head
        print("table_display", end=": " )
        while current:
            print(current.data, end=", " if current.next else "\n")
            current = current.next

    def cards_display(self):
        current = self.community_head
        count = 0
        while current:
            current = current.next
            count += 1
        return count

    def append(self, player):
        if not isinstance(player, Player):
            raise ValueError("Only Player instances can be added to the linked list.")

        if self.player_head is None:
            self.player_head = player
            player.next_player = player  # Create a self-loop for the initial player
        else:
            current_player = self.player_head
            while current_player.next_player != self.player_head:
                current_player = current_player.next_player
            current_player.next_player = player
            player.next_player = self.player_head  # Create a cycle

    def player_display(self):
        current_player = self.player_head
        while True:
            current_player.hand_display()
            current_player = current_player.next_player
            if current_player == self.player_head:
                break

    def hand_out_cards(self):
        current_player = self.player_head
        while True:
            for i in range(0,5):
                card = self.deck.deal_card()
                current_player.add_to_hand(card)
            current_player = current_player.next_player
            if current_player == self.player_head:
                break

MyTable = PokerTable()

# register players
player = Player("RRRRRR", None)
MyTable.append(player)

# register players
player = Player("Alex", None)
MyTable.append(player)

# register players
player = Player("Jack", None)
MyTable.append(player)

MyTable.hand_out_cards()
MyTable.player_display()

print("Number of cards in the deck:", MyTable.deck.count_cards())
MyTable.reset_deck()
print("Number of cards in the deck:", MyTable.deck.count_cards())