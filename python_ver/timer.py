import pygame
from timeit import default_timer as timer

clock = pygame.time.Clock()
prev = timer()
dt = 0

class Timer:

    @staticmethod
    def update():
        global prev
        global dt
        clock.tick(240)
        curr = timer()
        dt = curr - prev
        prev = curr

    @staticmethod
    def deltaTime():
        return dt
    
    @staticmethod
    def printFPS():
        print("FPS: ", 1.0 / (timer() - prev))
