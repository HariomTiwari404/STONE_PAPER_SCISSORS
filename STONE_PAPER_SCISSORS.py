import pygame
import sys
from pygame.locals import *
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.hand_animation_first_range = {
            'stone': list(range(1, 24)),
            'scissors': list(range(24, 66)),
            'paper': list(range(66, 104)),
        }
        self.computer_choices = ["stone", "scissors", "paper"]
        self.result_range = {
            'scissors': list(range(1, 52)),
            'stone': list(range(52, 103)),
            'paper': list(range(103, 150)),
        }
        self.current_hand_animation = None
        self.current_hand_animation_frame = 1
        self.hand_animation_played_once = False
        self.second_time_hand_range_adjusted = False
        self.image = None  # Initialize image in the update method
        self.rect = None

        self.set_animation('stone')  # Set the default animation to 'stone'

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        self.frames_to_skip = 16  # Number of frames to skip
        self.second_time_hand_range_adjusted = False
        self.result = None
        self.computer_choice = None
        self.player_choice = None



    def show_computer_choice(self, computer_choice, speed):
        if computer_choice in self.result_range:
            hand_frame_index = int(self.current_hand_animation_frame) % len(self.result_range[computer_choice])
            filename_of_hand_images = f'images2/gifFile 2-{self.result_range[computer_choice][hand_frame_index]} (dragged).tiff'
            self.image = pygame.image.load(filename_of_hand_images)
            self.rect = self.image.get_rect()  # Update rect here
            self.current_hand_animation_frame += speed
        else:
            print("Error: Invalid computer choice.")
      
    


    def set_animation(self, animation_name):
        
        if animation_name != self.current_hand_animation:
            self.hand_animation_played_once = False
            self.second_time_hand_range_adjusted = False
        self.current_hand_animation = animation_name
        self.current_hand_animation_frame = 1

        self.update_image()

    def update_image(self):
        if self.current_hand_animation:
            hand_frame_index = int(self.current_hand_animation_frame) % len(self.hand_animation_first_range[self.current_hand_animation])
            filename_of_hand_images = f'images/gifFile-{self.hand_animation_first_range[self.current_hand_animation][hand_frame_index]} (dragged).tiff'
            self.image = pygame.image.load(filename_of_hand_images)
            self.rect = self.image.get_rect()  

    def update(self, speed):
        if self.current_hand_animation :

            

            self.current_hand_animation_frame += speed



            if not self.hand_animation_played_once and self.current_hand_animation_frame >= len(self.hand_animation_first_range[self.current_hand_animation]):
                self.hand_animation_played_once = True
                self.current_hand_animation_frame = 1



            if self.hand_animation_played_once:
                  

               


                if not self.second_time_hand_range_adjusted and self.current_hand_animation == 'stone':
                    self.hand_animation_first_range['stone'] = list(range(1, 24))
                    self.second_time_hand_range_adjusted = True


                    
                        
                if not self.second_time_hand_range_adjusted and self.current_hand_animation == 'scissors':
                    self.hand_animation_first_range['scissors'] = list(range(34, 66))
                    self.second_time_hand_range_adjusted = True


                   
                    
                elif not self.second_time_hand_range_adjusted and self.current_hand_animation == 'paper':

                
                        
                    self.hand_animation_first_range['paper'] = list(range(77, 104))
                    self.second_time_hand_range_adjusted = True

            self.update_image()

    def determine_winner(self, player_choice, computer_choice):
        self.computer_choice = computer_choice

       

        if player_choice == computer_choice:
            self.result = "DRAW"
            
        else:
            player_choice_value = self.hand_animation_first_range.get(player_choice)

            if player_choice_value is not None:
                player_choice_key = next((key for key, value in self.hand_animation_first_range.items() if value == player_choice_value), None)
                
                if player_choice_key is not None:
                    if (
                        (player_choice_key == 'scissors' and computer_choice == "stone") or
                        (player_choice_key == 'stone' and computer_choice == "paper") or
                        (player_choice_key == 'paper' and computer_choice == "scissors")
                    ):
                        self.result = "COMPUTER WON!"
                    elif (
                        (player_choice_key == 'scissors' and computer_choice == "paper") or
                        (player_choice_key == 'stone' and computer_choice == "scissors") or
                        (player_choice_key == 'paper' and computer_choice == "stone")
                    ):
                        self.result = "YOU WON!"
                else:
                    print("Error: Player choice not found in hand_animation_first_range.")
            else:
                print("Error: Player choice not found in hand_animation_first_range.")


    
# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1200
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

#Font setup
font = pygame.font.SysFont(None, 30)  

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(0, 0)
moving_sprites.add(player)
game_active = True

external_font_path2 = "fonts/winner5.ttf"  
external_font2 = pygame.font.Font(external_font_path2, 20)



external_font_path3 = "fonts/winner3.ttf"  
external_font3 = pygame.font.Font(external_font_path3, 20)


external_font_path = "fonts/winner3.ttf"  
external_font = pygame.font.Font(external_font_path, 36)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_s:
                player.set_animation('stone')
            elif event.key == pygame.K_p:
                player.set_animation('paper')
            elif event.key == pygame.K_c:
                player.set_animation('scissors')
            elif (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):

                player.computer_choice = random.choice(player.computer_choices)
                player.player_choice = player.current_hand_animation  # Use current_hand_animation to get player's choice
                player.determine_winner(player.player_choice, player.computer_choice)
                game_active = False

                
            elif event.key == pygame.K_SPACE:

                
                # Reset relevant variables for a new game
                game_active = True
                player.current_hand_animation = None
                player.hand_animation_played_once = False
                player.second_time_hand_range_adjusted = False
                player.current_hand_animation_frame = 1
                player.result = None
                player.computer_choice = None
                player.player_choice = player.current_hand_animation
                player.set_animation('stone')
                
    

    computer_choices = ["stone", "scissors", "paper"]
    player_choices = None
    
 


   

   # Drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.2)

    
    # Render the text as usual
    current_choice_text = external_font.render(f"Your Choice: {player.current_hand_animation}", True, (0, 0, 0))
    previous_computer_choice_text = external_font.render(f"Computer's choice : {player.computer_choice}", True, (0, 0, 0))
  

    # Rotate and blit the texts directly
    rotated_text1 = pygame.transform.rotate(current_choice_text, -2)
    rotated_text2 = pygame.transform.rotate(previous_computer_choice_text, -3)
  

    # Blit the rotated texts at their respective positions
    screen.blit(rotated_text1, (15, 47))
    screen.blit(rotated_text2, (400, 60))

    

    if not game_active and player.result != None:
         previous_result_text = external_font.render(f"{player.result}", True, (255, 255, 255))
         rotated_text3 = pygame.transform.rotate(previous_result_text, -1)
         screen.blit(rotated_text3, (680, 200))


   
    
    # Display result and play again message
    if not game_active:
        lines = ["PRESS", "SPACE", "TO", "RESET"]
        y_position = 250

        for line in lines:
            play_again_text = external_font2.render(line, True, (255, 255, 255))
            
            # Rotate the text surface by 2 degrees
            rotated_text = pygame.transform.rotate(play_again_text, 1)
            
            # Get the rotated rectangle and its position
            rotated_rect = rotated_text.get_rect( topleft=(680, y_position))
            
            # Draw the rotated text on the screen
            screen.blit(rotated_text, rotated_rect.topleft)
            
            y_position += rotated_rect.height


    if  game_active:
        lines = ["PRESS", "ENTER", "TO", "SUBMIT"]
        y_position = 250

        for line in lines:
            play_again_text = external_font2.render(line, True, (40, 40, 40))
            
            # Rotate the text surface by 2 degrees
            rotated_text = pygame.transform.rotate(play_again_text, 2)
            
            # Get the rotated rectangle and its position
            rotated_rect = rotated_text.get_rect(topleft=(680, y_position))

            # Draw the rotated text on the screen
            screen.blit(rotated_text, rotated_rect.topleft)
            
            y_position += rotated_rect.height


        lines1 = ["SCISSORS : Press C","STONE : Press S","PAPER : Press P"]
        y_position1 = 150

        for line1 in lines1:
            play_again_text = external_font3.render(line1, True, (0, 0, 0))
            
            # Rotate the text surface by 2 degrees
            rotated_text = pygame.transform.rotate(play_again_text, -1)
            
            # Get the rotated rectangle and its position
            rotated_rect = rotated_text.get_rect(topleft=(680, y_position1))

            # Draw the rotated text on the screen
            screen.blit(rotated_text, rotated_rect.topleft)
            
            y_position1 += rotated_rect.height


     
    

            

    if  player.computer_choice == "stone":
        player.show_computer_choice("stone", 0.2)
        


    elif  player.computer_choice == "scissors":
        player.show_computer_choice("scissors", 0.2)
    elif  player.computer_choice == "paper":
        player.show_computer_choice("paper", 0.2)


   


    pygame.display.flip()
    clock.tick(60)
