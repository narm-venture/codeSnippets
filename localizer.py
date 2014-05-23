##Monte-Carlo Localization (version 1.0)
## created by : Shubhojyoti Ganguly
## Company: NARM Robotics



colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

##colors=[['green','green','green'],
##        ['green','red','red'],
##        ['green','green','green']]
measurements = ['green', 'green', 'green' ,'green', 'green']
##measurements=['red','red']

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
##motions=[[0,0],[0,1]]

sensor_right = 0.8

p_move = 0.7

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


p_Under=p_Over=(1-p_move)/2.



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

def multiply_to_list(lis,c):
    new_list=[]
    for x in range(len(lis)):
        new_list.append(float(lis[x]*c))
    return new_list

def add_lists(lisa,lisb):
    if not len(lisa)==len(lisb):
        return -1
    for x in range(len(lisa)):
        lisa[x]+=lisb[x]
    return lisa

def move(p,U):
    horizontal_steps=U[1]
    vertical_steps=U[0]
    q=[]
    row=[]
    if not horizontal_steps==0:
        for x in range(len(p)):
            tmp=p[x]
            for i in range(len(tmp)):
                prob=p_move*tmp[(i-horizontal_steps)%len(tmp)]
                prob+=p_Over*tmp[(i-horizontal_steps-1)%len(tmp)]
                prob+=p_Under*tmp[(i-vertical_steps+1)%len(tmp)]
                row.append(prob)
            q.append(row)
            row=[]

        p=q
        q=[]
        row=[]
    if not vertical_steps==0:            
        for x in range(len(p)):
            row=multiply_to_list(p[(x-vertical_steps)%len(p)],p_move)
            row=add_lists(row,multiply_to_list(p[(x-vertical_steps-1)%len(p)],p_Over))
            row=add_lists(row,multiply_to_list(p[(x-vertical_steps+1)%len(p)],p_Under))
            q.append(row)
            row=[]

        p=q
    
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
print 'The robot has ',flat_p[index]*100,'% chance of being present at (',(index/5),',',(index%5),')'



