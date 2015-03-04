import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound('crash.wav')
pygame.mixer.music.load('All_My_Shuffling.wav')

display_width = 600
display_height = 500

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 56
car_height = 111

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Smth Like Racing')
clock = pygame.time.Clock()

roadImg = pygame.image.load('road.png')
wallImg = pygame.image.load('wall.png')
carImg = pygame.image.load('car.png')
gameIcon = pygame.image.load('caricon.png')
pygame.display.set_icon(gameIcon)

pause = False

def walls_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (15,0))

def wall(xw,yw):
    gameDisplay.blit(wallImg,(xw,yw))

def road(xr,yr):
    gameDisplay.blit(roadImg,(xr,yr))
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects('You Crashed', largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button('Replay',120,325,75,40,green,bright_green,game_loop)
        button('Quit',405,325,75,40,red,bright_red,quitgame)
                      
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

    smallText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w/2)),(y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects('Paused', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Continue',120,325,75,40,green,bright_green,unpause)
        button('Quit',405,325,75,40,red,bright_red,quitgame)
                      
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
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects('A bit Racey', largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('GO!',120,325,75,40,green,bright_green,game_loop)
        button('Quit',405,325,75,40,red,bright_red,quitgame)
                      
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0

    dodged = 0

    speed_y = 5
    speed_x = 5

    border = 15

    wall_starty = -200
    wall_width = 110
    wall_height = 83
    wall_startx = random.randrange(border,display_width-wall_width-border)

    road_starty = -125
    road_height = 125
    
    #wall_count + 1     как это сделать?

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = - speed_x
                if event.key == pygame.K_RIGHT:
                    x_change = speed_x
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0
          
        x += x_change

        road(0,road_starty)
        road_starty += speed_y

        shift = 0
        while road_starty + shift < display_height:
            road(0, road_starty + shift)
            shift += road_height

        if road_starty > 0:
            road_starty -= road_height
       
        wall(wall_startx,wall_starty)
        wall_starty += speed_y
        
        car(x,y)
        
        walls_dodged(dodged)

        if x > display_width - car_width or x == 0:
            crash()

        if wall_starty > display_height:
            wall_starty = 0 - wall_height
            wall_startx = random.randrange(border,display_width-wall_width-border)
            dodged += 1
            #wall_speed += 1
            
        if y < wall_starty + wall_height and y > wall_starty or y + car_height > wall_starty and y + car_height < wall_starty + wall_height:
            if x > wall_startx and x < wall_startx + wall_width or x + car_width > wall_startx and x + car_width < wall_startx + wall_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
