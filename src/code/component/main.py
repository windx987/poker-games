# from __future__ import annotations
from typing import Any, Union
from .player import Player
# from .card import Deck, Card

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None        
          
class PokerTable:
    def __init__(self):
        self.community_cards = []
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