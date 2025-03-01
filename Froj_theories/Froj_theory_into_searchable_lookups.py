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

def create_lookups(spelling, ordered_outlines_for_this_particular_word, all_outlines, all_entries, resolved_entries):



    previous_ambiguity = 100


    for outline in ordered_outlines_for_this_particular_word:

        outline = outline[1]

        raw_steno = (outline['raw steno outline'][1:]
                     .replace("z*","*z")
                     .replace("d*","*d")
                     .replace("s*","*s")
                     .replace("t*","*t")
                     .replace("g*","*g")
                     .replace("l*","*l")
                     .replace("b*","*b")
                     .replace("p*","*p")
                     .replace("r*","*r")
                     .replace("f*","*f")
                     .replace("u*","*u")
                     .replace("e*","*e")
                     .replace("-*","*").upper()
        )
        ambiguity = outline['ambiguity']
        explanation = outline['explanation']

        #chance for words with the same spelling to overwrite stuff here :(
        if spelling in all_outlines:
            if ambiguity in all_outlines[spelling]['ambiguity']:

                if not any(d['raw steno outline'] == raw_steno and d['explanation'] == explanation for d in all_outlines[spelling]['ambiguity'][ambiguity]):

                    all_outlines[spelling]['ambiguity'][ambiguity].append(
                         {'raw steno outline': raw_steno,
                          'explanation': explanation})

            else:
                #nothing with that ambiguity exists yet
                all_outlines[spelling]['ambiguity'][ambiguity] = [
                    {'raw steno outline': raw_steno,
                     'explanation': explanation}]
        else:
            #nothing with that spelling exists yet
            all_outlines[spelling]={'ambiguity': {ambiguity: [
                {'raw steno outline': raw_steno,
                 'explanation': explanation}]}}


        #if it exists, add it alongside any with the same ambiguity
        if raw_steno in all_entries:
            if ambiguity in all_entries[raw_steno]['ambiguity']:
                if not any(d['spelling'] == spelling and d['explanation'] == explanation for d in all_entries[raw_steno]['ambiguity'][ambiguity]): #some words have the same spelling and the same outline, like a
                    all_entries[raw_steno]['ambiguity'][ambiguity].append(
                        {'spelling': spelling,
                         'explanation': explanation})
            else:
                #no entry with that ambiguity exists yet
                all_entries[raw_steno]['ambiguity'][ambiguity] = [
                    {'spelling': spelling,
                     'explanation': explanation}]
        else:
            #no entry exists yet
            resolved_entries[raw_steno] = spelling
            all_entries[raw_steno] = {'ambiguity':{ambiguity: [
                {'spelling': spelling,
                 'explanation': explanation}]}}

    return all_outlines, all_entries, resolved_entries


print('generating dictionaries')


#making these outside of the loop since they'll interact with each other (notify you of conflicts!!!)

#this could be a dictionary of dictionaries, but I'mma stick to three separate ones
all_outlines = {}
all_entries = {}
resolved_entries = {} #not for the Discord bot, but for me to have on Plover


for word in words:

    #some words have the same spelling, but I'd consider them different words, like point and point
    #I'm prepared to just suck it up and lose that data :(
    spelling = word['word'].split(":")[0]

    ordered_outlines_for_this_particular_word = (ordered_by_length(word))

    all_outlines, all_entries, resolved_entries = create_lookups(spelling, ordered_outlines_for_this_particular_word, all_outlines, all_entries, resolved_entries)


#print('writing best lookups')
#with open("Froj_theories/Froj_Harri_theory/best_outlines.json", "w") as outfile:
#        json.dump(best_outlines, outfile, indent=1)

print('writing word -> entry lookups')
with open("Froj_theories/Froj_Harri_theory/all_outlines.json", "w") as outfile:
        json.dump(all_outlines, outfile, indent=1)

print('writing entry -> word lookups')
with open("Froj_theories/Froj_Harri_theory/all_entries.json", "w") as outfile:
        json.dump(all_entries, outfile, indent=1)

print('writing Plover entry -> word')
with open("Froj_theories/Froj_Harri_theory/resolved_entries.json", "w") as outfile:
        json.dump(resolved_entries, outfile, indent=1)
