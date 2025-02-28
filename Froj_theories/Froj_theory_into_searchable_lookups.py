import json

with open("Froj_theories/Froj_Harri_theory/complete_output.json", 'r') as f:
    words = json.load(f)


sorted_words = {}

custom_alphabet = "QSTKPWHRAO-*eufrpblgtsdz_"

def sort_word_outlines(word):
    sorted_outlines = {}

    for outline in word['steno stuff']:
        outline_length = outline.count("/")

        try:
            # If the thing I'm going to add is less ambiguous, add it
            if sorted_outlines[f"length {outline_length}"]['ambiguity'] > word['steno stuff'][outline]['ambiguity']:
                sorted_outlines[f"length {outline_length}"] = {
                    'raw steno': outline,
                    'ambiguity': word['steno stuff'][outline]['ambiguity'],
                    'explanation': word['steno stuff'][outline]['explanation']}

        except KeyError:
            sorted_outlines[f'length {outline_length}'] = {
                'raw steno': outline,
                'ambiguity': word['steno stuff'][outline]['ambiguity'],
                'explanation': word['steno stuff'][outline]['explanation']}

    # Sort the dictionary by the length in ascending order, shortest outline first
    # Then sort by ambiguity level for outlines of the same length
    sorted_outlines = {key: value for key, value in
                       sorted(sorted_outlines.items(), key=lambda x: (int(x[0].split()[1]), x[1]['ambiguity']), reverse=False)}

    return sorted_outlines

def order_outlines(sorted_outlines):
    """
    essentially I've already got them ordered, I'm just getting rid of entries where a shorter stroke is less ambiguous
    """
    ordered_outlines = []


    least_ambiguous_so_far = 1000

    for outline in sorted_outlines.values():
        if outline['ambiguity'] < least_ambiguous_so_far:
            least_ambiguous_so_far = outline['ambiguity']
            ordered_outlines.append({'raw steno':outline['raw steno'][1:].upper(),'ambiguity':outline['ambiguity'], 'explanation':outline['explanation']})

    return ordered_outlines
"""
{
  "word": "aachen:",
  "word_class": "NNP",
  "pronunciation": " starting_root  aa  k  e5  n ",
  "word_boundaries": "aachen",
  "frequency": "11",
  "number of entries": 3,
  "steno stuff": {
   "/A/KWHA/Kepb": {
    "raw steno outline": "/A/KWHA/Kepb",
    "ambiguity": 4,
    "explanation": [
     {
      "theory": "",
      "chord": "A",
      "description": "short a"
     },
     {
      "theory": "",
      "chord": "/",
      "description": ""
     },
     {
      "theory": "Harri",
      "chord": "KWH",
      "description": "pretend consonant"
     },
     {
      "theory": "",
      "chord": "A",
      "description": "silent a"
     },
     {
      "theory": "",
      "chord": "/",
      "description": ""
     },
     {
      "theory": "",
      "chord": "K",
      "description": "ch pronounced k"
     },
     {
      "theory": "?",
      "chord": "E",
      "description": "e"
     },
     {
      "theory": "",
      "chord": "-PB",
      "description": "n"
     }
    ]
   },
   "/A/KWHAbg/KWHepb": {
    "raw steno outline": "/A/KWHAbg/KWHepb",
    "ambiguity": 6,
    "explanation": [
     {
      "theory": "",
      "chord": "A",
      "description": "short a"
     },
     {
      "theory": "",
      "chord": "/",
      "description": ""
     },
     {
      "theory": "Harri",
      "chord": "KWH",
      "description": "pretend consonant"
     },
     {
      "theory": "",
      "chord": "A",
      "description": "silent a"
     },
     {
      "theory": "?",
      "chord": "-BG",
      "description": "ch pronounced k"
     },
     {
      "theory": "",
      "chord": "/",
      "description": ""
     },
     {
      "theory": "Harri",
      "chord": "KWH",
      "description": "pretend consonant"
     },
     {
      "theory": "?",
      "chord": "E",
      "description": "e"
     },
     {
      "theory": "",
      "chord": "-PB",
      "description": "n"
     }
    ]
   },
   "/A/KWHAbg/Hepb": {
    "raw steno outline": "/A/KWHAbg/Hepb",
    "ambiguity": 4,
    "explanation": [
     {
      "theory": "",
      "chord": "A",
      "description": "short a"
     },
     {
      "theory": "",
      "chord": "/",
      "description": ""
     },
     {
      "theory": "Harri",
      "chord": "KWH",
      "description": "pretend consonant"
     },
     {
      "theory": "",
      "chord": "A",
      "description": "silent a"
     },
     {
      "theory": "",
      "chord": "-BG",
      "description": "c pronounced k"
     },
     {
      "theory": "",
      "chord": "/",
      "description": ""
     },
     {
      "theory": "?",
      "chord": "H",
      "description": "silent h"
     },
     {
      "theory": "?",
      "chord": "E",
      "description": "e"
     },
     {
      "theory": "",
      "chord": "-PB",
      "description": "n"
     }
    ]
   }
  }
 },
"""
word_lookup = {}
all_word_lookup = {}
entry_lookup = {}
plover_lookup = {}



def ordered_by_length(dictionary):
    ordered_dictionary = {}
    #print(dictionary)


    # Sort the keys by ambiguity
    ordered_by_ambiguity = sorted(dictionary['steno stuff'].items(), key=lambda item: item[1]['ambiguity'])

    # Sort the keys by the number of forward slashes in each key
    ordered_by_length = sorted(ordered_by_ambiguity, key=lambda item: item[0].count('/')) #, reverse=True

    return ordered_by_length

def create_lookups(outlines):

    best_outlines = {}
    all_outlines = {}
    entries = {}

    previous_ambiguity = 100

    for outline in outlines:

        outline = outline[1]

        outline_length = outline['raw steno outline'].count("/")

        if outline['ambiguity'] < previous_ambiguity:
            best_outlines['outline'] = {
                    'raw steno': outline['raw steno outline'],
                    'ambiguity': outline['ambiguity'],
                    'explanation': outline['explanation']}
            previous_ambiguity=outline[outline]['ambiguity']

    
    return best_outlines


print('generating dictionaries')
for word in words:



    ordered_outlines = (ordered_by_length(word))

    word_lookup = create_lookups(ordered_outlines)

    """
    all_word_lookup[word['word']] = {'text':
                            f"showing all {len(ordered_outlines)} out of {word['number of entries']} entries",
                            'entries': ordered_outlines}


    filtered_outlines = order_outlines(ordered_outlines)

    best_word_lookup[word['word']] = {'text':
                           f"showing the best {len(filtered_outlines)} out of {word['number of entries']} entries",
                           'entries': filtered_outlines}


                           


    #print(f"\n\n\n{word}")
    translation = word['word'].split(":")[0]
    for outline in word['steno stuff']:
        ambiguity = word['steno stuff'][outline]['ambiguity']
        explanation = word['steno stuff'][outline]['explanation']
        outline = (outline[1:]
                   .replace('z*','*z')
                   .replace('d*','*d')
                   .replace('s*','*s')
                   .replace('t*','*t')
                   .replace('g*','*g')
                   .replace('l*','*l')
                   .replace('b*','*b')
                   .replace('p*','*p')
                   .replace('r*','*r')
                   .replace('f*','*f')
                   .replace('u*','*u')
                   .replace('e*','*e')
                   .replace('-*','*')
                   .upper()
                   )



        if outline in plain_entry_lookup:
            if ambiguity < verbose_entry_lookup[outline]['ambiguity']:
                verbose_entry_lookup[outline] = {
                    'ambiguity': ambiguity,
                    'translation': translation,
                    'explanation': explanation}

                plain_entry_lookup[outline] = translation
            
        else:
            verbose_entry_lookup[outline] = {
                'ambiguity': ambiguity,
                'translation': translation,
                'explanation': explanation}
            plain_entry_lookup[outline] = translation

"""

print('writing best lookups')
with open("Froj_theories/Froj_Harri_theory/word_lookup.json", "w") as outfile:
        json.dump(word_lookup, outfile, indent=1)

print('writing all lookups')
with open("Froj_theories/Froj_Harri_theory/all_word_lookup.json", "w") as outfile:
        json.dump(all_word_lookup, outfile, indent=1)

print('writing normal entries')
with open("Froj_theories/Froj_Harri_theory/Froj_Plover_dictionary.json", "w") as outfile:
        json.dump(plover_lookup, outfile, indent=1)

print('writing verbose entry to word lookup')
with open("Froj_theories/Froj_Harri_theory/Froj_verbose_lookup.json", "w") as outfile:
        json.dump(entry_lookup, outfile, indent=1)



"""
try:
            # If the thing I'm going to add is less ambiguous, add it
            if best_outlines[f"length {outline_length}"]['ambiguity'] > word['steno stuff'][outline]['ambiguity']:
                best_outlines[f"length {outline_length}"] = {
                    'raw steno': outline,
                    'ambiguity': word['steno stuff'][outline]['ambiguity'],
                    'explanation': word['steno stuff'][outline]['explanation']}

        except KeyError:
            best_outlines[f'length {outline_length}'] = {
                'raw steno': outline,
                'ambiguity': word['steno stuff'][outline]['ambiguity'],
                'explanation': word['steno stuff'][outline]['explanation']}


"""