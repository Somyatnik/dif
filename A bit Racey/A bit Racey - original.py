import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
block_color = (53,115,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 51
car_height = 105000

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar_sh.png')
gameIcon = pygame.image.load('caricon.png')
pygame.display.set_icon(gameIcon)

pause = False
#crash = True

def blocks_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def blocks(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

##def message_display(text):
##    largeText = pygame.font.Font('freesansbold.ttf',115)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
##
##    pygame.display.update()
##
##    time.sleep(2)
##
##    game_loop()

def crash():
    #gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects('You Crashed', largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button('Replay',150,450,100,50,green,bright_green,game_loop)
        button('Quit',550,450,100,50,red,bright_red,quitgame)
                      
        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
         pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
         if click[0] == 1 and action != None:
             action()                            
    else:
         pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w/2)),(y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects('Paused', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Continue',150,450,100,50,green,bright_green,unpause)
        button('Quit',550,450,100,50,red,bright_red,quitgame)
                      
        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects('A bit Racey', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('GO!',150,450,100,50,green,bright_green,game_loop)
        button('Quit',550,450,100,50,red,bright_red,quitgame)
                      
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    dodged = 0

    block_starty = -600
    block_speed = 4
    block_width = 100
    block_height = 100
    block_startx = random.randrange(0,display_width)
    
    #thing_count = 1 как это сделать?

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        blocks(block_startx, block_starty, block_width, block_height, block_color)
        block_starty += block_speed
        car(x,y)
        blocks_dodged(dodged)

        if x > display_width - car_width or x == 0:
            crash()

        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0,display_width)
            dodged += 1
            #thing_speed += 1
            #thing_width += (dodged * 1.2)

        if y < block_starty + block_height and y > block_starty or y + car_height > block_starty and y + car_height < block_starty + block_height:
            if x > block_startx and x < block_startx + block_width or x + car_width > block_startx and x + car_width < block_startx + block_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
