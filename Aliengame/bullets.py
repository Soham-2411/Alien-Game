import pygame as pg
from pygame.sprite import Sprite
import random
class Bullet(Sprite):

	def __init__(self,AI,screen,my_ship):
		#start a bullet at ship's location
		super().__init__()
		self.screen=screen
		self.co1=random.randint(1,255)
		self.co2=random.randint(1,255)
		self.co3=random.randint(1,255)

		#self(0,0,width,height)
		self.rect=pg.Rect(0,0,AI.bullet_width,
			AI.bullet_height)
		#Then moving it to the ship's location	
		self.rect.centerx=my_ship.rect.centerx
		self.rect.top=my_ship.rect.top
		self.color=AI.bullet_color
		self.speed=AI.bullet_speed
		self.temp=my_ship.rect.centerx

	def update(self,pos):
		self.rect.y-=self.speed
		self.rect.centerx=self.temp-pos
	
	def draw_bullet(self):
		#To draw the bullet
		self.color=(self.co1,self.co2,self.co3)
		pg.draw.rect(self.screen,self.color,self.rect)
