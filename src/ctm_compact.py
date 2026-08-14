from PIL import Image, ImageDraw
from pathlib import Path


def ctm_compact_gen(base: str, overlay: str) -> list[Image.Image]:
    """
    Generates ctm tiles for ctm_compact (compact 8-way optifine spec) from 16x base and pattern images
    """
    print("\n[ctm_compact_gen]: ctm_compact_gen initialised")
    # open images
    bg_raw = Image.open(base)
    print(f"[ctm_compact_gen]: raw background image {base} loaded.")
    bg = bg_raw.convert("RGBA")
    print(f"[ctm_compact_gen]: background image {base} converted to RGBA.")

    pattern = Image.open(overlay)
    print(f"[ctm_compact_gen]: ore pattern image {pattern} load.")

    # generate 0.png (all sides)
    ctm_0 = bg.copy()
    ctm_0.alpha_composite(pattern)
    print(f"[ctm_compact_gen]: ctm_0 texture generated for {pattern} on {base}.")

    # generate 1.png (no sides/borders)
    pattern_1 = pattern.crop((1, 1, 15, 15))
    ctm_1 = bg.copy()
    ctm_1.alpha_composite(pattern_1, (1, 1))
    print(f"[ctm_compact_gen]: ctm_1 texture generated for {pattern} on {base}.")

    # generate 2.png (vertical borders only)
    pattern_2 = pattern.copy()
    pattern_2_draw = ImageDraw.Draw(pattern_2)
    pattern_2_draw.rectangle((1, 0, 14, 0), fill=(0, 0, 0, 0))
    pattern_2_draw.rectangle((1, 15, 14, 15), fill=(0, 0, 0, 0))
    ctm_2 = bg.copy()
    ctm_2.alpha_composite(pattern_2)
    print(f"[ctm_compact_gen]: ctm_2 texture generated for {pattern} on {base}.")

    # generate 3.png (horizontal borders only)
    pattern_3 = pattern.copy()
    pattern_3_draw = ImageDraw.Draw(pattern_3)
    pattern_3_draw.rectangle((0, 1, 0, 14), fill=(0, 0, 0, 0))
    pattern_3_draw.rectangle((15, 1, 15, 14), fill=(0, 0, 0, 0))
    ctm_3 = bg.copy()
    ctm_3.alpha_composite(pattern_3)
    print(f"[ctm_compact_gen]: ctm_3 texture generated for {pattern} on {base}.")

    # generate 4.png (corners only)
    pattern_4 = pattern.copy()
    pattern_4_draw = ImageDraw.Draw(pattern_4)
    pattern_4_draw.rectangle((1, 0, 14, 0), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((1, 15, 14, 15), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((0, 1, 0, 14), fill=(0, 0, 0, 0))
    pattern_4_draw.rectangle((15, 1, 15, 14), fill=(0, 0, 0, 0))
    ctm_4 = bg.copy()
    ctm_4.alpha_composite(pattern_4)
    print(f"[ctm_compact_gen]: ctm_4 texture generated for {pattern} on {base}.")

    # return image objects
    return [ctm_0, ctm_1, ctm_2, ctm_3, ctm_4]


def ctm_compact_wrapper():
    bg_dir = Path("./sprites/stones/")
    bgs = [f.stem for f in bg_dir.iterdir() if f.is_file()]
    ore_dir = Path("./sprites/ores/")
    patterns = [f.stem for f in ore_dir.iterdir() if f.is_file()]
    for bg in bgs:
        for pattern in patterns:
            images = ctm_compact_gen(f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png")
            if bg == "stone":
                Path(f"./output/compact/{pattern}/").mkdir(exist_ok=True)
                for i in range(5):
                    images[i].save(f"./output/compact/{pattern}/{i}.png")
            else:
                Path(f"./output/compact/{bg}_{pattern}/").mkdir(exist_ok=True)
                for i in range(5):
                    images[i].save(f"./output/compact/{bg}_{pattern}/{i}.png")


def ctm_compact_wrapper_local():
    bg_dir = Path("../sprites/stones/")
    bgs = [f.stem for f in bg_dir.iterdir() if f.is_file()]
    ore_dir = Path("../sprites/ores/")
    patterns = [f.stem for f in ore_dir.iterdir() if f.is_file()]
    for bg in bgs:
        for pattern in patterns:
            images = ctm_compact_gen(f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png")
            if bg == "stone":
                Path(f"../output/compact/{pattern}/").mkdir(exist_ok=True)
                for i in range(5):
                    images[i].save(f"../output/compact/{pattern}/{i}.png")
            else:
                Path(f"../output/compact/{bg}_{pattern}/").mkdir(exist_ok=True)
                for i in range(5):
                    images[i].save(f"../output/compact/{bg}_{pattern}/{i}.png")


def main():
    ctm_compact_wrapper_local()


if __name__ == "__main__":
    main()
