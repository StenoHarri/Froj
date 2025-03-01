import json

with open("Froj_theories/Froj_Harri_theory/complete_output.json", 'r') as f:
    words = json.load(f)


sorted_words = {}

custom_alphabet = "QSTKPWHRAO-*eufrpblgtsdz_"


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

def create_lookups(spelling, ordered_outlines_for_this_particular_word, best_outlines, all_outlines, all_entries, resolved_entries):



    previous_ambiguity = 100


    for outline in ordered_outlines_for_this_particular_word:

        outline = outline[1]

        raw_steno = outline['raw steno outline'][1:]
        ambiguity = outline['ambiguity']
        explanation = outline['explanation']

        #outline_length = outline['raw steno outline'].count("/")

        if outline['ambiguity'] < previous_ambiguity:
            best_outlines[spelling]= {
                raw_steno: {
                'ambiguity': ambiguity,
                'explanation': explanation}}
            previous_ambiguity=outline['ambiguity']


        #chance for words with the same spelling to overwrite stuff here :(
        all_outlines[spelling]= {
            raw_steno: {
            'ambiguity': ambiguity,
            'explanation': explanation}}

        #if it exists, add it alongside any with the same ambiguity
        if raw_steno in all_entries:
            if ambiguity in all_entries[raw_steno]:

                if not {spelling:explanation} in all_entries[raw_steno][ambiguity]: #some words have the same spelling and the same outline, like a
                    all_entries[raw_steno][ambiguity].append({spelling:explanation})
            else:
                all_entries[raw_steno][ambiguity] = [{spelling:explanation}]

        else:
            #at the moment there's no resolving, it's first come come come
            resolved_entries[raw_steno] = spelling
            all_entries[raw_steno] = {ambiguity: [{spelling:explanation}]}

    return best_outlines, all_outlines, all_entries, resolved_entries


print('generating dictionaries')


#making these outside of the loop since they'll interact with each other (notify you of conflicts!!!)

#this could be a dictionary of dictionaries, but I'mma stick to three separate ones
best_outlines = {}
all_outlines = {}
all_entries = {}
resolved_entries = {} #not for the Discord bot, but for me to have on Plover


for word in words:

    #some words have the same spelling, but I'd consider them different words, like point and point
    #I'm prepared to just suck it up and lose that data :(
    spelling = word['word'].split(":")[0]

    ordered_outlines_for_this_particular_word = (ordered_by_length(word))

    best_outlines, all_outlines, all_entries, resolved_entries = create_lookups(spelling, ordered_outlines_for_this_particular_word, best_outlines, all_outlines, all_entries, resolved_entries)


print('writing best lookups')
with open("Froj_theories/Froj_Harri_theory/best_outlines.json", "w") as outfile:
        json.dump(best_outlines, outfile, indent=1)

print('writing all lookups')
with open("Froj_theories/Froj_Harri_theory/all_outlines.json", "w") as outfile:
        json.dump(all_outlines, outfile, indent=1)

print('writing verbose entry to word lookup')
with open("Froj_theories/Froj_Harri_theory/all_entries.json", "w") as outfile:
        json.dump(all_entries, outfile, indent=1)

print('writing normal entries')
with open("Froj_theories/Froj_Harri_theory/resolved_entries.json", "w") as outfile:
        json.dump(resolved_entries, outfile, indent=1)


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