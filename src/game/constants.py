"""
Game-wide constants.

These values are referenced across many modules. Keeping them in one place
means we change them once instead of hunting through code. 
"""

# Window
# The size of the Pygame window in pixels. Standard 4:3 ratio, comfortable
# We may make this configurable later via config.yaml.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60  # Target frames per second for the game loop


# Grid
# The dungeon is a grid of cells. Each cell is one "tile" the character
# can stand on (if walkable) or bump into (if wall).
#
# TILE_SIZE is how many pixels wide each tile is when drawn. 
TILE_SIZE = 32

# How many tiles fit in the dungeon. We make the dungeon smaller than the
# window so we have margin around it for UI later (HUD, minimap, etc.).
# 20 wide x 15 tall = 640x480 pixels of dungeon, leaving 160 horizontal
# and 120 vertical pixels of slack inside our 800x600 window.
GRID_WIDTH = 20
GRID_HEIGHT = 15


# Tile types

# Each cell in the dungeon stores an integer representing what kind of tile
# it is. Using integers (not strings) is faster and uses less memory 
#
# We give them meaningful names for better readability

TILE_FLOOR = 0  # Walkable ground
TILE_WALL = 1   # Solid wall, blocks movement


# Colors
# Pygame colors are (Red, Green, Blue) tuples, each 0-255.

COLOR_BACKGROUND = (15, 15, 25)      # Deep blue-black — the void around the dungeon
COLOR_FLOOR = (60, 55, 70)           # Muted purple-grey — dim stone
COLOR_WALL = (110, 95, 80)           # Warm beige — torchlit walls
COLOR_FLOOR_OUTLINE = (40, 35, 50)   # Slightly darker than floor for subtle grid lines
COLOR_TEXT = (220, 200, 150)         # Warm gold for any text overlays