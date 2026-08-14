# import builtin libraries
import json

# import custom clases/functions
from src.overlay import single_wrapper
from src.ctm_compact import ctm_compact_wrapper
from src.ctm_complete import CTMComplete, zones, ctm_dict


def ctm_meta_gen(name: str, method: str) -> list[str]:
    """
    Returns .mcmeta and .properties strings for block name {name}
    "method" must be either ctm or ctm_compact
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


def ctm_complete_wrapper():
    pass


def main():
    in_menu = True
    while in_menu is True:
        print(
            "Select mode: \n1. Basic (full block outline, no ctm) \n2. Compact (ctm_compact 8way spec, 5 tiles per ore + metadata) \n3. Full (ctm 8-way spec, 47(6) tiles per ore + metadata) \n4. Exit"
        )
        mode = int(input(">>>"))
        if mode == 1:
            single_wrapper()
        elif mode == 2:
            ctm_compact_wrapper()
        elif mode == 3:
            ctm_complete_wrapper()
        elif mode == 4:
            in_menu = False
        else:
            print("  ^^^ Invalid option entered.")


if __name__ == "__main__":
    main()
