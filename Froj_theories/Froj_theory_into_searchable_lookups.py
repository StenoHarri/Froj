import json

print("loading the Froj output file into RAM")
with open("Froj_theories/Froj_Harri_theory/complete_output.json", 'r') as f:
    words = json.load(f)


sorted_words = {}

custom_alphabet = "QSTKPWHRAO-*eufrpblgtsdz_"


word_lookup = {}
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


def create_lookups(spelling, ordered_outlines_for_this_particular_word, all_outlines, all_entries, word_class):


    if spelling[0] == spelling[0].lower():

        #if it needs capitalising, pass it through again but capitalised
        if "NNP" in word_class:
            all_outlines, all_entries = create_lookups(spelling.capitalize(), ordered_outlines_for_this_particular_word, all_outlines, all_entries, word_class)

        # if it's a proper noun and nothing else, we're done here. (Mark vs mark would continue)
        if word_class.replace("POS/","").replace("NNPS","").replace("NNP","").replace("POS","").replace("|","") == "":
            return all_outlines, all_entries

        if "'s" in spelling:
            return all_outlines, all_entries

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
                     .replace("-*","*")
                     .replace("Q","#").upper()
        )

        ambiguity = outline['ambiguity']
        explanation = outline['explanation']
        length = len(raw_steno.split('/'))


        if spelling[0] == spelling[0].capitalize() and not raw_steno[0] == "#":
            raw_steno = "#"+raw_steno
            explanation.insert(0, {
                "theory": "Lapwing",
                "chord": "#",
                "description": "Proper noun"
                })

        # Chance for words with the same spelling to overwrite stuff here :(
        if spelling in all_outlines:
            if ambiguity in all_outlines[spelling]['ambiguity']:

                # Fix the condition to check if the raw_steno and explanation exist under the current ambiguity and length
                if not any(d['raw steno outline'] == raw_steno and d['explanation'] == explanation for d in all_outlines[spelling]['ambiguity'][ambiguity].get('number of strokes', {}).get(length, [])):

                    # Check if there's already an entry with the same ambiguity and length
                    if length in all_outlines[spelling]['ambiguity'][ambiguity].get('number of strokes', {}):
                        # There's already at least one entry with the same ambiguity and length
                        all_outlines[spelling]['ambiguity'][ambiguity]['number of strokes'][length].append(
                            {'raw steno outline': raw_steno,
                            'explanation': explanation})
                    else:
                        # Nothing with this ambiguity has this length
                        all_outlines[spelling]['ambiguity'][ambiguity]['number of strokes'][length] = [
                            {'raw steno outline': raw_steno,
                            'explanation': explanation}]
                else:
                    # An entry with this raw_steno and explanation already exists under this ambiguity and length
                    pass

            else:
                # No ambiguity exists yet for this spelling
                all_outlines[spelling]['ambiguity'][ambiguity] = {
                    'number of strokes': {length: [{'raw steno outline': raw_steno,
                                                    'explanation': explanation}]}}
        else:
            # No spelling exists yet
            all_outlines[spelling] = {
                'ambiguity': {ambiguity: {
                    'number of strokes': {length: [{'raw steno outline': raw_steno,
                                                    'explanation': explanation}]}}}
        }


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
            all_entries[raw_steno] = {'ambiguity':{ambiguity: [
                {'spelling': spelling,
                 'explanation': explanation}]}}

    return all_outlines, all_entries


print('generating dictionaries')


#making these outside of the loop since they'll interact with each other (notify you of conflicts!!!)

#this could be a dictionary of dictionaries, but I'mma stick to three separate ones
all_outlines = {}
all_entries = {}

for word in words:

    #some words have the same spelling, but I'd consider them different words, like point and point
    #I'm prepared to just suck it up and lose that data :(
    spelling = word['word'].split(":")[0]
    word_class = word['word_class']

    ordered_outlines_for_this_particular_word = (ordered_by_length(word))

    all_outlines, all_entries = create_lookups(spelling, ordered_outlines_for_this_particular_word, all_outlines, all_entries, word_class)


print('working out the resolved entries for Plover')
resolved_entries = {} #not for the Discord bot, but for me to have on Plover
for entry in all_entries:

    smallest_ambiguity = 100 #there's a chance there's no entries, so I'm doing it this way just to be safe

    for I_dont_need_this in all_entries[entry]: #this is bad habit since it's not a given that ambiguity is the only data I'll have under the word

        for ambiguity in all_entries[entry]['ambiguity']:

            if ambiguity < smallest_ambiguity:
                smallest_ambiguity = ambiguity
        
        resolved_entries[entry] = all_entries[entry]['ambiguity'][smallest_ambiguity][0]['spelling']

print('writing resolved entries for Plover')
with open("Froj_theories/Froj_Harri_theory/resolved_entries.json", "w") as outfile:
        json.dump(resolved_entries, outfile, indent=1)

print('writing word -> entry lookups')
with open("Froj_theories/Froj_Harri_theory/all_outlines.json", "w") as outfile:
        json.dump(all_outlines, outfile, indent=1)

print('writing entry -> word lookups')
with open("Froj_theories/Froj_Harri_theory/all_entries.json", "w") as outfile:
        json.dump(all_entries, outfile, indent=1)


