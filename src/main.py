import sys
import math
import pygame
import random

from math import sin, cos, pi

from constants import Colors
from road import Road

class Car:
	def __init__(self, screen_width):
		self.width = 30
		self.height = 50
		self.angle = 15
		self.x = screen_width / 2

	def draw(self):		
		s = pygame.Surface((self.width, self.height))
		s.fill(Colors.white)
		pygame.draw.rect(s, Colors.red, pygame.Rect(0, 0, self.width, self.height))
		s = pygame.transform.rotate(s, self.angle)
		return s


	def turn_left(self):
		self.angle += 1


	def turn_right(self):
		self.angle -= 1



def main():
	pygame.init()
	clock = pygame.time.Clock()

	size = width, height = 800, 600	
	road_size = road_width, road_height = 400, 400

	screen = pygame.display.set_mode(size)

	pygame.display.set_caption("Train the Game")


	road_surface = pygame.Surface(road_size)
	road = Road(road_width, road_height)

	car = Car(road_width)

	while True:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# elif event.type == pygame.KEYDOWN:
			# 	if event.key == pygame.K_LEFT:
			# 		car.turn_left()
			# 	elif event.key == pygame.K_RIGHT:
			# 		car.turn_right()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			car.turn_left()
		elif keys[pygame.K_RIGHT]:
			car.turn_right()


		road.scroll()
		road.draw(road_surface)

		frame_width = 5
		left = int((width - road_width) / 2)
		top = int((height - road_height) / 2)

		pygame.draw.rect(screen, 
			Colors.light_grey, 
			pygame.Rect(
				left - frame_width, 
				top - frame_width, 
				road_width + frame_width * 2, 
				road_height + frame_width * 2))

		screen.blit(road_surface, (left, top))

		car_surface = car.draw()
		w, h = car_surface.get_size()

		screen.blit(car_surface, (int((width - road_width) / 2 + car.x - w / 2), int((height + road_height) / 2 - h)))		

		pygame.display.flip()


if __name__ == "__main__":
	main()