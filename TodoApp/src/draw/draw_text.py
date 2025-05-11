"""Draws text on screen with pygames' screen.blit function"""
import pygame
import texts.firstscreen_text as texts

def draw_text(screen,textt,x,y):
    """Draws text on screen """
    font = pygame.font.Font('freesansbold.ttf', 18)
    img = font.render(str(textt), True, 'black')
    screen_blit = screen.blit(img, (x, y))
    return screen_blit

def print_money(screen,money):
    """Prints the amount of money on screen"""
    draw_text(screen,"Rahat(€): "+money,550,350)

def draw_phase0_1(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen, texts.phase0_11(),10,10)
    draw_text(screen, texts.phase0_12(),10,25)
    draw_text(screen,texts.phase0_13(),10,40)

def draw_phase1_1(screen,name):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.say_hi(name),10,10)
    draw_text(screen,texts.phase1_11(),10,25)
    draw_text(screen,texts.phase1_12(),10,40)

def draw_phase2(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase2_1(),10,10)

def draw_phase3_1(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase3_1(),10,10)

def draw_phase3_2(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase3_2(),10,10)

def draw_phase3_3(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase3_3(),10,10)

def draw_phase3_4(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase3_4(),10,10)

def draw_phase3_5(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase3_5(),10,10)

def draw_phase3_6(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase3_6(),10,10)

def draw_phase3_7(screen):
    """Draws all corresponding text lines for phasex_y (x=phase, y= y_th subphase)"""
    draw_text(screen,texts.phase3_7(),10,10)
