import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, player): # initialize bullet and add player to init to avoid player calling player
        super().__init__()
        self.player = player # we call the player to have access to self.player.game
        self.image = pygame.image.load("assets/bullet.png") # load image
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect() # initialize image
        self.rect.x = player.rect.x + player.rect.width 
        self.rect.y = player.rect.y + (player.rect.height * 0.5)
        self.velocity = 5
        self.angle = 0
        self.origine = self.image

    def remove(self):
        self.player.all_bullets.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origine, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

        # now we need to check collision with the monster and if there is one we remove the bullet
        for monster in self.player.game.check_collision(self, self.player.game.all_monster): # the game attribut is taken from player
            self.remove()
            monster.damage(self.player.attack, ) # when bullet touch monster, monster takes damage

        if self.rect.x > 1080:
            self.remove()


    
 


