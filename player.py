import pygame
import animation
from bullet import Bullet


# we create monster class
class Player(animation.AnimateSprite):# classe Player herit sprite

    def __init__(self, game): # init class
        super().__init__("player") # taking mother class
        self.game = game # init game to use it like for the collider
        self.image = pygame.image.load("assets/player.png") # init image/sprite
        self.rect = self.image.get_rect() # i init the hitbox for the image
        self.rect.x = 100 # init x pos
        self.rect.y = 530 # init y pos
        self.health = 100 # init health
        self.max_health = 100 # init max health
        self.attack = 10 # init attack 
        self.velocity = 5 # init speed
        self.all_bullets = pygame.sprite.Group() # we create a image group of all the bullets in pygame
        self.life = 3
        
    def move_right(self): # checks if there is no collision between the player (self) and any of the monsters (self.game.all_monster). if not then exec
        if not self.game.check_collision(self, self.game.all_monster): 
            self.rect.x += self.velocity

    def move_left(self): 
        self.rect.x -= self.velocity

    def update_animation(self):
        self.animate() # update animation call the animation function

    def update_health_bar(self, surface):
        bar_color = (11, 210, 46) # vert
        bg_bar_color = (250, 0, 0) # red

        bar_position = [self.rect.x, self.rect.y-20, self.health, 5] # bar position = player position + health bar + epaisseur 5
        bg_bar_position = [self.rect.x, self.rect.y-20, self.max_health, 5] # bar position = player position + health bar + epaisseur 5

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, attack):
        self.health -= attack
        if self.health <= 0:
            self.rect.x = 100 # init x pos
            self.health = self.max_health
            self.life -= 1

        if self.life == 0:
            self.game.game_over()

            
    def launch_bullets(self): # fonction who launch the bullet and add all bullets to the group
        self.all_bullets.add(Bullet(self))

    def launch_spell(self):
        self.all_bullets.add(Bullet(self))
        self.images = self.load_animation_images("spell")
        self.speed = 0.25
        

