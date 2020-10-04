import pygame as pg
#pg.init()
class Button():

	def __init__(self,AI,screen,msg,xpos,ypos,size,button_color,text_color,pos):
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.xpos=xpos
		self.ypos=ypos
		self.pos=pos
		# set the dimensions and properties of the button
		self.width,self.height=200,50
		self.button_color=button_color
		self.text_color=text_color
		self.font = pg.font.SysFont("freesansbold.ttf", size)

		# build the button's rect object and center it
		self.rect=pg.Rect(0,0,self.width,self.height)
		#self.rect.center=self.screen_rect.center
		self.rect.y=self.ypos-self.height/4
		self.rect.x=self.xpos-self.width/3
		# The button message needs to be prepped only once
		self.prep_msg(msg)

	def prep_msg(self,msg):
		self.msg_image=self.font.render(msg,True,self.text_color,
			self.button_color)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.y=self.ypos
		self.msg_image_rect.x=self.xpos-self.pos

	def draw_button(self):
		# Draw a button and then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)	