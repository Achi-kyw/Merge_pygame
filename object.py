import pygame as pg
from pygame.locals import *
class pinxiang():
    def __init__(self, id, weight, width, height, x, y, mode):
        self.id=id
        self.weight=weight
        self.width=width
        self.height=height
        self.x=x
        self.y=y
        self.mode=mode
        self.selected=False
    def draw(self,screen):
        if self.selected:
            pg.draw.rect(screen,(255,0,0),[self.x,self.y,self.width,self.height],3)
        else:
            pg.draw.rect(screen,(0,0,0),[self.x,self.y,self.width,self.height],3)
        if self.weight<10:
            font = pg.font.SysFont("couriernew", 50)
            text = font.render(str(self.weight), True, (0,0,0), (255,255,255))
            screen.blit(text, (self.x+35,self.y+25))
        elif self.weight<100:
            font = pg.font.SysFont("couriernew", 50)
            text = font.render(str(self.weight), True, (0,0,0), (255,255,255))
            screen.blit(text, (self.x+20,self.y+25))
        else:
            font = pg.font.SysFont("couriernew", 40)
            text = font.render(str(self.weight), True, (0,0,0), (255,255,255))
            screen.blit(text, (self.x+15,self.y+30))
