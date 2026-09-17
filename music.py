import pygame
from pygame import mixer
class Music:
    def __init__(self):
        pygame.init()
        mixer.init()
        # 在init_ui函数中初始化背景音乐文件
        mixer.music.load('music_zapsplat_above_the_clouds_100.mp3')
        self.bgm=mixer.music
        # 在init_ui函数中初始化音效文件
        self.button_sound = pygame.mixer.Sound("zapsplat_multimedia_button_click_004_78081.mp3")
        self.m1=pygame.mixer.Sound("w1.mp3")
        self.m2 = pygame.mixer.Sound("w2.mp3")
        self.m3 = pygame.mixer.Sound("w3.mp3")
        self.m4 = pygame.mixer.Sound("w4.mp3")
music_source=Music()