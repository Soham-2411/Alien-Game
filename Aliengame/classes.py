import pygame
class Settings():
	
	def __init__(self):
		self.screen_width=1200
		self.screen_height=700
		self.bk_color=(0,0,0)
		self.ship_limit=1
		self.bullet_width=2
		self.bullet_height=20
		self.bullet_color=(0,0,255)
		self.alien_bullet_width=2
		self.alien_bullet_height=20
		self.alien_bullet_color=(0,255,0)
		self.bullets_allowed=18
		self.alien_bullet_speed=0.25
		self.bullet_speed_up=0.5
		self.ship_speed_up=0.25
		self.alien_speed_up=0.05
		self.player_score=0
		self.score_increase=8
		self.player_level=0
		self.init_dynamic_settings()
	
	def init_dynamic_settings(self):
		self.ship_speed=2
		self.bullet_speed=1
		self.alien_speed=0.1
	
	def increase_speed(self):
		#Now to increase the speed
		self.ship_speed+=self.ship_speed_up
		self.bullet_speed+=self.bullet_speed_up
		self.alien_speed+=self.alien_speed_up

	def decrease_speed(self):
		#Now to increase the speed
		self.ship_speed-=self.ship_speed_up
		self.bullet_speed-=self.bullet_speed_up
		self.alien_speed-=self.alien_speed_up

class ship():
	def __init__(self,AI,screen,image_name,xpos,ypos):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.moving_right=False
		self.moving_left=False
		self.ypos=ypos
		self.AI=AI
		self.image_name=image_name
		self.image=pygame.image.load(image_name)
		self.rect=self.image.get_rect()

		#To make the ship at the set location
		self.rect.centerx=xpos
		self.rect.bottom=ypos
		self.center=float(self.rect.centerx)

	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.AI.ship_speed
		if self.moving_left and self.rect.left>0:
			self.center-=self.AI.ship_speed
		self.rect.centerx=self.center
	def blitme(self):
		# To make the screen at its curret location
		self.screen.blit(self.image,self.rect)