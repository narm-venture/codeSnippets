from math import *

angle_min=-2.35619449615
angle_max=2.35619449615
angle_increment= 0.00436332309619
resolution=10
scale=1

    # scale is the number of units per cm
    # size in (x,y) dentoes the boundaries of the map
map=[]
cordinates=[]
scale=scale

            
def polar_to_cartesian(ranges):
    angle=angle_min
    index=0
    for i in range(len(ranges)):
        x=int(ranges[i]*cos(angle+pi/2.)*resolution)
        y=int(ranges[i]*sin(angle+pi/2.)*resolution)
        cordinates.append((x,y))
        angle=angle+angle_increment
    return cordinates
        
def optimize_cordinates():
    #limit cordinates within maximum range and pop the rest
    #remove duplicate cordinates
    return

def map_init(size=(100,100)):
    map=[]
    for x in range(size[1]):
        tmp=[]
        for y in range(size[0]):
            tmp.append(' ')
        map.append(tmp)
    return map
def fill_map(cordinates,map):
#    robot_pos=(int(size[0]/2.),(size[1]-int(size[1]/sqrt(8))))
    for i in range(len(map)):
        for j in range(len(map[i])):
            y=65-i
            x=50+j
            if y < 100 and x <100:
                map[y][x]='*'

    return map


def show_map(map):
    tmp=""
    for x in map:
#        print x
        tmp=""
        for y in x:
            if y=='*':
                tmp=tmp+'.'
            else:
                tmp=tmp+' '
        print tmp

#ranges=input('Enter range list:')
