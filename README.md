# tic-tac-toe
Tick-Tac-Toe game state is defined as follows:
tile1 | tile2 | tile3
______|_________|______
tile4 | tile5 | tile6
______|_________|______
tile7 | tile8 | tile9
______|_________|______
A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.
We will estimate probability of winning for a player for different scenarios.
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
"""
import random
# There are 2 players: player1 and player2
player1=1
player2=2
# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2
tile1= 0
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0
# turn variable defines whose turn is now
turn = Player1
def validmove(move):
""" Checks whether a move played by a player is valid or invalid.
Return True if move is valid.
A move is valid if the corresponding tile for the move is not ticked.
"""
pass

def win():
""" Returns True if the board state specifies a winning state for some player.
A player wins if ticks made by the player are present either
i) in a row
ii) in a cloumn
iii) in a diagonal
"""
pass

def takeNaiveMove():
""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.
"""
pass

def takeStrategicMove():
""" Returns a tile number from the set of unchecked tiles
using some rules.
"""

def validBoard():
""" Return True if board state is valid.
A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
"""
pass

def game(gametype=1):
""" Returns 1 if player1 wins and 2 if player2 wins
and 0 if it is a draw.
gametype defines three types of games discussed above.
i.e., game1, game2, game3
"""

def game1(n):
""" Returns the winning probability for player1.
n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
"""
pass

def game2(n):
"""Returns the winning probability for player1.
n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
"""
pass

def game3(n):
"""Returns the winning probability for player1.
n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
"""
pass
