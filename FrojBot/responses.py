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



def display_outlines(outlines, complexity):
    #this is the one where you give it English words

    what_ambiguities_exist = []

    for ambiguity in outlines['ambiguity']:
        what_ambiguities_exist.append(ambiguity)

    return what_ambiguities_exist




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
            return display_entries(looked_up_data, complexity)
        
        elif lookup_type == "outlines":
            return display_outlines(looked_up_data, complexity)

        else:
            return "Huh, how did you get here?"
    
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