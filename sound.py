import pygame

# we create a sound class and create a dictionnary of sounds
class SoundManager:

    def __init__(self):
        self.sounds = {
            'tir': pygame.mixer.Sound('assets/sounds/tir.ogg'),
            'game_over': pygame.mixer.Sound('assets/sounds/game_over.ogg')
        }

    def play(self, name): # we take dictionnary of sounds and play the sound
        self.sounds[name].play()
        
