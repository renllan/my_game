import pygame

def text_object(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(str, x, y, font_size, color,gameDisplay):
    largeText = pygame.font.Font('freesansbold.ttf', font_size)
    TextSurf, TextRect = text_object(str, largeText, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
def message_display(str, center, font_size, color,gameDisplay):
    largeText = pygame.font.Font('freesansbold.ttf', font_size)
    TextSurf, TextRect = text_object(str, largeText, color)
    TextRect.center = center
    gameDisplay.blit(TextSurf, TextRect)