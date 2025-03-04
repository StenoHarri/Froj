import json
from collections import defaultdict
import os


def preprocess_json(filename, newname):
    """Preprocess the JSON data by splitting it into multiple files by the first letter."""
    with open(filename, 'r') as f:
        data = json.load(f)
    
    # Create a dictionary to store data by the first letter of the key
    binned_data = defaultdict(dict)
    
    for key, value in data.items():
        first_letter = key[0].lower()  # Get the first letter (case insensitive)
        binned_data[first_letter][key] = value
    
    # Save each bin into separate files
    for letter, letter_data in binned_data.items():
        output_filename = f"FrojBot/preprocessed_dictionaries/{newname}_{letter}.json"
        with open(output_filename, 'w') as f:
            json.dump(letter_data, f, indent=4)

# Preprocess both 'word lookup' and 'entry lookup'
preprocess_json("Froj_theories/Froj_Harri_theory/all_outlines.json", "outlines_starting")
preprocess_json("Froj_theories/Froj_Harri_theory/all_entries.json",  "entries_starting")