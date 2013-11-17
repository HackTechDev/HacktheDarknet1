import pyconsole
import pygame, os, sys, re
from pygame.locals import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tableDatabase import *

sys.path.append('./module')

from syntax import *

path = os.path.abspath(os.path.dirname(__file__))
img_path = os.path.join(path, "images")


pygame.init()

screen_width = 1024
screen_height = 768
screen=pygame.display.set_mode([screen_width,screen_height])

pygame.display.set_caption("Hack the Darknet")

Background = pygame.Surface((1024, 768))
bg_img = pygame.image.load(os.path.join(img_path,"worldmap.png"))
Background.blit(bg_img,(0,0))

bg_color = [0x0,0x0,0x0]

# Database

engine = create_engine('sqlite:///darknet.db', echo = False)
 
Session = sessionmaker(bind = engine)
session = Session()
 
def list(table):
    '''\
    Returns a record of a table
    '''

    if table == "user":
        users = ""
        res = session.query(User).all()
        for user in res:
            users += user.firstname + " " + user.lastname + "\n";
        return users      

    if table == "hacker":
        hackers = ""
        res = session.query(Hacker).all()
        for hacker in res:
            hackers += hacker.nickname + "\n";
        return hackers      

    return "Invalid table"


    """
    qry = session.query(User, Hacker)
    qry = qry.filter(User.id == Hacker.user_id)

    user, hacker = qry.filter(Hacker.nickname == "SolomonKane").first()
    return user.firstname + " " + user.lastname + " = " + hacker.nickname
    """

def f():
    return 100

def seive(n):
    '''\
    Returns a list of all prime numbers less than n
    Parameters: n - int
    '''
    
    primes = [0,0] + [1]*(n-2)
    for i in xrange(2, n):
        if primes[i] == 0:
            continue
        else:
            j = 2*i
            while j < n:
                primes[j] = 0
                j+=i
    return [m for m in xrange(0, n) if primes[m] == 1]


def line(start_pos, end_pos, color=[0,0,0], width=1):
    '''\
    Call pygame.draw.line
    Parameters:
        start_pos - x,y coordinate of start point
        end_pos - x,y coordinate of end point
        color - Line color in RGB format
        width - Line thickness 
    '''
    pygame.draw.line(Background, color, start_pos, end_pos, width)

def polygon(pointlist, color=[0,0,0], width=0):
    '''\
    Call pygame.draw.polygon
    Parameters:
        pointlist - list of vertices
        color - Line color in RGB format
        width - Line thickness 
    '''
    pygame.draw.polygon(Background, color, pointlist, width)

def circle(pos, radius, color=[0,0,0], width=0):
    '''\
    Call pygame.draw.circle
    Parameters:
        pos - x,y center of circle
        radius - radius of circle
        color - Line color in RGB format
        width - Line thickness 

    example:
            circle (100,100) 50 [0,255,0]
    '''
    pygame.draw.circle(Background, color, pos, radius, width)
    

def main():
    G_Screen = pygame.display.set_mode((1024, 768))
    cheat = False
    
    # An example Console object
    console = pyconsole.Console(
                                G_Screen, #The surface you want the console to draw on
                                (0,0,1024,500), #A rectangle defining the size and position of the console
                                functions={ "f":f,
                                            "prime": seive, 
                                            "type": type, 
                                            "line": line, 
                                            "polygon": polygon, 
                                            "circle": circle,
                                            "list": list
                                            }, # Functions for the console
                                key_calls={"d":sys.exit
                                            }, # Defines what function Control+char will call, in this case ctrl+d calls sys.exit()
                                syntax={re_add:console_add, 
                                        re_function:console_func
                                        }
                                )
    pygame.mouse.set_pos(300,240)
    vs = {"cheat":cheat,"a":100, "b":200, "c":300}
    console.setvars(vs)

    waiting = True

    while waiting:
        G_Screen.fill(bg_color)
        console.process_input()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    sys.exit()
                if event.key == K_w and pygame.key.get_mods() & KMOD_CTRL:
                    console.set_active()
                elif event.key == K_p and pygame.key.get_mods() & KMOD_CTRL: 
                    # Just a little hack so you can play with both pyconsole and python
                    # Hit ctrl w to hide pyconsole, then ctrl q to switch modes, then ctrl w again to show the console
                    # I don't expect anyone to actually use both modes in one app, if you really need to, you can be more creative than this.
                    console.setvar("python_mode", not console.getvar("python_mode"))
                    console.set_interpreter()
        
        G_Screen.blit(Background,(0,0))
        console.draw()
        pygame.display.flip()
        pygame.time.wait(10)
    

if __name__ == '__main__':
    main()
