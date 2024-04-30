import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animations = {
            'stone': list(range(1, 24)),
            'paper': list(range(24, 66)),
            'scissors': list(range(66, 104)),
            # Add more animations as needed
        }
        self.current_animation = None
        self.current_frame = 1
        self.played_once = False
        self.second_time_range_adjusted = False

        self.image = None  # Initialize image in the update method
        self.rect = None

        self.set_animation('stone')  # Set the default animation to 'stone'

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def set_animation(self, animation_name):
        if animation_name != self.current_animation:
            # Reset the flag to play the animation from the beginning
            self.played_once = False
            self.second_time_range_adjusted = False

        self.current_animation = animation_name
        self.current_frame = 1
        self.update_image()

    def update_image(self):
        if self.current_animation:
            frame_index = int(self.current_frame) % len(self.animations[self.current_animation])
            filename = f'images/gifFile-{self.animations[self.current_animation][frame_index]} (dragged).tiff'
            self.image = pygame.image.load(filename)

    def update_animation(self, speed):
        if self.current_animation:
            self.current_frame += speed

            if not self.played_once and self.current_frame >= len(self.animations[self.current_animation]):
                # Play the entire animation for the first time
                self.played_once = True
                self.current_frame = 1

            if self.played_once:
                # Adjust the range for 'scissors' during the second time
                if not self.second_time_range_adjusted and self.current_animation == 'scissors':
                    self.animations['scissors'] = list(range(77, 104))
                    self.second_time_range_adjusted = True

                # Adjust the range for 'paper' during the second time
                elif not self.second_time_range_adjusted and self.current_animation == 'paper':
                    self.animations['paper'] = list(range(34, 66))
                    self.second_time_range_adjusted = True

                if self.current_frame >= len(self.animations[self.current_animation]):
                    # Reset the flags and animation range for subsequent plays
                    self.played_once = False
                    self.second_time_range_adjusted = False
                    self.current_frame = 1

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.set_animation('stone')
            elif event.key == pygame.K_c:
                self.set_animation('paper')
            elif event.key == pygame.K_p:
                self.set_animation('scissors')

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(0, 0)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        player.handle_events(event)

    # Update animation and check for key press
    player.update_animation(0.2)

    # Drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

