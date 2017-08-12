# coding=gbk
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf
def run_game():
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	ai_settings =Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ��
	stats = GameStats(ai_settings)
	# ����һ�ҷɴ���һ���ӵ������һ�������˱���
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	#����������Ⱥ
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	# ��ʼ��Ϸ����ѭ��
	while True:
		# ��Ӧ����������¼�
		gf.check_events(ai_settings,screen,ship,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			#print(len(bullets)) ��������Ƿ�ɹ�ɾ���ӵ�
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		# ������Ļ�ػ���Ļ
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
		
