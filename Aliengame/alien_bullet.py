import pygame as pg
from pygame.sprite import Sprite

class alien_bullets(Sprite):
	def __init__(self,AI,screen,alien):
		super().__init__()
		self.screen=screen
	
		#self(0,0,width,height)
		self.rect=pg.Rect(0,0,AI.alien_bullet_width,
			AI.alien_bullet_height)
		#Then moving it to the ship's location	
		self.rect.centerx=alien.rect.centerx
		self.rect.top=alien.rect.bottom
		self.color=AI.alien_bullet_color
		self.speed=AI.alien_bullet_speed
		#self.temp=my_ship.rect.centerx

	def update_alien_bullet(self):
		self.rect.y+=self.speed
	
	def draw_alien_bullet(self):
		#To draw the bullet
		pg.draw.rect(self.screen,self.color,self.rect)