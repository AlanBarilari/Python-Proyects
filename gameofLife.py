# Importing the library
import pygame
import time
from random import randint

# Initializing Pygame
pygame.init()
 
w = 800 
h = 600 

# Initializing surface
surface = pygame.display.set_mode((w, h))
 
# Initializing Color
white = (255,255,255)
black = (0,0,0)

def rect (color, x, y, thickness):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, cellSize, cellSize), thickness)

# medidas 
cellSize = 10
gridwidth = int(w / cellSize)
gridheight = int(h / cellSize)

#gen
contador =  1 

def newGrid (): 
    grid = []
    for i in range(gridwidth):
        grid.append([])
        for j in range(gridheight): 
            grid[i].append (0) 
    return grid

def fillGridRandom (grid): 
    for i in range(gridwidth):
        for j in range(gridheight): 
            grid[i][j] = randint(0, 1)

grid = newGrid()

fillGridRandom (grid)

escWasPressed = False
while not escWasPressed:

    # dibujar grilla vacia
    for x in range(0, w, cellSize):
        for y in range(0, h, cellSize):
            rect(white, x, y, 2)

    # pintar cuadrados segun grid 
    for i in range(gridwidth):
        for j in range(gridheight):
            if grid[i][j] == 1:
                rect(white, i*cellSize, j*cellSize, 0)
            else:
                rect(black, i*cellSize, j*cellSize, 0)

    
    font = pygame.font.SysFont(None, 24)
    img = font.render("Generacion: "+ str(contador), True, (255,0,0))
    surface.blit(img, (20, 20))
    
    # next gen
    
    nextgen = newGrid()

    for i in range(gridwidth):
        for j in range(gridheight):
            vivos = 0   
            for ni in range(max(i - 1, 0), min(i + 2, gridwidth)):
                for nj in range(max(j - 1,0), min(j + 2, gridheight)): 
                    if grid[ni][nj] == 1:
                        vivos = vivos + 1
            vivos = vivos - grid[i][j]
            if grid[i][j] == 0 and vivos == 3: 
                nextgen[i][j] = 1 
            elif grid[i][j] == 1 and (vivos > 3 or vivos < 2): 
                nextgen[i][j] = 0 
            elif grid[i][j] == 1 and vivos < 4 and vivos > 1:
                nextgen[i][j] = 1
    
    grid = nextgen
    
    contador = contador + 1 
    
    # key activator
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                escWasPressed = True
    

    pygame.display.flip()
    time.sleep(0.1)
situacion = False
while situacion == False: 
    pass 
     
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                situacion = True