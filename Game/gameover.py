def isWin(board,x):
	if board.is_checkmate() or board.is_game_over():
		print(x,"won")
	

def isDraw(board):
	if board.is_stalement():
		print("Stalemate\nGame is Draw\n")
	elif board.is_insufficient_material():
		print("Insufficient Material\nGame is Draw\n")
	elif board.is_fivefold_repetition():
		print("a fivefold repetition occurs or if there are 75 moves without a pawn push or capture\nGame is Draw\n")
	elif board.is_seventyfive_moves():
		print("Seventyfive moves\nGame is Draw\n")
	
	

