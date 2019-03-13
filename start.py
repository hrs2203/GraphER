import turtle
import math

origin=[0,0]
pos=None

def draw():
    turtle.pen()
    #traces the abcisa and ordinate of a 2-D graph
    turtle.forward(700)
    turtle.backward(1400)
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(400)
    turtle.backward(800)
    turtle.forward(400)
    turtle.right(90)

def turn(a=[0,0],b=[0,0]):
    turn=0
    slope=0
    'a -- start , b -- end'
    'this function finds the slope for straight line'
    #turn is a function in degrees
    slope=(float(b[1]-a[1]))/(b[0]-a[0])
    turn=math.degrees(math.atan(slope))
    turtle.left(turn)

def calc_length(a=[0,0],b=[0,0]):
    #a -- from ; b -- to
    length=math.sqrt(((b[1]-a[1])**2)+((b[0]-a[0])**2))
    return (length)*100

def retrive(a=[0,0],b=[0,0]):
    #a -- start point ; b -- end point
    #turns the turtle parallel to the x axis
    turtle.right(math.degrees(math.atan((float(b[1]-a[1]))/(b[0]-a[0]))))

def line(f=[0,0],t=[0,0]):
    "f -- from ; t -- to"
    #streaches line from f to t
    if f==t:
        pass
    else:
        if t[0]-f[0]!=0:
            turn(f,t)
            length=calc_length(f,t)
            if t[0]-f[0]>0:
                turtle.forward(length)
            elif t[0]-f[0]<0:
                turtle.backward(length)
            retrive(f,t)
        elif t[0]-f[0]==0:
            length=calc_length(f,t)
            if t[1]-f[1]>0:
                turtle.left(90)
                turtle.forward(length)
                turtle.right(90)
            elif t[1]-f[1]<0:
                turtle.right(90)
                turtle.forward(length)
                turtle.left(90)
def go(s=[0,0],e=[0,0]):
    "s --> start ; e --> end"
    turtle.up()
    line(s,e)
    turtle.down()

def start_practice(): #def fxn for the user interface of this module
    turtle.speed(1)
    draw()
    initial_pos=origin
    trac=[[0,0]]
    while True:
        do=input('>>>what is the command:::')
        if do=='line':
            x=float(input('>>enter the x coordinates :::'))
            y=float(input('>>enter the y coordinates :::'))
            final_pos=[x,y]
            trac.append(final_pos)
            line(initial_pos,[final_pos[0],final_pos[1]])    
            initial_pos=[final_pos[0],final_pos[1]]
            final_pos=None
        elif do=='move':
            x=float(input('>>enter the x coordinates :::'))
            y=float(input('>>enter the y coordinates :::'))
            final_pos=[x,y]
            trac.append(final_pos)
            go(initial_pos,[final_pos[0],final_pos[1]])    
            initial_pos=[final_pos[0],final_pos[1]]
            final_pos=None
        elif do=='track':
            for i in trac:
                print (i)