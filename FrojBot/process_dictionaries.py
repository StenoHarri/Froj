import json
from collections import defaultdict
import os
from tqdm import tqdm


while True:
    selection = input("what theory would you like to sort into FrojBot dictionaries?\n1)\tTadpole\n2)\tEnglish Michela Phonetic Steno for Piano\n:")

    if selection == "1":
        theory = "Tadpole"
        break

    elif selection == "2":
        theory = "English_Michela_Phonetic_Steno_for_Piano"
        break
    else:
        print("try again")


def preprocess_json(filename, newname):
    """Preprocess the JSON data by splitting it into multiple files by the first three letters."""
    with open(filename, 'r') as f:
        data = json.load(f)
    
    # Create a dictionary to store data by the first three letters of the key
    binned_data = defaultdict(dict)
    
    for key in tqdm(data, desc=f"sort into bins", unit="entry"):
        first_three_letters = key[:3].replace("/","_")  # Get the first three letters (case sensitive!!!!!)
        binned_data[first_three_letters][key] = data[key]
    
    # Create the output directory if it doesn't exist
    output_dir = 'FrojBot/theories/'+theory
    os.makedirs(output_dir, exist_ok=True)
    
    # Save each bin into separate files, with progress bar
    for letters, letter_data in tqdm(binned_data.items(), desc=f"output bins into json", unit="bin", smoothing=0):
        output_filename = os.path.join(output_dir, f"{newname}_{letters}.json")
        with open(output_filename, 'w') as f:
            json.dump(letter_data, f, indent=4)

# Preprocess both 'word lookup' and 'entry lookup'
print('loading dictionary needed for word lookup (after this is entry lookup)')
preprocess_json("Froj_theories/"+theory+"/all_outlines.json", "outlines_starting")
print('loading dictionary needed for entry lookup')
preprocess_json("Froj_theories/"+theory+"/all_entries.json",  "entries_starting")
