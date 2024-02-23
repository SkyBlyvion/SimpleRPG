import math
import pygame
from game import Game

# Initialize pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

# initialize clases
game = Game()

pygame.display.set_caption("CSGO_2") # set the display and the title
screen = pygame.display.set_mode((1080, 700)) # call the display and set it to 1080x720

background = pygame.image.load("assets/fondEcran.png") # need to load the image before displaying it

banner = pygame.image.load("assets/banner2.png")
banner = pygame.transform.scale(banner, (400, 520))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.3)
banner_rect.y = math.ceil(screen.get_width() / 7)

play_button = pygame.image.load("assets/button5.png")
play_button = pygame.transform.scale(play_button, (150, 50))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.4)
play_button_rect.y = math.ceil(screen.get_width() / 5.2)

# collidepoint
running = True

while running: # Boucle while qui s execute tant que true
    #mise a jour de l affichage
    screen.blit(background, (0,95)) # apply the image to the display at coordinates

    if game.is_playing:
        game.update(screen)
    else :
        screen.blit(banner, (banner_rect.x, banner_rect.y))
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))

    pygame.display.flip() # 

    # gestion des events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Arette de jouer, va payer tes impôts")
        elif event.type == pygame.KEYDOWN: # si une touche est appuye
            game.pressed_keys[event.key] = True # j ajoute dans le tableau true

            if event.key == pygame.K_SPACE: # move here, was at bottom
                game.player.launch_bullets()
                game.player.launch_spell()
                game.sounds.play("tir")
            
        elif event.type == pygame.KEYUP: # si une touche est relache
            game.pressed_keys[event.key] = False # je modifie le tableau en false

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

        
    clock.tick(FPS)