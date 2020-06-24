# -*- coding:
import pygame

# Variables

WIDTH = 1200
HEIGHT = 600
BORDER = 20

# Define my Classes

class Ball:
    RADIUS = 10
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Paddle:
    pass

# Create objejcts 

ballplay = Ball(WIDTH-Ball.RADIUS, HEIGHT/2)
    

# Draw the Scenario

pygame.init() 

screen = pygame.display.set_mode((WIDTH,HEIGHT))

fgColor = pygame.Color("white")

pygame.draw.rect(screen, fgColor, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT():
        break
        
pygame.quit()