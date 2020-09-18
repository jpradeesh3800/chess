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
	cap=cv2.VideoCapture(3)
	
	while True:

		_,frame=cap.read()
		print(_)
		img=crop(frame)
		color2=detect(img)
		#cv2.imshow("1",frame)
		#cv2.imshow("2",img)
		#cv2.waitKey(0)
		return color2

def update1(position,color,x):
	position.iloc[x[0][1],x[1][1]]=position.iloc[x[0][0],x[1][0]]
	color.iloc[x[0][1],x[1][1]]=color.iloc[x[0][0],x[1][0]]
	color.iloc[x[0][0],x[1][0]]=position.iloc[x[0][0],x[1][0]]='e'

	return position,color

def update2(position,color,i,f):
	color.loc[f[0],f[1]]=color.loc[i[0],i[1]]
	position.loc[f[0],f[1]]=position.loc[i[0],i[1]]
	color.loc[i[0],i[1]]=position.loc[i[0],i[1]]='e'	

	return position,color

def pos(x,index,columns):
	initial=columns[x[1][0]]+index[x[0][0]]
	final=columns[x[1][1]]+index[x[0][1]]
	return initial+final

board=chess.Board()
sf=Stockfish("stockfish")

x=[list("rnbqkbnr"),['p']*8,*([['e']*8]*4),['P']*8,list("RNBQKBNR")]
index=list("87654321")
columns=list("abcdefgh")
position=pd.DataFrame(x,index=list("87654321"),columns=list("abcdefgh"))


color=capture()
print(color)



inp=False

while True:
	inp=input("Enter something: ")
	#while(input()=='g'):
	#	time.sleep(1)
	
	color2=capture()

	x=np.where(np.array(color)!=np.array(color2))
	
	print(np.array(color))
	print(x)		
	
	if color2.iloc[x[0][0],x[1][0]]!='e':
		x=np.array([[x[0][1],x[0][0]],[x[1][1],x[1][0]]])

	
	position,color=update1(position,color,x)
	
	print(board)
	print(color)
	print(position)
		
	move1=chess.Move.from_uci(pos(x,index,columns))
	board.push(move1)

	
	
	sf.set_fen_position(board.fen())
	zz=sf.get_best_move()
	move2=chess.Move.from_uci(zz)
	board.push(move2)
	
	

	initial=list(zz[1::-1])
	final=list(zz[3::-1])
	position,color=update2(position,color,initial,final)	


	print(board)
	print(color)
	print(position)

	
	
	
	
			
	

	
	
		
		
