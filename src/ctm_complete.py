from PIL import Image, ImageDraw, ImageOps
from pathlib import Path
# import json


class CTMComplete:
    def __init__(self, ctm_dict: dict, zones: dict) -> None:
        """
        Import zone coordinates and ctm definitions and set them to self variables.
        """

        # import and localise ctm_dict and zones
        self.ctm_dict = ctm_dict
        self.zones = zones

    def trim_zone(self, zone: str, sprite: Image.Image) -> Image.Image:
        """
        Overwrite a 16x image zone with transparent pixels based on a selected zone (cardinal direction) and return it.
        """

        # create ImageDraw object
        sprite_draw = ImageDraw.Draw(sprite)

        # overwrite corresponding zone with transparent pixels based on key "zone"
        sprite_draw.rectangle(self.zones[zone], fill=(0, 0, 0, 0))
        return sprite

    def trim_ctm(self, k, sprite: Image.Image) -> Image.Image:
        """
        Overwrite multiple zones with transparent pixels based on ctm preset, looping through all zones in corresponding
        print(self.zones)self.ctm_dict entry. For single overlay sprite generation, use while iterating through self.ctm_dict.
        Contains exceptions for full borders (id=0) and no borders (id=26)
        """

        # create ImageDraw object
        sprite_draw = ImageDraw.Draw(sprite)

        if type(self.ctm_dict[k]) is int:
            # do nothing if ctm_0 (full borders)
            return sprite

        elif type(self.ctm_dict[k]) is tuple:
            # do custom crop -> resize operation for ctm_26 (no borders)

            # crop centre 14x14 square
            sprite_centre = sprite.crop((1, 1, 15, 15))

            # restore 16x size by adding 1px layer of transparent pixels
            sprite_full = ImageOps.expand(sprite_centre, border=1, fill=(0, 0, 0, 0))
            return sprite_full
        else:
            # main iteration for all other ctm designations

            # iterates through cardinal directions given in selected ctm_dict set
            for zone in self.ctm_dict[k]:
                # fills tuple from zones[] to overwrite transparent pixels
                sprite_draw.rectangle(self.zones[zone], fill=(0, 0, 0, 0))
            return sprite

    def ctm_complete_gen(self, bg_path: str, overlay_path: str) -> list[Image.Image]:
        # import background image
        bg_raw = Image.open(bg_path)
        # import overlay image
        overlay = Image.open(overlay_path)
        # convert background to RGBA
        bg = bg_raw.convert("RGBA")
        ctm_images = []
        # Iterates through all 47 ctm_dict entries
        for k in self.ctm_dict.keys():
            # creates clean copy of bg and overlay
            temp_bg = bg.copy()
            temp_overlay = overlay.copy()

            # removes required zones from overlay using self.trim_ctm
            temp_overlay = self.trim_ctm(k, temp_overlay)

            # applies generated overlay to temp_bg and appends to ctm_images
            temp_bg.alpha_composite(temp_overlay)
            ctm_images.append(temp_bg)
        return ctm_images

    def ctm_complete_wrapper(self):
        bg_dir = Path("./sprites/stones/")
        bgs = [f.stem for f in bg_dir.iterdir() if f.is_file()]
        ore_dir = Path("./sprites/ores/")
        patterns = [f.stem for f in ore_dir.iterdir() if f.is_file()]
        for bg in bgs:
            for pattern in patterns:
                images = self.ctm_complete_gen(
                    f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png"
                )
                if bg == "stone":
                    Path(f"./output/complete/{pattern}/").mkdir(exist_ok=True)
                    for i in range(len(images)):
                        images[i].save(f"./output/complete/{pattern}/{i}.png")
                else:
                    Path(f"./output/complete/{bg}_{pattern}/").mkdir(exist_ok=True)
                    for i in range(len(images)):
                        images[i].save(f"./output/complete/{bg}_{pattern}/{i}.png")

    def ctm_complete_wrapper_local(self):
        bg_dir = Path("../sprites/stones/")
        bgs = [f.stem for f in bg_dir.iterdir() if f.is_file()]
        ore_dir = Path("../sprites/ores/")
        patterns = [f.stem for f in ore_dir.iterdir() if f.is_file()]
        for bg in bgs:
            for pattern in patterns:
                images = self.ctm_complete_gen(
                    f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png"
                )
                print(f"Image number for {bg} {pattern}: {len(images)}")
                if bg == "stone":
                    Path(f"../output/complete/{pattern}/").mkdir(exist_ok=True)
                    for i in range(5):
                        images[i].save(f"../output/complete/{pattern}/{i}.png")
                else:
                    Path(f"../output/complete/{bg}_{pattern}/").mkdir(exist_ok=True)
                    for i in range(5):
                        images[i].save(f"../output/complete/{bg}_{pattern}/{i}.png")


# zone dict
zones = {
    "n": (1, 0, 14, 0),
    "ne": (15, 0, 15, 0),
    "e": (15, 1, 15, 14),
    "se": (15, 15, 15, 15),
    "s": (1, 15, 14, 15),
    "sw": (0, 15, 0, 15),
    "w": (0, 1, 0, 14),
    "nw": (0, 0, 0, 0),
}

ctm_dict = {
    0: 0,
    1: {"e"},
    2: {"e", "w"},
    3: {"w"},
    4: {"e", "s"},
    5: {"s", "w"},
    6: {"n", "e", "s"},
    7: {"e", "s", "w"},
    8: {"n", "ne", "e", "s", "w"},
    9: {"n", "e", "se", "s", "w"},
    10: {"n", "e", "s", "sw", "w", "nw"},
    11: {"n", "ne", "e", "s", "w", "nw"},
    12: {"s"},
    13: {"e", "se", "s"},
    14: {"e", "se", "s", "sw", "w"},
    15: {"s", "sw", "w"},
    16: {"n", "e"},
    17: {"n", "w"},
    18: {"n", "e", "w"},
    19: {"n", "s", "w"},
    20: {"n", "e", "s", "w", "nw"},
    21: {"n", "e", "s", "sw", "w"},
    22: {"n", "e", "se", "s", "sw", "w"},
    23: {"n", "ne", "e", "se", "s", "w"},
    24: {"n", "s"},
    25: {"n", "ne", "e", "se", "s"},
    26: (1, 1, 14, 14),
    27: {"n", "s", "sw", "w", "nw"},
    28: {"n", "e", "se", "s"},
    29: {"e", "s", "sw", "w"},
    30: {"n", "ne", "e", "s"},
    31: {"e", "se", "s", "w"},
    32: {"n", "ne", "e", "s", "sw", "w", "nw"},
    33: {"n", "ne", "e", "se", "s", "w", "nw"},
    34: {"n", "ne", "e", "s", "sw", "w"},
    35: {"n", "e", "se", "s", "w", "nw"},
    36: {"n"},
    37: {"n", "ne", "e"},
    38: {"n", "ne", "e", "w", "nw"},
    39: {"n", "w", "nw"},
    40: {"n", "ne", "e", "w"},
    41: {"n", "s", "w", "nw"},
    42: {"n", "e", "w", "nw"},
    43: {"n", "s", "sw", "w"},
    44: {"n", "e", "se", "s", "sw", "w", "nw"},
    45: {"n", "ne", "e", "se", "s", "sw", "w"},
    46: {"n", "s", "e", "w"},
}


def main():
    ctm_obj = CTMComplete(zones, ctm_dict)
    ctm_obj.ctm_complete_wrapper_local()
