import pygame
from constants import (
    SPRITE_SIZE,
    WINDOW_SIZE
)


def display_sentence(window, instance, extra=None):
    """
    Display the good menu (start menu, win menu or lose menu).

    :param window: window that the sentences will appear.
    :param instance: Is there the start menu or the win menu.
    """
    # Initialize fonts.
    small_font = pygame.font.SysFont("monospace", 20)
    little_font = pygame.font.SysFont("monospace", 40)
    big_font = pygame.font.SysFont("monospace", 80)
    # Initialize the color.null
    white_color = (255, 255, 255)
    red_color = (255, 0, 0)

    if instance == 'start':
        play_game = little_font.render("Press Enter to play", 1, white_color)
        quit_game = little_font.render("Press Escape to quit", 1, white_color)
        window.blit(play_game, (0, WINDOW_SIZE[0] - (WINDOW_SIZE[0] / 1)))
        window.blit(quit_game, (0, WINDOW_SIZE[0] - (WINDOW_SIZE[0] / 1) + 60))
    elif instance == 'lose' or instance == 'win':
        back_menu_game = little_font.render(
            "Press Escape to get back", 1, white_color)
        if instance == 'win':
            win_game = big_font.render("You WIN", 1, white_color)
            window.blit(win_game, (0, WINDOW_SIZE[0] / 2))
        elif instance == 'lose':
            lose_game = big_font.render("You LOSE", 1, red_color)
            window.blit(lose_game, (0, WINDOW_SIZE[0] / 2))
        window.blit(back_menu_game, (0, 0))
    elif instance == 'pocket':
        for counter, item in enumerate(extra):
            pocket = small_font.render(item, 1, white_color)
            window.blit(pocket, (WINDOW_SIZE[1] - SPRITE_SIZE * 3,
                                 counter * 15))
