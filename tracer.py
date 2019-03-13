from start import *
from inserter import *
from coordinates import *
from math import *
import turtle

turtle.speed(0)             # done as to work at the maximum speed

draw()

i=0
go(origin,[path[0][0],0])

while i<(len(path)-1):
    if (path[i][1]) == None:
        go([path[i][0],0],[path[i+1][0],0])
        print([path[i][0],0],[path[i+1][0],0])
        i+=1
    elif (path[i][1]) != None:
        go([path[i][0],0],path[i])
        if (path[i+1][1]) != None:
            line(path[i],path[i+1])
            print(path[i],path[i+1])
            i+=1
            go(path[i],[path[i][0],0])
        elif (path[i+1][1]) == None:
            go(path[i],[path[i+1][0],0])
            print(path[i],[path[i+1][0],0])
            i+=1
