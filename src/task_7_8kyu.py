# iven a positive integer N, return all the extra perfect numbers in the range from 1 to N, inclusive.
# An extra perfect number is a positive integer whose first and last bits in binary representation are set (i.e., both are 1).
def extra_perfect(n: int) -> list[int] :
    
    lst = []
    for i in range(1, n + 1):
        if check_bite(i):
            lst.append(i)
    return lst

def check_bite(n: int) -> bool:
    bin_numb_str = bin(n).lstrip('0b')  
    return bin_numb_str[0] == bin_numb_str[-1]

def extra_perfect_2(n):
     return [i for i in range(n+1) if bin(i)[2] == '1' and bin(i)[-1] == '1']

def extra_perfect_3(n):
    return list(range(1,n+1,2))


# Description:The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one is chosen.
# Task:Given an array of Player objects and a position (first position is 1), return the name of the chosen Player.
# name is a property of Player objects, e.g Player.name
from dataclasses import dataclass
@dataclass
class Player:
    name: str
    id: int
    
def duck_duck_goose(players: list[Player], goose: int):
    player = goose % (len(players))
    return players[player - 1].name

def test_duck_duck_goose():
    players = []
    for i in 'abcdfegs':
        obj = Player()
        obj.name = i
        players.append(obj)
    assert duck_duck_goose(players, 1) == 'a'
    
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
# The binary number returned should be a string.    

def add_binary(a,b):
    return bin(a + b).lstrip('0b')