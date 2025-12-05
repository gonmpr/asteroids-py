import pygame


def draw_text(screen, text, color, x, y):
    font = pygame.font.SysFont("Arial", 30)
    img = font.render(text, True, color)
    screen.blit(img, (x,y))
