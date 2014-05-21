import random

board = [[0, 0, 0, 0],
		 [0, 0, 0, 0],
		 [0, 0, 1, 0],
		 [0, 0, 0, 0]]

filled_dict = {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (1, 0): False, (1, 1): False, (1, 2): False, (1, 3): False, (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (3, 0): False, (3, 1): False, (3, 2): False, (3, 3): False}

def print_board():
	for i in board:
		print i

def two_or_four():
	choice = random.randint(1, 10)
	if choice < 10:
		return 2
	else:
		return 4

def place_random():
	spots = []
	for i, j in enumerate(board):
		for x, y in enumerate(j):
			if y == 0:
				spots.append([i, x])
	placement = random.choice(spots)
	board[placement[0]][placement[1]] = two_or_four()
	return spots

def move_up():
	moved = False
	for i, j in enumerate(board):
		for x, y in enumerate(j):
			if i in range(1, 4):
				if board[i - 1][x] == 0 and board[i][x] != 0:
					board[i - 1][x] = board[i][x]
					board[i][x] = 0
					moved = True
	if moved == True:
		move_up()

def move_down():
	moved = False
	for i, j in enumerate(board):
		for x, y in enumerate(j):
			if i in range(0, 3):
				if board[i + 1][x] == 0 and board[i][x] != 0:
					board[i + 1][x] = board[i][x]
					board[i][x] = 0
					moved = True
	if moved == True:
		move_down()

def move_left():
	moved = False
	for i, j in enumerate(board):
		for x, y in enumerate(j):
			if x in range(1, 4):
				if board[i][x - 1] == 0 and board[i][x] != 0:
					board[i][x - 1] = board[i][x]
					board[i][x] = 0
					moved = True
	if moved == True:
		move_left()

def move_right():
	moved = False
	for i, j in enumerate(board):
		for x, y in enumerate(j):
			if x in range(0, 3):
				if board[i][x + 1] == 0 and board[i][x] != 0:
					board[i][x + 1] = board[i][x]
					board[i][x] = 0
					moved = True
	if moved == True:
		move_right()

move_up()
move_right()
move_down()
move_left()
print_board()