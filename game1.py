# Imports
import pygame
from sys import exit


# Initialize pygame
pygame.init()

# Creates a display surface
screen = pygame.display.set_mode((800,400))
# Changed the program window title. Displayed ontop of the display surface. 
pygame.display.set_caption("Game1 : V0.0.2")

# Sets the variable clock to time.Clock. Which is used to control the game clock for 
# how fast to runt he game
clock = pygame.time.Clock()

# Applies the specified font to the variable test_font. 
test_font  = pygame.font.Font("font/Pixeltype.ttf", 50)

# This is a test regular surface. It has a width of 100 and a height of 200.
# test_surface = pygame.Surface((100,200))
# test_surface.fill("Red")

# This loads the img sky to the variable sky_img.
sky_img = pygame.image.load("graphics/Sky.png").convert()

# This loads the ground img and assigns it to the variable ground_img.
ground_img = pygame.image.load("graphics/ground.png").convert()

# This loads the snail img and assigns it to the variable snail_img.
snail_img =pygame.image.load("graphics/snail/snail1.png").convert_alpha()
# Snails x position.
snail_x_pos = 800

# Creates a text text variable that uses the render method on the test_font variable.
# Dont not use anti alias and uses the black color.
text_surface = test_font.render("Test Text", False, "black")                         

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

    # This uses the clock variable to control the max tick rate of the game. 
    # The tick rate is how many times a second the game updated. 
    # This variable and method don't control the minimum tick rate only the max or "ceiling".
    clock.tick(60)     

    # Places the image sky_ig ontop of the display surface at position 0,0 as a regular surface.
    screen.blit(sky_img, (0,0))

    # Places the image ground_img ontop of the display surface as a regular surface at postion 
    screen.blit(ground_img,(0,300))

    # Places the text stored in the variable text_surface on the display surface. 
    screen.blit(text_surface, (300,50))

    # Places the image snail_img ontop of the display surface and moves it x 1 pixel each frame. 
    snail_x_pos += -4
    screen.blit(snail_img,(snail_x_pos,265))
    if snail_x_pos < -10:
       snail_x_pos = 800
    
    # Draws all elements
    # Updated everything
    pygame.display.update()


