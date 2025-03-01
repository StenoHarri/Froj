
import json
import re

lookup = {}

with open("Froj_theories/Froj_Harri_theory/best_of_word_to_entry_lookup.json", "r") as f:
    lookup['word_lookup'] = json.load(f)

with open("Froj_theories/Froj_Harri_theory/Froj_verbose_lookup.json", "r") as f:
    lookup['entry_lookup'] = json.load(f)


is_raw_steno = re.compile(r'^(S?T?K?P?W?H?R?[AO*\-EU]+F?R?P?B?L?G?T?S?D?Z?)(/S?T?K?P?W?H?R?[AO*\-EU]+F?R?P?B?L?G?T?S?D?Z?)*$')



def get_annotation_level(word_to_find):

    if word_to_find.startswith(":>>"):
        return word_to_find.replace(":>>","").strip(), True

    else: # it must be :>
        return word_to_find.replace(":>","").strip(), False


def get_response( user_input:str) -> str:

    word_to_find, complexity = get_annotation_level(user_input)

    if word_to_find == '':
        return 'you can do :> for lookup, :>> for annotated lookup'


    if re.search(is_raw_steno, word_to_find):

        type_of_lookup = 'entry lookup'
    else:
        type_of_lookup = 'word lookup'
        word_to_find = word_to_find.lower()


    



    if 'hello' in word_to_find:
        return f"Hi friend (ΘoΘ )"
    elif 'froj' in word_to_find:
        return f"That's me! How can I help?"
    elif 'shrimp' in word_to_find:
        return "🦐"
    elif 'crazy' in word_to_find:
        return "I was crazy once"
    elif type_of_lookup == 'entry lookup' and word_to_find in lookup['entry_lookup']:
        return f"hi"
    elif type_of_lookup == 'word lookup' and f"{word_to_find}:" in lookup['word_lookup']:
        return f"hello"


    else:
        return "```ANSI\n\033[31mHello\033[0mSorry, I'm missing the pronunciation data for that word :(```"



"""
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