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



def add_chord_to_chords(old_chords, new_chord, criteria):




    #if old_chords == "/KHROud":
    #    print("here")
    if criteria.fullmatch(old_chords):

        if new_chord:
            old_chords = old_chords.replace("_","")

        unalphabetical_entry = (old_chords + new_chord).split("/")

        # Check and sort the last part if necessary
        if sorted(unalphabetical_entry[-1], key=lambda x: order_map[x]) != list(unalphabetical_entry[-1]):
            unalphabetical_entry[-1] = ''.join(sorted(unalphabetical_entry[-1], key=lambda x: order_map[x]))

        return "/".join(unalphabetical_entry)
    return False

def add_pronunciation_to_pronunciation(old_pronunciation, new_pronunciation, criteria):
    criteria = re.compile(criteria+".*")
    if criteria.fullmatch(old_pronunciation+new_pronunciation):
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
    criteria = re.compile(old_pronunciation + new_pronunciation +".*")

    target

    if criteria.fullmatch(target):
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
    criteria = re.compile(old_spelling + new_spelling + ".*")

    target

    if criteria.fullmatch(target):
        return old_spelling+new_spelling

    return False

def is_entry_complete(entry, pronunciation_target, spelling_target):

    if not re.fullmatch(r'.*[AOeufrpblgtsdz]\*?', entry['built-up']["steno outline"]):
        return False

    pronunciation_regex_attempt = re.compile(entry['built-up']['pronunciation'])
    spelling_regex_attempt = re.compile(entry['built-up']['spelling'])
    if pronunciation_regex_attempt.fullmatch(pronunciation_target) and spelling_regex_attempt.fullmatch(spelling_target):

        
        return {"steno outline": entry["built-up"]["steno outline"],
                "ambiguity":entry["built-up"]["ambiguity"],
                "explanation":entry["explanation of each chord"]},

    return False


def add_a_chord_onto_each_incomplete_entry(initial_dictionary, target_pronunciation, target_spelling, never_seen_before_entries=[], every_complete_entry_generated={}, steno_chords_and_their_meanings={}):

    

    dictionary_with_a_chord_added_to_each_entry =[]
    for entry in initial_dictionary:

        #if entry['built-up']["steno outline"] == "/KHROu/TKeu/KWR":
        #    print("here")
        #if entry['built-up']["steno outline"] == "/KHROu/TKeu":
        #    print("here")

        for chord in steno_chords_and_their_meanings:
            
            #Um actually it's fine to break steno order
            #if not is_steno_order.match(entry["built-up"]["steno outline"] + chord):
            #    next


            for chord_interpretation in steno_chords_and_their_meanings[chord]:

                #if chord_interpretation["description"] == "folding ER for suffix er":
                #    print("here")
                #if chord_interpretation["description"] == "folding ER for suffix er":
                #    print("here")
                #if entry["built-up"]["spelling"] == "clown":
                #    print("here")
                #if chord_interpretation["description"] == "folded -G for -ing":
                #    print("here")

                #if entry["built-up"]["steno outline"] == "/KHROupb/KWReurb":
                #    print("here")



                chords = add_chord_to_chords(entry["built-up"]["steno outline"], chord, chord_interpretation["what must come before"])
                if not chords:
                    continue

                #if chord_interpretation["spelling"] == "s":
                #    print("here")


                #if chord_interpretation["description"] == "TPH for linking n":
                #    print("here")

                spelling = add_spelling_to_spelling(entry["built-up"]["spelling"], chord_interpretation["spelling"], target_spelling)
                if not spelling:
                    continue

                pronunciation = add_pronunciation_to_pronunciation(entry["built-up"]["pronunciation"], chord_interpretation["pronunciation"], target_pronunciation)
                if not pronunciation:
                    continue





                ambiguity = entry["built-up"]["ambiguity"] + chord_interpretation["ambiguity"]

                #if entry["built-up"]["steno outline"] == "/KHROupb/KWReurb":
                #    print("here")

                explanation=[]
                #I can't just assign this because of deep copies or something
                explanation += (entry["explanation of each chord"])
                explanation.append([chord_interpretation["description"],"steno theory: "+chord_interpretation["steno theory"],"How arbitrary: "+str(chord_interpretation["ambiguity"])])


                dictionary_with_a_chord_added_to_each_entry+=[{
                    "built-up":{
                        "steno outline":chords,
                        "pronunciation":pronunciation,
                        "spelling":spelling,
                        "ambiguity":ambiguity,},
                    "explanation of each chord":explanation
                }]

    new_never_seen_before_entries = []
    for entry in dictionary_with_a_chord_added_to_each_entry:
        if not entry in initial_dictionary or never_seen_before_entries:
            #print("added "+entry['built-up']["steno outline"], entry['built-up']['spelling'])


            #remember that a valid entry can still be added to... maybe not?
            #actually yeah it can't, because /K and /K can be different chords
            is_entry_complete_answer = is_entry_complete(entry, target_pronunciation, target_spelling)
            if is_entry_complete_answer:


                #now I'm just gonna check to see if the entry we're adding is the least briefy for that entry
                if every_complete_entry_generated == {}:
                    every_complete_entry_generated[is_entry_complete_answer[0]["steno outline"]] = is_entry_complete_answer[0]
                elif not is_entry_complete_answer[0]["steno outline"] in every_complete_entry_generated:
                        every_complete_entry_generated[is_entry_complete_answer[0]["steno outline"]] = is_entry_complete_answer[0]


                        #So far it seems the least briefy entry is ALWAYS added to the stroke first... why? Whatever, it means I can just say "if it's not in there, it's the best, if it's in there, it's already been beaten

            else:
                new_never_seen_before_entries.append(entry)

    if new_never_seen_before_entries:



        never_seen_before_entries, every_complete_entry_generated = (add_a_chord_onto_each_incomplete_entry(new_never_seen_before_entries, target_pronunciation, target_spelling, new_never_seen_before_entries, every_complete_entry_generated, steno_chords_and_their_meanings=steno_chords_and_their_meanings))

        #this is where I should put more multiprocessing

        #with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:

        #    never_seen_before_entries, every_complete_entry_generated = pool.map(add_a_chord_onto_each_incomplete_entry, (new_never_seen_before_entries, target_pronunciation, target_spelling, new_never_seen_before_entries, every_complete_entry_generated))

    
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





def generate_write_outs(input_word, user_chords):

    list_of_incomplete_entries = [
        {
        "built-up":{
            "steno outline":"",
            "pronunciation":"",
            "spelling":"",
            "ambiguity": 0},
        "explanation of each chord":[]
        }
    ]

    user_chords = filter_user_chords_to_only_the_chords_that_feasibly_can_come_up(input_word, user_chords)

    #print(input_word['word'])
    last_entry_generated ,list_of_incomplete_entries = add_a_chord_onto_each_incomplete_entry(list_of_incomplete_entries, input_word['pronunciation'], input_word['word_boundaries'], every_complete_entry_generated={}, steno_chords_and_their_meanings=user_chords)

    if list_of_incomplete_entries==[]:
        return["###########################################################################"]
    
    return(list_of_incomplete_entries)




#print(generate_write_outs("test"))
