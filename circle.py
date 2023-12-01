import pygame
import math
from settings import *

class Circle:

    def __init__(self, main, xVelocity, yVelocity, explode=False):

        self.main = main
        if not explode:
            self.pos = self.main.initialMousePos
        else:
            self.pos = pygame.mouse.get_pos()
        self.velocity = (xVelocity,yVelocity)
        self.bounces = 0
        self.stopped = False
        self.tracing = False
        self.traceDict = []
        

        if self.pos[1] > 565 and self.velocity[1] < 0.01:
            self.verticalCollisionCheck()
            self.velocity = (self.velocity[0], 0)
            self.stopped = True


    def verticalCollisionCheck(self):

        if self.pos[1] > LINE_BOTTOM - CIRCLE_RADIUS:
            self.velocity = (self.velocity[0] + -BOUNCE_FRICTION_ENERGY_LOSS*self.velocity[0], -self.velocity[1]*BOUNCE_ENERGY_LOSS_FACTOR)
            
            self.pos = (self.pos[0], LINE_BOTTOM-CIRCLE_RADIUS - 2)
            self.bounces += 1

        if self.pos[1] < LINE_TOP + CIRCLE_RADIUS:
            self.velocity = (self.velocity[0] + -BOUNCE_FRICTION_ENERGY_LOSS*self.velocity[0], -self.velocity[1])
            
            self.pos = (self.pos[0], LINE_TOP + CIRCLE_RADIUS + 2)

        
            
    def horizontalCollisionCheck(self):   

        if self.pos[0] < LINE_LEFT + CIRCLE_RADIUS:
            self.velocity = (-self.velocity[0], self.velocity[1] + -BOUNCE_FRICTION_ENERGY_LOSS*self.velocity[1])
            
            self.pos = (LINE_LEFT + CIRCLE_RADIUS + 2, self.pos[1])
        
        if self.pos[0] > LINE_RIGHT - CIRCLE_RADIUS:
            self.velocity = (-self.velocity[0], self.velocity[1] + -BOUNCE_FRICTION_ENERGY_LOSS*self.velocity[1])
            
            self.pos = (LINE_RIGHT - CIRCLE_RADIUS - 2, self.pos[1])     

    def stopContinuousBounce(self):
        #if 0 < self.velocity[1] < 0.00005 and 545 - CIRCLE_RADIUS < self.pos[1] < 550 - CIRCLE_RADIUS:
        #    self.velocity = (self.velocity[0], 0)
         #   self.pos = (self.pos[0], 550 - CIRCLE_RADIUS - 2)
         #   self.stopped = True

         if self.bounces == BOUNCES_TO_STOP:
            self.velocity = (self.velocity[0], 0)
            self.pos = (self.pos[0], LINE_BOTTOM - CIRCLE_RADIUS - 2)
            self.stopped = True

    def update(self):

        
        pygame.draw.circle(self.main.screen, 'white', self.pos, CIRCLE_RADIUS)
        self.traceDict.append(self.pos)

        if self.tracing:
            for i in range(len(self.traceDict)):
                if i != len(self.traceDict) - 1:
                    pygame.draw.line(self.main.screen, 'red', self.traceDict[i], self.traceDict[i+1])
        
        if not self.stopped:
            self.velocity = (self.velocity[0], self.velocity[1] + GRAVITY)
            self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])
            self.stopContinuousBounce()
            #self.verticalCollisionCheck()
            #self.horizontalCollisionCheck()
        else:
            self.velocity = (self.velocity[0] + -FRICTION_VELOCITY_FACTOR*self.velocity[0], self.velocity[1])
            self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])
            self.horizontalCollisionCheck()
        #self.checkCircleCollision()

        self.acceleration = [0,0]

        for gravObject in self.main.gravObjectList:
            direction = ((gravObject.pos[0] - self.pos[0])/ (self.dist(gravObject.pos, self.pos)), (gravObject.pos[1] - self.pos[1])/ (self.dist(gravObject.pos, self.pos))) 
            accelerationMagnitude = gravObject.strength/(self.dist(gravObject.pos, self.pos)**2)

            self.acceleration[0] += accelerationMagnitude*direction[0]
            self.acceleration[1] += accelerationMagnitude*direction[1]

            if abs(self.acceleration[0]) > ACCELERATION_CAP:
                if self.acceleration[0] < 0:
                    self.acceleration[0] = -ACCELERATION_CAP
                else:
                    self.acceleration[0] = ACCELERATION_CAP

            if abs(self.acceleration[1]) > ACCELERATION_CAP:
                if self.acceleration[1] < 0:
                    self.acceleration[1] = -ACCELERATION_CAP
                else:
                    self.acceleration[1] = ACCELERATION_CAP

        for repulObject in self.main.repulObjectList:
            direction = ((repulObject.pos[0] - self.pos[0])/ (self.dist(repulObject.pos, self.pos)), (repulObject.pos[1] - self.pos[1])/ (self.dist(repulObject.pos, self.pos))) 
            accelerationMagnitude = repulObject.strength/(self.dist(repulObject.pos, self.pos)**2)

            self.acceleration[0] += accelerationMagnitude*direction[0]
            self.acceleration[1] += accelerationMagnitude*direction[1]

            if abs(self.acceleration[0]) > ACCELERATION_CAP:
                if self.acceleration[0] < 0:
                    self.acceleration[0] = -ACCELERATION_CAP
                else:
                    self.acceleration[0] = ACCELERATION_CAP

            if abs(self.acceleration[1]) > ACCELERATION_CAP:
                if self.acceleration[1] < 0:
                    self.acceleration[1] = -ACCELERATION_CAP
                else:
                    self.acceleration[1] = ACCELERATION_CAP
        
        
        self.velocity = (self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1])

    def checkCircleCollision(self):

        for circle in self.main.circleList:

            if circle != self:

                if self.dist(self.pos, circle.pos) < CIRCLE_RADIUS + 5:
                    
                    self.velocity = (-self.velocity[0], -self.velocity[1] * BOUNCE_ENERGY_LOSS_FACTOR)
                    self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])

                    circle.velocity = (-circle.velocity[0], -circle.velocity[1] * BOUNCE_ENERGY_LOSS_FACTOR)
                    circle.pos = (circle.pos[0] + circle.velocity[0], circle.pos[1] + circle.velocity[1])


    def dist(self, pos1, pos2):

        return math.dist(pos1, pos2)