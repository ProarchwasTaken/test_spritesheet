import pygame


# The HourGlass object that will hold the animation
class HourGlass:
    # The frame order for the animation
    order = [0, 1, 2, 3, 4, 5, 6, 7]

    def __init__(self, sprite_list, x, y, size, prevtime):
        self.sprites = sprite_list  # Stores sprite_list
        frame1 = self.sprites[0]  # Stores the first frame of sprite list

        # Gets the rect of the first frame and places the rect at the center.
        self.rect = frame1.get_rect()
        self.rect.topleft = x, y

        # Size of the image
        self.imageSize = size, size
        # Used for animation delay
        self.prev_time = prevtime
        self.delay = 0.1
        # Determines the current frame of the animation
        self.currentFrame = 0
        # The current index in order list
        self.index = 0

    def update(self, surface, current_time):

        self.animation(current_time)

        self.draw(surface)

    def animation(self, curTime):
        # Checks self.delay is over
        if curTime - self.prev_time >= self.delay:
            # If so then set self.currentFram to the list value of index
            self.currentFrame = HourGlass.order[self.index]

            # Increment index by 1
            self.index += 1
            # Wraps the value of index around if it's over the lenghth of order list
            self.index = self.index % len(HourGlass.order)

            self.prev_time = curTime

    # Draws and scales the image. According to self.size, and it's current frame.
    def draw(self, surface):

        surface.blit(pygame.transform.scale(
            surface=self.sprites[self.currentFrame],
            size=self.imageSize),
            self.rect
        )
