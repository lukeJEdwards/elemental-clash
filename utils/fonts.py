from pygame import font
from pygame.font import Font

from utils.paths import assetsDirs

__all__ = [
    "FONT_NORMAL_S",
    "FONT_NORMAL_M",
    "FONT_NORMAL_L",
    "FONT_NORMAL_XL",
    "FONT_NORMAL_XXL",
    "FONT_LIGHT_S",
    "FONT_LIGHT_M",
    "FONT_LIGHT_L",
    "FONT_LIGHT_XL",
    "FONT_LIGHT_XXL",
]


font.init()

FONT_NORMAL_S = Font(f"{assetsDirs.FONTS}\\Abaddon Bold.ttf", 16)
FONT_NORMAL_M = Font(f"{assetsDirs.FONTS}\\Abaddon Bold.ttf", 32)
FONT_NORMAL_L = Font(f"{assetsDirs.FONTS}\\Abaddon Bold.ttf", 48)
FONT_NORMAL_XL = Font(f"{assetsDirs.FONTS}\\Abaddon Bold.ttf", 64)
FONT_NORMAL_XXL = Font(f"{assetsDirs.FONTS}\\Abaddon Bold.ttf", 80)

FONT_LIGHT_S = Font(f"{assetsDirs.FONTS}\\Abaddon Light.ttf", 16)
FONT_LIGHT_M = Font(f"{assetsDirs.FONTS}\\Abaddon Light.ttf", 32)
FONT_LIGHT_L = Font(f"{assetsDirs.FONTS}\\Abaddon Light.ttf", 48)
FONT_LIGHT_XL = Font(f"{assetsDirs.FONTS}\\Abaddon Light.ttf", 64)
FONT_LIGHT_XXL = Font(f"{assetsDirs.FONTS}\\Abaddon Light.ttf", 80)
