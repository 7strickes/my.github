import pygame
class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width_1, hight_1, scale, color):
        image = pygame.Surface((width_1, hight_1)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*width_1), 0, width_1, hight_1))
        image = pygame.transform.scale(image, (int(width_1 * scale), int(hight_1 * scale)))
        image.set_colorkey(color)
    
        return image