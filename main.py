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
def main():
    print("Hello from ore-gen!")


if __name__ == "__main__":
    main()
