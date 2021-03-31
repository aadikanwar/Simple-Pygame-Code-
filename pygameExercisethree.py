"""
Aadi Kanwar
March 11, 2020 - The Race
This program is exercise three of pygame. There is a graphical race between an elephant and a car
"""
# importing pygame library
import pygame
# import math library for radians
import math

# initializing pygame
pygame.init()
# screen standards
windowWidth = 800
windowHeight = 600
screen = pygame.display.set_mode((windowWidth, windowHeight))

gameRunning = False
# coordinates for the clouds
x_pos = 0
x_posTwo = 0
x_posThree = 0
x_posFour = 0
y_pos = 80

# timing clock for animations
clock = pygame.time.Clock()

# establishing colour pallet
RED = (225, 0, 0)
BLUE = (0, 0, 128)
GREEN = (0, 225, 0)
PURPLE = (102, 0, 102)
YELLOW = (225, 225, 0)
BLACK = (0, 0, 0)
ORANGE = (225, 130, 0)
WHITE = (225, 225, 225)
LIGHTBLUE = (38, 186, 250)
BROWN = (102, 51, 0)
HOUSE = (102, 0, 0)
LIGHTBROWN = (115, 51, 0)
GREY = (160, 160, 160)
VIOLET = (102, 0, 204)
PINK = (255, 51, 255)
DARKGREY = (64, 64, 64)

# elephant png functions, parameters (size)
playerIMG = pygame.image.load("elephant (1).png")
playerX = 20
playerY = 525
speed = [4, 5]

# loading the image into my code
imgRect = playerIMG.get_rect()

# car png functions, parameters (size)
playerTwoIMG = pygame.image.load("baby-car.png")
playerTwoX = 10
playerTwoY = 485
speedTwo = [5, 5]


# function for the elephant png. NOTE - I use these functions so that I can call them within the loop and make it --
# look cleaner
def player():
    screen.blit(playerIMG, (playerX, playerY))


# function for the car png
def car(x, y):
    screen.blit(playerTwoIMG, (x, y))


# variable for changing of the x coordinate of the elephant

x_change = 0

# loop for keeping the game running
while not gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
            elif event.key == pygame.K_RIGHT:
                x_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    playerX += x_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY >= 390: # starting point for the elephant
        playerY = 390

    screen.fill(LIGHTBLUE)

    # drawing the rainbow
    start = math.radians(0)
    finish = math.radians(220)
    pygame.draw.arc(screen, RED, (328, 15, 600, 500), start, finish, 11)
    pygame.draw.arc(screen, ORANGE, (333, 25, 595, 508), start, finish, 11)
    pygame.draw.arc(screen, YELLOW, (338, 35, 590, 516), start, finish, 11)
    pygame.draw.arc(screen, GREEN, (343, 45, 585, 524), start, finish, 11)
    pygame.draw.arc(screen, BLUE, (348, 55, 580, 532), start, finish, 11)
    pygame.draw.arc(screen, VIOLET, (353, 65, 575, 540), start, finish, 11)
    pygame.draw.arc(screen, PINK, (358, 75, 570, 548), start, finish, 11)
    # making a ground
    pygame.draw.rect(screen, BROWN, [0, 230, 800, 400])
    # making the sun
    pygame.draw.circle(screen, YELLOW, [0, 0], 79)
    # rays of the sun
    pygame.draw.line(screen, YELLOW, (0, 0), (90, 80), 10)
    pygame.draw.line(screen, YELLOW, (0, 0), (40, 100), 10)
    pygame.draw.line(screen, YELLOW, (0, 0), (100, 40), 10)
    pygame.draw.line(screen, YELLOW, (0, 0), (110, 4), 10)
    pygame.draw.line(screen, YELLOW, (0, 0), (4, 110), 10)
    # making the pool first so I can overlap the body of the house
    pygame.draw.ellipse(screen, BLUE, [450, 235, 150, 50])
    # concentric ellipses for ripple effect in the pond
    for i in range(4):
        pygame.draw.ellipse(screen, WHITE, [(470 + i * 10), 246 + i * 1.5, 90 - i * 20, 27 - i * 3], 2)
    # making the house body
    pygame.draw.rect(screen, HOUSE, [542, 200, 200, 100])
    # making the roof of the house as a polygon
    pygame.draw.polygon(screen, BROWN, ((542, 200), (640, 160,), (742, 200,)))
    # creating the door of the house
    pygame.draw.rect(screen, LIGHTBROWN, [575, 250, 35, 51])
    # creating the doorknob of the door
    pygame.draw.circle(screen, BLACK, (601.6766, 281.5), 3)
    # creating the window
    pygame.draw.rect(screen, LIGHTBROWN, [680, 268, 15, 15], 2)
    pygame.draw.rect(screen, LIGHTBROWN, [698, 268, 15, 15], 2)
    pygame.draw.rect(screen, LIGHTBROWN, [680, 251, 15, 15], 2)
    pygame.draw.rect(screen, LIGHTBROWN, [698, 251, 15, 15], 2)
    # creating the "sidewalk"
    sidewalk = pygame.draw.rect(screen, GREY, [0, 325, 800, 50])
    for i in range(16):
        pygame.draw.rect(screen, BLACK, [0 + i * 50, 325, 50, 50], 1)
    # creating the road
    pygame.draw.rect(screen, BLACK, [0, 375, 800, 225])
    # creating the lines on the road
    pygame.draw.line(screen, YELLOW, (0, 480), (75, 480), 10)
    pygame.draw.line(screen, YELLOW, (150, 480), (225, 480), 10)
    pygame.draw.line(screen, YELLOW, (300, 480), (375, 480), 10)
    pygame.draw.line(screen, YELLOW, (450, 480), (525, 480), 10)
    pygame.draw.line(screen, YELLOW, (600, 480), (675, 480), 10)
    pygame.draw.line(screen, YELLOW, (750, 480), (800, 480), 10)
    # drawing the clouds
    pygame.draw.ellipse(screen, WHITE, [x_pos, y_pos, 200, 100])
    x_pos = x_pos + 1
    if x_pos == 800:
        x_pos = -250

    pygame.draw.ellipse(screen, WHITE, [x_posTwo, 65, 100, 50])
    x_posTwo = x_posTwo + 1
    if x_posTwo == 800:
        x_posTwo = -250

    pygame.draw.ellipse(screen, WHITE, [x_posThree, 100, 200, 100])
    x_posThree = x_posThree + 2
    if x_posThree == 800:
        x_posThree = -250

    pygame.draw.ellipse(screen, WHITE, [x_posThree, 165, 100, 50])
    x_posThree = x_posThree + 2
    if x_posThree == 800:
        x_posThree = -250

    # At a certain coordinate, the clouds become storm clouds
    if x_pos <= x_posThree:
        pygame.draw.ellipse(screen, DARKGREY, [x_pos, y_pos, 200, 100])
        pygame.draw.ellipse(screen, DARKGREY, [x_posThree, 100, 200, 100])
        pygame.draw.ellipse(screen, DARKGREY, [x_posTwo, 65, 100, 50])
        pygame.draw.ellipse(screen, DARKGREY, [x_posThree, 165, 100, 50])

    # GAME OVER Screen
    if playerTwoX < -120:
        playerTwoX = -300000
        playerY = -300
        screen.fill(LIGHTBLUE)
        font = pygame.font.SysFont("Impact", 100)
        textIMG = font.render("Car Won!", True, BLUE)
        screen.blit(textIMG, [215, 245])

    if playerX == 736:
        playerTwoX = -300
        playerTwoY = 300
        playerY = -300
        screen.fill(LIGHTBLUE)
        font = pygame.font.SysFont("Impact", 100)
        textIMG = font.render("Elephant Won!", True, BLUE)
        screen.blit(textIMG, [110, 230])

    # Car loop
    playerTwoX += 2.8
    if playerTwoX >= 800:
        playerTwoX = -128

    clock.tick(75)  # FPS in my entire program

    player()  # calling in the screen.blit def function that was created before the while loop was made
    car(playerTwoX, playerTwoY)  # calling in the screen.blit def function for the car
    # update code line
    pygame.display.flip()
pygame.quit()
