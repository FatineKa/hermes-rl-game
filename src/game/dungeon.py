"""
The dungeon — a 2D grid of tiles.

Design choice: we use a list of lists of integers, where each integer is
a tile type from constants.py. 
"""

from src.game.constants import (
    GRID_WIDTH,
    GRID_HEIGHT,
    TILE_FLOOR,
    TILE_WALL,
)


# A hardcoded starter dungeon. Each character in this layout becomes a tile:
#   '#' = wall, '.' = floor.
# Using characters here (instead of integers directly) lets us see the
# dungeon shape clearly when reading the source code. The function below
# translates it into the integer grid the rest of the game uses.
_RAW_LAYOUT = [
    "####################",
    "#..................#",
    "#..................#",
    "#..####............#",
    "#.....#............#",
    "#.....#......####..#",
    "#.....#......#..#..#",
    "#.....#......#..#..#",
    "#............#..#..#",
    "#............####..#",
    "#..................#",
    "#......####........#",
    "#......#..#........#",
    "#......####........#",
    "####################",
]


def create_dungeon():
    """
    Build the dungeon grid.

    Returns a 2D list `grid` such that `grid[y][x]` is the tile at
    column x, row y. Note the y-first indexing — that matches how
    we read the layout above (top to bottom, left to right) and how
    Pygame thinks of screen coordinates (y goes down).

    Later we'll want create_dungeon() to take parameters
    (seed, difficulty, size) and produce different dungeons each call.

    """
    grid = []

    # Walk through each row of the raw layout.
    # `enumerate` gives us both the index (y) and the value (row string),
    for y, row in enumerate(_RAW_LAYOUT):
        row_tiles = []
        for x, char in enumerate(row):
            # Translate the visual character into a tile type integer.
            if char == "#":
                row_tiles.append(TILE_WALL)
            else:
                row_tiles.append(TILE_FLOOR)
        grid.append(row_tiles)

    # The layout should match the dimensions
    # declared in constants. If someone edits the layout but forgets to
    # update GRID_WIDTH/HEIGHT, this assert catches it immediately
    # instead of producing weird rendering bugs later.
    assert len(grid) == GRID_HEIGHT, (
        f"Layout has {len(grid)} rows but GRID_HEIGHT is {GRID_HEIGHT}"
    )
    assert all(len(row) == GRID_WIDTH for row in grid), (
        f"Layout rows must all be {GRID_WIDTH} columns wide"
    )

    return grid