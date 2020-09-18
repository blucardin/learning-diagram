import random 
import pygame

pygame.init()

radius = 10
sizex = 5
sizey = 9

color = (225,225 , 225 )

if sizex > sizey or sizey == sizex:
    squaresize = int( ( 979 - 23) /(sizex)) - radius * 2
else:
    squaresize = int(1680 /(sizey )) - radius * 2

winxlength = (sizex - 1) * squaresize
winywidth = (sizey- 1) * squaresize
win = pygame.display.set_mode((winywidth + (radius * 2), winxlength + (radius * 2)))

run = True
while run:

    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    for i in range( 0 , sizey):
        for x in range( 0 , sizex ):
            pygame.draw.circle( win , color, (i * squaresize + radius , x * squaresize + radius ), radius)
    
    pygame.display.update() 



