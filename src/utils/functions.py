import pygame
from constants import (
    WINDOW_SIZE
)


def display_sentence(window, instance):
    """
    Display the good menu (start menu, win menu or lose menu).

    :param window: window that the sentences will appear.
    :param instance: Is there the start menu or the win menu.
    """
    # Initialize fonts.
    little_font = pygame.font.SysFont("monospace", 45)
    big_font = pygame.font.SysFont("monospace", 80)
    # Initialize the color.null
    white_color = (255, 255, 255)

    # Render text.
    back_menu_game = little_font.render(
        "Press Escape to get back", 1, white_color)
    lose_game = big_font.render("You LOSE", 1, white_color)
    play_game = little_font.render("Press Enter to play", 1, white_color)
    quit_game = little_font.render("Press Escape to quit", 1, white_color)
    win_game = big_font.render("You WIN", 1, white_color)

    if instance == 'start':
        window.blit(play_game, (0, WINDOW_SIZE[0] - (WINDOW_SIZE[0] / 1)))
        window.blit(quit_game, (0, WINDOW_SIZE[0] - (WINDOW_SIZE[0] / 1) + 60))
    elif instance == 'lose' or instance == 'win':
        if instance == 'win':
            window.blit(win_game, (0, WINDOW_SIZE[0] / 2))
        elif instance == 'lose':
            window.blit(lose_game, (0, WINDOW_SIZE[0] / 2))
        window.blit(back_menu_game, (0, 0))
