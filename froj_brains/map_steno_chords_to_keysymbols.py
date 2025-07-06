"""
Using the layout

STKPWHRAO*eufrpblgtsds
Making the right hand lowercase so I don't have to worry about left P vs right P

"""

import re


def custom_sort_key(word, order_map):
    return [order_map[char] for char in word]



def add_chord_to_chords(old_chords, new_chord, order_map):

    if new_chord:
        old_chords = old_chords.replace("_","")

    unalphabetical_entry = (old_chords + new_chord).split("/")

    # Check and sort the last part if necessary
    #if sorted(unalphabetical_entry[-1], key=lambda x: order_map[x]) != list(unalphabetical_entry[-1]):
    #    unalphabetical_entry[-1] = ''.join(sorted(unalphabetical_entry[-1], key=lambda x: order_map[x]))

    #Chat's
    last_part = unalphabetical_entry[-1]
    if list(last_part) != sorted(last_part, key=lambda x: order_map[x]):
        unalphabetical_entry[-1] = ''.join(sorted(last_part, key=lambda x: order_map[x]))

    return "/".join(unalphabetical_entry)




def add_pronunciation_to_pronunciation(old_pronunciation, new_pronunciation, target):
    criteria = re.compile(f"^{old_pronunciation}{new_pronunciation}")

    target

    if criteria.match(target):
        return f"{old_pronunciation}{new_pronunciation}"
    return False


def add_spelling_to_spelling(old_spelling, new_spelling, target):
    criteria = re.compile(f"^{old_spelling}{new_spelling}")

    if criteria.match(target):
        return f"{old_spelling}{new_spelling}"

    return False

def is_entry_complete(entry, pronunciation_target, spelling_target, valid_final_letter):

    if not re.search(r'['+valid_final_letter+']\*?$', entry["raw steno outline"]):
        return False

    pronunciation_regex_attempt = re.compile(entry['pronunciation'])
    spelling_regex_attempt = re.compile(entry['spelling'])
    if pronunciation_regex_attempt.fullmatch(pronunciation_target) and spelling_regex_attempt.fullmatch(spelling_target):

        return {"raw steno outline": entry["raw steno outline"],
                "ambiguity":entry["ambiguity"],
                "explanation":entry["explanation of each chord"]},

    return False



def add_chord_for_entry(entry, preconditions_chord, target_pronunciation, target_spelling, order_map):
    """
    Adds a chord to the entry if it's valid.
    Returns the updated entry or None if not valid.
    """
    # Add spelling if it's valid
    spelling = add_spelling_to_spelling(entry["spelling"], preconditions_chord["spelling"], target_spelling)
    if not spelling:
        return None  # No valid spelling found

    # Add pronunciation if it's valid
    pronunciation = add_pronunciation_to_pronunciation(entry["pronunciation"], preconditions_chord["pronunciation"], target_pronunciation)
    if not pronunciation:
        return None  # No valid pronunciation found

    # Update the raw steno outline
    raw_steno_outline = add_chord_to_chords(entry["raw steno outline"], preconditions_chord["raw steno"], order_map)

    # Update ambiguity and explanation
    ambiguity = entry["ambiguity"] + preconditions_chord["ambiguity"]


    explanation = (entry["explanation of each chord"] +
                   [
                       {
                        'theory': preconditions_chord["theory"],
                        'chord': preconditions_chord["chord"],
                        'description': preconditions_chord["description"]
                       }
                    ]
                   )


    return {
        "raw steno outline": raw_steno_outline,
        "pronunciation": pronunciation,
        "spelling": spelling,
        "ambiguity": ambiguity,
        "explanation of each chord": explanation
    }


def process_preconditions_and_chords(entry, preconditions_and_their_chords, target_pronunciation, target_spelling, order_map):
    """
    Processes the chords for a given entry and returns valid updates.
    """
    updated_entries = []

    for precondition, preconditions_chords in preconditions_and_their_chords.items():
        # If the precondition matches the entry, process the chords
        if precondition.search(entry["raw steno outline"]):
            for preconditions_chord in preconditions_chords:
                # Try adding a chord for the entry
                updated_entry = add_chord_for_entry(entry, preconditions_chord, target_pronunciation, target_spelling, order_map)
                if updated_entry:
                    updated_entries.append(updated_entry)

    return updated_entries



def add_a_chord_onto_each_incomplete_entry(initial_dictionary, target_pronunciation, target_spelling, never_seen_before_entries=[], every_complete_entry_generated={}, preconditions_and_their_chords={}, order_map={}, valid_final_letter=''):
    """
    Adds a chord to each incomplete entry, with optimized logic.
    """
    # List to store entries with added chords
    dictionary_with_a_chord_added_to_each_entry = []

    for entry in initial_dictionary:
        updated_entries = process_preconditions_and_chords(entry, preconditions_and_their_chords, target_pronunciation, target_spelling, order_map)

        # Add updated entries to the result list
        dictionary_with_a_chord_added_to_each_entry.extend(updated_entries)

    # Create a set of unique identifiers (e.g., 'raw steno outline') from initial_dictionary
    initial_set = set(entry["raw steno outline"] for entry in initial_dictionary)

    # Initialize the list for new entries
    new_never_seen_before_entries = []

    for entry in dictionary_with_a_chord_added_to_each_entry:
        raw_steno_outline = entry["raw steno outline"]

        # If the raw_steno_outline is not in initial_set or hasn't been processed yet, check it
        if raw_steno_outline not in initial_set and raw_steno_outline not in every_complete_entry_generated:
            is_entry_complete_answer = is_entry_complete(entry, target_pronunciation, target_spelling, valid_final_letter)

            if is_entry_complete_answer:
                # Add the complete entry to the dictionary
                every_complete_entry_generated[raw_steno_outline] = is_entry_complete_answer[0]
            else:
                new_never_seen_before_entries.append(entry)



    # Handle recursion if there are still new entries that haven't been seen before
    if new_never_seen_before_entries:
        never_seen_before_entries, every_complete_entry_generated = add_a_chord_onto_each_incomplete_entry(
            new_never_seen_before_entries,
            target_pronunciation,
            target_spelling,
            new_never_seen_before_entries,
            every_complete_entry_generated,
            preconditions_and_their_chords=preconditions_and_their_chords,
            order_map=order_map,
            valid_final_letter=valid_final_letter
        )

    return never_seen_before_entries, every_complete_entry_generated

from collections import defaultdict

def filter_chords_by_which_can_feasibly_come_up_then_sort_by_their_precondition(input_word, steno_chords_and_their_meanings):

    #Use a defaultdict(list) from the collections module to avoid repeatedly checking and setting default values.
    preconditions_and_their_chords = defaultdict(list)

    for chord in steno_chords_and_their_meanings:

        for chord_interpretation in steno_chords_and_their_meanings[chord]:

            if (re.search(chord_interpretation["pronunciation"], input_word["pronunciation"]) and
                re.search(chord_interpretation["spelling"],      input_word["word_boundaries"])):

                chord_interpretation["raw steno"] = chord

                # Add value to the key, initializing it if it does not exist (thanks ChatGPT
                preconditions_and_their_chords[chord_interpretation["what must come before"]].append(chord_interpretation)


            #chord_interpretation["raw steno"] = chord
            #preconditions_and_their_chords[chord_interpretation["what must come before"]] = chord_interpretation


    return preconditions_and_their_chords




def generate_write_outs(input_word, user_chords, order_map, valid_final_letter):

    list_of_incomplete_entries = [
        {
        "raw steno outline":"/",
        "pronunciation":" starting_(prefix|root) ",
        "spelling":"",
        "ambiguity": 0,
        "explanation of each chord": []
        }
    ]

    #user_chords = filter_user_chords_to_only_the_chords_that_feasibly_can_come_up(input_word, user_chords)

    #I actually want to sort chords by their precondition, since things like vowels will all have the same preconditions, I can save on logic by just checking once
    preconditions_and_their_chords = filter_chords_by_which_can_feasibly_come_up_then_sort_by_their_precondition(input_word, user_chords)

    #print(input_word['word'])
    last_entry_generated ,list_of_incomplete_entries = add_a_chord_onto_each_incomplete_entry(list_of_incomplete_entries, input_word['pronunciation'], input_word['word_boundaries'], every_complete_entry_generated={}, preconditions_and_their_chords=preconditions_and_their_chords, order_map=order_map, valid_final_letter= valid_final_letter)

    if list_of_incomplete_entries==[]:
        return["###########################################################################"]

    return(list_of_incomplete_entries)




#print(generate_write_outs("test"))
