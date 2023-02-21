import pygame, time
from spriteloader import Spritesheet
from hourAnimation import HourGlass
running = True

'''=====================================================================================================================
This program tests handling spritesheets, and playing proper animation. I just felt like learning how to do this kind of
thing is very important to making any kind of game with graphics beyond simple, single colored shapes. I learned a bit
about how surfaces work and how many more uses they have. I think they can act as layers and you can chose area of an
image you want to draw when using "surface.blit", you can use this feature to get a specific image from a spritesheet.
I wonder what else I could do with Surfaces?

You are free to use this program as a reference for future projects

I had to follow a tutorial to figure out how to use spritesheets but I figured out the animation system on my own! The
previous animation prototype I wrote was kinda messy, and inefficient. Is there anything I could've done better?
====================================================================================================================='''
# Window Setup
pygame.init()
WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spritesheet Test")

# Canvas Setup
CANVAS = pygame.Surface((WIDTH, HEIGHT))

# Clock and FPS Setup
CLOCK = pygame.time.Clock()
PREV_TIME = time.time()
FPS = 60

# Colors
white = 255, 255, 255

# Declares the Hourglass sprite sheet.
hoursheet = Spritesheet("hoursheet.png")

# Saves every sprite needed for hourglass
# Is there a better way of doing this?
hourglassSprites = [
    hoursheet.parseSprite("hourglass0.png"),
    hoursheet.parseSprite("hourglass1.png"),
    hoursheet.parseSprite("hourglass2.png"),
    hoursheet.parseSprite("hourglass3.png"),
    hoursheet.parseSprite("hourglass4.png"),
    hoursheet.parseSprite("hourglass5.png"),
    hoursheet.parseSprite("hourglass6.png"),
    hoursheet.parseSprite("hourglass7.png")
]

# Creates hourglass instance
hourglass = HourGlass(
    sprite_list=hourglassSprites,
    x=200,
    y=200,
    size=100,
    prevtime=PREV_TIME
)

# Main game loop
while running:
    # Does stuff related to time. I already explained this a hundred times already
    CLOCK.tick(FPS)
    CURRENT_TIME = time.time()
    PREV_TIME = CURRENT_TIME

    # Refreshes the canvas
    CANVAS.fill(white)

    # Checks for game events.
    for event in pygame.event.get():
        # Allows the player to close the game.
        if event.type == pygame.QUIT:
            running = False

    # Updates hourglass
    hourglass.update(CANVAS, CURRENT_TIME)

    # Updates the screeen to display changes.
    SCREEN.blit(CANVAS, (0, 0))
    pygame.display.flip()
