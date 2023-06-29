import pygame as pg
import config
import movement
import object
import sys
instructs=['123','Merge的代價為兩者體重乘積','Merge的代價為兩者體重加起來','Merge的代價為兩者體重較小的','Merge的代價為兩者體重較大的','Merge的代價為兩者體重差距']
def update(screen):
    screen.fill(config.background_color)
    font = pg.font.SysFont("microsoftjhenghei", 32)
    text = font.render(instructs[mode], True, (0,0,0), (255,255,255))
    screen.blit(text, (250,20))
    for i in objects:
        i.draw(screen)
    
    pg.display.flip()


def main(argv):
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
    update(screen)
    while run:
        for event in pg.event.get():
            #print(event)
            if event.type == pg.QUIT:
                run = False
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