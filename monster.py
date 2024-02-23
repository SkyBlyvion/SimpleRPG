import random
import pygame
import animation

# on cree la classe player
class Monster(animation.AnimateSprite):# classe Monster qui herite de la classe Sprite de Pygame

    def __init__(self, game): # j initialise la classe
        super().__init__("monster") # je recupere de la classe mere
        self.game = game
        self.health = 100 # j initialise la vie
        self.max_health = 100 # j initialise la vie max
        self.image = pygame.image.load("assets/monster.png") # j initialise l image
        self.rect = self.image.get_rect() # j initialise le rectangle de l image (rectangle = display de l image)
        self.rect.x = 1000 + random.randint(0, 300) # j initialise la position x
        self.rect.y = 525 # j initialise la position y
        self.attack = 0.5 # j initialise l attaque à 10
        self.velocity = random.randint(2, 5) # j initialise la vitesse du monstre
    
    def damage(self, attack):
        self.health -= attack 
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 5)
            self.game.score += 16

    def move(self): 
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack) # we add the damage attack to the monsster
    
    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        bar_color = (11, 210, 46) # vert
        bg_bar_color = (250, 0, 0) # red

        bar_position = [self.rect.x, self.rect.y-20, self.health, 5] 
        bg_bar_position = [self.rect.x, self.rect.y-20, self.max_health, 5]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

        if self.rect.x < 0: # if monster at the edge of the screen we remove it
            self.remove()