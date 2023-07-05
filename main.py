import pygame as pg
import config
import movement
import object
import sys
from pygame.locals import *
instructs=['Merge的代價為兩者體重最大公因數','Merge的代價為兩者體重乘積','Merge的代價為兩者體重加起來','Merge的代價為兩者體重較小的','Merge的代價為兩者體重較大的','Merge的代價為兩者體重差距']

def update(screen):
    screen.fill(config.background_color)
    font = pg.font.SysFont("microsoftjhenghei", 32)
    text = font.render(instructs[mode], True, (0,0,0), (255,255,255))
    screen.blit(text, (250,20))
    text = font.render("總花費："+str(cost)+"   ", True, (0,0,0), (255,255,255))
    screen.blit(text, (250,config.height-50))
    text = font.render("時間：", True, (0,0,0), (255,255,255))
    screen.blit(text, (800,20))
    text = font.render(info[0], True, (0,0,0), (255,255,255))
    screen.blit(text, (100,300))
    text = font.render(info[1], True, (0,0,0), (255,255,255))
    screen.blit(text, (100,350))
    font = pg.font.SysFont("couriernew", 32)
    text = font.render(str(120-(pg.time.get_ticks()-start_ticks)//1000).rjust(3), True, (0,0,0), (255,255,255))
    screen.blit(text, (890,27))
    for i in objects:
        i.draw(screen)
    pg.display.flip()
def main(argv):
    global selected_num,selected_id,cost,clock,start_ticks,info,game_end,mode
    clock = pg.time.Clock()
    selected_num=0
    selected_id=[]
    cost=0
    info=["",""]
    game_end=False
    pg.init()
    start_ticks=pg.time.get_ticks()
    screen = pg.display.set_mode((config.width, config.height))
    pg.display.set_caption('我要跟你 merge')
    mode=int(argv[0])
    with open("testdata/"+str(mode)+".txt",'r') as f:
        global objects,text
        objects=[]
        for i,j in enumerate(f.read().split(' ')):
            objects.append(object.pinxiang(i,int(j),config.object_width,config.object_height,10+(config.object_width+10)*i,100,mode))
    run = True
    processing=False
    update(screen)
    while run:
        if len(objects)==1:
            game_end=True
        for event in pg.event.get():
            #print(event)
            if event.type == pg.QUIT:
                run = False
            elif event.type == MOUSEBUTTONUP:
                x,y=pg.mouse.get_pos()
                for i in objects:
                    if x-i.x<=i.width and x-i.x>0 and y-i.y<=i.height and y-i.y>0:
                        if i.selected:
                            if selected_num==1:
                                i.selected=False
                                selected_num=0
                                selected_id.pop()
                        else:
                            i.selected=True
                            selected_id.append(i.id)
                            selected_num+=1
                            if selected_num==2:
                                selected_num=0
                                for t,i in enumerate(objects):
                                    if i.id==selected_id[0]:
                                        a=i.weight
                                    if i.id==selected_id[1]:
                                        b=i.weight
                                tmp_cost=movement.merge(objects,selected_id,mode)
                                cost+=tmp_cost
                                info[0]="體重為"+str(a)+"的品庠對體重為"+str(b)+"的品庠說：「我要跟你merge」                "
                                info[1]="付出的代價："+str(tmp_cost)+"                 "
                                selected_id.clear()
                                break
        #pg.time.wait(10)
        if game_end:
            font = pg.font.SysFont("microsoftjhenghei", 32)
            text = font.render("恭喜你完成了！", True, (0,0,0), (255,255,255))
            screen.blit(text, (100,400))
            pg.display.flip()
        elif (pg.time.get_ticks()-start_ticks)//1000>=3:
            font = pg.font.SysFont("microsoftjhenghei", 128)
            text = font.render("        時間到！        ", True, (0,0,0), (255,255,255))
            screen.blit(text, (0,250))
            font = pg.font.SysFont("microsoftjhenghei", 32)
            text = font.render("時間：", True, (0,0,0), (255,255,255))
            screen.blit(text, (800,20))
            font = pg.font.SysFont("couriernew", 32)
            text = font.render(str(0).rjust(3), True, (0,0,0), (255,255,255))
            screen.blit(text, (890,27))
            pg.display.flip()
        elif (pg.time.get_ticks()-start_ticks)//1000<=120:
            update(screen)
    pg.quit()

if __name__ == "__main__":
    main(sys.argv[1:])