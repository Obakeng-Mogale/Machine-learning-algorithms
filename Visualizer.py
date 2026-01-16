import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
red = pygame.Color(255,0,0, a = 255) # uses rgba

def placeDot(x,y):
    """
    function used for placing a dot on the screen according to the mouses x, y 
    """
    radius=2
    center = (x,y)
    pygame.draw.circle(surface,color, center, radius)
    pass

def draw_line():

def main():
    """ 
    contains the main loop for the screen
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        # Logical Updates here



        #---------------------------------------------------
        pygame.display.flip()
        pygame.tick(60)
