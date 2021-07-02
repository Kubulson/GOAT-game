import pygame

SCREEN_SIZE = (1280, 720)
LIGHT_BLUE = (51, 141, 196)
DARK_GREEN = (55, 138, 52)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Nazwa_Gry')

#postać
player_image = pygame.image.load('dinozaur/vita_00.png')
player_x = 300

#platforms
platform = pygame.Rect(100,300,400,50)
platform1 = pygame.Rect(600, 250, 200, 50)

running = True
while running:

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #controls (keybinds, player's speed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= 3
    if keys[pygame.K_d]:
        player_x += 3

    #background
    screen.fill((0, 0, 0))
    background = pygame.image.load('backgrounds/hallow.jpg')
    screen.blit(background, (0,0))

    #drawing platforms
    pygame.draw.rect(screen, DARK_GREEN, platform)
    pygame.draw.rect(screen, DARK_GREEN, platform1)

    #player
    screen.blit(player_image, (player_x,250))

    #screen
    pygame.display.flip()

#fps limit
clock = pygame.time.Clock()
clock.tick(60)

#quit
pygame.quit()
