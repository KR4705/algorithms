# need to implement a simple path finding game in python.
# import pprint 
board = [[0]*7 for _ in range(7)]

def print_grid(grid):
    for row in grid:
        for e in row:
            print e,
        print  

# print print_grid(board)

def set_goal(a,b):
	board[a][b] = "g"	

# set_goal(3,3)
# print print_grid(board)

def set_block(a,b):
	board[a][b] = "b"

set_block(4,2)
set_block(2,2)
set_block(3,2)
set_block(5,2)
set_block(1,0)
set_block(1,2)
set_block(1,1)

print print_grid(board)

def fill(board,a,b):
	if a<5 and b<5 and a>1 and b>1: 
		if not board[a-1][b] == "b" and board[a-1][b] == 0: board[a-1][b] = board[a][b] + 1
		if not board[a][b+1] == "b" and board[a][b+1] == 0: board[a][b+1] = board[a][b] + 1
		if not board[a+1][b] == "b" and board[a+1][b] == 0: board[a][b+1] = board[a][b] + 1
		if not board[a][b-1] == "b" and board[a][b-1] == 0: board[a][b+1] = board[a][b] + 1
		fill(board,a-1,b)
		fill(board,a,b+1)
		fill(board,a+1,b)
		fill(board,a,b+1)
	return 

fill(board,3,3)

print_grid(board)

