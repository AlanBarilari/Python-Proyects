import pygame
from random import randint
import time

# Initializing Pygame
pygame.init()
 
w = 800 
h = 600 

# medidas 
cellSize = 50
gridwidth = int(w / cellSize)
gridheight = int(h / cellSize)

# Initializing surface
screen = pygame.display.set_mode((w, h))

# Initializing Color
white = (255,255,255)
black = (0,0,0)

# Direcciones 
UP = 0 
DOWN = 1
RIGHT = 2
LEFT = 3

def rect (color, x, y, thickness):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, cellSize, cellSize), thickness)

class Snake:
    def __init__(self):
       self.positions = [(3, 3)] 
       self.direction = RIGHT
       self.length = 3 

    def nextHead (self):
        currentHead = self.positions[0]
        x = currentHead[0]
        y = currentHead[1]
        if self.direction == RIGHT:
            newHead = (x + 1, y)
        elif self.direction == LEFT:
            newHead = (x - 1, y)
        elif self.direction == UP:
            newHead = (x, y - 1)
        elif self.direction == DOWN:
            newHead = (x, y + 1)
        return newHead

    def move (self):
        head = self.nextHead()   
        self.positions = [head] + self.positions 
        if len(self.positions) >= self.length + 1:
            self.positions.pop()
    
    def turn (self, dire):
        if dire != None:
            oldIsHorizontal =  (self.direction == RIGHT or self.direction == LEFT)
            oldIsVertical = (self.direction == UP or self.direction == DOWN) 
            newIsVertical = (dire == UP or dire == DOWN)
            newIsHorizontal = (dire == RIGHT or dire == LEFT)
            if oldIsHorizontal and newIsVertical:
                self.direction = dire
            elif oldIsVertical and newIsHorizontal:
                self.direction = dire 
    
    def selfCollision (self):
        head = self.positions[0]
        for i in range(len(self.positions)):
            pos = self.positions[i]
            if i != 0:
                if pos == head:
                    return True
        return False

def outOfBounds(x, y): 
    if x >= gridwidth or y >= gridheight:
        return True
    elif x < 0 or y < 0:
        return True
    else: 
        return False 

def randomPos ():
    x = randint(0, gridwidth - 1)
    y = randint(0, gridheight - 1)
    return (x, y)


def drawSnakeCell (x, y):
    if randint (0,1) == 0:
        snakeimg = perro1Img
    else:
        snakeimg = perro2Img
    screen.blit(snakeimg, (x * cellSize, y * cellSize))

def drawChickenCell (x, y): 

    screen.blit (chickenImg, (x * cellSize, y * cellSize))

#Controles
def getDirection ():
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return UP       
            elif event.key == pygame.K_DOWN:
                return DOWN
            elif event.key == pygame.K_RIGHT:
                return RIGHT
            elif event.key == pygame.K_LEFT:
                return LEFT
            return None    

def gameOver():
    font = pygame.font.SysFont(None, 100)
    img = font.render("NOMANNN ", True, (255,0,0))
    screen.blit(img, (110, 270))
    pygame.display.flip()
    time.sleep(3)

snake = Snake ()

delay = 0.15

chicken = randomPos()
 

perro1Img = pygame.image.load('files/perro1.jpg')
perro1Img = pygame.transform.scale(perro1Img, (cellSize, cellSize))
perro2Img = pygame.image.load('files/perro2.jpg')
perro2Img = pygame.transform.scale(perro2Img, (cellSize, cellSize))
chickenImg = pygame.image.load("files/pollo.png")   
chickenImg = pygame.transform.scale (chickenImg, (cellSize, cellSize))

# Score        
def score():
    font = pygame.font.SysFont(None, 100)
    img = font.render("Score: "+str(puntos), True, (255,255,255))
    screen.blit(img, (230, 500))      
puntos = 0

while True:
    
    screen.fill(black)
    score ()
    for pos in snake.positions:
        drawSnakeCell(pos[0], pos[1])
    direction = getDirection()
    #CambiarDireccion 
    snake.turn(direction)
    snake.move()    
    drawChickenCell(chicken[0], chicken[1])
    head = snake.positions[0]

    if outOfBounds(head[0], head[1]) or snake.selfCollision():
        gameOver()
        break   

    if head == chicken:
        snake.length = snake.length + 1
        puntos = puntos + 10
        chicken = randomPos()
        if snake.length == 6:
            delay = 0.10
        if snake.length == 13:
            delay = 0.05

    pygame.display.flip()
    time.sleep(delay)


    