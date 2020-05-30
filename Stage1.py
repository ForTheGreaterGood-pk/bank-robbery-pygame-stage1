import pygame

pygame.init()

display_width = 1000
display_height = 700
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("zimaH the Deceiver")

walkRight=[pygame.image.load('R1.png'), # 1 image will be shown for 3 frames
           pygame.image.load('R2.png'),# so total of 27 frames per second
           pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),
           pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),
           pygame.image.load('R9.png')]

walkLeft=[pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),
          pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),
          pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]

EwalkRight=[pygame.image.load('R1E.png'),#Total 8 images
           pygame.image.load('R2E.png'),#1 image will be shown for 3 frames#so total 28fps
           pygame.image.load('R3E.png'),pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),
           pygame.image.load('R6E.png'),pygame.image.load('R7E.png'),pygame.image.load('R8E.png')]

EwalkLeft=[pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),
          pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),
          pygame.image.load('L7E.png'),pygame.image.load('L8E.png')]

bg_level1=pygame.image.load('background.jpg')
bg_level1=pygame.transform.scale(bg_level1,(1000,700))
char_r=pygame.transform.scale(pygame.image.load('standing.png'),(80,80))
char_l=pygame.transform.scale(pygame.image.load('standingleft.png'),(80,80))


class Zimah_level1:
    def __init__(self):
        self.x=38
        self.y=50
        self.vel=2
        self.walkCount=0
        self.left=False
        self.right=False
        self.standing=True

    def character(self,win):
        if self.walkCount+1>27:
            self.walkCount=0

        if not self.standing:
            if self.left:
                win.blit(pygame.transform.scale(walkLeft[self.walkCount//3],(80,80)),(self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(pygame.transform.scale(walkRight[self.walkCount // 3], (80, 80)), (self.x, self.y))
                self.walkCount+=1
        else:
            if self.left:
                win.blit(char_l,(self.x,self.y))
            else:
                win.blit(char_r, (self.x, self.y))

        pygame.display.update()


class Enemy_level1:
    def __init__(self,x,y,width,height,end,vel):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x,self.end]
        self.walkCount=0
        self.vel=vel

    def draw(self,win):
        self.move()
        if self.walkCount+1>24:
            self.walkCount=0

        if self.vel>0:
            win.blit(pygame.transform.scale(EwalkRight[self.walkCount // 3],
                     (self.width, self.height)),(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(pygame.transform.scale(EwalkLeft[self.walkCount // 3],
                                            (self.width, self.height)), (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.vel>0:
            if self.x +self.vel<self.path[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkCount=0

        else:
            if self.x-self.vel>self.path[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkCount=0



class Stage1:
    player=Zimah_level1()
    enemy1 =Enemy_level1(360,50,80,80,770,2)
    enemy2 =Enemy_level1(370,190,80,80,600,2)
    enemy3 =Enemy_level1(190,330,80,80,600,2)
    enemy4 =Enemy_level1(680,330,80,80,930,2)
    enemy5 =Enemy_level1(350,470,80,80,780,2)

    def wall(self):
        if self.player.y == 50 and self.player.x >=760:
            self.player.x=760
        if self.player.y == 190 and self.player.x >=590:
            self.player.x=590
        if self.player.y == 330 and self.player.x >=590:
            self.player.x=590
        if self.player.y == 470 and self.player.x >=770:
            self.player.x=770


    def stairs(self):
        keys=pygame.key.get_pressed()
        if self.player.x in range(520,580) and self.player.y == 50:
            if keys[pygame.K_DOWN]:
                self.player.y = 190

        if self.player.x in range(520,580) and self.player.y == 190:
            if keys[pygame.K_UP]:
                self.player.y = 50

        if self.player.x in range(20,80) and self.player.y == 190:
            if keys[pygame.K_DOWN]:
                self.player.y = 330

        if self.player.x in range(20,80) and self.player.y == 330:
            if keys[pygame.K_UP]:
                self.player.y = 190

        if self.player.x in range(360,420) and self.player.y == 330:
            if keys[pygame.K_DOWN]:
                self.player.y = 470

        if self.player.x in range(360,420) and self.player.y == 470:
            if keys[pygame.K_UP]:
                self.player.y = 330



    def enemies(self):
        #here we will check for collisions

        if self.player.x +5 > self.enemy1.x -5 and self.player.x -5<self.enemy1.x +5:
            if self.player.y+5>self.enemy1.y-5 and self.player.y -5<self.enemy1.y +5:
                self.player.x=38
                self.player.y=50

        if self.player.x +5 > self.enemy2.x -5 and self.player.x -5<self.enemy2.x +5:
            if self.player.y+5>self.enemy2.y-5 and self.player.y -5<self.enemy2.y +5:
                self.player.x=38
                self.player.y=50

        if self.player.x +5 > self.enemy3.x -5 and self.player.x -5<self.enemy3.x +5:
            if self.player.y+5>self.enemy3.y-5 and self.player.y -5<self.enemy3.y +5:
                self.player.x=38
                self.player.y=50

        if self.player.x +5 > self.enemy4.x -5 and self.player.x -5<self.enemy4.x +5:
            if self.player.y+5>self.enemy4.y-5 and self.player.y -5<self.enemy4.y +5:
                self.player.x=38
                self.player.y=50

        if self.player.x +5 > self.enemy5.x -5 and self.player.x -5<self.enemy5.x +5:
            if self.player.y+5>self.enemy5.y-5 and self.player.y -5<self.enemy5.y +5:
                self.player.x=38
                self.player.y=50


    def drawings_level1(self):
        self.player.character(win)
        win.blit(bg_level1,(0,0))
        self.enemy1.draw(win)
        self.enemy2.draw(win)
        self.enemy3.draw(win)
        self.enemy4.draw(win)
        self.enemy5.draw(win)


    def level1(self):
        run =True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run =False
                    break

            keys = pygame.key.get_pressed()

            self.wall()
            self.stairs()
            self.enemies()

############################Showing passing throught gate effect####################################
            if self.player.x in range(260,300) and self.player.y == 50:
                self.player.x =330

            if self.player.x in range(300,330) and self.player.y == 50:
                self.player.x =260

            if self.player.x in range(330,360) and self.player.y == 190:
                self.player.x =270

            if self.player.x in range(280,320) and self.player.y == 190:
                self.player.x =360

            if self.player.x in range(120,130) and self.player.y == 330:
                self.player.x =180

            if self.player.x in range(160,170) and self.player.y == 330:
                self.player.x =110

            if self.player.x in range(330,350) and self.player.y == 470:
                self.player.x =270

            if self.player.x in range(280,310) and self.player == 470:
                self.player.x =360

############################ When player reaches the vault###########################################

            if self.player.x in range (80,90) and self.player.y==470:
                pygame.time.delay(1000)
                run =False

##############################Player Position#######################################################

            if keys[pygame.K_LEFT] and self.player.x>30:
                self.player.x-=self.player.vel
                self.player.left=True
                self.player.right=False
                self.player.standing=False
            elif keys[pygame.K_RIGHT] and self.player.x<915:
                self.player.x+=self.player.vel
                self.player.left=False
                self.player.right=True
                self.player.standing=False
            else:
                self.player.standing=True
                self.player.walkCount=0

            self.drawings_level1()

def game_intro():
    intro = True
    while intro:
        main_screen=pygame.image.load('mybg.jpg')
        main_screen = pygame.transform.scale(main_screen,(1000,700))
        win.blit(main_screen,(0,0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro =False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range (510,680):#checking for start button
                    for y in range(270,375):
                        if pygame.mouse.get_pos()==(x,y):
                            intro = False

                            pygame.mixer.music.load('Weirding_Way.mp3')
                            level1_music=pygame.mixer.music.play(-1,31)
                            x=Stage1()
                            x.level1()
                 #checking for quit button
                for x in range (510,680):
                    for y in range(270,375):
                        if pygame.mouse.get_pos()==(x,y):
                            pygame.quit()
                            quit()


if __name__ == "__main__":
    game_intro()
    msg=True
    while msg:
        main_screen = pygame.image.load('thanks.png')
        main_screen=pygame.transform.scale(main_screen,(1000,700))
        win.blit(main_screen,(0,0))
        pygame.display.update()
        pygame.time.delay(2000)
        msg=False


















