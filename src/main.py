"""
Hermes — entry point.

Opens the Pygame window and runs the main game loop. Each iteration of
the loop handles input, updates state, draws, and ticks the clock.
At this stage there's no movement or game logic yet — we're just
showing a static dungeon to confirm rendering works.
"""

import sys
import pygame

from src.game.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    GRID_WIDTH,
    GRID_HEIGHT,
    TILE_SIZE,
    COLOR_BACKGROUND,
)
from src.game.dungeon import create_dungeon
from src.rendering.dungeon_renderer import draw_dungeon


def main():
    # Pygame needs to be initialized before any of its features work.
    # This call sets up the audio, font, display, and event subsystems.
    pygame.init()

    # Create the window with thechosen size, and give it a title.
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Hermes")

    # A Clock object lets us cap the frame rate. Without this the loop
    # would run as fast as the CPU allows, wasting power and making
    # any future motion-based code behave inconsistently across machines.
    clock = pygame.time.Clock()

    # Build the dungeon once at startup. (Later we'll regenerate it
    # at level transitions, but for now one dungeon for the whole session.)
    dungeon = create_dungeon()

    # Compute where the dungeon should sit on screen. We want it centered:
    # window is WINDOW_WIDTH wide, dungeon is GRID_WIDTH*TILE_SIZE wide,
    # so the left margin is half the difference.
    dungeon_pixel_width = GRID_WIDTH * TILE_SIZE
    dungeon_pixel_height = GRID_HEIGHT * TILE_SIZE
    offset_x = (WINDOW_WIDTH - dungeon_pixel_width) // 2
    offset_y = (WINDOW_HEIGHT - dungeon_pixel_height) // 2

    # The main loop 
    # Almost every game ever made is structured around a loop like this.
    # The body runs ~60 times per second (controlled by clock.tick at the end).
    running = True
    while running:

        # --- 1. Handle events ---
        # Pygame queues up events (key presses, mouse moves, window close)
        # and we process them all each frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Window close button was clicked.
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Escape key — also exit. 
                    running = False

        # --- 2. Update game state ---
        # Nothing to update yet. Once we have a moving character or
        # animated tiles, this is where their per-frame logic will live.

        # --- 3. Draw everything ---
        # Order matters: things drawn later appear ON TOP of things drawn earlier.
        # Right now we fill the background, then draw the dungeon. Soon we'll
        # add: dungeon -> entities -> character -> HUD -> menu overlays.
        screen.fill(COLOR_BACKGROUND)
        draw_dungeon(screen, dungeon, offset_x, offset_y)

        # display.flip() pushes our newly-drawn frame to the actual screen.
        # Until you call this, everything you drew lives in memory invisible.
        pygame.display.flip()

        # --- 4. Tick the clock ---
        # Tells Pygame to wait however long is needed so we don't exceed FPS.
        clock.tick(FPS)

    # Clean shutdown — close the window, release resources.
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # This idiom means "only run main() if this file is executed directly,
    # not if it's imported as a module." It's standard in Python entry points.
    main()