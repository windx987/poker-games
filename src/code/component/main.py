from __future__ import annotations
from typing import Any, Union
from .player import Player, PlayerStatus
from .deck import Deck
from .utils import ListNode

class PokerTable:

    def __init__(self):
        self.community_cards = []
        self.player_head = None
        self.deck = Deck()
        self.total_bet = None

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
            
    def find_highest_point(self):
        current = self.player_head
        while current.next != self.player_head:
            if current.status == PlayerStatus.ACTIVE and current.hand.strength > highest_points:
                highest_points = current.hand.strength
            current = current.next
        return highest_points
    
    def find_winners_with_highest_points(self):
        highest = self.find_highest_point()
        current = self.player_head
        winners = []
        while current.next != self.player_head:
            if current.status == PlayerStatus.ACTIVE and current.hand.strength == highest:
                winners.append(current)
            current = current.next
        return winners
        
    def determine(self):
        winners = self.find_winners_with_highest_points()
        if len(winners) < 1:
            raise ("error")
        elif len(winners) == 1 :
            return self.distribute_chips_to_single_winner(winners[0])
        else:
            return self.distribute_chips_equally(winners)
        
    def distribute_chips_to_single_winner(self, player):
        winner = player  # Assuming there's a single winner
        winner.add_chips(self.total_bet)
        print(f"{winner.name} wins and receives {self.total_bet} chips.")
    
    def distribute_chips_equally(self, players):
        share_per_winner = self.total_bet // len(players)
        for player in players:
            player.add_chips(share_per_winner)
        winner_names = ', '.join([player.name for player in players])
        print(f"{winner_names} win and each receives {self.total_bet // len(players)} chips.")
            
    
    
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