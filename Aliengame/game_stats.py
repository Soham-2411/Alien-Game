class Gamestats():

	def __init__(self,AI):
		self.AI=AI
		self.reset_stats(AI)
		self.game_active=False
	
	def reset_stats(self,AI):
		self.ship_left=self.AI.ship_limit
		AI.ship_speed=2
		AI.bullet_speed=1
		AI.alien_speed=0.1
		AI.player_score=0
		AI.increase_score=8