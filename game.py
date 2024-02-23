import pygame
from player import Player
from monster import Monster
from sound import SoundManager


class Game:
    def __init__(self): # no boucles in init 
        self.is_playing = False
        self.player = Player(self)
        self.all_players = pygame.sprite.Group() # i create a variable all_players group for player and then
        self.all_players.add(self.player) # i add the player
        self.all_monster = pygame.sprite.Group()
        # self.spawn_monster(3) # il n y aura que 2 monstres par defaut
        self.pressed_keys = {}
        self.score = 0
        self.sounds = SoundManager()

    def start(self):
        self.is_playing = True
        self.spawn_monster(3)
        self.life = 3
        # vie des monstres uici
    
    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.life = 3
        self.score = 0
        self.is_playing = False
        self.sounds.play("game_over")

    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)

        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (100, 100))

        font = pygame.font.SysFont("monospace", 16)
        life_text = font.render(f"Life : {self.player.life}", 1, (0, 0, 0))
        screen.blit(life_text, (120, 120))

        self.player.update_health_bar(screen)
        self.player.update_animation() # update animation
        
        self.player.all_bullets.draw(screen) # we draw the image group of all the bullets

        if self.pressed_keys.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width(): # if right is pressed and game.player not at the edge of the screen
            self.player.move_right()
        elif self.pressed_keys.get(pygame.K_LEFT) and self.player.rect.x > 0 : # if left is pressed and plauer not at the edge of the screen
            self.player.move_left()

        for bullet in self.player.all_bullets: # for each bullet in the group
            bullet.move()

        for monster in self.all_monster: # for each monster in the group
            monster.move()
            monster.update_health_bar(screen)
            monster.update_animation()
        self.all_monster.draw(screen)


    def spawn_monster(self, number):
        for _ in range(number):
            monster = Monster(self) # i added self to the global class here to be able to use game in monster
            self.all_monster.add(monster)
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
