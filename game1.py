# Imports
import pygame
from sys import exit
from random import randint, choice

# Game Classes:
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    player_walk1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
    player_walk2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
    self.player_walk =[player_walk1, player_walk2]
    self.player_index = 0
    self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()
    self.image = self.player_walk[self.player_index]
    self.rect = self.image.get_rect(midbottom = (80,300))
    self.gravity = 0
    self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
  def player_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
      self.gravity = -20
      self.jump_sound.play()
      self.jump_sound.set_volume(0.5)

  def apply_gravity(self):
    self.gravity += 1
    self.rect.y += self.gravity
    if self.rect.bottom >= 300:
      self.rect.bottom = 300
  def animation_state(self):
    if self.rect.bottom < 300:
      self.image = self.player_jump
    else:
      self.player_index += 0.1
      if self.player_index >= len(self.player_walk):
        self.player_index = 0
      self.image = self.player_walk[int(self.player_index)]
  def update(self):
    self.player_input()
    self.apply_gravity()
    self.animation_state()
  
class Obstacle(pygame.sprite.Sprite):
  def __init__(self,type):
    super().__init__()

    if type == "fly":
      fly_frame1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
      fly_frame2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
      self.frames = [fly_frame1, fly_frame2]
      y_pos = 210
    else:
      snail_frame1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
      snail_frame2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
      self.frames = [snail_frame1,snail_frame2]
      y_pos = 300

    self.animation_index = 0
    self.image = self.frames[self.animation_index]
    self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

  def animation_state(self):
    self.animation_index += 0.1
    if self.animation_index >= len(self.frames):
      self.animation_index = 0
    else:
      self.image = self.frames[int(self.animation_index)]
  def update(self):
    self.animation_state()
    self.rect.x -= 6
    self.destroy()
  def destroy(self):
    if self.rect.x <= -100:
      self.kill()


# Functions for the game:
# Score function
def display_score():
  # Sets the score to 0 on game start while also showing the score in seconds.
  # Also converts to an integer so not to be a float.
  current_time = int(pygame.time.get_ticks() / 1000) - start_time
  score_surf = test_font.render(("Score: " + str(current_time)),False,(64,64,64))
  score_rect = score_surf.get_rect(center = (400,50))
  screen.blit(score_surf,score_rect)
  print(current_time)
  return current_time



# Player / enemy collision detection.
def collisions(player, obstacles):
  if obstacles:
    for obstacles_rect in obstacles:
      if player.colliderect(obstacles_rect):
        return False
  return True

def collision_sprite():
  if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
    obstacle_group.empty()
    return False
  else:
    return True


# Initialize pygame
pygame.init()

# Game music
music = pygame.mixer.Sound("audio/music.wav")
music.set_volume(0.5)
music.play()

# Creates a display surface
screen = pygame.display.set_mode((800,400))
# Changed the program window title. Displayed ontop of the display surface. 
pygame.display.set_caption("Space Pickel : V1.0.0")

# Game states
game_active = False
# This is used to set to score back to 0 when the game starts. 
start_time = 0
score = 0 
# Sets the variable clock to time.Clock. Which is used to control the game clock for 
# how fast to runt he game
clock = pygame.time.Clock()

# Groups:
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()


# Applies the specified font to the variable test_font. 
test_font  = pygame.font.Font("font/Pixeltype.ttf", 50)

# This is a test regular surface. It has a width of 100 and a height of 200.
# test_surface = pygame.Surface((100,200))
# test_surface.fill("Red")

# Environment surfaces and rectangles beloew: 
# This loads the img sky to the variable sky_img.
sky_img = pygame.image.load("graphics/Sky.png").convert()
# This loads the ground img and assigns it to the variable ground_img.
ground_img = pygame.image.load("graphics/ground.png").convert()

obstacle_rect_list = []

player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()

# Intro / End game screen player character sprite.
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2.0)
player_stand_rect = player_stand.get_rect(center = (400,200))
# Text in intro screen:
# Game Title
game_name = test_font.render("Space Pickel - V1.0.0",False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,60))
# Text to start game:
game_start_text = test_font.render("Press Space To Start!",False, (111,196,169))
game_start_rect = game_start_text.get_rect(center = (400, 380))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 300)



# Text Surfaces and rectangles below: 
# Creates a text text variable that uses the render method on the test_font variable.
# Dont not use anti alias and uses the black color.
text_surface = test_font.render("Test Text", False, (73, 80, 79))
text_rect = text_surface.get_rect(center = (400,50))
# Some logic for making the text_rect behind the text_surface a little bigger. 
padding = 2
background_rect = pygame.Rect(text_rect.left - padding,
                               text_rect.top - padding,
                               text_rect.width + 2 * padding,
                               text_rect.height + 2 * padding)
                      

# This is the games main while loop. It runs untill the exit() method stops the game inside
# the event for loop.
while True:
    
    # This for loop checks all events.
    # If the event is QUIT. Then the if statement. Will quit pygame.
    # The if statement will also run pygame.quit which stops the code from running.
    # Using the system package.  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if game_active == True:
          # Event loop logic to check if a key is pressed. 
          if event.type == pygame.KEYDOWN:
            print("keydown")
          if event.type == obstacle_timer:
            print("obstacle_timer is active")
            obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))
        else:
          # Event loop logic to check if a key is pressed. And restart the game when the 
          # space key is pressed.
          if event.type == pygame.KEYDOWN:
            print("keydown")
            if event.key == pygame.K_SPACE:
                print("space has been pressed!")
                game_active = True
                # Updates start_time to the amount of ticks when the player died. So it can be set
                # back to 0. 
                start_time = int(pygame.time.get_ticks() / 1000)
                obstacle_rect_list = []

    # Main game state.  
    if game_active:
      # Places the image sky_ig ontop of the display surface at position 0,0 as a regular surface.
      screen.blit(sky_img, (0,0))

      # Places the image ground_img ontop of the display surface as a regular surface at postion 
      screen.blit(ground_img,(0,300))

      # Places the text stored in the variable text_surface on the display surface. 
      # pygame.draw.rect(screen,(200,255,249), background_rect)
      # screen.blit(text_surface, text_rect)
      score = display_score()

      # Test to draw a line across the screen.
      # pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(),10)

      # Test to draw a circle
      #pygame.draw.ellipse(screen, "Brown", pygame.Rect(50,200,100,100))

      # Places the image snail_img ontop of the display surface and moves it's x 4 pixel each frame. 

      # Game loop player info:

      # This is to make sure the player can't leave the screen area. 
      player.draw(screen)
      player.update()

      obstacle_group.draw(screen)
      obstacle_group.update()

      game_active = collision_sprite()
      
    else:
      # Game over / start screen
      # Background color
      screen.fill((94,129,162))
      # Player character in middle of screen.
      screen.blit(player_stand,player_stand_rect)
      # Game title at top of screen
      screen.blit(game_name,game_name_rect)
      # Last game score below character.
      if score == 0:
        print("noting")
      else:
        last_score = test_font.render("Your last score: " + str(score), False, (111,196,169))
        last_score_rect = last_score.get_rect(center=(400,330))
        screen.blit(last_score,last_score_rect)
      #Instructions to start game.
      screen.blit(game_start_text,game_start_rect)

    # Draws all elements
    # Updated everything
    pygame.display.update()
    # This uses the clock variable to control the max tick rate of the game. 
    # The tick rate is how many times a second the game updated. 
    # This variable and method don't control the minimum tick rate only the max or "ceiling".
    clock.tick(60)   



