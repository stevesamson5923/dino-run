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

class BG:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y 
        self.bg = pygame.image.load('bg.jpg')
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

bg1 = BG(bg1_x,bg1_y,1280,690)

run = True
while run:
    bg1.update(win)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()



