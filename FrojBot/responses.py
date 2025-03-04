import json
import re
import os
from typing import Dict, Optional

# Cached data (only loaded once, then unloaded after each use)
_lookup_data_cache: Optional[Dict[str, dict]] = {}

def load_json(filename: str) -> dict:
    """Helper function to load JSON data from a file."""
    with open(filename, 'r') as f:
        return json.load(f)

def get_lookup_data(letter: str, lookup_type: str) -> Dict[str, dict]:
    """Return the relevant lookup data for the given first letter and lookup type."""
    global _lookup_data_cache
    # Ensure that we load data only once for the given letter
    if lookup_type not in _lookup_data_cache:
        _lookup_data_cache[lookup_type] = {}

    if letter not in _lookup_data_cache[lookup_type]:
        # Lazy load the corresponding file based on the letter and lookup type
        filename = f"FrojBot/preprocessed_dictionaries/{lookup_type}_starting_{letter}.json"
        if os.path.exists(filename):
            _lookup_data_cache[lookup_type][letter] = load_json(filename)
        else:
            _lookup_data_cache[lookup_type][letter] = {}  # Empty if not found
    
    # After lookup, clear the cache
    result = _lookup_data_cache[lookup_type][letter]
    _lookup_data_cache[lookup_type].pop(letter, None)  # Remove this entry from cache after use
    if not _lookup_data_cache[lookup_type]:  # Clean up cache if it's empty
        _lookup_data_cache.pop(lookup_type, None)
    
    return result

# Define regex once globally
is_raw_steno = re.compile(r'^(S?T?K?P?W?H?R?[AO*\-EU]+F?R?P?B?L?G?T?S?D?Z?)(/S?T?K?P?W?H?R?[AO*\-EU]+F?R?P?B?L?G?T?S?D?Z?)*$')

def get_annotation_level(word_to_find: str) -> tuple:
    """Return the base word and whether it's complex."""
    if word_to_find.startswith(":>>"):
        return word_to_find.replace(":>>", "").strip(), True
    else:  # it must be :>
        return word_to_find.replace(":>", "").strip(), False





def display_entries(entries, complexity):
    #this is the one where you give it raw steno

    what_ambiguities_exist = []

    for ambiguity in entries:
        what_ambiguities_exist.append(ambiguity)

    return entries


# Function to print the smallest stroke count per ambiguity level, ensuring more ambiguous strokes only show if shorter than previous ones
def best_outlines(spelling, outlines, complexity):
    output = ""
    ambiguity = outlines.get("ambiguity", {})

    number_of_best_entries = 0

    total_number_of_entries = sum(
        len(ambiguity[amb]["number of strokes"]) for amb in ambiguity
    )
    
    # Sort ambiguity levels by their numeric value (e.g., "2", "5")
    sorted_ambiguities = sorted(ambiguity.keys(), key=int)

    # Keep track of the smallest stroke count encountered
    smallest_stroke_count = float('inf')  # Initialize to infinity, so the first stroke will always be considered
    
    for amb in sorted_ambiguities:
        entries = ambiguity[amb]["number of strokes"]
        
        # Sort the stroke counts for the ambiguity level to pick the smallest first
        sorted_stroke_counts = sorted(entries.keys(), key=int)
        
        for stroke_count in sorted_stroke_counts:
            # Only consider this stroke if it's smaller than the smallest stroke count so far
            if int(stroke_count) < smallest_stroke_count:
                steno_entries = entries[stroke_count]
                for entry in steno_entries:
                    raw_steno = entry['raw steno outline']
                    output += ("```Ansi\n\n")
                    output += (f"{raw_steno} → {spelling}")

                    if complexity:
                        for chord in entry['explanation']:

                            linker = " ┐ " if "/" in chord['chord'] else " │ "

                            output += (f"\n\033[2;30m{chord['theory'].ljust(8)}\033[0m{chord['chord'].rjust(7)}{linker}{chord['description']}")

                    output += ("```")

                    # Update the smallest stroke count to this one, since it's smaller
                    smallest_stroke_count = int(stroke_count)
                    number_of_best_entries+=1
                    break  # Only print the smallest number of strokes for this ambiguity level
                break  # Stop at the first entry (smallest strokes for this level)
    output = f"Here's the best {number_of_best_entries}/{total_number_of_entries} entries in Tad theory\n{output}"

    return output

def display_outlines(spelling, outlines, complexity):
    #this is the one where you give it English words


    return best_outlines(spelling, outlines, complexity)




def get_response(user_input: str) -> str:
    """Returns the appropriate response for user input."""
    word_to_find, complexity = get_annotation_level(user_input)

    # Default response if input is empty
    if word_to_find == '':
        return 'you can do :> for lookup, :>> for annotated lookup'

    # Check if the word matches raw steno format
    if re.search(is_raw_steno, word_to_find):
        lookup_type = 'entries'
    else:
        lookup_type = 'outlines'
        word_to_find = word_to_find.lower()

    # Get the first letter of the word to load the relevant part of the data
    first_letter = word_to_find[0].lower()

    # Load only the relevant data for that letter
    lookup_data = get_lookup_data(first_letter, lookup_type)

    # Handle specific word lookups
    if 'hello' in word_to_find:
        return "Hi friend (ΘoΘ )"
    elif 'froj' in word_to_find:
        return "That's me! How can I help?"

    # Lookup based on word or entry
    if word_to_find in lookup_data:
        looked_up_data = lookup_data[word_to_find]

        if lookup_type == "entries":
            return display_entries(word_to_find, looked_up_data, complexity)
        
        elif lookup_type == "outlines":
            return display_outlines(word_to_find, looked_up_data, complexity)

        else:
            return "Huh, how did you get here?"

    if word_to_find in open("FrojBot/preprocessed_dictionaries/words_that_Edinburgh_has.txt").read():
        return "Sorry, Tad theory doesn't cover that word"

    return "Sorry, I'm missing the pronunciation data for that word :("


"""

 f"FrojBot/preprocessed_dictionaries/{lookup_type}_starting_{letter}.json"
{
 "a": {
  "ambiguity": {
   "0": [
    {
     "raw steno outline": "AEU",
     "explanation": [
      {
       "theory": "",
       "chord": "AEU",
       "description": "long a"
      }
     ]
    },
    {
     "raw steno outline": "A",
     "explanation": [
      {
       "theory": "",
       "chord": "A",
       "description": "short a"
      }
     ]
    }
   ]
  }
"""


"""
{
 "AEU": {
  "ambiguity": {
   "0": [
    {
     "spelling": "a",
     "explanation": [
      {
       "theory": "",
       "chord": "AEU",
       "description": "long a"
      }
     ]
    }
   ],
   "1": [
    {
     "spelling": "et",
     "explanation": [
      {
       "theory": "",
       "chord": "AEU",
       "description": "et pronounced long a"
      }
     ]
    }
   ]
  }
 },
 "A": {
  "ambiguity": {
   "0": [
    {
     "spelling": "a",
     "explanation": [
      {
       "theory": "",
       "chord": "A",
       "description": "short a"
      }
     ]
    }
   ]
  }
 },
"""