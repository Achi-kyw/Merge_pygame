import pygame as pg
import config
import movement
import object
import sys
from pygame.locals import *
instructs=['123','Merge的代價為兩者體重乘積','Merge的代價為兩者體重加起來','Merge的代價為兩者體重較小的','Merge的代價為兩者體重較大的','Merge的代價為兩者體重差距']

def update(screen):
    screen.fill(config.background_color)
    font = pg.font.SysFont("microsoftjhenghei", 32)
    text = font.render(instructs[mode], True, (0,0,0), (255,255,255))
    screen.blit(text, (250,20))
    font = pg.font.SysFont("microsoftjhenghei", 32)
    text = font.render("總花費："+str(cost), True, (0,0,0), (255,255,255))
    screen.blit(text, (250,config.height-50))
    for i in objects:
        i.draw(screen)
    #Merge 動畫寫在這裡
    pg.display.flip()


def main(argv):
    global selected_num
    global selected_id
    global cost
    selected_num=0
    selected_id=[]
    cost=0
    pg.init()
    screen = pg.display.set_mode((config.width, config.height))
    pg.display.set_caption('我要跟你 merge')
    global mode
    mode=int(argv[0])
    with open("testdata/"+str(mode)+".txt",'r') as f:
        global objects
        objects=[]
        for i,j in enumerate(f.read().split(' ')):
            objects.append(object.pinxiang(i,int(j),config.object_width,config.object_height,10+(config.object_width+10)*i,100,mode))
    run = True
    processing=False
    update(screen)
    while run:
        for event in pg.event.get():
            #print(event)
            if event.type == pg.QUIT:
                run = False
            elif len(objects)==1:
                pass
            #elif processing:
            #    pass
            elif event.type == MOUSEBUTTONUP:
                x,y=pg.mouse.get_pos()
                #print(x,y)
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
                                pass
                                processing=True
                                selected_num=0
                                cost+=movement.merge(objects,selected_id,mode)
                                selected_id.clear()
        #pg.time.wait(10)    
        update(screen)
                        
        #這裡寫滑鼠點選角色的部分
        '''
        for event in pg.event.get():
            #print(event)
            
            if event.type == pg.QUIT:
                run = False
            elif shot.win == False and event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    shot = Movement.up(shot)
                elif event.key == pg.K_DOWN:
                    shot = Movement.down(shot)
                elif event.key == pg.K_LEFT:
                    shot = Movement.left(shot)
                elif event.key == pg.K_RIGHT:
                    shot = Movement.right(shot)
            if shot.win:
                screen.fill(config.background_color)
                screen.blit(config.pic['win'], tuple_mul(tuple_mul((shot.width, shot.height), config.grid), 0.5))
                pg.display.flip()
            else:
                update(screen, shot)
            '''

    pg.quit()

if __name__ == "__main__":
    main(sys.argv[1:])