"""
Renders the dungeon grid to the Pygame screen.

This module's only job is "given a dungeon and a screen, draw the dungeon."

"""

import pygame

from src.game.constants import (
    TILE_SIZE,
    TILE_FLOOR,
    TILE_WALL,
    COLOR_FLOOR,
    COLOR_WALL,
    COLOR_FLOOR_OUTLINE,
)


def draw_dungeon(screen, dungeon, offset_x=0, offset_y=0):
    """
    Draw every tile of the dungeon onto the given Pygame screen.

    Args:
        screen:   The Pygame surface to draw on (the window).
        dungeon:  The 2D grid returned by create_dungeon().
        offset_x: How many pixels to shift the whole dungeon right.
        offset_y: How many pixels to shift the whole dungeon down.


    """
    # Walk every cell in the grid and draw the matching tile.
    # iterate y (rows) outer and x (columns) inner — same order as the
    # layout was written, so it stays easy to reason about.
    for y, row in enumerate(dungeon):
        for x, tile in enumerate(row):
            # Compute the screen position of this tile's top-left corner.
            # Each tile is TILE_SIZE pixels wide, so column x sits at
            # x * TILE_SIZE pixels from the left of the dungeon area.
            # Then we add the offset to position the whole dungeon.
            pixel_x = offset_x + x * TILE_SIZE
            pixel_y = offset_y + y * TILE_SIZE

            # A Pygame Rect describes a rectangle: (x, y, width, height).
            # We'll fill this rectangle with the tile's color.
            rect = pygame.Rect(pixel_x, pixel_y, TILE_SIZE, TILE_SIZE)

            
            if tile == TILE_WALL:
                pygame.draw.rect(screen, COLOR_WALL, rect)
            elif tile == TILE_FLOOR:
                pygame.draw.rect(screen, COLOR_FLOOR, rect)
                # Subtle outline on floor tiles makes the grid readable
                # without being noisy. The `1` is the line thickness.
                pygame.draw.rect(screen, COLOR_FLOOR_OUTLINE, rect, 1)