colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = [[0,0,0,0,0]]*4

//sense function to increase entropy of P(X)
def sense(p,Z):
    q=[]
    tmp=[]
    map=[x for sublist in colors for x in sublist]
    p_z=(float(map.count(Z))/len(map))*sensor_right
    p_notz=(1.-float((map.count(Z))/len(map)))*(1.-sensor_right)
    p_z/=(p_z+p_notz)
    p_notz/=(p_z+p_notz)
    p_z=p_z/map.count(Z)
    p_notz/=(len(map)-map.count(Z))
    for x in range(len(p)):
        for i in range(len(p[x])):
            tmp.append(p_z if colors[x][i]==Z else p_notz)
        q.append(tmp)
        tmp=[]
    return q

def move(p,U):
    horizontal_steps=U[1]
    vertical_steps=U[0]
    p=p[-vertical_steps:]+p[:-vertical_steps]
    
    return p




#Your probability array must be printed 
#with the following code.
p= sense(p,'green')
p=move(p,[1,0])
show(p)




