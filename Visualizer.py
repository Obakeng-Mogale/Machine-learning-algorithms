import pygame
from ObLearn import *
import time
#initialize pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
reg_font = pygame.font.SysFont('Comic Sans MS', 20)
WIDTH = 1280
HEIGHT = 720
IS_CLEAR = True
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
red = pygame.Color(255,0,0, a = 255) # uses rgba
current_Matrix = []
current_y = []
black = pygame.Color(0,0,0)
right_border = WIDTH - 0.2 * WIDTH
bottom_border = HEIGHT - 0 * HEIGHT

def placeDot(x,y):
    """
    function used for placing a dot on the screen according to the mouses x, y 
    """
    radius=5
    center = (x,y)
    #by default it will be filled
    pygame.draw.circle(screen,red, center, radius)
    return

def draw_line(start_x, end_x, vals):
    start_y = vals[0] + start_x * vals[1]
    end_y = vals[0] + vals[1] * end_x
    pygame.draw.aaline(screen, black, (start_x,start_y), (end_x, end_y))
    eqn = my_font.render(f"y = {round(vals[1] * -1,3)}*X + {round(HEIGHT -vals[0],3)}", False, (0,0,0))

    screen.blit(eqn, (0,0))
    return


def addToMatrix(x,y):
    """
    x: position on the x axis
    y : position on the y axis
    """
    current_Matrix.append([x])
    current_y.append([y])
    return

def setup():
    #buttons
    """clear screen button"""
    clear_button = pygame.draw.rect(screen, black, (1050,(HEIGHT-100)//2,200,100), border_radius
                     = 10, width = 5)
    """regression button"""
    reg_button = pygame.draw.circle(screen, black, (WIDTH - (WIDTH -
        right_border)//2, 550), 50, width = 5)
    """
    border lines
    """
    pygame.draw.line(screen, black, (right_border, 0), (right_border,
                                                        bottom_border))

    text_surface = my_font.render('clear Screen', False, (0, 0, 0))
    reg_text = reg_font.render("Regress", False, (0, 0 ,0))
    screen.blit(text_surface, (1065, (HEIGHT-100)//2 + 25))
    screen.blit(reg_text, (WIDTH - (WIDTH - right_border)//2 - 35, 535))
    return [clear_button, reg_button]


def clearScreen():
    global current_y, current_Matrix, IS_CLEAR
    screen.fill("white")
    current_Matrix = []
    current_y = []
    IS_CLEAR = True
    return


def main():
    """ 
    contains the main loop for the screen
    """
    global IS_CLEAR
    screen.fill("white")

    lr = LinearRegression() 

    buttons = setup()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        #fill the screen with white
        # Logical Updates here
        """
        pos 0 : left click
        pos 1 : middle mouse
        pos 2 : right click
        """
        mouse = pygame.mouse
        if mouse.get_pressed()[0]:
            x,y = mouse.get_pos()

            if x < WIDTH - 0.2*WIDTH and IS_CLEAR:
                placeDot(x,y)
                addToMatrix(x,y)
            elif pygame.Rect.collidepoint(buttons[0], (x,y)):
                clearScreen()
                buttons = setup()
            elif pygame.Rect.collidepoint(buttons[1], (x,y)) and IS_CLEAR:
                IS_CLEAR = False
                line_values = lr.fit(Matrix(current_Matrix),current_y)
                if line_values: 
                    draw_line(0, WIDTH - 0.2*WIDTH, line_values) 
                else:
                    print("FAIL : not enough data points")

            time.sleep(0.15)

            
            



        #---------------------------------------------------
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
