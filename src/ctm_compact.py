from PIL import Image, ImageDraw
from pathlib import Path


def ctm_compact_gen(base: str, overlay: str) -> list[Image.Image]:
    """
    Generates ctm tiles for ctm_compact (compact 8-way optifine spec) from 16x base and pattern images
    """
    # open images
    bg_raw = Image.open(base)
    bg = bg_raw.convert("RGBA")
    pattern = Image.open(overlay)

    # generate 0.png (all sides)
    ctm_0 = bg.copy()
    ctm_0.alpha_composite(pattern)

    # generate 1.png (no sides/borders)
    pattern_1 = pattern.crop((1, 1, 15, 15))
    ctm_1 = bg.copy()
    ctm_1.alpha_composite(pattern_1, (1, 1))

    # generate 2.png (vertical borders only)
    pattern_2 = pattern.copy()
    pattern_2_draw = ImageDraw.Draw(pattern_2)
    pattern_2_draw.rectangle((1, 0, 14, 0), fill=(0, 0, 0, 0))
    pattern_2_draw.rectangle((1, 15, 14, 15), fill=(0, 0, 0, 0))
    ctm_2 = bg.copy()
    ctm_2.alpha_composite(pattern_2)

    # generate 3.png (horizontal borders only)
    pattern_3 = pattern.copy()
    pattern_3_draw = ImageDraw.Draw(pattern_3)
    pattern_3_draw.rectangle((0, 1, 0, 14), fill=(0, 0, 0, 0))
    pattern_3_draw.rectangle((15, 1, 15, 14), fill=(0, 0, 0, 0))
    ctm_3 = bg.copy()
    ctm_3.alpha_composite(pattern_3)

    # generate 4.png (corners only)
    pattern_4 = pattern.copy()
    pattern_4_draw = ImageDraw.Draw(pattern_4)
    pattern_4_draw.rectangle((1, 0, 14, 0), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((1, 15, 14, 15), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((0, 1, 0, 14), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((15, 1, 15, 14), fill=(0, 0, 0, 0))
    ctm_4 = bg.copy()
    ctm_4.alpha_composite(pattern_4)

    # return image objects
    return [ctm_0, ctm_1, ctm_2, ctm_3, ctm_4]


def main():
    bg_dir = Path("../sprites/stones/")
    bgs = [f.stem for f in bg_dir.iterdir() if f.is_file()]
    ore_dir = Path("../sprites/ores/")
    patterns = [f.stem for f in ore_dir.iterdir() if f.is_file()]
    for bg in bgs:
        for pattern in patterns:
            Path(f"../output/{bg}_{pattern}/").mkdir(exist_ok=True)
            images = ctm_compact_gen(f"{bg_dir}/{bg}", f"{ore_dir}/{pattern}")
            images[0].save(f"../output/{bg}_{pattern}/0.png")
            images[1].save(f"../output/{bg}_{pattern}/1.png")
            images[2].save(f"../output/{bg}_{pattern}/2.png")
            images[3].save(f"../output/{bg}_{pattern}/3.png")
            images[4].save(f"../output/{bg}_{pattern}/4.png")


if __name__ == "__main__":
    main()
