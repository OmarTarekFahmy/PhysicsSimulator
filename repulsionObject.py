from settings import *
import math
import pygame

class RepulsionObject:

    def __init__(self, main):
        self.main = main
        self.strength = -GRAVITY_OBJECT_STRENGTH
        self.pos = pygame.mouse.get_pos()
        self.miniCircleList = [] #stores positions
        

    def update(self):
        pygame.draw.circle(self.main.screen, 'green', self.pos, 8)
        self.animate()

    def animate(self):
        
        self.animationTicks = self.main.ticks 
        print(self.animationTicks)
        for i in range(GRAV_OBJECT_MINI_CIRCLE_COUNT):
            
            miniCirclePos = (self.pos[0] + 20*math.cos(self.animationTicks/20 - (2*math.pi * i)/GRAV_OBJECT_MINI_CIRCLE_COUNT), self.pos[1] + 20*math.sin(self.animationTicks/20 - (2*math.pi * i)/GRAV_OBJECT_MINI_CIRCLE_COUNT))
            pygame.draw.circle(self.main.screen, 'dark green', miniCirclePos, 2)
        


