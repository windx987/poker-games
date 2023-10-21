from __future__ import annotations
from typing import Any, Union
from player import Player, Hand, Action
from deck import Deck, Card
from utils import ListNode
from myenum import Action, CurrentPhase


class PokerTable:

    def __init__(self):
        self.community_cards = []
        self.player_head = None
        self.deck = Deck()
        self.total_bet = 0
        self.highest_bet = 0
        self.current_phase = CurrentPhase.PREFLOP
        self.preflop = True

    def reset_deck(self):
        self.deck = Deck()

    def add_community_card(self, card):
        if not isinstance(card, Card):
            raise ValueError(
                "Only Card instances can be added to the array."
            )
        self.community_cards.append(card)

    def clear_community_cards(self):
        self.community_cards = []

    def append(self, player):
        if not isinstance(player, Player):
            raise ValueError(
                "Only Player instances can be added to the linked list.")

        if self.player_head is None:
            self.player_head = player
            player.next = player

        else:
            current_player = self.player_head
            while current_player.next != self.player_head:
                current_player = current_player.next
            current_player.next = player
            player.next = self.player_head

    def player_count(self):
        total_player = 0
        if self.player_head is None:
            return total_player  # Return 0 if the list is empty

        current = self.player_head
        while True:
            total_player += 1
            current = current.next
            if current == self.player_head:
                break

        return total_player

    def check_active_player(self):
        total_active_players = 0
        if self.player_head is None:
            return total_active_players  # Return 0 if the list is empty

        current = self.player_head
        while True:
            if current.status != Action.FOLD:
                total_active_players += 1
            current = current.next
            if current == self.player_head:
                break

        return total_active_players

    def player_info(self):
        current = self.player_head
        while True:
            print(current)
            current = current.next
            if current == self.player_head:
                break

    def find_highest_point(self):
        current = self.player_head
        while current.next != self.player_head:
            if current.status != Action.FOLD and current.hand.strength > highest_points:
                highest_points = current.hand.strength
            current = current.next
        return highest_points

    def find_winners_with_highest_points(self):
        highest = self.find_highest_point()
        current = self.player_head
        winners = []
        while current.next != self.player_head:
            if current.status != Action.FOLD and current.hand.strength == highest:
                winners.append(current)
            current = current.next
        return winners

    def determine(self):
        winners = self.find_winners_with_highest_points()
        if len(winners) < 1:
            raise ("determine error")
        elif len(winners) == 1:
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
        print(
            f"{winner_names} win and each receives {self.total_bet // len(players)} chips.")

    def update_player_strength(self):
        current = self.player_head
        while True:
            cards = current.hand.cards + self.community_cards
            current.hand.update_strength(cards)
            current = current.next
            if current == self.player_head:
                break

    def reset_player_status(self):
        current = self.player_head
        while True:
            current.status = None
            current = current.next
            if current == self.player_head:
                break

    def reset_highest(self):
        self.highest_bet = 0
        current = self.player_head
        while True:
            self.total_bet += current.bet
            current.reset_bet()
            if current.status != Action.FOLD:
                current.status = None
            current = current.next
            if current == self.player_head:
                break

    def all_checked(self):
        current = self.player_head
        while True:
            if current.status != Action.FOLD:
                if current.status != Action.CHECK:
                    return False
            current = current.next
            if current == self.player_head:
                break
        return True

    def check_highest(self):
        current = self.player_head
        while True:
            if current.status != Action.FOLD or current.status != Action.ALL_IN:
                if current.bet > self.highest_bet:
                    self.highest_bet = current.bet
                    return True
            current = current.next
            if current == self.player_head:
                break
        return False

    def pre_flop(self):
        current = self.player_head
        while True:
            for _ in range(2):
                current.hand.add_card(self.deck.deal_card())
            current = current.next
            if current == self.player_head:
                break

    def flop(self):
        for _ in range(3):
            self.add_community_card(self.deck.deal_card())

    def turn(self):
        self.add_community_card(self.deck.deal_card())

    def river(self):
        self.add_community_card(self.deck.deal_card())

    def showdown(self):
        self.determine()

    def start_next_phase(self):

        if self.current_phase == CurrentPhase.PREFLOP:
            self.current_phase = CurrentPhase.FLOP

        elif self.current_phase == CurrentPhase.FLOP:
            self.current_phase = CurrentPhase.TURN

        elif self.current_phase == CurrentPhase.TURN:
            self.current_phase = CurrentPhase.RIVER

        elif self.current_phase == CurrentPhase.RIVER:
            self.current_phase = CurrentPhase.SHOWDOWN

        else:
            raise ValueError("Invalid phase transition.")

    def play_round(self):

        if self.player_count() < 2:
            raise ValueError("Need 2 or more player")

        while self.current_phase != CurrentPhase.SHOWDOWN:
            print(f"Current Phase: {self.current_phase}")

            if self.current_phase == CurrentPhase.PREFLOP:
                self.pre_flop()

            if self.current_phase == CurrentPhase.FLOP:
                self.flop()
                self.update_player_strength()

            if self.current_phase == CurrentPhase.TURN:
                self.turn()
                self.update_player_strength()

            if self.current_phase == CurrentPhase.RIVER:
                self.river()
                self.update_player_strength()

            while not (self.all_checked()):
                current = self.player_head
                while True:
                    if current.status != Action.FOLD:

                        print(f"community-cards: {self.community_cards}")
                        print(current)

                        if self.preflop:

                            if current == self.player_head:
                                while True:
                                    print(f"highest bet: {self.highest_bet}")
                                    move = input(
                                        "SMALL BLIND Move: [B]et (5 chips)\nInput: ").strip().lower()
                                    if move in ["bet", "b"]:
                                        current.add_bet(5)
                                        break
                                    else:
                                        print(
                                            "invalid input. Please enter 'bet' or 'b'.")

                            elif current == self.player_head.next:
                                while True:
                                    print(f"highest bet: {self.highest_bet}")
                                    move = input(
                                        "BIG BLIND Move: [B]et (10 chips)\nInput: ").strip().lower()
                                    if move in ["bet", "b"]:
                                        self.preflop = False
                                        current.add_bet(10)
                                        break
                                    else:
                                        print(
                                            "invalid input. Please enter 'bet' or 'b'.")
                        else:
                            while True:
                                print(f"highest bet: {self.highest_bet}")
                                available_moves = ""

                                if current.bet == self.highest_bet or current.status == Action.ALL_IN:
                                    available_moves += "[C]heck, "

                                if current.chips > self.highest_bet + 10 or current.chips == self.highest_bet:
                                    available_moves += "[B]et, "

                                if current.status != Action.FOLD:
                                    available_moves += "[A]ll-in, [F]old"

                                move = input(
                                    f"NORMAL Move: {available_moves}\nInput: ").strip().lower()

                                if move in ["check", "c"] and (current.bet == self.highest_bet or current.status == Action.ALL_IN):
                                    current.status = Action.CHECK
                                    break

                                elif move in ["bet", "b"] and (current.chips > self.highest_bet + 10 or current.chips == self.highest_bet):
                                    while True:

                                        available_moves = []
                                        if current.chips > self.highest_bet + 10:
                                            available_moves.append(
                                                f"[R]aise: minimum: {self.highest_bet} + 10 chips")

                                        if current.chips >= self.highest_bet:
                                            available_moves.append(
                                                f"[C]all: via highest bet {self.highest_bet} chips")

                                        prompt_message = f"{' or '.join(available_moves)} Mode: "
                                        mode = input(
                                            prompt_message).strip().lower()

                                        if mode in ["raise", "r"]:
                                            bet_input = input("bet: ")
                                            try:
                                                bet = int(bet_input)
                                                if bet >= self.highest_bet + 10 and bet <= current.chips:
                                                    current.add_bet(bet)
                                                    if current.bet == current.chips:
                                                        current.status = Action.ALL_IN
                                                    break
                                                else:
                                                    print(
                                                        "Invalid number. Minimum bet is 10 chips more than the highest bet.")
                                                break
                                            except ValueError:
                                                print(
                                                    "Invalid input. Please enter a valid number for the bet.")

                                        elif mode in ["call", "c"]:
                                            current.add_bet(
                                                self.highest_bet)
                                            if current.bet == current.chips:
                                                current.status = Action.ALL_IN
                                            break

                                        else:
                                            print(
                                                "invaild input. Please enter [R]aise: minimum: 10 chips or [P]ass: via highest bet.")
                                    break

                                elif move in ["all-in", "a"] and (current.status != Action.FOLD):
                                    current.add_bet(current.chips)
                                    current.status = Action.ALL_IN
                                    break
                                elif move in ["fold", "f"] and (current.status != Action.FOLD):
                                    current.status = Action.FOLD
                                    break
                                else:
                                    print(
                                        f"invalid input. Please enter {available_moves}")

                    self.check_highest()
                    current = current.next
                    if current == self.player_head or self.all_checked():
                        break
            else:
                print("in else")
                self.reset_highest()
                self.player_info()
                if self.check_active_player() == 1:
                    self.determine()

                self.start_next_phase()
        else:
            self.showdown()


mygame = PokerTable()

player1 = Player("Alex", 1000)
player2 = Player("Jack", 1000)
player3 = Player("Tomy", 1000)
player4 = Player("John", 1000)

mygame.append(player1)
mygame.append(player2)
mygame.append(player3)
mygame.append(player4)
# mygame.player_info()

mygame.play_round()
