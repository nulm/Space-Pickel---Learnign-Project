# Imports
import pygame
from sys import exit
from random import randint


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

# Enemy spawn / delete and move function.
def obstacle_movement(obstacle_list):
  if obstacle_list:
    for obstacle_rect in obstacle_list:
      obstacle_rect.x -= 2
      
      if obstacle_rect.bottom == 300:
        screen.blit(snail_img,obstacle_rect)
      else:
        screen.blit(fly_surf,obstacle_rect)

    # This list comprehension will only copy the elements within the obstacle_list 
    # if the elements x cords are greater than -10. If less than -10 the element wont
    # be copied making sure the list does not become a memeory leak. 
    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -10]
    # Returns the obstacle_list. 
    return obstacle_list
  # This else statment needs to be here. Otherwise the game will crash on the first game.
  # As the list will return none.
  else:
    return []


# Player / enemy collision detection.
def collisions(player, obstacles):
  if obstacles:
    for obstacles_rect in obstacles:
      if player.colliderect(obstacles_rect):
        return False
  return True

# Initialize pygame
pygame.init()

# Creates a display surface
screen = pygame.display.set_mode((800,400))
# Changed the program window title. Displayed ontop of the display surface. 
pygame.display.set_caption("Game1 : V0.2.0")

# Game states
game_active = False
# This is used to set to score back to 0 when the game starts. 
start_time = 0
score = 0 
# Sets the variable clock to time.Clock. Which is used to control the game clock for 
# how fast to runt he game
clock = pygame.time.Clock()

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

# Enemy surfaces and rectangles beloew:
# This loads the snail img and assigns it to the variable snail_img.
# Creates a  rectangle for the snail.
snail_img = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# Snail_rect is no longer neeeded as the rect is created in the event loop.
#snail_rect = snail_img.get_rect(bottomright = (850,300))
# Loads teh fly image and assigns it to variable fly_surf.
# Creates a rectangle for the fly. 
fly_surf = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
# fly_rect is no longer needed as the rect is created in teh event loop. 
#fly_rect = fly_surf.get_rect(bottomright = (850, 200))

obstacle_rect_list = []


# Player surfaces and rectangles beloew:
# Import the player img/surface. And creates the player rectangle.
player_img = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_img.get_rect(midbottom = (80,300))

# Intro / End game screen player character sprite.
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2.0)
player_stand_rect = player_stand.get_rect(center = (400,200))
# Text in intro screen:
# Game Title
game_name = test_font.render("Python Game - V0.2.0",False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,60))
# Text to start game:
game_start_text = test_font.render("Press Space To Start!",False, (111,196,169))
game_start_rect = game_start_text.get_rect(center = (400, 380))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)


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

# Gravity stuff:
player_gravity = 0                         

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
          if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
              print("mosue hits player")
              if player_rect.bottom == 300:
                player_gravity = -30
          # Event loop logic to check if a key is pressed. 
          if event.type == pygame.KEYDOWN:
            print("keydown")
            if event.key == pygame.K_SPACE:
                print("space has been pressed!")
                if player_rect.bottom == 300:
                  player_gravity = -20
            # if event.key == pygame.K_a:
            #   player_rect.left -= 2
            # if event.key == pygame.K_d:
            #   player_rect.right += 2
          # Event loop for obstacle_timer:
          if event.type == obstacle_timer:
            print("obstacle_timer is active")
            # This is creating the rectangle of the fly or snail evey time the 
            # obsacle_timer is activated. It depends on a random number which one is spawned.
            # Then the rectangle is added (appended) to the obstacle_rect_list list. 
            if randint(0,2) == 0:
              obstacle_rect_list.append(snail_img.get_rect(bottomright = (randint(900,1100),300)))
            else:
              obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 160)))
        else:
          # Event loop logic to check if a key is pressed. And restart the game when the 
          # space key is pressed.
          if event.type == pygame.KEYDOWN:
            print("keydown")
            if event.key == pygame.K_SPACE:
                print("space has been pressed!")
                game_active = True
                player_rect.bottom = 300
                player_rect.left = 80
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
      player_gravity += 1
      player_rect.y += player_gravity
      if player_rect.bottom >= 300:
        player_rect.bottom = 300
      if player_rect.left <= 1:
        player_rect.left = 1
      if player_rect.right >= 799:
        player_rect.right = 799

      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
        player_rect.left -= 4
      if keys[pygame.K_d]:
        player_rect.right += 4
      
      # Places the image player_img ontop of the display surface.
      screen.blit(player_img,player_rect)

      # Obstacle movement
      obstacle_rect_list = obstacle_movement(obstacle_rect_list)
      

      # if player_rect.colliderect(snail_rect): 
      #    print("Collision")
      
      # Collisions
      # Ends game if player collids with enemy rectangle.
      game_active = collisions(player_rect,obstacle_rect_list)
      
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



