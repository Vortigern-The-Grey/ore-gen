from PIL import Image
from pathlib import Path
import json
from ctm_compact import ctm_compact_gen


def ctm_meta_gen(name: str) -> list[str]:
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

    return [properties_template, json.dumps(mcmeta_template, indent=4)]


def texture_gen(base: str, overlay: str) -> Image.Image:
    """
    Loads two images and pastes one ontop of the other, returning the result.
    """
    # load images from arg paths
    bg = Image.open(base)
    pattern = Image.open(overlay)

    # paste second image ontop of first and return the result
    bg.alpha_composite(pattern)
    return bg



def main():
    bg_dir = Path("./sprites/stones/")
    bgs = [f.name for f in bg_dir.iterdir() if f.is_file()]
    ore_dir = Path("./sprites/ores/")
    patterns = [f.name for f in ore_dir.iterdir() if f.is_file()]
    for bg in bgs:
        for pattern in patterns:
            img_0, img_1, img_2, img_3, img_4 = ctm_texture_gen(bg, pattern)
    pass


if __name__ == "__main__":
    main()
