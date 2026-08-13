from PIL import Image, ImageDraw
import json


def ctm_meta_gen(name: str):
    """
    Returns .mcmeta and .properties strings for block name {name}
    """

    # mcmeta and properties template strings
    properties_template = f"""
    matchblocks={name}
    method=ctm_compact
    tiles=0-4
    """
    mcmeta_template = {
        "ctm": {
            "ctm_version": 1,
            "type": "ctm",
            "layer": "SOLID",
            "textures": [f"minecraft:block/{name}_ctm"],
            "extra": {"ignore_states": False, "connect_inside": True},
        }
    }

    return properties_template, json.dumps(mcmeta_template, indent=4)


def texture_gen(base: str, overlay: str):
    """
    Loads two images and pastes one ontop of the other, returning the result.
    """
    # load images from arg paths
    bg = Image.open(base)
    pattern = Image.open(overlay)

    # paste second image ontop of first and return the result
    bg.alpha_composite(pattern)
    return bg


def ctm_texture_gen(base: str, overlay: str):
    """
    Generates ctm tiles for ctm_compact (compact 8-way optifine spec) from 16x base and pattern images
    """
    # open images
    bg = Image.open(base)
    pattern = Image.open(overlay)

    # generate 0.png (all sides)
    ctm_0 = bg.alpha_composite(pattern)

    # generate 1.png (no sides/borders)
    pattern_1 = pattern.crop((1, 1, 15, 15))
    ctm_1 = bg.alpha_composite(pattern_1, (1, 1))

    # generate 2.png (vertical borders only)
    pattern_2 = pattern.copy()
    pattern_2_draw = ImageDraw.Draw(pattern_2)
    pattern_2_draw.rectangle((1, 0, 14, 0), fill=(0, 0, 0, 0))
    pattern_2_draw.rectangle((1, 15, 14, 15), fill=(0, 0, 0, 0))
    ctm_2 = bg.alpha_composite(pattern_2)

    # generate 3.png (horizontal borders only)
    pattern_3 = pattern.copy()
    pattern_3_draw = ImageDraw.Draw(pattern_3)
    pattern_3_draw.rectangle((0, 1, 0, 14), fill=(0, 0, 0, 0))
    pattern_3_draw.rectangle((15, 1, 15, 14), fill=(0, 0, 0, 0))
    ctm_3 = bg.alpha_composite(pattern_3)

    # generate 4.png (corners only)
    pattern_4 = pattern.copy()
    pattern_4_draw = ImageDraw.Draw(pattern_4)
    pattern_4_draw.rectangle((1, 0, 14, 0), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((1, 15, 14, 15), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((0, 1, 0, 14), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((15, 1, 15, 14), fill=(0, 0, 0, 0))
    ctm_4 = bg.alpha_composite(pattern_4)

    # return image objects
    return ctm_0, ctm_1, ctm_2, ctm_3, ctm_4


def main():
    bg_dir = Path("./sprites/stones/")
    bgs = [f.name for f in dir_path.iterdir() if f.is_file()]
    ore_path = Path("./sprites/ores/")
    patterns = [f.name for f in dir_path.iterdir() if f.is_file()]
    for bg in bgs:
        for pattern in patterns:
            img_0, img_1, img_2, img_3, img_4 = ctm_texture_gen(bg, pattern)
    pass


if __name__ == "__main__":
    main()
