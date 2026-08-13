from PIL import Image, ImageDraw
import os


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
    mcmeta_template = f"""
    {"ctm":{"ctm_version": 1,
            "type":"ctm",
            "layer":"SOLID",
            "textures":[
                "minecraft:block/{name}_ctm"
            ],
            "extra":{"ignore_states":false,
        	    "connect_inside":true
            }
        }
    }
    """

    return properties_template, mcmeta_template


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

def main():
    print("Hello from ore-gen!")


if __name__ == "__main__":
    main()
