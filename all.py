print ('''
PROGRESS STARTED
KARYA PREGATI PAR HAI
HONEE WALI ASUVIDHA KEE LIYE KHEED HAI
''')
#from tracer import *

print ('''
DONE
''')

from start import *
from coordinates import *

def start_practice(): #def fxn for the user interface of this module
    turtle.speed(1)
    initial_pos=path[-1]
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

start_practice()
