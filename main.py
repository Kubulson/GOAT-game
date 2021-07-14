import pygame

SCREEN_SIZE = (1280, 720)
LIGHT_BLUE = (51, 141, 196)
DARK_GREEN = (55, 138, 52)
BROWN = (54, 4, 4)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Nazwa_Gry')

#character
player_image = pygame.image.load('dinozaur/vita_00.png')
player_x = 300

player_y = 0
player_speed = 0
player_acceleration = 0.2

#platforms
platforms = [
    #first platform
    pygame.Rect(100,300,400,50),
    #second platform
    pygame.Rect(100,250,50,50),
    #third platform
    pygame.Rect(450,250,50,50)

]

running = True
while running:

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #new player x, y postiion
    new_player_x = player_x
    new_player_y = player_y

    #controls, player's speed
    keys = pygame.key.get_pressed()
    #left
    if keys[pygame.K_a]:
        new_player_x -= 3
    #right
    if keys[pygame.K_d]:
        new_player_x += 3
    #jump
    if keys[pygame.K_w]:
        player_speed = -5

    #horizontal movement
    new_player_rect = pygame.Rect(player_x,new_player_y,72,72)
    x_collision = False

    #horizontal collisions
    for p in platforms:
        if p.colliderect(new_player_rect):
            x_collision = True
            break

    if x_collision == False:
        player_x = new_player_x

    #vertical movement
    player_speed += player_acceleration
    new_player_y += player_speed

    new_player_rect = pygame.Rect(player_x,new_player_y,72,72)
    y_collision = False

    #horizontal collisions
    for p in platforms:
        if p.colliderect(new_player_rect):
            y_collision = True
            player_speed = 0
            break

    if y_collision == False:
        player_y = new_player_y

    #background
    screen.fill((0, 0, 0))
    background = pygame.image.load('backgrounds/hallow.jpg')
    screen.blit(background, (0,0))

    #drawing platforms
    for p in platforms:
        pygame.draw.rect(screen, DARK_GREEN, p)

    #player
    screen.blit(player_image, (player_x,player_y))

    #screen
    pygame.display.flip()

#fps limit
clock = pygame.time.Clock()
clock.tick(60)

#quit
pygame.quit()
