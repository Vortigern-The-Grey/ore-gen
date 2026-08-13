from PIL import Image, ImageDraw, ImageOps
# from pathlib import Path
# import json


class CTMComplete:
    def __init__(self, ctm_dict: dict, zones: dict) -> None:
        """
        Import zone coordinates and ctm definitions and set them to self variables.
        """
        self.ctm_dict = ctm_dict
        self.zones = zones

    def trim_zone(self, zone: str, sprite: Image.Image) -> Image.Image:
        """
        Overwrite a 16x image zone with transparent pixels based on a selected zone (cardinal direction) and return it.
        """
        sprite_draw = ImageDraw.Draw(sprite)
        sprite_draw.rectangle(zones[zone], fill=(0, 0, 0, 0))
        return sprite

    def trim_ctm(self, num: int, sprite: Image.Image) -> Image.Image:
        """
        Overwrite multiple zones with transparent pixels based on ctm preset, looping through all zones in corresponding self.ctm_dict entry.
        Contains exceptions for full borders (id=0) and no borders (id=26)
        """
        sprite_draw = ImageDraw.Draw(sprite)
        if type(self.ctm_dict[num]) is int:
            return sprite
        elif type(self.ctm_dict[num]) is tuple:
            sprite_centre = sprite.crop((1, 1, 15, 15))
            sprite_full = ImageOps.expand(sprite_centre, border=1, fill=(0, 0, 0, 0))
            return sprite_full
        else:
            for zone in self.ctm_dict[num]:
                sprite_draw.rectangle(self.zones[zone], fill=(0, 0, 0, 0))
            return sprite

    def ctm_complete_gen(self, bg_path: str, overlay_path: str) -> list[Image.Image]:
        bg = Image.open(bg_path)
        overlay = Image.open(overlay_path)
        ctm_images = []
        for i in ctm_dict:
            temp_bg = bg.copy()
            temp_overlay = overlay.copy()
            temp_overlay = self.trim_ctm(i, temp_overlay)
            temp_bg.alpha_composite(temp_overlay)
            ctm_images.append(temp_bg)
        return ctm_images

ctm_dict = {
    0: None,
    1: "e",
    2: {"e", "w"},
    3: "w",
    4: {"e", "s"},
    5: {"s", "w"},
    6: {"n", "e", "s"},
    7: {"e", "s", "w"},
    8: {"n", "ne", "e", "s", "w"},
    9: {"n", "e", "se", "s", "w"},
    10: {"n", "e", "s", "sw", "w", "nw"},
    11: {"n", "ne", "e", "s", "w", "nw"},
    12: "s",
    13: {"e", "se", "s"},
    14: {"e", "se", "s", "sw", "w"},
    15: {"s", "sw", "w"},
    16: {"n", "e"},
    17: {"n", "w"},
    18: {"n", "e", "w"},
    19: {"n", "s", "w"},
    20: {"n", "e", "s", "w", "nw"},
    21: {"n", "e", "s", "sw", "w"},
    22: {},
    23: {},
    24: {},
    25: {},
    26: (1, 1, 14, 14),
    27: {},
    28: {},
    29: {},
    30: {},
    31: {},
    32: {},
    33: {},
    34: {},
    35: {},
    36: {},
    37: {},
    38: {},
    39: {},
    40: {},
    41: {},
    42: {},
    43: {},
    44: {},
    45: {},
    46: {}, 
}
