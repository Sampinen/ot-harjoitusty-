"""Draws background art"""
import pygame

def draw_background(screen):
    """Draws the background"""
    image = pygame.image.load('src/draw/static/background.png')
    image = pygame.transform.scale(image, (1280, 720))
    screen.blit(image, (0, 0))
def draw_bird(screen):
    """Draws the bird"""
    image = pygame.image.load('src/draw/static/bird.png')
    image = pygame.transform.scale(image, (190, 178))
    screen.blit(image, (100, 400))

def draw_bottles(screen):
    """Draws the bottles"""
    image = pygame.image.load('src/draw/static/bottles.png')
    image = pygame.transform.scale(image, (254, 376))
    screen.blit(image, (390, 360))

def draw_character1(screen):
    """Draws a character"""
    image = pygame.image.load('src/draw/static/character1.png')
    image = pygame.transform.scale(image, (257, 515))
    screen.blit(image, (800, 100))

def draw_character2(screen):
    """Draws a character"""
    image = pygame.image.load('src/draw/static/character2.png')
    image = pygame.transform.scale(image, (160, 339))
    screen.blit(image, (1050, 150))

def draw_lawnmover(screen):
    """Draws a lawnmower"""
    image = pygame.image.load('src/draw/static/lawnmover.png')
    image = pygame.transform.scale(image, (341, 259))
    screen.blit(image, (100, 100))

def draw_player(screen):
    """Draws the player"""
    image = pygame.image.load('src/draw/static/player.png')
    image = pygame.transform.scale(image, (191, 227))
    screen.blit(image, (100, 100))

def draw_trash_can(screen):
    """Draws a trash can"""
    image = pygame.image.load('src/draw/static/trash_can.png')
    image = pygame.transform.scale(image, (171, 237))
    screen.blit(image, (500, 420))
