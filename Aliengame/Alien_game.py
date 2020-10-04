from classes import Settings
from classes import ship
import functions as f
import sys
import pygame as pg
from pygame.sprite import Group
from bullets import Bullet
from alien import Alien
import random
from game_stats import Gamestats
from button import Button
from alien_bullet import alien_bullets
import time
def delete_bullets(bullet,bullets):
	for bullet in bullets.copy():
			if bullet.rect.bottom<=0:
				bullets.remove(bullet)
def run_game():
	pg.init()
	bullet_sound=pg.mixer.Sound("Bullet.wav")
	pg.mixer.music.load("music.wav")
	AI=Settings()
	stats=Gamestats(AI)
	# to store the bullets
	alien_bullets_shoot=Group()
	bullets=Group()
	aliens=Group()
	screen=pg.display.set_mode((AI.screen_width,AI.screen_height))
	pg.display.set_caption("Space Wars")
	print(str(AI.screen_width) + " " + str(AI.screen_height))
	my_ship=ship(AI,screen,"my_ship.png",AI.screen_width/2,AI.screen_height-30)
	wallpaper=ship(AI,screen,"space.png",AI.screen_width/2,AI.screen_height)
	# To make a play button
	play_button=Button(AI,screen,"Play",AI.screen_width/2-50,AI.screen_height/2-150,42,(0,0,255),(0,255,0),0)
	exit_button=Button(AI,screen,"Exit",AI.screen_width/2-50,AI.screen_height/2+50,42,(0,0,255),(0,255,0),0)
	scoreboard=Button(AI,screen,"Leaderboard",AI.screen_width/2-50,AI.screen_height/2-50,40,(0,0,255),(0,255,0),50)
	GameOver=Button(AI,screen,"Game over",AI.screen_width/2-50,AI.screen_height/2,50,(0,0,0),(0,255,0),0)
	bullet=Bullet(AI,screen,my_ship)
	no_aliens=f.find_no_aliens(AI,screen,"alienship.png")
	temp=0
	x=[]
	count=0
	tmp=random.randint(8,no_aliens)
	for c in range(tmp):
		x.append(c+1)
	random.shuffle(x)
	pg.mixer.music.play(-1)
	while True:
		with open("file.txt") as score:
			last_score=score.read()
		if stats.ship_left>0 and stats.game_active:
			count=1
			if len(aliens)==0:
				bullets.empty()
				if stats.game_active:
					AI.increase_speed()
					AI.score_increase+=2 
					AI.player_level+=1
				temp=0
				x=[]
				tmp=random.randint(no_aliens-4,no_aliens)
				for c in range(tmp):
					x.append(c+1)
					random.shuffle(x)	
			f.event_check(AI,screen,my_ship,bullets,stats,play_button,aliens,bullets,bullet_sound,exit_button)
			if stats.game_active:
				if temp<tmp:
					temp=f.create_fleet(AI,screen,aliens,"alienship.png",no_aliens,temp,x)
				my_ship.update()
				f.bullets_collision_check(AI,aliens,bullets)
				f.update_screen(AI,screen,my_ship,bullets,aliens,
					stats,"my_ship.png",alien_bullets_shoot,last_score)
				delete_bullets(bullet,bullets)
				f.display_aliens(screen,AI,aliens,my_ship,stats,bullets)
			if not stats.game_active:
				wallpaper.blitme()
				play_button.draw_button()
				exit_button.draw_button()
				scoreboard.draw_button()
			pg.display.update()
		else:
			if count==1:
				c=5
				if int(last_score)<int(AI.player_score):
					with open("file.txt",'w') as file_object:
						file_object.write(str(AI.player_score))
				pg.mixer.music.pause()
				while c>0:
					screen.fill((0,0,0))
					msg="Re-directing to main menu in....... "+str(c)
					new_game=Button(AI,screen,msg,AI.screen_width/2-100,30,25,(0,0,0),(255,0,0),0)
					new_game.draw_button()
					GameOver.draw_button()
					pg.display.update()
					time.sleep(1)
					c-=1	
				count=0
			elif count==0:
				wallpaper.blitme()
				play_button.draw_button()
				exit_button.draw_button()
				scoreboard.draw_button()
				pg.display.update()
				stats.game_active=False
				f.event_check(AI,screen,my_ship,bullets,stats,play_button,aliens,bullets,bullet_sound,exit_button)
				pg.mixer.music.unpause()

	pg.display.flip()
run_game()