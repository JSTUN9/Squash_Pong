# -*- coding:
import pygame
import pandas as pd
import math
import random
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

        if newx < BORDER + self.RADIUS: # collision with left side wall
            self.vx= -self.vx

        elif newy < BORDER + self.RADIUS or newy > HEIGHT - BORDER - self.RADIUS: # collision with top wall
            self.vy = -self.vy

        elif newx + Ball.RADIUS == WIDTH - Paddle.WIDTH and abs(newy-paddle.y) < Paddle.HEIGHT//2 : #collide with paddle
            if newx < WIDTH - Paddle.WIDTH//2 :
                angle = (self.y - paddle.y + paddle.HEIGHT//2 )/ Paddle.HEIGHT * - 90 + 225
                print (angle)
                self.vx = int(-VELOCITY*math.cos(Radians))
                self.vy = int(-VELOCITY*math.sin(Radians))


        elif newx - Ball.RADIUS > WIDTH + Ball.RADIUS*10: # reset game if passes line
            self.x = WIDTH-Paddle.WIDTH-Ball.RADIUS
            self.y = HEIGHT//2
            self.vx = -self.vx
            self.vy = -VELOCITY 
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

Angle = random.randint(-45,45)
Radians = math.radians(Angle)
print (Radians)
ballplay = Ball(WIDTH//2, HEIGHT//2, int(-VELOCITY*math.cos(Radians)), int(-VELOCITY*math.sin(Radians)))

    

# Draw the Scenario

pygame.init() 

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Squash Pong")

fgColor = pygame.Color("white")
bgColor = pygame.Color("black")

pygame.draw.rect(screen, fgColor, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

ballplay.show(fgColor)

paddle = Paddle(HEIGHT//2)
paddle.show(fgColor)

clock = pygame.time.Clock()




while True:
    e = pygame.event.poll() # closes game when press x
    if e.type == pygame.QUIT:
        break

    #pygame.time.delay(10)
    clock.tick(FRAMERATE)
    pygame.display.flip()

    paddle.update()
    ballplay.update() #always updating ball position

    #print ("{},{},{},{},{}".format(ballplay.x,ballplay.y,ballplay.vx,ballplay.vy,paddle.y), file = sample)
    
pygame.quit()
