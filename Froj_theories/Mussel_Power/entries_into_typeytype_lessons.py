import json



left_joystick = {
    "1": "R",
    "2": "K",
    "3": "B",
    "4": "P",
    "5": "L",
    "6": "D",
    "7": "S",
    "8": "T",
}

# Mapping when the digit follows a vowel or a hyphen
right_joystick = {
    "1": "SS",
    "2": "NG",
    "3": "Y",
    "4": "L",
    "5": "D",
    "6": "N",
    "7": "T",
    "8": "R",
}

VOWELS = set("AOEU")

with open("Froj_theories/Mussel_Power/Mussel_Power_base.json", "r") as f:
    entries = json.load(f)


def convert_key(key):
    result = []

    for i, c in enumerate(key):
        if c.isdigit():
            prev = key[i - 1] if i > 0 else None

            if prev == "-" or prev in VOWELS:
                result.append(right_joystick[c])
            else:
                result.append(left_joystick[c])
        else:
            result.append(c)

    readable = "".join(result)
    return f"{readable} | {key}"


new_entries = {}

for key, value in entries.items():
    if key.startswith("S/"):
        continue

    new_entries[convert_key(key)] = value

with open("Froj_theories/Mussel_Power/inner_ring_simple_vowels_tapeytape.json", "w") as f:
    json.dump(new_entries, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(new_entries)} entries.")
