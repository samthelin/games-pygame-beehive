GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (220, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

# Set up the player, bee, flower and honey data structure.
FPS = 40    # Controls the speed of the game in frames per second. 
honeyCollect = False   # Controls if honey is drawn to the screen and if it can be collected. 
honeyNumber = -1    # Controls the size of the honey list and which honey is being drawn. 
honeyTime = 0    # Controls for how long a honey remains on the screen (if not collected) and when the next one is drawn.
HONEYWIN = 20    # Controls number of honyes needed to win the game. 
HONEYSIZE = 8    # Controls the size of the honey
HONEYCYCLE = 250    # Controls how quickly the honeys are updated. They occur on the screen (when not collected) for 80 percent of this time. 
HONEYDURATION = 200
beeNumber = -1    # Controls which bee is entering the hive. 
beeTime = 0    # Controls the life cycle of the bees.
beeSpeedLimit = 2    # Controls the maximum speed of the bees. 
beeBuzz = 0    # Controls the buzzing phase of the bees.
BEEDURATION = 120    # Controls have often new bees are born. 
BEES = 40   # Controls the number of bees.
BEESIZE = 20    # Controls the size of the bees. 
BEEVARIANCE = 5    # Contols to what degree the size of the bees vary. 
BEESPEED = 1    # Controls the random component of the bees momevent.
PLAYERLIVES = 5   # Controls the number of lives the player is given at the start.PLAYERLIVES = 5   # Controls the number of lives the player is given at the start.
playerIn = False    # Controls if the player has entered the nest. 
playerLives = PLAYERLIVES   # Keeps track of the number of lives of the player.
playerHoney = 0    # Keeps track of the number of honeys collected by the player. 
playerBumbling = 1    # Controls the random component of the movement of the player. This is increased for the duration of an immunity phase, i.e. after a collision with a bee. 
playerImmune = 0    # Controls the immunity phase of the player, i.e. the phase directly after colliding with a bee. 
playerColor = GREEN    # Controls the colour of the player, which changes during the immunity phase.  
PLAYERSIZE = 25    # Controls the size of the player.
ENTRANCESIZE = 5    # Controls the size of the entrance to the beeHive.
entranceColor = BLUE    # Controls the colour of the entrance. 
TEXTCOLOR = YELLOW    #Controls the color of the text.
ENTRANCEX = 0.5 * (WINDOWWIDTH - ENTRANCESIZE) + 85    # Controls the x-coordinate of the entrance. 
ENTRANCEY = 0.5 * (WINDOWHEIGHT - ENTRANCESIZE) - 40     # Controls the y-coordinate of the entrance. 
FLOWERX = 100
FLOWERY = 100
FLOWERSIZE = 20
FLOWERCYCLE = 1000
FLOWERDURATION = 150
FLOWERIMMUNE = 400
flowerCollect = False
flowerNumber = -1
flowerTime = 0

# The background.
background = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT)

# A hole in the beeHive where the new bees climb inside.
entrance = pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE)

# The player is being implemented as a rectangle. 
player = pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE)

# The honeys are being kept in a list, that has a single entry to start and is then being added to. 
flowers = [pygame.Rect(random.randint(0, WINDOWWIDTH - FLOWERSIZE), random.randint(0, WINDOWHEIGHT - FLOWERSIZE), FLOWERSIZE, FLOWERSIZE)]

# The honeys are being kept in a list, that has a single entry to start and is then being added to. 
honeys = [pygame.Rect(random.randint(0, WINDOWWIDTH - HONEYSIZE), random.randint(0, WINDOWHEIGHT - HONEYSIZE), HONEYSIZE, HONEYSIZE)]

# The sizes of the bees is being kept in a list. This list is then used to create the bees.
beesizes = []
for i in range(BEES):
    beesizes.append(random.randint(BEESIZE - BEEVARIANCE, BEESIZE + BEEVARIANCE))

# Each bee is a dictionary with entries a rectangle representing the bee, a colour, and two speed parameters. These dictionaries are being stored in a list. 
bees = []
for i in range(BEES):
    bees.append({'rect': pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE),
                 'color':BLACK,'speedDown': 0, 'speedRight': 0, 'beeBorn': False, 'beeIn': False })

# Loading and stretching the player image.
playerImage = pygame.image.load('beesprite.png')
playerStretchedImage = pygame.transform.scale(playerImage, (ENTRANCESIZE, ENTRANCESIZE))

# Loading and stretching the background image.
backgroundImage = pygame.image.load('hive2.png')
backgroundStretchedImage = pygame.transform.scale(backgroundImage, (WINDOWWIDTH, WINDOWHEIGHT))

# Set up movement variables for the player.
moveLeft = 0
moveRight = 0
moveUp = 0
moveDown = 0
 
# Set up parameters controlling the speed of the player. MAXSPEED, ACCELERATION AND DECELERATION are multiplied with the SPEEDFACTOR to obtain the actual values (this is to
# avoid trouble with the player not coming to rest because of floating numbers not evaluating to zero. 
MOVESPEED = 1
MAXSPEED = 120
ACCELERATION = 8
DECELERATION = 2
SPEEDFACTOR = 0.1

# Set the font.
font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 24)

# Define a function that checks if two circular bees have collided.
def circleCollision(rect1, rect2):
    v1 = pygame.math.Vector2(rect1.centerx, rect1.centery)
    v2 = pygame.math.Vector2(rect2.centerx, rect2.centery)
    dist = v2.distance_to(v1)
    if dist < 0.5 * (rect1.width + rect2.width):
        return True
    else:
        return False

# Define a function writing text on the board.
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Define a function asking the player to press a button to continue.
def waitForPlayerToPressKey():
    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return

# Define a function that resets all the necessary parameters in order to be able to restart the game.
def resetParameters():
    honeyCollect = False   
    honeyNumber = -1    
    honeyTime = 0    
    beeNumber = -1    
    beeTime = 0    
    beeSpeedLimit = 2    
    beeBuzz = 0    
    playerIn = False    
    playerLives = PLAYERLIVES   
    playerHoney = 0    
    playerBumbling = 1    
    playerImmune = 0    
    playerColor = GREEN
    flowerCollect = False
    flowerNumber = -1
    flowerTime = 0
    player = pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE)
    honeys = [pygame.Rect(random.randint(0, WINDOWWIDTH - HONEYSIZE), random.randint(0, WINDOWHEIGHT - HONEYSIZE), HONEYSIZE, HONEYSIZE)]
    beesizes = []
    for i in range(BEES):
        beesizes.append(random.randint(BEESIZE - BEEVARIANCE, BEESIZE + BEEVARIANCE))
    bees = []
    for i in range(BEES):
        bees.append({'rect': pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE),
                 'color':BLACK,'speedDown': 0, 'speedRight': 0, 'beeBorn': False, 'beeIn': False })
    playerStretchedImage = pygame.transform.scale(playerImage, (ENTRANCESIZE, ENTRANCESIZE))
    moveLeft = 0
    moveRight = 0
    moveUp = 0
    moveDown = 0
    return


# Import the background music.
pygame.mixer.music.load('beeBuzz2.wav')
pygame.mixer.music.play(-1, 0.0)           
        
#### Draw the start screen
windowSurface.blit(backgroundStretchedImage, background)
drawText('Welcome to Beehive!', font, windowSurface, WINDOWWIDTH/4 + 20, WINDOWHEIGHT/2)
drawText('Press Esc to quit, and any other key to enter.', font2, windowSurface, WINDOWWIDTH/4 + 20, WINDOWHEIGHT/2 + 30)
pygame.display.update()
waitForPlayerToPressKey()


#### Start the game. ####

# Run the game loop.
while True:

    
    #### Checking if the game is over.  ####

    
    # Checking if the player has collected enough honey and thus won the game. 
    if playerHoney == HONEYWIN:
        drawText('You Win!', font, windowSurface, WINDOWWIDTH/4 + 120, WINDOWHEIGHT/2)
        drawText('Press Esc to quit, and any other key to play again.', font2, windowSurface, WINDOWWIDTH/4 + 20, WINDOWHEIGHT/2 + 30)
        pygame.display.update()
        waitForPlayerToPressKey()
        honeyCollect = False   
        honeyNumber = -1    
        honeyTime = 0    
        beeNumber = -1    
        beeTime = 0    
        beeSpeedLimit = 2    
        beeBuzz = 0    
        playerIn = False    
        playerLives = PLAYERLIVES   
        playerHoney = 0    
        playerBumbling = 1    
        playerImmune = 0    
        playerColor = GREEN
        flowerCollect = False
        flowerNumber = -1
        flowerTime = 0
        player = pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE)
        flowers = [pygame.Rect(random.randint(0, WINDOWWIDTH - FLOWERSIZE), random.randint(0, WINDOWHEIGHT - FLOWERSIZE), FLOWERSIZE, FLOWERSIZE)]
        honeys = [pygame.Rect(random.randint(0, WINDOWWIDTH - HONEYSIZE), random.randint(0, WINDOWHEIGHT - HONEYSIZE), HONEYSIZE, HONEYSIZE)]
        beesizes = []
        for i in range(BEES):
            beesizes.append(random.randint(BEESIZE - BEEVARIANCE, BEESIZE + BEEVARIANCE))
        bees = []
        for i in range(BEES):
            bees.append({'rect': pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE),
                     'color':BLACK,'speedDown': 0, 'speedRight': 0, 'beeBorn': False, 'beeIn': False })
        playerStretchedImage = pygame.transform.scale(playerImage, (ENTRANCESIZE, ENTRANCESIZE))
        moveLeft = 0
        moveRight = 0
        moveUp = 0
        moveDown = 0 
        
    
    # Checking if the player has got any live left. If not, the game is lost. 
    if playerLives == 0:
        drawText('You Lose!', font, windowSurface, WINDOWWIDTH/4 + 120, WINDOWHEIGHT/2)
        drawText('Press Esc to quit, and any other key to play again.', font2, windowSurface, WINDOWWIDTH/4 + 20, WINDOWHEIGHT/2 + 30)
        pygame.display.update()
        waitForPlayerToPressKey()
        resetParameters()
        honeyCollect = False   
        honeyNumber = -1    
        honeyTime = 0    
        beeNumber = -1    
        beeTime = 0    
        beeSpeedLimit = 2    
        beeBuzz = 0    
        playerIn = False    
        playerLives = PLAYERLIVES   
        playerHoney = 0    
        playerBumbling = 1    
        playerImmune = 0    
        playerColor = GREEN
        flowerCollect = False
        flowerNumber = -1
        flowerTime = 0
        player = pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE)
        flowers = [pygame.Rect(random.randint(0, WINDOWWIDTH - FLOWERSIZE), random.randint(0, WINDOWHEIGHT - FLOWERSIZE), FLOWERSIZE, FLOWERSIZE)]
        honeys = [pygame.Rect(random.randint(0, WINDOWWIDTH - HONEYSIZE), random.randint(0, WINDOWHEIGHT - HONEYSIZE), HONEYSIZE, HONEYSIZE)]
        beesizes = []
        for i in range(BEES):
            beesizes.append(random.randint(BEESIZE - BEEVARIANCE, BEESIZE + BEEVARIANCE))
        bees = []
        for i in range(BEES):
            bees.append({'rect': pygame.Rect(ENTRANCEX, ENTRANCEY, ENTRANCESIZE, ENTRANCESIZE),
                     'color':BLACK,'speedDown': 0, 'speedRight': 0, 'beeBorn': False, 'beeIn': False })
        playerStretchedImage = pygame.transform.scale(playerImage, (ENTRANCESIZE, ENTRANCESIZE))
        moveLeft = 0
        moveRight = 0
        moveUp = 0
        moveDown = 0 
        
    
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #### Adjust the honey data. ####


    # Run the honey timer
    if honeyTime < HONEYCYCLE:
        honeyTime += 1
    else:
        honeyTime = 0

    # Remove the expired honey
    if honeyTime == 0:
        honeyCollect = False

    # Increase the honey number and add an extra honey to the honey list
    if honeyTime == HONEYCYCLE - HONEYDURATION:
        honeyCollect = True
        honeyNumber += 1
        honeys.append(pygame.Rect(random.randint(0, WINDOWWIDTH - HONEYSIZE), random.randint(0, WINDOWHEIGHT - HONEYSIZE), HONEYSIZE, HONEYSIZE))


    #### Adjust the flower data. ####


    # Run the flower timer
    if flowerTime < FLOWERCYCLE:
        flowerTime += 1
    else:
        flowerTime = 0

    # Remove the expired honey
    if flowerTime == 0:
        flowerCollect = False

    # Increase the honey number and add an extra honey to the honey list
    if flowerTime == FLOWERCYCLE - FLOWERDURATION:
        flowerCollect = True
        flowerNumber += 1
        flowers.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FLOWERSIZE), random.randint(0, WINDOWHEIGHT - FLOWERSIZE), FLOWERSIZE, FLOWERSIZE))
    

    #### Adjust the bee data. ####


    # Run the bee timer:
    if beeTime < BEEDURATION:
        beeTime += 1
    else:
        beeTime = 0

    # Increase the bee number and have the corresponding bee be born.
    if beeTime == int(0.6 * BEEDURATION) and beeNumber < BEES - 1:
        beeNumber += 1
        bees[beeNumber]['beeBorn'] = True

    # Have the bee that has been born enter the hive.
    if bees[beeNumber]['beeBorn'] == True:
        if bees[beeNumber]['rect'].width < beesizes[beeNumber]:
            bees[beeNumber]['rect'].width += 1
            bees[beeNumber]['rect'].height += 1
            (bees[beeNumber]['rect'].centerx, bees[beeNumber]['rect'].centery)  = (entrance.centerx, entrance.centery)
        else:
            bees[beeNumber]['beeIn'] = True

    
    # Controlling the buzz of the bees. When the bees are buzzing, their maximum speed increases. The bees all start buzzing when the player collides with one of them. 
    if beeBuzz > 0:
        beeSpeedLimit = 10
        beeBuzz -= 1
    else:
        beeSpeedLimit = 2
        playerBumbling = 1

    # Changing the speed of the bees and then moving them.

    # First we check if any of the bees have surpassed the speed limit. In this case, they are slowed down. Else their speed is set at random. This is only done for the bees that
    # are already in the hive. 
    for bee in bees:
        if bee['beeIn']:
            if bee['speedDown'] > beeSpeedLimit:
                bee['speedDown'] += random.randint(-BEESPEED, 0)
            elif bee['speedDown'] < -beeSpeedLimit:
                bee['speedDown'] += random.randint(0, BEESPEED)
            else:
                bee['speedDown'] += random.randint(-BEESPEED, BEESPEED)

            if bee['speedRight'] >beeSpeedLimit :
                bee['speedRight'] += random.randint(-BEESPEED, 0)
            elif bee['speedRight'] < -beeSpeedLimit:
                bee['speedRight'] += random.randint(0, BEESPEED)
            else:
                bee['speedRight'] += random.randint(-BEESPEED, BEESPEED)
            
            # After the speed of all the bees has been set, the bees are being moved correspondingly. 

            if (bee['rect'].top > 0 or bee['speedDown'] > 0) and (bee['rect'].bottom < WINDOWHEIGHT or bee['speedDown'] < 0):
                bee['rect'].top += bee['speedDown']
            else:
                bee['speedDown'] = - bee['speedDown']
                bee['rect'].top += bee['speedDown']

            
            if (bee['rect'].left > 0 or bee['speedRight'] > 0) and (bee['rect'].right < WINDOWWIDTH or bee['speedRight'] < 0):
                bee['rect'].right += bee['speedRight']
            else:
                bee['speedRight'] = - bee['speedRight']
                bee['rect'].right += bee['speedRight']
            


    #### Adjust the player data. ####

    # Let the player enter the hive.
    if player.width < PLAYERSIZE:
        player.width += 1
        player.height += 1
        (player.centerx, player.centery) = (entrance.centerx, entrance.centery)
        playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
    else:
        playerIn = True


    # Controlling the immunity of the player. The player is immune directly after it has collided with one of the bees. 
    if playerImmune > 0:
        playerImmune -= 1

    # Setting the player colour. The player is blinking during the phase of immunity. 
    x = playerImmune
    if (0 <= x < 10) or (20 <= x < 30) or (40 <= x < 50) or (60 <= x < 70) or (80 <= x < 90):
        playerColor = GREEN
    else:
        playerColor = RED
   
    # The player is being moved through checking if keys are being held down. This gives the list of the pressed-down keys. 
    keys = pygame.key.get_pressed()

    # Moving the player at variable speed. If the corresponding key is pressed down, the player accelerates until it has reached the speed limit. 
    if playerIn: 
        if keys[pygame.K_UP]:
            if moveUp < MAXSPEED:
                moveUp += ACCELERATION
        if keys[pygame.K_DOWN]:
            if moveDown < MAXSPEED:
                moveDown += ACCELERATION
        if keys[pygame.K_LEFT]:
            if moveLeft < MAXSPEED:
                moveLeft += ACCELERATION
        if keys[pygame.K_RIGHT]:
            if moveRight < MAXSPEED:
                moveRight += ACCELERATION

    # If a key is not held down anymore, the player decelerates (but does not come to an immediate standstill - a certain drag or delay is built into the system). 
    if playerIn:
        if not keys[pygame.K_UP]:
            if moveUp > 0:
                moveUp -= DECELERATION
        if not keys[pygame.K_DOWN]:
            if moveDown > 0:
                moveDown -= DECELERATION
        if not keys[pygame.K_LEFT]:
            if moveLeft > 0:
                moveLeft -= DECELERATION
        if not keys[pygame.K_RIGHT]:
            if moveRight > 0:
                moveRight -= DECELERATION

    # Check if the player is out of bounds. If this is the case, the speed (that was set above) is set to zero in the relevant direction. 
    if player.bottom > WINDOWHEIGHT:
        moveDown = 0
    if player.top < 0:
        moveUp = 0
    if player.left < 0:
        moveLeft = 0
    if player.right > WINDOWWIDTH:
        moveRight = 0
        
    # After the speed of the player has been set above, the player is actually moved. The Move parameters are integersm, and we use the speed factor to ensure not having
    # problems with floating numbers not evaluating to exactly zero. 
    moveHor = (moveRight - moveLeft) * SPEEDFACTOR
    moveVer = (moveDown - moveUp) * SPEEDFACTOR

    # Move the player.
    if playerIn:
        player.top += moveVer + random.randint(-playerBumbling, playerBumbling)
        player.right += moveHor + random.randint(-playerBumbling, playerBumbling)


    #### Checking for collisions. ####

    # Check if the player has intersected with any bees. If this is the case, and the player is not immune, the bees start moving mor quickly, the player obtains immunity,
    # the player starts moving more erratically (playerBumbling is increased) and the numer of lives go down. This all only applies to bee in the hive. 
    for bee in bees:
        if bee['beeIn'] and playerIn:
            if circleCollision(player, bee['rect']) and playerImmune == 0:
                playerBumbling = 3
                beeBuzz = 200
                playerImmune = 100
                playerLives -= 1

    # Check if the player has collected any honey. If the player collides with a honey, the honey disapperas of the screen and the parameter counting the number of honey collected
    # increases by one. honeyCollect is set to false so that the honey is no more drawn on the screen and can no more be collected. 
    if circleCollision(player, honeys[honeyNumber]) and honeyCollect:
        honeyCollect = False
        playerHoney += 1
        honeyTime = 0

    # Check if the player has collected any honey. If the player collides with a honey, the honey disapperas of the screen and the parameter counting the number of honey collected
    # increases by one. honeyCollect is set to false so that the honey is no more drawn on the screen and can no more be collected. 
    if circleCollision(player, flowers[flowerNumber]) and flowerCollect:
        flowerCollect = False
        playerImmune = FLOWERIMMUNE
        flowerTime = 0 
        

    #### Draw all the components. ####
        

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Draw the background. 
    windowSurface.blit(backgroundStretchedImage, background)

    # Draw the flower.
    if flowerCollect:
        pygame.draw.circle(windowSurface, PINK, (flowers[flowerNumber].centerx, flowers[flowerNumber].centery), int(flowers[flowerNumber].width / 2), 0)
        pygame.draw.circle(windowSurface, BLUE, (flowers[flowerNumber].centerx, flowers[flowerNumber].centery), int(flowers[flowerNumber].width / 6), 0)
        #pygame.draw.rect(windowSurface, PINK, flower)

    # Draw the text on the screen keeping track of the number of lives and honeys the player has collected.
    drawText('Honey: %s / %s ' % (playerHoney, HONEYWIN), font2, windowSurface, 30, 30)
    drawText('Lives: %s ' % (playerLives), font2, windowSurface, 30, 50)
    
    # Draw the entrance onto the surface.
    #pygame.draw.rect(windowSurface, entranceColor, entrance)
    pygame.draw.circle(windowSurface, entranceColor, (entrance.centerx, entrance.centery), int(entrance.width / 2), 0)

    # Draw the player image onto the player.
  #  windowSurface.blit(playerStretchedImage, player)

    # Draw the player onto the surface.
    #pygame.draw.rect(windowSurface, playerColor, player)
    flap = random.randint(0, 1)
    pygame.draw.circle(windowSurface, playerColor, (player.centerx, player.centery), int(player.width / 2) + flap, 0)
    pygame.draw.circle(windowSurface, BLACK, (player.centerx, player.centery), int(player.width / 4) + flap, 0)
    pygame.draw.circle(windowSurface, playerColor, (player.centerx, player.centery), int(player.width / 10) + flap, 0)
        
    # Draw the relevant honey in the honey list. This is only drawn if the honeyCollect parameter is True. 
    if honeyCollect:
        #pygame.draw.rect(windowSurface, GREEN, honeys[honeyNumber])
        x = honeys[honeyNumber].centerx
        y = honeys[honeyNumber].centery
        radius = (1 / math.sqrt(2)) * honeys[honeyNumber].width
        pygame.draw.polygon(windowSurface, YELLOW,
                            ((int(x + radius * math.cos(0)),
                              int(y + radius * math.sin(0))),
                             (int(x + radius * math.cos(math.pi / 3)),
                              int(y + radius * math.sin(math.pi / 3))),
                             (int(x + radius * math.cos(2 * math.pi / 3)),
                              int(y + radius * math.sin(2 * math.pi / 3))),
                             (int(x + radius * math.cos(3 * math.pi / 3)),
                              int(y + radius * math.sin(3 * math.pi / 3))),
                             (int(x + radius * math.cos(4 * math.pi / 3)),
                              int(y + radius * math.sin(4 * math.pi / 3))),
                             (int(x + radius * math.cos(5 * math.pi / 3)),
                              int(y + radius * math.sin(5 * math.pi / 3)))),
                            0)
                             
    # Draw the bees that have been born. 
    for bee in bees:
        if bee['beeBorn']:
            flap = random.randint(0, 1)
            pygame.draw.circle(windowSurface, bee['color'], (bee['rect'].centerx, bee['rect'].centery), int(bee['rect'].width / 2) + flap, 0)
            pygame.draw.circle(windowSurface, YELLOW, (bee['rect'].centerx, bee['rect'].centery), int(bee['rect'].width / 3) + flap , 0)
            pygame.draw.circle(windowSurface, bee['color'], (bee['rect'].centerx, bee['rect'].centery), int(bee['rect'].width / 10) + flap, 0)
            

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(FPS)
