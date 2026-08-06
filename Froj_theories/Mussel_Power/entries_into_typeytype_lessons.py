import json
import re

TOKEN_RE = re.compile(r"\d(?:[lrLR])?|.")

LEFT = {
    "1": "R", "1l": "W", "1r": "V", "1L": "RY", "1R": "KM",
    "2": "K", "2l": "KR", "2r": "KN", "2L": "KW", "2R": "KL",
    "3": "B", "3l": "M", "3r": "H", "3L": "BR", "3R": "BL",
    "4": "P", "4l": "Y", "4r": "PL", "4L": "PR", "4R": "Z",
    "5": "L", "5l": "G", "5r": "J", "5L": "GR", "5R": "SH",
    "6": "D", "6l": "F", "6r": "DS", "6L": "FL", "6R": "FR",
    "7": "S", "7l": "N", "7r": "ST", "7L": "SP", "7R": "STR",
    "8": "T", "8l": "AH", "8r": "TR", "8L": "AN", "8R": "CH",
}

RIGHT = {
    "1": "SS", "1l": "Z", "1r": "S", "1L": "RY", "1R": "ST",
    "2": "NG", "2l": "SH", "2r": "NK", "2L": "CH", "2R": "B",
    "3": "Y", "3l": "V", "3r": "K", "3L": "J", "3R": "BL",
    "4": "L", "4l": "LY", "4r": "LD", "4L": "LSS", "4R": "LT",
    "5": "D", "5l": "P", "5r": "M", "5L": "RM", "5R": "MP",
    "6": "N", "6l": "ND", "6r": "NT", "6L": "NS", "6R": "NSS",
    "7": "T", "7l": "F", "7r": "G", "7L": "TH", "7R": "RK",
    "8": "R", "8l": "RT", "8r": "RSS", "8L": "RD", "8R": "RS",
}

VOWELS = set("AOEU")

with open("Froj_theories/Mussel_Power/Mussel_Power_base.json", "r") as f:
    entries = json.load(f)


def convert_key(key):
    tokens = TOKEN_RE.findall(key)
    out = []

    prev = None
    for token in tokens:
        if token[0].isdigit():
            if prev == "-" or prev in VOWELS:
                out.append(RIGHT[token])
            else:
                out.append(LEFT[token])
        else:
            out.append(token)
        prev = token

    readable = "".join(out)
    return f"{readable} | {key}"


new_entries = {}

for key, value in entries.items():
    if key.startswith("S/"):
        continue

    new_entries[convert_key(key)] = value

with open("Froj_theories/Mussel_Power/inner_ring_simple_vowels_tapeytape.json", "w") as f:
    json.dump(new_entries, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(new_entries)} entries.")
