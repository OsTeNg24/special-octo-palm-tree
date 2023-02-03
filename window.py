import sys, pygame

class Window:
	def __init__(self, title, width, height):
		pygame.init()
		self.title = title
		self.width = width
		self.height = height

		pygame.display.set_caption(title)
		self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

	def update(self):
		self.screen.fill((0, 0, 0))
		self.handle_events()	

	def handle_events(self):
		pass

