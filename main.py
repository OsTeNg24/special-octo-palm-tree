import pygame, sys, time, random
import window

# setup
window = window.Window("Window", 800, 600)

class Object(pygame.sprite.Sprite):
	def __init__(self, x, y, img_path):
		# setup
		super().__init__()
		self.image = pygame.image.load(img_path)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.velocity = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]

	def update(self):
		self.is_colliding()
		speed = 2
		self.rect = self.rect.move(tuple([x*speed for x in self.velocity]))

	def is_colliding(self):
		if self.rect.left < 0 or self.rect.right > window.width:
			self.velocity[0] *= -1
		if self.rect.top < 0 or self.rect.bottom > window.height:
			self.velocity[1] *= -1

OBJECT_CAPACITY = 3000
objects = pygame.sprite.Group()
for i in range(OBJECT_CAPACITY):
	ball = Object(400, 300, "intro_ball.gif")
	objects.add(ball)

# TODO: figure out a way to make dt a consistent way to move objects
prev_time = time.time()
dt = 0

while True:
	# timing
	curr_time = time.time()
	dt = curr_time - prev_time
	prev_time = curr_time

	window.update()

	# events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# input
	# pressed = pygame.key.get_pressed()
	# if pressed[pygame.K_w] == True:
	# 	pass
	
	objects.update()
	objects.draw(window.screen)
	pygame.display.flip()

	print("FPS: ", 1.0 / (time.time() - curr_time))