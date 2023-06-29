import pygame as pg
import config
import movement
import object

objects={object.pinxiang(1,2,config.object_width,config.object_height,50,50)}

def update(screen):
    screen.fill(config.background_color)
    for i in objects:
        i.draw(screen)
    pg.display.flip()


def main():
    pg.init()
    screen = pg.display.set_mode((config.width, config.height))
    pg.display.set_caption('我要跟你 merge')
    update(screen)
    
    run = True
    while run:
        for event in pg.event.get():
            #print(event)
            if event.type == pg.QUIT:
                run = False
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
    main()