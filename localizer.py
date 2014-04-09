colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 1.0

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

p = [[1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1]]





#sense function to increase entropy of P(X)
def sense(p,Z):
    q=p
    tmp=0
    for i in range(len(q)):
        for x in range(len(q[i])):
            tmp=q[i][x]
            if colors[i][x]==Z:
                tmp*=sensor_right
            else:
                tmp*=(1.-sensor_right)
            q[i][x]=tmp
    tot=sum([x for sublist in q for x in sublist])
    for i in range(len(q)):
        for x in range(len(q[i])):
            if not (q[i][x]==0):
                q[i][x]/=tot
    return q

def move(p,U):
    horizontal_steps=U[1]
    vertical_steps=U[0]
    p=p[-vertical_steps:]+p[:-vertical_steps]
    for x in range(len(p)):
        tmp=p[x][-horizontal_steps:]+p[x][:-horizontal_steps]
        p[x]=tmp
    return p




#Your probability array must be printed 
#with the following code.
#show(p)

for x in range(len(measurements)):
    p=move(p,motions[x])
    p=sense(p, measurements[x])
show(p)

flat_p=[x for sublist in p for x in sublist]
index=flat_p.index(max(flat_p))
print '------------------------------------------------------'
print 'Localization complete'
print '------------------------------------------------------'
print 'Your robot is probably present at (',(index/5),',',(index%5),')'



