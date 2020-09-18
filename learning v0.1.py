
import random 
import pygame

pygame.init()

radius = 10
sizex = 5
sizey = 9

border = radius * 2

color = (225,225 , 225 )

if sizex > sizey or sizey == sizex:
    squaresize = int( ( 979 - 23) /(sizex)) - border
else:
    squaresize = int(1680 /(sizey )) - border

winxlength = (sizex - 1) * squaresize
winywidth = (sizey- 1) * squaresize
win = pygame.display.set_mode((winywidth + (radius * 2), winxlength + (radius * 2)))

brightness = 225
iterations = 5

lists = []

for x in range(0, sizey - 1):
    lists.append( 100 / sizey)

chosenlist = []

coloum = 0

run = True
while run:

    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for i in range( 0 , sizey):
        for x in range( 0 , sizex ):
            pygame.draw.circle( win , color, (i * squaresize + radius , x * squaresize + radius ), radius)

    vidot = random.randint(0, 100)

    checker = 0
    count = 0

    for x in lists:
        if vidot <= x + checker and vidot > checker:
            chosenlist.append(count - 1)

        else:
            checker += x


    if coloum == sizex - 1:
        coloum = 0
    else:
        coloum += 1
    
    
    pygame.display.update() 



