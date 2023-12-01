import pygame
from circle import *
from settings import *
from gravityObject import *
from repulsionObject import *

class main:

    def __init__(self):

        pygame.init()
        self.circleList = []
        self.gravObjectList = []
        self.repulObjectList = []
        
        self.screen = pygame.display.set_mode((800, 600))
        self.clicking = False
        self.optionsChanging = False
        self.rainbow = False
        self.drawingCircle = False
        self.alternateClick = False
        self.ticks = 0
        self.infoScreen = pygame.surface.Surface((150,50))
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        self.drawColor = 'white'
        self.size = 1
        self.clock = pygame.time.Clock()
        rect = pygame.rect.Rect(120, 55, 650, 500)
        pygame.draw.rect(self.screen, 'white', rect, 1)

        #Rainbow Colors

        self.violet = (148.0, 0.0, 211.0)
        self.indigo = (75.0, 0.0, 120.0)
        self.blue = (0.0, 0.0, 255.0)
        self.green = (0, 255, 0)
        self.yellow = (255, 255, 0)
        self.orange = (255, 127, 0)
        self.red = (255, 0, 0)

    def run(self):

        
        while True:
            pygame.display.set_caption(str(round(self.clock.get_fps(),0)))
            self.ticks+=1
            self.clock.tick(60)
            #self.cycleColor()
            self.takeInput()
            
            #self.draw()
            #self.drawCircle()
            #self.displayInfo()

            self.screen.fill('black')

            self.renderAll()
        
            pygame.display.update()
            
            
    def addCircle(self, xVelocity, yVelocity):
        self.circleList.append(Circle(self, xVelocity, yVelocity))
    def addGravObject(self):
        self.gravObjectList.append(GravityObject(self))
    def addRepulObject(self):
        self.repulObjectList.append(RepulsionObject(self))
    
    def renderAll(self):

        for circle in self.circleList:
                circle.update()
        for gravObject in self.gravObjectList:
            gravObject.update()
        for repulObject in self.repulObjectList:
            repulObject.update()
        
        pygame.draw.line(self.screen, 'white', (LINE_LEFT, LINE_TOP), (LINE_RIGHT,LINE_TOP), 5)
        pygame.draw.line(self.screen, 'white', (LINE_LEFT, LINE_BOTTOM), (LINE_RIGHT,LINE_BOTTOM), 5)
        pygame.draw.line(self.screen, 'white', (LINE_RIGHT, LINE_TOP-2), (LINE_RIGHT,LINE_BOTTOM+2), 5)
        pygame.draw.line(self.screen, 'white', (LINE_LEFT, LINE_TOP-2), (LINE_LEFT,LINE_BOTTOM+2), 5)

        if self.drawingCircle:
            pygame.draw.line(self.screen, 'green', self.initialMousePos, pygame.mouse.get_pos(), 1)

        


    def takeInput(self):

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:
                    self.clicking = True
                    self.drawingCircle = True
                    self.initialMousePos = pygame.mouse.get_pos()
                
                
                
            if event.type == pygame.MOUSEBUTTONUP:
                
                if event.button == 1:
                    self.addCircle(xVelocity = (pygame.mouse.get_pos()[0] - self.initialMousePos[0])*MOUSE_VELOCITY_FACTOR, yVelocity=(pygame.mouse.get_pos()[1] - self.initialMousePos[1])*MOUSE_VELOCITY_FACTOR)
                    self.clicking = False
                    self.drawingCircle = False
                if event.button == 3 and not self.alternateClick:
                    self.addGravObject()
                elif event.button == 3 and self.alternateClick:
                    self.addRepulObject()

                    


            #Color Keybinds

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    for circle in self.circleList:
                        circle.traceDict = []
                        circle.tracing = True

                if event.key == pygame.K_LCTRL:
                    self.circleList = []
                    self.gravObjectList = []
                    self.repulObjectList = []
                
                if event.key == pygame.K_RCTRL:
                    self.alternateClick = True

                if event.key == pygame.K_b and self.optionsChanging:
                    self.drawColor = 'blue'
                if event.key == pygame.K_r and self.optionsChanging:
                    self.drawColor = 'red'
                if event.key == pygame.K_g and self.optionsChanging:
                    self.drawColor = 'green'
                if event.key == pygame.K_y and self.optionsChanging:
                    self.drawColor = 'yellow'
                if event.key == pygame.K_w and self.optionsChanging:
                    self.drawColor = 'white'
                if event.key == pygame.K_q and self.optionsChanging:
                    self.rainbow = True
                if event.key == pygame.K_x and self.optionsChanging:
                    self.clearScreen()

                if event.key == pygame.K_1 and self.optionsChanging:
                    self.size = 1
                if event.key == pygame.K_2 and self.optionsChanging:
                    self.size = 2
                if event.key == pygame.K_3 and self.optionsChanging:
                    self.size = 3
                if event.key == pygame.K_4 and self.optionsChanging:
                    self.size = 4
                if event.key == pygame.K_5 and self.optionsChanging:
                    self.size = 5
                if event.key == pygame.K_6 and self.optionsChanging:
                    self.size = 6
                if event.key == pygame.K_7 and self.optionsChanging:
                    self.size = 7
                if event.key == pygame.K_8 and self.optionsChanging:
                    self.size = 8
                if event.key == pygame.K_9 and self.optionsChanging:
                    self.size = 9
                



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    for circle in self.circleList:
                        
                        circle.tracing = False

                if event.key == pygame.K_RCTRL:
                    self.alternateClick = False

    def explodeCircles(self):

        self.circleList.append(Circle(self, -EXPLODE_VELOCITY_FACTOR, -EXPLODE_VELOCITY_FACTOR, True))
        self.circleList.append(Circle(self, -EXPLODE_VELOCITY_FACTOR, EXPLODE_VELOCITY_FACTOR, True))
        self.circleList.append(Circle(self, EXPLODE_VELOCITY_FACTOR, -EXPLODE_VELOCITY_FACTOR, True))
        self.circleList.append(Circle(self, EXPLODE_VELOCITY_FACTOR, EXPLODE_VELOCITY_FACTOR, True))

        self.circleList.append(Circle(self, 0, -EXPLODE_VELOCITY_FACTOR, True))
        self.circleList.append(Circle(self, 0, EXPLODE_VELOCITY_FACTOR, True))
        self.circleList.append(Circle(self, EXPLODE_VELOCITY_FACTOR, 0, True))
        self.circleList.append(Circle(self, -EXPLODE_VELOCITY_FACTOR, 0, True))


app = main()

app.run()



    
