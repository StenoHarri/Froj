import json

with open("Froj_Harri_theory/complete_output.json", 'r') as f:
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

best_word_lookup = {}
all_word_lookup = {}
plain_entry_lookup = {}
verbose_entry_lookup = {}

print('generating dictionaries')
for word in words:

    ordered_outlines = (sort_word_outlines(word))

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



print('writing best lookups')
with open("Froj_Harri_theory/best_of_word_to_entry_lookup.json", "w") as outfile:
        json.dump(best_word_lookup, outfile, indent=1)

print('writing all lookups')
with open("Froj_Harri_theory/best_of_word_to_entry_lookup.json", "w") as outfile:
        json.dump(all_word_lookup, outfile, indent=1)

print('writing normal entries')
with open("Froj_Harri_theory/Froj_Plover_dictionary.json", "w") as outfile:
        json.dump(plain_entry_lookup, outfile, indent=1)

print('writing verbose entry to word lookup')
with open("Froj_Harri_theory/Froj_verbose_lookup.json", "w") as outfile:
        json.dump(verbose_entry_lookup, outfile, indent=1)
