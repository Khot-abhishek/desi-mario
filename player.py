import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        #print('self.animations:',self.animations)
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        
        #player Movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        
        #player Status - idle/running/jumping....
        self.status = 'idle'
        self.facing_right = True

    def import_character_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
        
            self.animations[animation] = import_folder(full_path)    
    
    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x == 0:
                self.status = 'idle'
            else:
                self.status = 'run'
            
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
    
    def animate(self):
        animations = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animations):
            self.frame_index = 0
        image =  animations[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = self.jump_speed
    
    def update(self):
        self.get_input()
        self.get_status()
        self.animate()