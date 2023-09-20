from __future__ import annotations
from typing import Any, Union
from .player import Player
from .deck import Deck
from .utils import ListNode

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

    def append(self, player):
        if not isinstance(player, Player):
            raise ValueError("Only Player instances can be added to the linked list.")

        if self.player_head is None:
            self.player_head = player
            player.next = player  # Create a self-loop for the initial player
        else:
            current_player = self.player_head
            while current_player.next != self.player_head:
                current_player = current_player.next
            current_player.next = player
            player.next = self.player_head  # Create a cycle
            
    def _player_info(self):
        current = self.player_head
        while current.next != self.player_head:
            print(current)
            current = current.next
            
            

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

MyTable._player_info()
