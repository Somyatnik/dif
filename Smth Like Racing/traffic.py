imagesBus = [
pygame.image.load('busBlue.png'),
pygame.image.load('busRed.png')]

imagesCar = [
pygame.image.load('carOrange.png'),
pygame.image.load('carBlue.png'),
pygame.image.load('carGreen.png'),
pygame.image.load('carPurple.png')]

def globalRand()

def bus(xb,yb,images):
    gameDisplay.blit(random.choice(imagesBus),(xb,yb))

def cars(xc,yc):
    gameDisplay.blit(random.choice(imagesCar),(xc,yc))

tstartx_1 = random.randrange(9,140)
tstartx_2 = random.randrange(145,284)
tstartx_3 = random.randrange(310,457)
tstartx_4 = random.randrange(462,591)
tstarty = - 200
cars_width = 56
cars_height = 120
bus_width = 75
bus_height = 230
