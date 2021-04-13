import pygame
pygame.init()
WIN_WIDTH = 1280
WIN_HEIGHT = 690

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption('My second Game - Dinos')

font = pygame.font.SysFont('Comic Sans MS',30,True)

WIDTH_HERO = 100
HEIGHT_HERO = 200

idle_dino = [pygame.image.load('dinos\Idle (1).png'),pygame.image.load('dinos\Idle (2).png'),pygame.image.load('dinos\Idle (3).png'),
            pygame.image.load('dinos\Idle (4).png'),pygame.image.load('dinos\Idle (5).png'),pygame.image.load('dinos\Idle (6).png')
            ,pygame.image.load('dinos\Idle (7).png'),pygame.image.load('dinos\Idle (8).png'),pygame.image.load('dinos\Idle (9).png'),
            pygame.image.load('dinos\Idle (10).png')]

idle_dino_a = [pygame.transform.scale(idle_dino[0],(WIDTH_HERO,HEIGHT_HERO)),pygame.transform.scale(idle_dino[1],(WIDTH_HERO,HEIGHT_HERO)),pygame.transform.scale(idle_dino[2],(WIDTH_HERO,HEIGHT_HERO)),
            pygame.transform.scale(idle_dino[3],(WIDTH_HERO,HEIGHT_HERO)),pygame.transform.scale(idle_dino[4],(WIDTH_HERO,HEIGHT_HERO)),pygame.transform.scale(idle_dino[5],(WIDTH_HERO,HEIGHT_HERO)),
            pygame.transform.scale(idle_dino[6],(WIDTH_HERO,HEIGHT_HERO)),pygame.transform.scale(idle_dino[7],(WIDTH_HERO,HEIGHT_HERO)),pygame.transform.scale(idle_dino[8],(WIDTH_HERO,HEIGHT_HERO)),
            pygame.transform.scale(idle_dino[9],(WIDTH_HERO,HEIGHT_HERO))]

walking_dino = [pygame.image.load('dinos\Walk (1).png'), pygame.image.load('dinos\Walk (2).png'), pygame.image.load('dinos\Walk (3).png'), pygame.image.load('dinos\Walk (4).png'),
             pygame.image.load('dinos\Walk (5).png'), pygame.image.load('dinos\Walk (6).png'), pygame.image.load('dinos\Walk (7).png'),
             pygame.image.load('dinos\Walk (8).png'), pygame.image.load('dinos\Walk (9).png'), pygame.image.load('dinos\Walk (10).png')]

walking_dino_a = [pygame.transform.scale(walking_dino[0], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(walking_dino[1], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(walking_dino[2], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(walking_dino[3], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(walking_dino[4], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(walking_dino[5], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(walking_dino[6], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(walking_dino[7], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(walking_dino[8], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(walking_dino[9], (WIDTH_HERO, HEIGHT_HERO))]

run_dino = [pygame.image.load('dinos\Run (1).png'), pygame.image.load('dinos\Run (2).png'), pygame.image.load('dinos\Run (3).png'), pygame.image.load('dinos\Run (4).png'),
             pygame.image.load('dinos\Run (5).png'), pygame.image.load('dinos\Run (6).png'), pygame.image.load('dinos\Run (7).png'),
             pygame.image.load('dinos\Run (8).png')]

run_dino_a =[pygame.transform.scale(run_dino[0], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(run_dino[1], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(run_dino[2], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(run_dino[3], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(run_dino[4], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(run_dino[5], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(run_dino[6], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(run_dino[7], (WIDTH_HERO, HEIGHT_HERO))]

jump_dino = [pygame.image.load('dinos\Jump (1).png'), pygame.image.load('dinos\Jump (2).png'), pygame.image.load('dinos\Jump (3).png'), pygame.image.load('dinos\Jump (4).png'),
             pygame.image.load('dinos\Jump (5).png'), pygame.image.load('dinos\Jump (6).png'), pygame.image.load('dinos\Jump (7).png'),
             pygame.image.load('dinos\Jump (8).png'),pygame.image.load('dinos\Jump (9).png'),pygame.image.load('dinos\Jump (10).png'),pygame.image.load('dinos\Jump (11).png'),
             pygame.image.load('dinos\Jump (12).png')]

jump_dino_a =[pygame.transform.scale(jump_dino[0], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[1], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[2], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(jump_dino[3], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[4], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[5], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(jump_dino[6], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[7], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[8], (WIDTH_HERO, HEIGHT_HERO)),
               pygame.transform.scale(jump_dino[9], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[10], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(jump_dino[11], (WIDTH_HERO, HEIGHT_HERO))]

dead_dino = [pygame.image.load('dinos\Dead (1).png'), pygame.image.load('dinos\Dead (2).png'), pygame.image.load('dinos\Dead (3).png'), pygame.image.load('dinos\Jump (4).png'),
             pygame.image.load('dinos\Dead (5).png'), pygame.image.load('dinos\Dead (6).png'), pygame.image.load('dinos\Dead (7).png'),
             pygame.image.load('dinos\Dead (8).png')]

dead_dino_a =[pygame.transform.scale(dead_dino[0], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(dead_dino[1], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(dead_dino[2], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(dead_dino[3], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(dead_dino[4], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(dead_dino[5], (WIDTH_HERO, HEIGHT_HERO)),
              pygame.transform.scale(dead_dino[6], (WIDTH_HERO, HEIGHT_HERO)), pygame.transform.scale(dead_dino[7], (WIDTH_HERO, HEIGHT_HERO))]

class Dino:
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.velx = 0
        self.vely = 0
        self.state = 0 #0 - idle, 1-walk, 2-  Run, 3-Jump, 4- Dead
        self.prev_state = False
        self.hit = False
        self.score = 0
        self.count = 0
    def draw(self,win):
        if self.state == 0 : # Idle
            win.blit(idle_dino_a[self.count],(self.x,self.y))
        elif self.state == 1:    #walking
            win.blit(walking_dino_a[self.count],(self.x,self.y))
        elif self.state == 2:
            win.blit(run_dino_a[self.count],(self.x,self.y))
        elif self.state == 3:
            win.blit(jump_dino_a[self.count],(self.x,self.y))
        elif self.state == 4:
            win.blit(dead_dino_a[self.count],(self.x,self.y))
        else:
            pass
    def update(self,win):
        self.draw(win)
        self.count = self.count + 1
        if self.state == 2:
            if self.count == 8:
                self.count = 0
        elif self.state == 3:
            if self.count == 11:
                self.count = 0
        elif self.state == 4:
            if self.count == 8:
                self.count = 7
        else:
            if self.count == 10:
                self.count = 0
        
class BG:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y 
        self.bg = pygame.transform.scale(pygame.image.load('bg.jpg'),(1280,690))
        self.width = width 
        self.height = height
        self.velx = 4
    def draw(self,win):
        win.blit(self.bg,(self.x,self.y))
    def update(self,win):
        self.x = self.x - self.velx
        self.draw(win)

bg1_x = 0
bg1_y = 0
bg2_x = 1281
bg2_y = 0

bg1 = BG(bg1_x,bg1_y,1280,690)
bg2 = BG(bg2_x,bg2_y,1280,690)
dino_char = Dino(200,270,WIDTH_HERO,HEIGHT_HERO)

run = True
while run:
    if bg1.x <= -1280:
        bg1.x = bg2.x + 1280
    if bg2.x <= -1280:
        bg2.x = bg1.x + 1280

    bg1.update(win)
    bg2.update(win)
    dino_char.update(win)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dino_char.state = 1  #walking
                dino_char.count = 0
                bg1.velx = 2
                bg2.velx = 2
            elif event.key == pygame.K_r: #running
                dino_char.state = 2
                dino_char.count = 0
                bg1.velx = 7
                bg2.velx = 7
                dino_char.prev_state = dino_char.state
            elif event.key == pygame.K_s:  #Jumping
                dino_char.prev_state = dino_char.state
                dino_char.state = 3
                dino_char.count = 0
            elif event.key == pygame.K_l: #restart
                dino_char.x = 200
                dino_char.y = 270
                dino_char.score = 0
                dino_char.hit = False
                bg1_x = 0
                bg1_y = 0
                bg2_x = 1281
                bg2_y = 0
                dino_char.state = 0 #idle
                dino_char.prev_state = 0
pygame.quit()



