import os
import pygame


class AnimateSprite(pygame.sprite.Sprite):
    
    def __init__(self, sprite_name): # we add 2 arguments/ parameters in the init
        super().__init__()
        self.sprite_name = sprite_name
        self.images = pygame.image.load(f'{sprite_name}/{sprite_name}01.png')
        self.current_image = 0
        self.image_to_take = 0
        self.images = self.load_animation_images(sprite_name)
        self.speed = 0.1
    
    def animate(self): # increment 1 beacause it star 0 ; 
        self.current_image += 1
        self.image_to_take = int(self.current_image*self.speed) # adapte la vitesse a laquelle les images sont chargés
        if self.image_to_take >= len(self.images):
            self.restore() # reset animation 6 to 0
        self.image = self.images[self.image_to_take]

    def restore(self): # reset animation, without, the curl doesnt curl
        self.current_image = 0
        self.speed = 0.1
        self.images = self.load_animation_images(self.sprite_name)
        self.image_to_take = int(self.current_image * self.speed) # i go back to the base image

    def load_animation_images(self, sprite_name):
        "thefuckareyoudoinghere"
        images = []
        path = f"{sprite_name}"
        folder = os.listdir(path)

        for file in folder :
            image_path = path + "/" + str(file)
            images.append(pygame.image.load(image_path))
            self.current_images = 0 # need to have it to 0 to avoid loading in a loop +1
        return images

