grid=[[0,0,1,0,0,0],
      [0,0,1,0,0,0],
      [0,0,0,0,1,0],
      [0,0,1,1,1,0],
      [0,0,0,0,1,0]]

init=[0,0]
goal=[len(grid)-1,len(grid[0])-1]

delta=[[-1,0],  #go up
       [0,-1],   #go left
       [1,0],   #go down
       [0,1]]  #go right

delta_name=['^','<','>','V']

def add(a,b):
    if not len(a)==len(b):
        return
    tmp=[]
    for x in range(len(a)):
        tmp.append(a[x]+b[x])
    return tmp    

open=[init]
closed=[]
gvalue=[0]

min=gvalue.index(min(gvalue))
gvalue.pop(min)
min=open.pop(min)
closed.append(min)
if tmp not in open and tmp not in closed and map:
    tmp
