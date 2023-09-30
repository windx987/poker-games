from enum import Enum


class RoleStatus(Enum):
    OFF = False
    ON = True


class Action(Enum):
    FOLD = 0
    CHECK = 1
    RISE = 2
    CALL = 3
    ALL_IN = 4


class CurrentPhase(Enum):
    PREFLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
    SHOWDOWN = 5
