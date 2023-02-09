import pygame, math, random
from timer import Timer


from object import Object

class Player(Object):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
        self.target = list(self.rect.center)
        self.pos = list(self.rect.center)
        self.velocity = [0, 0]
        self.speed = 1500
    
    def update(self):
        self.bound()
        dt = Timer.deltaTime()

        # poll for input
        key_pressed = pygame.key.get_pressed()
        # msb_pressed = pygame.mouse.get_pressed()
        
        # update target and velocity 
        if key_pressed[pygame.K_a] == True:
            self.target = list(pygame.mouse.get_pos())
        
        x = self.target[0] - self.pos[0]
        y = self.target[1] - self.pos[1]
        mag = math.sqrt(x**2 + y**2)
        if mag == 0:
            self.velocity = [0, 0]  
        else:
            self.velocity = [x / mag, y / mag]
        
        # move player to target and stop 
        if (self.pos[0] != self.target[0]) or (self.pos[1] != self.target[1]):
            x = round(self.velocity[0] * self.speed * dt)
            y = round(self.velocity[1] * self.speed * dt)
            self.move(x, y)
        
        self.pos = list(self.rect.center)
    
    def get_pos(self):
        return self.pos
    