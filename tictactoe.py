#Anand
#2017218
#anand17218@iiitd.ac.in
#Homework Assignment 2---> Tic Tac Toe Game
'''We will estimate probability of winning for a player for different scenarios.
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
"""
# There are 2 players: player1 and player2'''
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
player1=1
player2=2
# turn variable defines whose turn is now
turn=1


import random

def validmove(move):
	if((move==1 and tile1==0) or (move==2 and tile2==0) or (move==3 and tile3==0) or (move==4 and tile4==0) or (move==5 and tile5==0) or (move==6 and tile6==0) or (move==7 and tile7==0) or (move==8 and tile8==0) or (move==9 and tile9==0) ):
		return True
	else:
		return False		

def win():
	p1=(tile1*tile2*tile3==1 or tile4*tile5*tile6==1 or tile7*tile8*tile9==1 or tile1*tile4*tile7==1 or tile2*tile5*tile8==1 or tile3*tile6*tile9==1 or  tile1*tile5*tile9==1 or tile3*tile5*tile7==1) 
	p2=(tile1*tile2*tile3==8 or tile4*tile5*tile6==8 or tile7*tile8*tile9==8 or tile1*tile4*tile7==8 or tile2*tile5*tile8==8 or tile3*tile6*tile9==8 or  tile1*tile5*tile9==8 or tile3*tile5*tile7==8) 
	if(p1 or p2):
		return True
	else:
		return False

def takeNaiveMove():
	y=random.randint(1,9)
	if(validmove(y)==True):
		return y
	else:
		return takeNaiveMove()

def count_checked_tiles():
	ct=0
	for x in range(1,10):
		if(eval('tile'+str(x))!=0):
			ct+=1
	return ct

def takeStrategicMove(g):
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9  
	global player1,player2,turn
	if(turn==player1 and g==3):
		if(count_checked_tiles()==0):
			return 1
		elif(count_checked_tiles()==2):
			return 4
		elif(count_checked_tiles()==4):
			return 3
		elif(count_checked_tiles()==6):
			return 8
		elif(count_checked_tiles()==8):
			return 9
	elif(turn==player2 and g==3):
		if(count_checked_tiles()==1):
			return 5
		elif(count_checked_tiles()==3):
			return 7
		elif(count_checked_tiles()==5):
			return 2
		elif(count_checked_tiles()==7):
			return 6
	elif(g==2):
		if(count_checked_tiles()==1):
			if(tile1==1 or tile3==1 or tile7==1 or tile9==1):
				return 5
			elif(tile5==1):
				return 3
			elif(tile2==1):
				return 8
			elif(tile4==1):
				return 6
			elif(tile6==1):
				return 4
			elif(tile8==1):
				return 2
		elif(count_checked_tiles()>=3):
			if(tile1==tile2==1):
				return 3
			elif(tile1==tile4==1):
				return 7
			elif(tile2==tile5==1):
				return 8
			elif(tile5==tile8==1):
				return 2
			elif(tile5==tile6==1):
				return 4
			elif(tile4==tile5==1):
				return 6
			elif(tile3==tile2==1):
				return 1
			elif(tile3==tile6==1):
				return 9
			elif(tile4==tile7==1):
				return 1
			elif(tile6==tile9==1):
				return 3
			elif(tile5==tile7==1):
				return 1
			else:
				return(takeNaiveMove())	
			


def validBoard():
	p1=0;p2=0
	for x in range(1,10):
		if(eval('tile'+str(x))==1):
			p1+=1
		elif(eval('tile'+str(x))==2):
			p2+=1
	if(p1>=p2):
		return True
	else:
		return False


def marktile(number,player):
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9  
	global player1,player2,turn
	if(number==1):
		tile1=player
	elif(number==2):
		tile2=player
	elif(number==3):
		tile3=player
	elif(number==4):
		tile4=player
	elif(number==5):
		tile5=player
	elif(number==6):
		tile6=player
	elif(number==7):
		tile7=player
	elif(number==8):
		tile8=player
	elif(number==9):
		tile9=player
def refreshtiles():
	#to reset tiles to 0
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9  
	global player1,player2,turn
	tile1=tile2=tile3=tile4=tile5=tile6=tile7=tile8=tile9=0

def whoseturn():
	#whose turn is now
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9  
	global player1,player2,turn
	if(turn==player1):
		 turn=player2
	else:
		turn=player1

def check():
	#returns true if any one of the tile is 0
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9  
	global player1,player2,turn
	if((tile1*tile2*tile3*tile4*tile5*tile6*tile7*tile8*tile9)==0):
		return True
	else:
		return False

def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
and 0 if it is a draw.
gametype defines three types of games discussed above.
i.e., game1, game2, game3
"""
	global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9  
	global player1,player2,turn
	draw=0
	g=0
	turn=player1
	if(gametype==1):
		while(check()):
			x=takeNaiveMove()
			marktile(x,turn)
			if(win()):
				draw=1
				return turn
			whoseturn()
		if(draw==0):
			return 0	
	elif(gametype==2):
		g=2
		while(check()):
			if(turn==player1):
				x=takeNaiveMove()
				marktile(x,player1)
				if(win()):
					draw=1
					return player1
			elif(turn==player2):
				y=takeStrategicMove(2)
				marktile(y,player2)
				if(win()):
					draw=1
					return player2
			whoseturn()	
		if(draw==0):
			return 0
	elif(gametype==3):
		g=3
		while(check()):
			x=takeStrategicMove(3)
			marktile(x,turn)
			if(win()):
				draw=1
				return turn
			whoseturn()
		if(draw==0):
			return 0	


def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""	
	count=0
	for x in range(n):
		refreshtiles()
		if(game(1)==1):
			count+=1
	return(float(count)/n)

def game2(n):
	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	count=0
	for x in range(n):
		refreshtiles()
		if(game(2)==2):
			count+=1
	return(float(count)/n)

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	count=0
	for x in range(n):
		refreshtiles()
		if(game(3)==1):
			count+=1
	return(float(count)/n)

print(game1(10000))
print(game2(10000))
print(game3(10000))