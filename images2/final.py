import pygame
import sys
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.hand_animation_first_range = {
            'stone': list(range(1, 24)),
            'paper': list(range(24, 66)),
            'scissors': list(range(66, 104)),}
            # Add more animations as needed
        self.current_hand_animation = None
        self.current_hand_animation_frame = 1
        self.hand_animation_played_once = False
        self.set_animation('stone') # Set the default animation to 'stone'
        self.rect = self.image.get_rect() 
        self.rect.topleft = [pos_x, pos_y] #position for the sprite
        self.second_time_hand_range_adjusted = False


    def set_animation(self, animation_name): # it is setting the animation from start when switched 
        self.current_hand_animation = animation_name
        self.current_hand_animation_frame = 1
        if animation_name != self.current_hand_animation: #we are reseting to hand_animation_first_range so after switching whole animation will be played again if we comeback
            self.hand_animation_played_once = False
            self.second_time_hand_range_adjusted = False

        self.update_image() #dont know why calling this

    
    def update_image(self):
        if self.current_hand_animation: #something is playing

            hand_frame_index = int(self.current_hand_animation_frame) % len(self.hand_animation_first_range[self.current_hand_animation]) 
            filename_of_hand_images = f'images/gifFile-{self.hand_animation_first_range[self.current_hand_animation][hand_frame_index]} (dragged).tiff'
            self.image = pygame.image.load(filename_name_of_hand_images)

    def update(self, speed):
        if self.current_hand_animation:
            self.current_hand_animation_frame += speed 

            if not self.hand_animation_played_once and self.current_hand_animation_frame >= len(self.hand_animations[self.current_hand_animation]):
                self.hand_animation_played_once = True
                self.current_hand_animation_frame = 1

        






        

        

