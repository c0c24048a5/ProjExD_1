import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rect = kk_img.get_rect()
    
    

    x = 0
    keyx = 0
    keyy = 0
    kk_rect.center = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        keyx = -1
        keyy = 0
        
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            keyy -= 1
        if key_lst[pg.K_DOWN]:
            keyy += 1
        if key_lst[pg.K_RIGHT]:
            keyx += 2
        if key_lst[pg.K_LEFT]:
            keyx -= 2
        kk_rect.move_ip((keyx, keyy))
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [1600 + (-x), 0])
        screen.blit(bg_img, [3200 + (-x), 0])
        screen.blit(kk_img, kk_rect)
        pg.display.update()
        x += 1        
        clock.tick(200)
        if x == 3199:
            x = 0
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()