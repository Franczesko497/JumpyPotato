import pygame
from random import randint
from sys import exit

pygame.init()
s = 4.2
game_active = -1

#SCREEN
screen = pygame.display.set_mode((960, 1280))
pygame.display.set_caption("Jumpy Potato")
clock = pygame.time.Clock()

#SURFACE
ground_y = 1112
ground = pygame.image.load('JumpyPotato/ground.png').convert()
ground_rect = ground.get_rect(topleft = (0, ground_y))

#SCORE
score_y = 50
score = 0
text_font = pygame.font.Font(None, 50)
text = text_font.render(f"Score: {score}", True, 'black')
text_s = text.get_rect(center = (480, score_y))

#POTATO
potato = pygame.image.load('JumpyPotato/potato.png').convert_alpha()
potato_x = 430
potato_y = 1000
potato_rect = potato.get_rect(topleft = (potato_x, potato_y))

#CLOUD1
c1 = 600
y1 = randint(100, 800)
cloud1 = pygame.image.load('JumpyPotato/cloud.png').convert_alpha()
cloud1_rect = cloud1.get_rect(topleft = (y1, c1))

#CLOUD2
c2 = 100
y2 = randint(100, 800)
cloud2 = pygame.image.load('JumpyPotato/cloud.png').convert_alpha()
cloud2_rect = cloud2.get_rect(topleft = (y2, c2))

#CLOUD3
c3 = -400
y3 = randint(100, 800)
cloud3 = pygame.image.load('JumpyPotato/cloud.png').convert_alpha()
cloud3_rect = cloud3.get_rect(topleft = (y3, c3))

#CLOUD4
c4 = -900
y4 = randint(100, 800)
cloud4 = pygame.image.load('JumpyPotato/cloud.png').convert_alpha()
cloud4_rect = cloud4.get_rect(topleft = (y4, c4))

#CLOUD5
c5 = -1400
y5 = randint(100, 800)
cloud5 = pygame.image.load('JumpyPotato/cloud.png').convert_alpha()
cloud5_rect = cloud5.get_rect(topleft = (y5, c5))

gravity = 0
sy = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if potato_rect.y >= 1280:
        game_active = False

    if game_active == -1:
        screen.fill((230, 225, 225))
        stext = pygame.font.Font(None, 150)
        start_text = stext.render("Jumpy Potato", True, 'black')
        screen.blit(start_text, (150, 300))
        space = pygame.font.Font(None, 50)
        space_text = space.render("Press SPACE to Start", True, 'black')
        screen.blit(space_text, (300, 900))
        potat = pygame.image.load('JumpyPotato/potato.png').convert_alpha()
        potat_scale = pygame.transform.scale(potat, (400, 350))
        screen.blit(potat_scale, (300, 500))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_active = 1

    if game_active == 1:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            potato_rect.x -= 15
            potato_x -= 15
        if keys[pygame.K_RIGHT]:
            potato_rect.x += 15
            potato_x += 15

        if(potato_x > 960):
            potato_x = 0-potato.get_width()  
            potato_rect.x = 0-potato.get_width()  
        elif(potato_x < 0-potato.get_width()):
            potato_x = 960 
            potato_rect.x = 960

        gravity += 0.35
        potato_rect.y += gravity

        if potato_rect.y >= ground_y-potato.get_width() and pygame.Rect.colliderect(potato_rect, ground_rect):
            potato_rect.y = ground_y-potato.get_width()
            gravity = -20

        for cloud_rect in [cloud1_rect, cloud2_rect, cloud3_rect, cloud4_rect, cloud5_rect]:
            if potato_rect.colliderect(cloud_rect) and potato_rect.y <= cloud_rect.y and gravity > 0:
                gravity = -20
                score += 1

        sy += s
        #potato_rect.y += s
        potato_y += s
        ground_y += s
        score_y += s
        c1 += s
        c2 += s
        c3 += s
        c4 += s
        c5 += s

        text = text_font.render(f"Score: {score}", True, 'black')
        screen.blit(screen, (0, sy))
        screen.fill('cyan')
        screen.blit(text, (400,30))
        screen.blit(ground, (0,ground_y))
        screen.blit(potato, potato_rect)

        screen.blit(cloud1, (y1, c1))
        cloud1_rect.y = c1
        screen.blit(cloud2, (y2, c2))
        cloud2_rect.y = c2
        screen.blit(cloud3, (y3, c3))
        cloud3_rect.y = c3
        screen.blit(cloud4, (y4, c4))
        cloud4_rect.y = c4
        screen.blit(cloud5, (y5, c5))
        cloud5_rect.y = c5
        if c1 > 1280:
            c1 -= 2500
            cloud1_rect.y -= c1
            y1 = randint(100, 800)
            cloud1_rect.x = y1
        if c2 > 1280:
            c2 -= 2500
            cloud2_rect.y -= c2
            y2 = randint(100, 800)
            cloud2_rect.x = y2
        if c3 > 1280:
            c3 -= 2500
            cloud3_rect.y -= c3
            y3 = randint(100, 800)
            cloud3_rect.x = y3
        if c4 > 1280:
            c4 -= 2500
            cloud4_rect.y -= c4
            y4 = randint(100, 800)
            cloud4_rect.x = y4
        if c5 > 1280:
            c5 -= 2500
            cloud5_rect.y -= c5
            y5 = randint(100, 800)
            cloud5_rect.x = y5
        #print(potato_rect.y, sy+1280, potato_rect.y >= 1280)
        #print(c1, clouds_rects_y[0].y, potato_y,sy)
        pygame.display.update()
        clock.tick(100)
    elif game_active == 0:
        screen.fill('black')
        game_over = pygame.font.Font(None, 125)
        game_over_t = game_over.render("GAME OVER", True, 'gold')
        screen.blit(game_over_t, (225, 450))
        game_score = pygame.font.Font(None, 75)
        game_score_m = game_score.render(f"SCORE: {score}", True, 'gold')
        screen.blit(game_score_m, (380, 550))
        game_over_text = text_font.render("[Press SPACE to Restart]", True, 'gold')
        screen.blit(game_over_text, (280, 680))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_active = 1
            potato_rect.y = 1000
            potato_x = 430
            potato_rect.x = potato_x
            gravity = 0
            score = 0
            c1, c2, c3, c4, c5 = 600, 100, -400, -900, -1400
            y1, y2, y3, y4, y5 = [randint(100, 800) for _ in range(5)]
            cloud1_rect.topleft = (y1, c1)
            cloud2_rect.topleft = (y2, c2)
            cloud3_rect.topleft = (y3, c3)
            cloud4_rect.topleft = (y4, c4)
            cloud5_rect.topleft = (y5, c5)
            ground_y = 1112
            ground_rect.topleft = (0, ground_y)