import pygame
import random
pygame.init()
win =pygame.display.set_mode((852,480))
pygame.display.set_caption("HERO")
run =True
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')
walkRight1 = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'), pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load('Game/R6E.png'), pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'),  pygame.image.load('Game/R11E.png')]
walkLeft1 = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'), pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load('Game/L6E.png'), pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'),  pygame.image.load('Game/L11E.png')]
bullets=[]
bullets1=[]
gun=True
score=0
x=random.randint(200,800)
y=random.randint(50,600)
draw=0
class gamer:

    def __init__(self,x,y,height,width):
        self.x=x
        self.y=y
        self.height=height
        self.jump=False
        self.width=width
        self.vel=8
        self.counter=10
        self.left=False
        self.right=False
        self.walk=0
        self.standing=True
        self.c=1
        self.d=0
        self.facing=0
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health=0

    def jumper(self,win):
        if not self.standing:
            if self.left:
             self.c=0
             win.blit(walkLeft[self.walk], (self.x, self.y))
             self.walk += 1
             if self.walk >= 9:
                    self.walk = 0
             if self.standing:
                win.blit(walkLeft[0], (self.x, self.y))

            if self.right:
             self.c=1
             win.blit(walkRight[self.walk], (self.x, self.y))
             self.walk += 1
             if self.walk >= 9:
                    self.walk = 0

        elif self.standing:
            if self.c==0:
                win.blit(walkLeft[0], (self.x, self.y))

            if self.c==1:
                win.blit(walkRight[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, (50 - self.health), 10))
    def hit(self):
        self.health+=5


       #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


player1=gamer(500,400,64,64)
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 14 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
class enemy:

    def __init__(self,x,y,height,width):
            self.x=x
            self.y=y
            self.height=height
            self.width=width
            self.vel=6
            self.face=[1,-1]
            self.walk=0
            self.path=[0,800]
            self.condition=False
            self.hitbox = (self.x + 13, self.y + 2, 31, 57)
            self.health=1

    def mover(self):

        if self.vel >0:
            self.condition=True
            if self.x < random.randint(500,800):
                print(random.randint(500,800))
                self.x+=self.vel

            else:
                self.vel=self.vel*-1

        else:
            self.condition=False
            if self.x >random.randint(0,400):

                self.x+=self.vel
            else:
                self.vel=self.vel*-1

    def move(self):
        self.mover()
        if  self.condition:
            win.blit(walkRight1[self.walk],(self.x,self.y))
            self.walk += 1
            if self.walk >= 9:
                self.walk = 0

        else:

            win.blit(walkLeft1[self.walk], (self.x, self.y))
            self.walk += 1
            if self.walk >= 9:
                self.walk = 0

        self.hitbox = (self.x + 13, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0),(self.hitbox[0], self.hitbox[1] - 20, (50-self.health), 10))
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        global score
        win.blit(walkRight1[0], (self.x, self.y))
        print('hit')
        self.health+=0.5


        score+=1

goblin=enemy(10,400,64,64)
def rungame():
    win.blit(bg,(0,0))
    player1.jumper(win)
    goblin.move()
    win.blit(font.render("Score: "+ str(score),1,(0,0,0)), (620, 35))
    for bullet in bullets:
        bullet.draw(win)

    for bullet in bullets1:
        bullet.draw(win)
    if player1.health>=50:
        win.blit(bg,(0,0))
        win.blit(font.render("YOU LOSE", 1, (0, 0, 0)), (300, 300))
    if goblin.health >= 50:
        win.blit(bg, (0, 0))
        win.blit(font.render("GAME OVER", 1, (0, 0, 0)), (300, 35))




    pygame.display.update()

###main loop for the pressed keys###
font=pygame.font.SysFont('comicsans',50,True)
while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    #if pygame.key.get_pressed()==pygame.K_f:


    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[
            1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] +   goblin.hitbox[2]:

                goblin.hit()

                bullets.pop(bullets.index(bullet))
        if bullet.x < 852 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    for bullet in bullets1:
        if bullet.y - bullet.radius < player1.hitbox[1] + player1.hitbox[3] and bullet.y + bullet.radius > player1.hitbox[
            1]:
            if bullet.x + bullet.radius > player1.hitbox[0] and bullet.x - bullet.radius < player1.hitbox[0] +   player1.hitbox[2]:
                player1.hit()
                bullets1.pop(bullets1.index(bullet))
        if bullet.x < 852 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets1.pop(bullets1.index(bullet))
    if gun:
        if not goblin.condition:
            facing = -1
        else:
            facing = 1

        if len(bullets1) < 2:
            bullets1.append(
                projectile(round(goblin.x + goblin.width // 2), round(goblin.y + goblin.height // 2), 6, (0, 0, 255),
                           facing))


    keys=pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if player1.left:
            facing = -1
        else :
            facing = 1

        if len(bullets) < 4:
            bullets.append(
                projectile(round(player1.x + player1.width // 2), round(player1.y + player1.height // 2), 6, (0, 0, 0), facing))
    if keys[pygame.K_LEFT]:
        player1.x-=player1.vel
        player1.left=True
        player1.right=False

        player1.standing=False
        if player1.x < 0:
             player1.x+=1000
    elif keys[pygame.K_RIGHT]:
            player1.x+=player1.vel
            player1.left=False
            player1.right=True

            player1.standing=False
            if player1.x >1000:
                player1.x=0
    else:
        player1.left=False
        player1.right=False
        player1.standing=True
    if not player1.jump:

        if keys[pygame.K_UP]:
            player1.jump = True
    else:
        if player1.counter >= -10:
            player1.y -= (player1.counter * abs(player1.counter)) *0.45
            player1.counter -= 1

        else:
            player1.counter = 10
            player1.jump = False
            player1.standing = True

    rungame()

