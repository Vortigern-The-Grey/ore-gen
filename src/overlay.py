from PIL import Image
from pathlib import Path


def single_gen(base: str, overlay: str) -> Image.Image:
    """
    Loads two images and pastes one ontop of the other, returning the result.
    """
    print("\n[single_gen]: single_gen() initialised.")

    # load images from arg paths
    bg_raw = Image.open(base)
    print("[single_gen]: Raw background image '{base}' loaded.")
    bg = bg_raw.convert("RGBA")
    print("[single_gen]: Background image '{base}' converted to RGBA.")
    pattern = Image.open(overlay)
    print("[single_gen]: Pattern image '{pattern}' loaded")

    # paste second image ontop of first and return the result
    bg.alpha_composite(pattern)
    print("[single_gen]: '{pattern}' successfully composited onto '{base}'.")
    return bg


def single_wrapper():
    """
    Generates ore border textures without ctm for modless or basic texture pack usage.
    """
    bg_dir = Path("./sprites/stones/")
    bgs = [f.stem for f in bg_dir.iterdir() if f.is_file()]
    ore_dir = Path("./sprites/ores/")
    patterns = [f.stem for f in ore_dir.iterdir() if f.is_file()]
    for bg in bgs:
        if bg == "netherrack":
            for pattern in patterns:
                if "nether" in pattern.split("_"):
                    image = single_gen(f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png")
                    image.save(f"./output/single/{pattern}.png")
        else:
            for pattern in patterns:
                image = single_gen(f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png")
                Path("./output/single/").mkdir(exist_ok=True)
                if bg == "stone":
                    image.save(f"./output/single/{pattern}.png")
                else:
                    image.save(f"./output/single/{bg}_{pattern}.png")


def single_wrapper_local():
    """
    Generates ore border textures without ctm for modless or basic texture pack usage.
    """
    bg_dir = Path("../sprites/stones/")
    bgs = [f.stem for f in bg_dir.iterdir() if f.is_file()]
    ore_dir = Path("../sprites/ores/")
    patterns = [f.stem for f in ore_dir.iterdir() if f.is_file()]
    for bg in bgs:
        if bg == "netherrack":
            for pattern in patterns:
                if "nether" in pattern.split("_"):
                    image = single_gen(f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png")
                    image.save(f"../output/single/{pattern}.png")
        else:
            for pattern in patterns:
                image = single_gen(f"{bg_dir}/{bg}.png", f"{ore_dir}/{pattern}.png")
                Path("../output/single/").mkdir(exist_ok=True)
                if bg == "stone":
                    image.save(f"../output/single/{pattern}.png")
                else:
                    image.save(f"../output/single/{bg}_{pattern}.png")


def main():
    single_wrapper_local()


if __name__ == "__main__":
    main()
