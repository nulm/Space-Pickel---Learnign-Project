# Imports
import pygame
from sys import exit


# Initialize pygame
pygame.init()

# Creates a display surface
screen = pygame.display.set_mode((800,400))
# Changed the program window title. Displayed ontop of the display surface. 
pygame.display.set_caption("Game1 : V0.0.3")

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
snail_rect = snail_img.get_rect(bottomright = (850,300))

# Player surfaces and rectangles beloew:
# Import the player img/surface. And creates the player rectangle.
player_img = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_img.get_rect(midbottom = (80,300))

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
        if event.type == pygame.MOUSEBUTTONDOWN:
          if player_rect.collidepoint(event.pos):
            print("mosue hits player")
            if player_rect.bottom == 300:
              player_gravity = -20
        # Event loop logic to check if a key is pressed. 
        if event.type == pygame.KEYDOWN:
           print("keydown")
           if event.key == pygame.K_SPACE:
              print("space has been pressed!")
              if player_rect.bottom == 300:
                player_gravity = -20


    # This uses the clock variable to control the max tick rate of the game. 
    # The tick rate is how many times a second the game updated. 
    # This variable and method don't control the minimum tick rate only the max or "ceiling".
    clock.tick(60)     

    # Places the image sky_ig ontop of the display surface at position 0,0 as a regular surface.
    screen.blit(sky_img, (0,0))

    # Places the image ground_img ontop of the display surface as a regular surface at postion 
    screen.blit(ground_img,(0,300))

    # Places the text stored in the variable text_surface on the display surface. 
    pygame.draw.rect(screen,(200,255,249), background_rect)
    screen.blit(text_surface, text_rect)

    # Test to draw a line across the screen.
    # pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(),10)

    # Test to draw a circle
    #pygame.draw.ellipse(screen, "Brown", pygame.Rect(50,200,100,100))

    # Places the image snail_img ontop of the display surface and moves it's x 4 pixel each frame. 
    screen.blit(snail_img,snail_rect)
    snail_rect.x -= 4
    # Returns snail to starting position after leaving display surface.
    if snail_rect.x < -30:
       snail_rect.x = 850

    # Game loop player info:
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
       player_rect.bottom = 300
    
    # Places the image player_img ontop of the display surface.
    screen.blit(player_img,player_rect)
    

    # if player_rect.colliderect(snail_rect): 
    #    print("Collision")
    

    # Draws all elements
    # Updated everything
    pygame.display.update()


