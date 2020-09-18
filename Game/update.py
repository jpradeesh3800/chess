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

