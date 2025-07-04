"""

"""
import multiprocessing
import json
import tqdm

from froj_brains.convert_unilex_into_readable_lists import (
    full_entry_pattern,
    make_boundaries_into_list,
    make_target_pronunciation_into_string,
)

from froj_brains.map_steno_chords_to_keysymbols import generate_write_outs

from Froj_theories.Froj_Harri_theory.chord_definitions import steno_chords_and_their_meanings
import time

def make_unilex_definition_into_dictionary_entry(unilex_definition, user_chords):
    word = full_entry_pattern.fullmatch(unilex_definition).groupdict()

    word['pronunciation'] = make_target_pronunciation_into_string(make_boundaries_into_list(word['pronunciation']))
    word['word_boundaries'] = word["word"].split(":")[0]
    word['number of entries'] = 0
    word['steno stuff'] = generate_write_outs(word, user_chords)
    word['number of entries'] = len(word['steno stuff'])
    word['pronunciation'] = str(word['pronunciation'])
    word['word_boundaries'] = str(word['word_boundaries'])
    return word


with (open("pronunciation_data/big.txt", "r", encoding="utf-8")) as txt_dictionary:
    outlines = txt_dictionary.readlines()

# for one at a time (not multiprocessing), uncomment the next two lines
#for outline in outlines:
#    results = make_unilex_definition_into_dictionary_entry(outline, steno_chords_and_their_meanings)

def make_unilex_entry_helper(args):
    return make_unilex_definition_into_dictionary_entry(*args)

if __name__ == '__main__':

    start_time = time.time()
    print(f"Start Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_time))}")

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        tasks = ((outline, steno_chords_and_their_meanings) for outline in outlines)
        results = list(tqdm.tqdm(pool.imap(make_unilex_entry_helper, tasks),
                                 total=len(outlines),
                                 unit="words",
                                 smoothing=0, #don't use a moving average for the words/s
                                 desc="converting words into entries"))

    end_time = time.time()
    print(f"End Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time))}")

    runtime = end_time - start_time
    print(f"Total Runtime: {runtime:.2f} seconds")

    print('now writing it to the json file...')

    with open("Froj_theories/Froj_user_theory.json", "w") as outfile:
        json.dump(results, outfile, indent=1)
