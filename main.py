import pygame

class main:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clicking = False
        self.optionsChanging = False
        self.rainbow = False
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
            self.ticks+=1
            self.clock.tick(1200)
            self.cycleColor()
            self.takeInput()
            self.draw()
            self.displayInfo()
            pygame.display.update()
            
            


    def takeInput(self):

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.clicking = True
                self.previousMousePos = pygame.mouse.get_pos()
                
            if event.type == pygame.MOUSEBUTTONUP:
                
               self.clicking = False

            #Color Keybinds

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    self.optionsChanging = True

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
                    self.optionsChanging = False

    

    def cycleColor(self):
        
        self.ticks = self.ticks % 700
        self.percentage = self.ticks%100
        if self.rainbow:
            if 0 < self.ticks < 100:
                self.color = ((self.indigo[0] - self.violet[0])* (self.percentage/100), (self.indigo[1] - self.violet[1])* (self.percentage/100), (self.indigo[2] - self.violet[2])* (self.percentage/100)) 
                self.color = (self.color[0] + self.violet[0], self.color[1] + self.violet[1], self.color[2] + self.violet[2])
            if 100 < self.ticks < 200:
                self.color = ((self.blue[0] - self.indigo[0])* (self.percentage/100), (self.blue[1] - self.indigo[1])* (self.percentage/100), (self.blue[2] - self.indigo[2])* (self.percentage/100)) 
                self.color = (self.color[0] + self.indigo[0], self.color[1] + self.indigo[1], self.color[2] + self.indigo[2])
            if 200 < self.ticks < 300:
                self.color = ((self.green[0] - self.blue[0])* (self.percentage/100), (self.green[1] - self.blue[1])* (self.percentage/100), (self.green[2] - self.blue[2])* (self.percentage/100)) 
                self.color = (self.color[0] + self.blue[0], self.color[1] + self.blue[1], self.color[2] + self.blue[2])
            if 300 < self.ticks < 400:
                self.color = ((self.yellow[0] - self.green[0])* (self.percentage/100), (self.yellow[1] - self.green[1])* (self.percentage/100), (self.yellow[2] - self.green[2])* (self.percentage/100)) 
                self.color = (self.color[0] + self.green[0], self.color[1] + self.green[1], self.color[2] + self.green[2])
            if 400 < self.ticks < 500:
                self.color = ((self.orange[0] - self.yellow[0])* (self.percentage/100), (self.orange[1] - self.yellow[1])* (self.percentage/100), (self.orange[2] - self.yellow[2])* (self.percentage/100)) 
                self.color = (self.color[0] + self.yellow[0], self.color[1] + self.yellow[1], self.color[2] + self.yellow[2])
            if 500 < self.ticks < 600:
                self.color = ((self.red[0] - self.orange[0])* (self.percentage/100), (self.red[1] - self.orange[1])* (self.percentage/100), (self.red[2] - self.orange[2])* (self.percentage/100)) 
                self.color = (self.color[0] + self.orange[0], self.color[1] + self.orange[1], self.color[2] + self.orange[2])
            if 600 < self.ticks < 700:
                self.color = ((self.violet[0] - self.red[0])* (self.percentage/100), (self.violet[1] - self.red[1])* (self.percentage/100), (self.violet[2] - self.red[2])* (self.percentage/100)) 
                self.color = (self.color[0] + self.red[0], self.color[1] + self.red[1], self.color[2] + self.red[2])

            self.drawColor = (self.color[0], self.color[1], self.color[2], 255)
            
    def draw(self):
        
        mousePos = pygame.mouse.get_pos()
        inBox = 120 < mousePos[0] < 120 + 650 and 55 < mousePos[1] < 55+550
        if not inBox:
            self.clicking = False

        if self.clicking and inBox:
            
            pygame.draw.line(self.screen, self.drawColor, self.previousMousePos, mousePos, self.size)
            self.previousMousePos = mousePos
            
    def displayInfo(self):
        if not self.rainbow:
            text = self.font.render("Color: " + self.drawColor, True, self.drawColor, 'black')
        else:
            text = self.font.render("Color: RAINBOW!!", True, self.drawColor, 'black')
        
        textRect = pygame.rect.Rect(60, 30, 60, 20)
        textRect.center = (31, 13)
        self.infoScreen.fill("black")
        self.infoScreen.blit(text, textRect)
        self.screen.blit(self.infoScreen, textRect)

    def clearScreen(self):
        self.screen.fill('black')
        rect = pygame.rect.Rect(120, 55, 650, 500)
        pygame.draw.rect(self.screen, 'white', rect, 1)


app = main()

app.run()



    
