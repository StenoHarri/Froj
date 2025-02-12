"""
Using the layout

STKPWHRAO*eufrpblgtsds
Making the right hand lowercase so I don't have to worry about left P vs right P

"""

import re

from chord_definitions import custom_alphabet

order_map = {char: index for index, char in enumerate(custom_alphabet)}
def custom_sort_key(word):
    return [order_map[char] for char in word]



def add_chord_to_chords(old_chords, new_chord):

    if new_chord:
        old_chords = old_chords.replace("_","")

    unalphabetical_entry = (old_chords + new_chord).split("/")

    # Check and sort the last part if necessary
    if sorted(unalphabetical_entry[-1], key=lambda x: order_map[x]) != list(unalphabetical_entry[-1]):
        unalphabetical_entry[-1] = ''.join(sorted(unalphabetical_entry[-1], key=lambda x: order_map[x]))

    return "/".join(unalphabetical_entry)


def add_pronunciation_to_pronunciation(old_pronunciation, new_pronunciation, criteria):
    criteria = re.compile("^"+criteria)
    if criteria.search(old_pronunciation+new_pronunciation):
        return  old_pronunciation+new_pronunciation
    return False

"""
def make_target_pronunciation_into_string(target_list):
    string=" starting__"
    for morpheme in target_list:
        #print(morpheme[1][0]) would print stuff like root root root root
        string+=' '+morpheme[1][0] + "  " + "  ".join(morpheme[0]) + " "
    return string.replace('_ ','')
"""

def add_pronunciation_to_pronunciation(old_pronunciation, new_pronunciation, target):
    criteria = re.compile("^"+old_pronunciation + new_pronunciation)

    target

    if criteria.search(target):
        return old_pronunciation+new_pronunciation
    return False

"""
def make_target_spelling_into_string(target_list):
    string=""
    for morpheme in target_list:
        string+="Something went wrong".join(morpheme[0])
    return string
"""
    
def add_spelling_to_spelling(old_spelling, new_spelling, target):
    criteria = re.compile("^"+old_spelling + new_spelling)

    if criteria.search(target):
        return old_spelling+new_spelling

    return False

def is_entry_complete(entry, pronunciation_target, spelling_target):

    if not re.search(r'[AOeufrpblgtsdz]\*?$', entry["raw steno outline"]):
        return False

    pronunciation_regex_attempt = re.compile(entry['pronunciation'])
    spelling_regex_attempt = re.compile(entry['spelling'])
    if pronunciation_regex_attempt.fullmatch(pronunciation_target) and spelling_regex_attempt.fullmatch(spelling_target):

        
        return {"raw steno outline": entry["raw steno outline"],
                "ambiguity":entry["ambiguity"],
                "explanation":entry["explanation of each chord"]},

    return False


def add_a_chord_onto_each_incomplete_entry(initial_dictionary, target_pronunciation, target_spelling, never_seen_before_entries=[], every_complete_entry_generated={}, preconditions_and_their_chords={}):

    

    dictionary_with_a_chord_added_to_each_entry =[]
    for entry in initial_dictionary:

        for precondition in preconditions_and_their_chords:

            #many chords, like vowels, all share the same precondition, also it's a cheap check computationally
            if not precondition.search(entry["raw steno outline"]):
                continue

            for preconditions_chord in preconditions_and_their_chords[precondition]:

                #I don't know which of these is computationally cheaper, but on longwords, spelling being first is more than twice as fast as pronunciation being first

                spelling = add_spelling_to_spelling(entry["spelling"], preconditions_chord["spelling"], target_spelling)
                if not spelling:
                    continue

                pronunciation = add_pronunciation_to_pronunciation(entry["pronunciation"], preconditions_chord["pronunciation"], target_pronunciation)
                if not pronunciation:
                    continue

                raw_steno_outline = add_chord_to_chords(entry["raw steno outline"] , preconditions_chord["raw steno"])

                ambiguity = entry["ambiguity"] + preconditions_chord["ambiguity"]

                #I can't just assign explanation=explanation because of deep copies or something
                #apparently it's not though, but I still gotta create it empty first so I'll keep it
                explanation=[]

                #use the already built up explanation
                explanation += (entry["explanation of each chord"])

                #add this chord to the explanation
                explanation.append([preconditions_chord["description"],
                                    #"steno theory: "+preconditions_chord["steno theory"],
                                    #"How arbitrary: "+str(preconditions_chord["ambiguity"])
                                    ])

                dictionary_with_a_chord_added_to_each_entry+=[{
                    "raw steno outline":raw_steno_outline,
                    "pronunciation":pronunciation,
                    "spelling":spelling,
                    "ambiguity":ambiguity,
                    "explanation of each chord":explanation
                }]

    new_never_seen_before_entries = []
    for entry in dictionary_with_a_chord_added_to_each_entry:
        if not entry in initial_dictionary or never_seen_before_entries:

            #remember that a valid entry can still be added to... maybe not?
            #actually yeah it can't, because /K and /K can be different chords
            is_entry_complete_answer = is_entry_complete(entry, target_pronunciation, target_spelling)
            if is_entry_complete_answer:


                #now I'm just gonna check to see if the entry we're adding is the least briefy for that entry
                if every_complete_entry_generated == {}:
                    every_complete_entry_generated[is_entry_complete_answer[0]["raw steno outline"]] = is_entry_complete_answer[0]
                elif not is_entry_complete_answer[0]["raw steno outline"] in every_complete_entry_generated:
                        every_complete_entry_generated[is_entry_complete_answer[0]["raw steno outline"]] = is_entry_complete_answer[0]

                        #So far it seems the least briefy entry is ALWAYS added to the stroke first... why? Whatever, it means I can just say "if it's not in there, it's the best, if it's in there, it's already been beaten

                        #Since I made that comment, I've redone how the chords are stored so perhaps this is now broken

            else:
                new_never_seen_before_entries.append(entry)

    if new_never_seen_before_entries:

        #this is where I would have put more multiprocessing
        never_seen_before_entries, every_complete_entry_generated = (
            add_a_chord_onto_each_incomplete_entry(
                new_never_seen_before_entries,
                target_pronunciation,
                target_spelling,
                new_never_seen_before_entries,
                every_complete_entry_generated,
                preconditions_and_their_chords=preconditions_and_their_chords))


    return never_seen_before_entries, every_complete_entry_generated


def filter_user_chords_to_only_the_chords_that_feasibly_can_come_up(input_word, user_chords):
    filtered_user_chords = {}
    for user_chord in user_chords:

        chord_interpretations = []
        for chord_interpretation in user_chords[user_chord]:

            if re.search(chord_interpretation["pronunciation"], input_word["pronunciation"]) and re.search(chord_interpretation["spelling"], input_word["word_boundaries"]):

                chord_interpretations.append(chord_interpretation)

        if chord_interpretations:
            filtered_user_chords[user_chord]=chord_interpretations

    return filtered_user_chords

def filter_chords_by_which_can_feasibly_come_up_then_sort_by_their_precondition(input_word, steno_chords_and_their_meanings):

    preconditions_and_their_chords = {}

    for chord in steno_chords_and_their_meanings:

        for chord_interpretation in steno_chords_and_their_meanings[chord]:

            if (re.search(chord_interpretation["pronunciation"], input_word["pronunciation"]) and
                re.search(chord_interpretation["spelling"],      input_word["word_boundaries"])):

                chord_interpretation["raw steno"] = chord

                # Add value to the key, initializing it if it does not exist (thanks ChatGPT
                preconditions_and_their_chords[chord_interpretation["what must come before"]] = preconditions_and_their_chords.setdefault(chord_interpretation["what must come before"], []) + [chord_interpretation]


            #chord_interpretation["raw steno"] = chord
            #preconditions_and_their_chords[chord_interpretation["what must come before"]] = chord_interpretation


    return preconditions_and_their_chords




def generate_write_outs(input_word, user_chords):

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
    last_entry_generated ,list_of_incomplete_entries = add_a_chord_onto_each_incomplete_entry(list_of_incomplete_entries, input_word['pronunciation'], input_word['word_boundaries'], every_complete_entry_generated={}, preconditions_and_their_chords=preconditions_and_their_chords)

    if list_of_incomplete_entries==[]:
        return["###########################################################################"]
    
    return(list_of_incomplete_entries)




#print(generate_write_outs("test"))
