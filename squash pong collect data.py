# -*- coding:
import pygame
import pandas as pd

# Variables

WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 20
FRAMERATE = 40

# Define my Classes

class Ball:
    RADIUS = 20
    
    def __init__(self,x,y,vx,vy) :
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


    def show(self , colour):
    	global screen
    	pygame.draw.circle(screen, colour, (self.x, self.y), self.RADIUS)

    def update(self):
        global bgColor, fgColor

        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER + self.RADIUS:
            self.vx= -self.vx

        elif newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS:
            self.vy = -self.vy

        elif newx + Ball.RADIUS > WIDTH - Paddle.WIDTH and abs(newy-paddle.y) < paddle.HEIGHT//2 :
            self.vx = -self.vx

        elif newx - Ball.RADIUS > WIDTH + Ball.RADIUS*10:
            self.x = WIDTH-Paddle.WIDTH-Ball.RADIUS
            self.vx = -self.vx
            self.vy = VELOCITY
            self.y = HEIGHT//2
            paddle.y = HEIGHT//2
        else :
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgColor)


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__ (self, y):
        self.y = y

    def show(self, colour):
        global screen
        pygame.draw.rect(screen, colour, pygame.Rect(WIDTH - self.WIDTH, self.y-self.HEIGHT//2, self.WIDTH, self.HEIGHT))

    def update(self):
        newY = pygame.mouse.get_pos()[1]
        if newY-self.HEIGHT//2>BORDER \
        	and newY+self.HEIGHT//2<HEIGHT-BORDER :
        	self.show(bgColor)
        	self.y = newY
        	self.show(fgColor)

# Create objejcts 

ballplay = Ball(WIDTH-Paddle.WIDTH-Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)

    

# Draw the Scenario

pygame.init() 

screen = pygame.display.set_mode((WIDTH,HEIGHT))

fgColor = pygame.Color("white")
bgColor = pygame.Color("black")

pygame.draw.rect(screen, fgColor, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

ballplay.show(fgColor)

paddle = Paddle(HEIGHT//2)
paddle.show(fgColor)

clock = pygame.time.Clock()

sample = open ("game.csv","w")

print ("x,y,vx,vy,Paddle.y" , file = sample)




while True:
    e = pygame.event.poll() # closes game when press x
    if e.type == pygame.QUIT:
        break

    clock.tick(FRAMERATE)
    pygame.display.flip()

    
    paddle.update()
    ballplay.update() #always updating ball position

    print ("{},{},{},{},{}".format(ballplay.x,ballplay.y,ballplay.vx,ballplay.vy,paddle.y), file = sample)
    
pygame.quit()
