import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 680))
clock = pygame.time.Clock()
running = True
playerturn = True
# Load the background image
background_image = pygame.image.load("background.png")

def drawcircle(x,y):
    pygame.draw.circle(background_image,(227, 11, 33),(x,y),25,5)

def drawcross(x,y):
    pygame.draw.line(background_image,(7, 107, 222),(x-25,y+25),(x+25,y-25),4)
    pygame.draw.line(background_image,(7, 107, 222),(x+25,y+25),(x-25,y-25),4)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            positionx,positiony = event.pos
            if playerturn == True:
                drawcircle(positionx,positiony)
            else:
                drawcross(positionx,positiony)  

            playerturn = not playerturn
    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background_image, (0, 0))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()