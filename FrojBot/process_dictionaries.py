import json
from collections import defaultdict
import os


def preprocess_json(filename, newname):
    """Preprocess the JSON data by splitting it into multiple files by the first two letters."""
    with open(filename, 'r') as f:
        data = json.load(f)

    # Create a dictionary to store data by the first three letters of the key
    binned_data = defaultdict(dict)

    for key, value in data.items():
        first_three_letters = key[:3].lower().replace("/","_")  # Get the three two letters (case insensitive)
        binned_data[first_three_letters][key] = value

    # Create the output directory if it doesn't exist
    output_dir = 'FrojBot/preprocessed_dictionaries'
    os.makedirs(output_dir, exist_ok=True)

    # Save each bin into separate files
    for letters, letter_data in binned_data.items():
        output_filename = os.path.join(output_dir, f"{newname}_{letters}.json")
        with open(output_filename, 'w') as f:
            json.dump(letter_data, f, indent=4)

# Preprocess both 'word lookup' and 'entry lookup'
preprocess_json("Froj_theories/Froj_Harri_theory/all_outlines.json", "outlines_starting")
preprocess_json("Froj_theories/Froj_Harri_theory/all_entries.json",  "entries_starting")
