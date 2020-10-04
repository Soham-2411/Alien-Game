import pygame as pg
from pygame.sprite import Sprite as sp

class Alien(sp):
	#This is to create a single alien

	def __init__(self,AI,screen,image_name):
		super().__init__()
		self.screen=screen
		self.AI=AI

		#load the alien image and set its rect attribute
		self.image=pg.image.load(image_name)
		self.rect=self.image.get_rect()

		#Start a new alien at the top of the screen
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height-140

		#Start the alien's exact position
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		
	def update(self,AI):
		self.y+=AI.alien_speed
		self.rect.y=self.y  

	def blitme(self):
		self.screen.blit(self.image,self.rect)	