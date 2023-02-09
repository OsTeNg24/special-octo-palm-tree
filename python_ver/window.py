import sys, pygame

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

class Window:
	def __init__(self, title, width, height):
		pygame.init()
		self.title = title
		self.width = width
		self.height = height

		pygame.display.set_caption(title)
		self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

	def update(self):
		global WINDOW_WIDTH
		global WINDOW_HEIGHT
		WINDOW_WIDTH = self.width
		WINDOW_HEIGHT = self.height

		self.screen.fill((0, 0, 0))
		self.handle_events()

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.VIDEORESIZE:
				self.screen = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
				self.width = event.w
				self.height = event.h
				pygame.display.update()
			elif event.type == pygame.VIDEOEXPOSE:
				pygame.display.update()

def wind_width():
	return WINDOW_WIDTH

def wind_height():
	return WINDOW_HEIGHT