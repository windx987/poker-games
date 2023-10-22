"""Utilities."""
from __future__ import annotations
import os

import random


def sample_cards(size: int) -> [int]:
    """Sample random cards with size."""
    return random.sample(range(52), k=size)


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def clear_screen():
    if os.name == "posix":
        os.system("clear")  # For Unix/Linux/macOS
    else:
        os.system("cls")    # For Windows
