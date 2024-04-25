import pygame
import random

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("meu joguinho")

bg = pygame.image.load('jogo1.jpg').convert_alpha() 
bg = pygame.transform.scale(bg, (x, y))

alien = pygame.image.load('alien.png').convert_alpha()
alien = pygame.transform.scale(alien, (50, 50))

player = pygame.image.load('aeronave.png').convert_alpha()
player = pygame.transform.scale(player, (50, 50))
player = pygame.transform.rotate(player, -90)

missil = pygame.image.load('missil.png').convert_alpha()
missil = pygame.transform.scale(missil, (25, 25))
missil = pygame.transform.rotate(missil, -45)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 300

pontos = 3

triggered = False 

rodando = True

font = pygame.font.SysFont('Keystone-Regular.otf', 50)

player_rect = player.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()

# Funções

def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x,y]


def respawn_missil():
    global triggered, vel_missil_x
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return [respawn_missil_x, respawn_missil_y]

def colisions():
    global pontos
    if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
        pontos -=1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos += 1
        return True
    else:
        return False
    

while rodando: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width  
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))  
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    # Teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 1
        if not triggered: 
            pos_missil_y -= 1

    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 1
        if not triggered: 
            pos_missil_y += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 2

    if pontos == -1:
        rodando = False

    # Respawn do alienígena
    if pos_alien_x <= 0:
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]

    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y = respawn_missil()

    
    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn () [1]


    #posição do rect 

    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.x = pos_missil_x
    missil_rect.y = pos_missil_y

    alien_rect.x = pos_alien_x
    alien_rect.y = pos_alien_y

    # Movimento
    x -= 2
    pos_alien_x -= 1

    pos_missil_x += vel_missil_x

    pygame.draw.rect(screen, (255,0,0), player_rect, 4)
    pygame.draw.rect(screen, (255,0,0), missil_rect, 4)
    pygame.draw.rect(screen, (255,0,0), alien_rect, 4)

    score = font.render(f'Pontos: {int(pontos)}', True, (0,0,0))
    screen.blit(score, (50,50))

    screen.blit(alien, (pos_alien_x, pos_alien_y))  
    screen.blit(missil,(pos_missil_x, pos_missil_y))
    screen.blit(player, (pos_player_x, pos_player_y))

    print(pontos)

    pygame.display.update()


baseando no vídeo : https://www.youtube.com/watch?v=mNjcrarT3Io
