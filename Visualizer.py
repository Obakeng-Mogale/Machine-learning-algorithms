import pygame
from ObLearn import *
import time
#initialize pygame
pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
red = pygame.Color(255,0,0, a = 255) # uses rgba
current_Matrix = []
current_y = []

def placeDot(x,y):
    """
    function used for placing a dot on the screen according to the mouses x, y 
    """
    radius=3
    center = (x,y)
    print(center)
    #by default it will be filled
    pygame.draw.circle(screen,red, center, radius)
    return

def draw_line(start, end):
    pygame.draw.aaline(start, end)
    pass

def addToMatrix(x,y):
    """
    x: position on the x axis
    y : position on the y axis
    """
    current_Matrix.append([x])
    current_y.append([y])
    print(current_Matrix)
    print(current_y)
    return

def main():
    """ 
    contains the main loop for the screen
    """
    screen.fill("white")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        #fill the screen with white
        # Logical Updates here
        mouse = pygame.mouse
        if mouse.get_pressed()[0]:
            
            time.sleep(0.15)
            x,y = mouse.get_pos()
            placeDot(x,y)
            addToMatrix(x,y)
        elif mouse.get_pressed()[2]:
            draw_line(start, end)
        """
        pos 0 : left click
        pos 1 : middle mouse
        pos 2 : right click
        """




        #---------------------------------------------------
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
