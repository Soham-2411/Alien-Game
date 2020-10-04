import sys
from classes import ship
import pygame as pg
from pygame.sprite import Sprite
from bullets import Bullet
from alien import Alien
import random
from time import sleep
from button import Button
from alien_bullet import alien_bullets
def check_keydown_event(event,AI,screen,my_ship,bullets,bullet_sound):
	# create a new bullet and add to bullets group
	if len(bullets)<AI.bullets_allowed:
		new_bullet_left=Bullet(AI,screen,my_ship)
		bullets.add(new_bullet_left)
		new_bullet_right=Bullet(AI,screen,my_ship)
		bullets.add(new_bullet_right)
		pg.mixer.Sound.play(bullet_sound)

def alien_bullet(AI,screen,alien,alien_bullets):
	new_bullet=alien_bullets(AI,screen,alien)
	alien_bullets.add(new_bullet)

def event_check(AI,screen,my_ship,bullet,stats,play_button,
				aliens,bullets,bullet_sound,exit_button):
	for event in pg.event.get():
		if event.type==pg.QUIT:
			pg.quit()
		elif event.type==pg.KEYDOWN:
			if event.key==pg.K_SPACE:
				check_keydown_event(event,AI,screen,my_ship,bullet,bullet_sound)
			elif event.key==pg.K_RIGHT:
				my_ship.moving_right=True
			elif event.key==pg.K_LEFT:
				my_ship.moving_left=True
			elif event.key==pg.K_q:
				pg.quit()	
		elif event.type==pg.KEYUP:
			if event.key==pg.K_RIGHT:
				my_ship.moving_right=False
			elif event.key==pg.K_LEFT:
				my_ship.moving_left=False
		elif event.type==pg.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pg.mouse.get_pos()
			check_play_button(AI,screen,stats,play_button,my_ship,
				aliens,bullets,mouse_x,mouse_y)
			button_clicked=exit_button.rect.collidepoint(mouse_x,mouse_y)
			if button_clicked:
				pg.quit()	

def check_play_button(AI,screen,stats,play_button,my_ship,aliens
					,bullets,mouse_x,mouse_y):
	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		stats.reset_stats(AI)
		aliens.empty()
		bullets.empty()
		c=3
		while c>0:
			msg="Game starts in....... "+str(c)
			new_game=Button(AI,screen,msg,AI.screen_width/2-100,30,25,(0,0,0),(255,0,0),0)
			new_game.draw_button()
			pg.display.update()
			sleep(1)
			c-=1
		stats.game_active=True

def create_fleet(AI,screen,aliens,image_name,number_of_aliens,alien_number,x):
	x2=random.randint(1,150)
	if x2==1 or len(aliens)==0:
		alien=Alien(AI,screen,image_name)
		alien.x=alien.rect.width+2*alien.rect.width*x[alien_number]
		alien.rect.x=alien.x
		aliens.add(alien)
		alien_number+=1
	return alien_number

def ship_hit(AI,stats,aliens,bullets):
	stats.ship_left-=1
	aliens.empty()
	bullets.empty()
	AI.decrease_speed()
	AI.score_increase-=2
	sleep(0.5)
	AI.player_level-=1

def display_aliens(screen,AI,aliens,my_ship,stats,bullets):
	for alien in aliens.sprites():
		alien.update(AI)
		screen_rect=screen.get_rect()
		if alien.rect.bottom>=screen_rect.bottom:
			ship_hit(AI,stats,aliens,bullets)
			break
		alien.blitme()
	pg.display.update()
	if pg.sprite.spritecollideany(my_ship,aliens):
		ship_hit(AI,stats,aliens,bullets)

def find_no_aliens(AI,screen,image_name):
	# To create a full fleet of aliens 
	# and to check how many aliens fit in the row
	alien=Alien(AI,screen,image_name)
	available_space=AI.screen_width-2*alien.rect.width
	number_of_aliens=int(available_space/(2*alien.rect.width))
	return number_of_aliens

def bullets_collision_check(AI,aliens,bullets):
	# To check whether the bullet has hit the alien or not
	for alien in aliens.sprites():
		for bul in bullets.sprites():
			if pg.sprite.collide_rect(bul,alien):
				alien.kill()
				y=bul.rect.y
				for bullet in bullets.sprites():
					if y==bullet.rect.y:
						bullet.kill()
						AI.player_score+=int(AI.score_increase/2)

def print_life(AI,screen,image_name,stats):
	c=stats.ship_left
	while c>0:
		ships_left=ship(AI,screen,image_name,70,30+c*70)   
		c-=1
		ships_left.blitme()

def update_screen(AI,screen,my_ship,bullets,alien,stats,image_name,alien_bullets,last_score):
	if int(AI.player_score)>int(last_score):
		last_score=AI.player_score
	dis_scr=Button(AI,screen,"Score: "+str(AI.player_score),AI.screen_width-170,50,40,(0,0,0),(206,234,230),0)
	last_score=Button(AI,screen,"Highscore: "+str(last_score),AI.screen_width-170,100,32,(0,0,0),(41,27,79),0)
	level=Button(AI,screen,"Level: "+str(AI.player_level),AI.screen_width-170,150,32,(0,0,0),(253,213,44),0)
	my_ship.update()
	screen.fill(AI.bk_color)
	my_ship.blitme()
	print_life(AI,screen,image_name,stats)
	count=0
	pos=0
	dis_scr.draw_button()
	last_score.draw_button()
	level.draw_button()
	for bullet in bullets.sprites():
		if count%2==0:
			pos=-8
		else:
			pos=8
		bullet.update(pos)
		bullet.draw_bullet()
		count+=1