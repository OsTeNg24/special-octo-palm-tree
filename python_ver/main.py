import pygame
from timer import Timer
from window import Window, WINDOW_WIDTH, WINDOW_HEIGHT
from player import Player

# setup
window = Window("Window", WINDOW_WIDTH, WINDOW_HEIGHT)

OBJECT_CAPACITY = 1
objects = pygame.sprite.Group()
# for i in range(OBJECT_CAPACITY):
# 	ball = Object(400, 300, "intro_ball.gif")
# 	objects.add(ball)
player = Player(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, "intro_ball.gif")
objects.add(player)

while True:
	window.update()
	Timer.update()

	start = (player.pos[0], player.pos[1])
	end = (player.target[0], player.target[1])
	pygame.draw.line(window.screen, (255, 255, 255), start, end)
	
	objects.update()
	objects.draw(window.screen)
	pygame.display.flip()

	Timer.printFPS()