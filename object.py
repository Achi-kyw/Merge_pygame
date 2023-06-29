import pygame as pg
from pygame.locals import *
class pinxiang():
    def __init__(self, id, weight, width, height, x, y):
        self.id=id
        self.weight=weight
        self.width=width
        self.height=height
        self.x=x
        self.y=y
    def draw(self,screen):
        pg.draw.rect(screen,(0,0,0),[self.x,self.y,self.width,self.height],3)
        '''
        font = pg.font.SysFont("微軟正黑體",16)
        text = font.render("Hello", True, (0,0,255), (255,255,255))
        '''
