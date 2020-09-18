import cv2
import numpy as np
import matplotlib.pyplot as plt
import chess
import time
import pandas as pd
from stockfish import Stockfish
from chess_crop import crop
from detection import detect

def capture():
	cap=cv2.VideoCapture(4)
	
	while True:

		_,frame=cap.read()
		print(_)
		
		
		img=crop(frame)
		color2,intensity=detect(img)
		print(intensity)
		#cv2.imshow("1",frame)
		cv2.imshow("2",img)
		cv2.waitKey(0)

		return color2

def update1(position,color,x):
	position.iloc[x[0][1],x[1][1]]=position.iloc[x[0][0],x[1][0]]
	color.iloc[x[0][1],x[1][1]]=color.iloc[x[0][0],x[1][0]]
	color.iloc[x[0][0],x[1][0]]=position.iloc[x[0][0],x[1][0]]='e'

	return position,color

def update2(position,color,z,i,f):
	if z=='e8g8' and position.loc['8','e']=='k':
		color.loc['8','h']=color.loc['8','e']='e'
		color.loc['8','f']=opp
		color.loc['8','g']=opp
		position.loc['8','h']=position.loc['8','e']='e'
		position.loc['8','g']='K'
		position.loc['8','f']='R'
	elif z=='e8c8' and position.loc['8','e']=='k':
		color.loc['8','e']=color.loc['8','a']='e'
		color.loc['8','c']=opp
		color.loc['8','d']=opp
		position.loc['8','e']=position.loc['1','a']='e'
		position.loc['8','c']='K'
		position.loc['8','d']='R'
	else:		
		color.loc[f[0],f[1]]=color.loc[i[0],i[1]]
		position.loc[f[0],f[1]]=position.loc[i[0],i[1]]
		color.loc[i[0],i[1]]=position.loc[i[0],i[1]]='e'	

	return position,color

def update3(position,color,s,opp):
	if s=='small':
		color.loc['1','h']=color.loc['1','e']='e'
		color.loc['1','f']=opp
		color.loc['1','g']=opp
		position.loc['1','h']=position.loc['1','e']='e'
		position.loc['1','g']='K'
		position.loc['1','f']='R'
	elif s=='long':
		color.loc['1','e']=color.loc['1','a']='e'
		color.loc['1','c']=opp
		color.loc['1','d']=opp
		position.loc['1','e']=position.loc['1','a']='e'
		position.loc['1','c']='K'
		position.loc['1','d']='R'
	return position,color


def pos(x,index,columns):
	initial=columns[x[1][0]]+index[x[0][0]]
	final=columns[x[1][1]]+index[x[0][1]]
	return initial+final

def isWin(board,x):
	if board.is_checkmate() or board.is_game_over():
		print("Checkmate\n",x,"won")
		
	

def isDraw(board):
	if board.is_stalemate():
		print("Stalemate\nGame is Draw\n")
	elif board.is_insufficient_material():
		print("Insufficient Material\nGame is Draw\n")
	elif board.is_fivefold_repetition():
		print("a fivefold repetition occurs or if there are 75 moves without a pawn push or capture\nGame is Draw\n")
	elif board.is_seventyfive_moves():
		print("Seventyfive\n")
		

board=chess.Board()
sf=Stockfish("stockfish")

x=[list("rnbqkbnr"),['p']*8,([['e']*8]*4),['P']*8,list("RNBQKBNR")]
index=list("87654321")
columns=list("abcdefgh")
position=pd.DataFrame(x,index=list("87654321"),columns=list("abcdefgh"))


color=capture()
opp=color.loc['1','a']
print(color)



inp=False

while True:
	inp=input("Enter something: ")
	
	color2=capture()

	x=np.where(np.array(color)!=np.array(color2))
	
	
	print(np.array(color))
	print(np.array(color2))
	print(x)
		
	if len(x[0])==2:
		if color2.iloc[x[0][0],x[1][0]]!='e':
			x=np.array([[x[0][1],x[0][0]],[x[1][1],x[1][0]]])
		try:
			move1=chess.Move.from_uci(pos(x,index,columns))
			board.push(move1)
			position,color=update1(position,color,x)	
		except:
			print("Wrong Move")
			continue

	elif len(x[0])==4:
		try:
			if set(x[1])==set([0,1,2,3]) and list(x[0])==[1]*4:
				board.push_san('O-O')
				update3(position,color,'small',opp)
			elif set(x[1])==set([3,4,5,7]) and list(x[0])==[1]*4:
				board.push_san('O-O-O')
				position,color=update3(position,color,'long',opp)
			else:
				print("Wrong Move")
				continue
		except:
			print("Wrong Move")
			continue	
	
	elif len(x[0])==0:
		print("Please make a move")
		continue	


	print(board)
	print(color)
	print(position)

	isWin(board,'You')
	isDraw(board)
	
	sf.set_fen_position(board.fen())
	zz=sf.get_best_move()
	move2=chess.Move.from_uci(zz)
	board.push(move2)
	
	isWin(board,'I')
	isDraw(board)

	initial=list(zz[1::-1])
	final=list(zz[3::-1])
	position,color=update2(position,color,zz,initial,final)	


	print(board)
	print(color)
	print(position)

	
	
	
	
			
	

	
	
		
		
