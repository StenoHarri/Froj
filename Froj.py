"""
questions for professor
why is pancake pang+cake
but suncream sun+cream not sung+cream

huh? why is it "sh == n" and not "== sh n"?
starting_root  l  i  .  k  w  I2  =.=  f  a  k  .  sh  ==  n ",
  "word_boundaries": "lique==fact==ion",


parallelepiped

  
in my accent, the 'air r' in Aaron is different to the 'air r' in aerate.



  
why is
clowned::VBD/VBN/JJ: { k l * ow n }> d > :{clown}>ed>:4
but



  
I've found missing pronunciations for "lithe"
HRAO*EUT seems to be the most common
HR*EUT https://youtu.be/CTgk5pGOe1g?si=MwXHGoLloZJcPXFq&t=517
(8:37)
HRAO*ET https://youtu.be/-5FEgL-BkIk?si=1XSGHabJnnN6g-fg&t=10239
(2:50:40)

I've also found voiced and unvoiced versions for "lithe", but I don't know of any steno theory that makes a distinction so that doesn't interest me


The word "outworkings" is missing,



Going based off word boundaries instead of the spelling means there's no difference between downy and downie
"""
import multiprocessing
import json

from convert_unilex_into_readable_lists import (
    full_entry_pattern,
    make_boundaries_into_list,
    make_target_pronunciation_into_string,
    make_target_spelling_into_string)

from map_steno_chords_to_keysymbols import generate_write_outs

from chord_definitions import steno_chords_and_their_meanings








def make_input_into_dictionary_entry(input, user_chords):
    word = full_entry_pattern.fullmatch(input).groupdict()

    word['pronunciation'           ] = make_target_pronunciation_into_string(make_boundaries_into_list(word['pronunciation']))
    word['word_boundaries'         ] = make_target_spelling_into_string(make_boundaries_into_list(word['word_boundaries']))
    word['number of entries'   ] = (0)
    word['steno stuff'         ] = generate_write_outs(word, user_chords)
    word['number of entries'   ] = len(word['steno stuff'])



    word['pronunciation'           ] = str(word['pronunciation'])
    word['word_boundaries'           ] = str(word['word_boundaries'])
    return word



with (open("big.txt", "r", encoding="utf-8")) as txt_dictionary:
    outlines = txt_dictionary.readlines()



#for outline in outlines:
#    results = make_input_into_dictionary_entry(outline, steno_chords_and_their_meanings)



#using multiple inputs
with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    results = pool.starmap(make_input_into_dictionary_entry, [(outline, steno_chords_and_their_meanings) for outline in outlines])


with open("Froj_output.json", "w") as outfile:
    json.dump(results, outfile, indent=1)

