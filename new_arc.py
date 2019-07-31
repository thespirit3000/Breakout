import pygame
import math

#pygame.init()

#_________Functions________
def collide(p1, p2):
    # center of brick
    dx = p1.x - (p2.x + (p2.width//2))
    dy = p1.y - (p2.y + (p2.height//2))
    dist = math.hypot(dx, dy)
    if dist < p1.size:
        angle = -p1.angle

        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)   


#_________Classes________
class Game:
    def __init__(self, blocks, paddle, ball):
        self.blocks = blocks
        self.ball = ball
        self.paddle = paddle

        
                

class ball(object):
    def __init__(self,x,y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 2
        self.angle = 0.2
        self.onTruck = True
        self.run = False    
    
    def draw(self,win):
        circle = (int(self.x), int(self.y))
        pygame.draw.circle(win, light_blue, circle, self.size)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
    
    def bounce(self):
        if self.x > WIDTH - self.size:
            self.x = 2*(WIDTH - self.size) - self.x
            self.angle = - self.angle

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
	 
        if self.y > HEIGHT - self.size:
            print('life minus')
            self.y = 2*(HEIGHT - self.size) - self.y
            self.angle = math.pi - self.angle	 

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
   
class block(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
    
    def draw(self, win):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, red, rect)

class paddle(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = 10
        self.speed = PADDLE_SPEED

    def draw(self,win):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, red, rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > VEL:
            self.x -= self.speed
            
        elif keys[pygame.K_RIGHT] and self.x < WIDTH - self.width - VEL:
            self.x += self.speed
            
#_________Config________
WIDTH = 500
HEIGHT = 600
FPS = 60
BALL_SPEED = 20
PADDLE_WIDTH = 50
PADDLE_SPEED = 3
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20
QTY_ROWS = 5
QTY_COLUMNS = 10
VEL = 5

#_________Colours________
red = (255,0,0)
light_blue = (52,153,255)
background_colour = (255,255,255)
game_paddle = paddle((WIDTH//2) - (PADDLE_WIDTH//2), HEIGHT - 14, 1)


#_________Init________
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My arcanoid game')
game_ball = ball(150, 1, 10)
bricks = []

for y in range(0,BLOCK_HEIGHT*QTY_ROWS, BLOCK_HEIGHT+1):
    for x in range(2, WIDTH, BLOCK_WIDTH+1):
        bricks.append(block(x, y))


running = True
#_________Main loop________
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background_colour)
    for brick in bricks:
        brick.draw(screen)
    game_ball.move()
    game_ball.bounce()
    game_ball.draw(screen)
    game_paddle.draw(screen)
    game_paddle.move()
    pygame.display.flip()

pygame.quit()
