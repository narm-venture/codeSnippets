import math

ranges=input('Enter sample sensor_data:')
#populate ranges from sensor_scan

x_cordinates=[]
y_cordinates=[]
start_angle=-2.35619449615
end_angle=2.35619449615
step=0.00436332309619
total_angle=end_angle-start_angle
resolution=10
# end of declaration of settings

#generate x and y cordinates
i=0.0
count=0
while i < total_angle:
    x_cordinates.append(ranges[count]*math.cos(i))
    y_cordinates.append(ranges[count]*math.sin(i))
    i=i+step
    count=count+1

#shifting origin to min(x) and min(y)
absolute_cordinates=[]
for x in range(len(ranges)):
    x=int((x_cordinates[x]-min(x_cordinates))*resolution)
    y=int((y_cordinates[x]-min(y_cordinates))*resolution)
    absolute_cordinates.append((x,y))

#generate empty map
map=[]
for y in range(int(max(y_cordinates))):
    tmp=[]
    for x in range(int(max(x_cordinates))):
        tmp.append('')
    map.append(tmp)

#filling up of map
for i in range(len(ranges)):
    x=absolute_cordinates[i][0]
    y=absolute_cordinates[i][1]
    if y < int(max(y_cordinates)) and x < int(max(x_cordinates)):
        map[y][x]=1


#showing of map
for x in map:
    print x
