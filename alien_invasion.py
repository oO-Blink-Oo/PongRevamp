# # Ian Michael Jesu Alvarez
# # CPSC 386 (Friday)
# # This creates the window for the whole game
#
# import pygame
# from pygame.sprite import Group
# from settings import Settings
# from ship import Ship
# from alien import Alien
# from game_stats import GameStats
# from button import Button
# from scoreboard import Scoreboard
#
# import game_functions as gf
#
#
# def run_game():
#
#     # Initialize game, settings, and screen object.
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # Make the Play button.
#     play_button = Button(ai_settings, screen, "Play")
#
#     # Create an instance to store game statistics and create a scoreboard.
#     stats = GameStats(ai_settings)
#     sb = Scoreboard(ai_settings, screen, stats)
#
#     # Make an alien.
#     alien = Alien(ai_settings, screen)
#
#     # Make a ship, a group of bullets, and a group of aliens.
#     ship1 = Ship(ai_settings, screen)
#     ship2 = Ship(ai_settings, screen)
#     bullets = Group()
#     aliens = Group()
#
#     # Create the fleet of aliens.
#     gf.create_fleet(ai_settings, screen, ship1, aliens)
#
#     # Start the main loop for the game.
#     while True:
#         gf.check_events(ai_settings, screen, stats, sb, play_button, ship1, aliens, bullets)  # has ship
#
#         if stats.game_active:
#             # Redraw and update screen
#             ship1.update()  # has ship
#             ship2.update()
#             bullets.update()
#
#             gf.update_bullets(ai_settings, screen, stats, sb, ship1, aliens, bullets)  # has ship
#             gf.update_aliens(ai_settings, stats, screen, sb, ship1, aliens, bullets)  # has ship
#
#         gf.update_screen(ai_settings, screen, stats, sb, ship1, aliens, bullets, play_button)  # has ship
#
#
# run_game()