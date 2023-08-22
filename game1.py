# Imports
import pygame
from sys import exit


# Initialize pygame
pygame.init()

# Creates a display surface
screen = pygame.display.set_mode((800,400))
# Changed the program window title. Displayed ontop of the display surface. 
pygame.display.set_caption("Pygame : Game 1")

# Sets the variable clock to time.Clock. Which is used to control the game clock for 
# how fast to runt he game
clock = pygame.time.Clock()

# This is a test regular surface. It has a width of 100 and a height of 200.
test_surface = pygame.Surface((100,200))
test_surface.fill("Red")
                              

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

    # Places the surface "test_surface" ontop of the display surface at position 0,0.
    screen.blit(test_surface, (200,100))
    
    # Draws all elements
    # Updated everything
    pygame.display.update()


