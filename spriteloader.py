import pygame, json, os

# Grabs the file path to the main python file
filedir = os.path.dirname("__main__")

# This file is used for dealing with sprite sheets.


class Spritesheet:
    def __init__(self, filename):
        # Gets the filepath and the spreadsheet image
        self.filepath = os.path.join(filedir, "sprites", filename)
        self.spritesheet = pygame.image.load(self.filepath).convert()

        # Replaces filename's extension with .json
        self.filepath = self.filepath.replace(".png", ".json")

        # Opens hoursheet.json and saves the list into self.metadata
        with open(self.filepath) as f:
            self.metadata = json.load(f)
            f.close()

    def getSprite(self, x, y, w, h):
        # Sets up the sprite Surface and color key.
        sprite = pygame.Surface((w, h))
        # Decides what color will be transparent
        sprite.set_colorkey((0, 0, 0))
        # Draws spritesheet onto the sprite with the area being x, y, w, h
        sprite.blit(self.spritesheet, (0, 0), (x, y, w, h))

        return sprite

    def parseSprite(self, filename):
        # Stores the frame data of specified filename.
        frame = self.metadata["frames"][filename]["frame"]
        # Store the positional data of frame into seperate variables
        x, y, w, h = frame["x"], frame["y"], frame["w"], frame["h"]
        # Calls getSprite using previous variables
        image = self.getSprite(x, y, w, h)

        return image
