import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Catch Me!")

box_x = 250
box_y = 250
box_h = 80
box_w = 80
speed = 5 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        box_x = box_x-speed
    if keys[pygame.K_RIGHT]:
        box_x = box_x+speed
    if keys[pygame.K_UP]:
        box_y = box_y-speed
    if keys[pygame.K_DOWN]:
        box_y = box_y+speed
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,0,0),(box_x,box_y,box_w,box_h))

    pygame.display.flip()
    pygame.time.delay(13)