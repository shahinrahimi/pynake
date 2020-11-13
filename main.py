import pygame


pygame.init()

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
color = (255,0,0)
pos_size = pygame.Rect(50,50,100,100)
box = pygame.draw.rect(screen,color,(50,50,100,100))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()