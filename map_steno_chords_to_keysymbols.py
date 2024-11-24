"""
Using the layout

STKPWHRAO*eufrpblgtsds
Making the right hand lowercase so I don't have to worry about left P vs right P

"""

import re

from chord_definitions import y_chord,silent_linker,keysymbol_shorthands,spelling_shorthands,steno_chords_and_their_meanings


pronunciation_dictionary={
    #word   :  pronunciation spelling incomplete:[steno pronunciation spelling], complete:
    "cloudiness:" : {
        "pronunciation":[[['k', 'l', 'ow', 'd'], ['root']], [['iy'], ['suffix']], [['n', 'E5', 's'], ['suffix']]],
        "word_boundaries":[[['cloud'], ['root']], [['y'], ['suffix']], [['ness'], ['suffix']]],
        "incomplete steno":[
            {
                'built-up':{
                    "steno outline":"K", 
                    "pronunciation":" k ",
                    "spelling":"c",
                    "ambiguity": 0,
                    "steno theories": ["WSI"]},
                'explanation of each chord':[
                    {
                        "chord":"K",
                        "pronunciation":" k ",
                        "spelling":"c",
                        "ambiguity": 0,
                        "steno theory": "WSI"
                    }
                    ]
            }
            ,
            {
                'built-up':{
                    "steno outline":"KHR",
                    "pronunciation":" k l ",
                    "spelling":"cl",
                    "ambiguity": 0,
                    "steno theories": ["WSI"]},
                'explanation of each chord':[
                    {
                        "chord":"K",
                        "pronunciation":" k ",
                        "spelling":"c",
                        "ambiguity": 0,
                        "steno theory": "WSI"},
                    {
                        "chord":"HR",
                        "pronunciation":" l ",
                        "spelling":"l",
                        "ambiguity": 0,
                        "steno theory": "WSI"}]
            }
            ],
        "steno":[]},

}



def add_chord_to_chords(old_chords, new_chord, criteria):
    #if old_chords == "/KHROud":
    #    print("here")
    criteria = re.compile(criteria)
    if criteria.fullmatch(old_chords):
        return old_chords + new_chord
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


def add_a_chord_onto_each_incomplete_entry(initial_dictionary, target_pronunciation, target_spelling, never_seen_before_entries=[], every_complete_entry_generated=[]):

    dictionary_with_a_chord_added_to_each_entry =[]
    for entry in initial_dictionary:

        #if entry['built-up']["steno outline"] == "/KHROu":
        #    print("here")

        for chord in steno_chords_and_their_meanings:
            
            #Um actually it's fine to break steno order
            #if not is_steno_order.match(entry["built-up"]["steno outline"] + chord):
            #    next


            for chord_interpretation in steno_chords_and_their_meanings[chord]:

                #if chord_interpretation["description"] == "*D for dy":
                #    print("here")
                #if chord_interpretation["description"] == "folded -G for -ing":
                #    print("here")


                chords = add_chord_to_chords(entry["built-up"]["steno outline"], chord, chord_interpretation["what must come before"])
                if not chords:
                    continue

                #if chord_interpretation["description"] == "folded -G for -ing":
                #    print("here")

                pronunciation = add_pronunciation_to_pronunciation(entry["built-up"]["pronunciation"], chord_interpretation["pronunciation"], target_pronunciation)
                if not pronunciation:
                    continue

                spelling = add_spelling_to_spelling(entry["built-up"]["spelling"], chord_interpretation["spelling"], target_spelling)
                if not spelling:
                    continue

                ambiguity = entry["built-up"]["ambiguity"] + chord_interpretation["ambiguity"]

                #if entry["built-up"]["steno outline"] == "/KHROud":
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
                every_complete_entry_generated.append(is_entry_complete_answer)
            else:
                new_never_seen_before_entries.append(entry)

    if new_never_seen_before_entries:
        never_seen_before_entries, every_complete_entry_generated = (add_a_chord_onto_each_incomplete_entry(new_never_seen_before_entries, target_pronunciation, target_spelling, new_never_seen_before_entries, every_complete_entry_generated))
    
    return never_seen_before_entries, every_complete_entry_generated




def generate_write_outs(input_word):

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

    #print(input_word['word'])
    last_entry_generated ,list_of_incomplete_entries = add_a_chord_onto_each_incomplete_entry(list_of_incomplete_entries, input_word['pronunciation'], input_word['word_boundaries'], every_complete_entry_generated=[])

    if list_of_incomplete_entries==[]:
        return["###########################################################################"]
    
    return(list_of_incomplete_entries)




#print(generate_write_outs("test"))
