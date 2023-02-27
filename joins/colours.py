# def hex_to_rgb(value):
#     value = value.lstrip('#')
#     lv = len(value)
#     return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

joins_palette_hex = {
    "deepspace": "#242456",
    "electron": "#64ABFF",
    "supernova": "#FFE352",
    "ultraviolet": "#4D61F4",
    "aurora": "#59D8A1",
    "molten": "#FF7C66",
    "whitedwarf": "#F4F4F4"
}

joins_palette_rgb = {"deepspace": (36, 36, 86),
                  "electron": (100, 171, 255),
                  "supernova": (255, 227, 82),
                  "ultraviolet": (77, 97, 244),
                  "aurora": (89, 216, 161),
                  "molten": (255, 124, 102),
                  "whitedwarf": (244, 244, 244)}