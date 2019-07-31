import pygame
import math

#pygame.init()

(width, height) = (480, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My arcanoid game')
#Colours
red = (255,0,0)
light_blue = (52,153,255)
background_colour = (255,255,255)

#Functions
def collide(p1, p2):
    # center of brick
    dx = p1.x - (p2.x + (p2.width//2))
    dy = p1.y - (p2.y + (p2.height//2))
    dist = math.hypot(dx, dy)
    if dist < p1.size:
        angle = -p1.angle

        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)   
    """ dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.hypot(dx, dy)
    if dist < p1.size:
        tangent = math.atan2(dy, dx)
        angle = 0.5 * math.pi + tangent

        angle1 = 2*tangent - p1.angle

        p1.x += math.sin(angle)
        p1.y -= math.cos(angle) """

#Classes
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
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
	 
        if self.y > height - self.size:
            print('life minus')
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle	 

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
        
    
        


class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

    def draw(self, win):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, red, rect)
    
game_ball = ball(150, 1, 10)
enemy_bricks = []
n_of_rows, n_in_row = 5, 10
init_x = 0
init_y = 500
row = []

for i in range(n_of_rows):
    for m in range(n_in_row):
        row.append(enemy(init_x,init_y,(width-n_in_row)//n_in_row,20))
        init_x += (width//n_in_row)
    enemy_bricks.append(row)
    init_x = 0
    init_y += 22

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)
    #enemy_brick.draw(screen)
    
    for row in enemy_bricks:
        for enemy in row:
            enemy.draw(screen)
            
            collide(game_ball, enemy)
            
    game_ball.move()
    game_ball.bounce()
    game_ball.draw(screen)
    pygame.display.flip()

pygame.quit()
