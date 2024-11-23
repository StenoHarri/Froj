"""
Using the layout

STKPWHRAO*eufrpblgtsds
Making the right hand lowercase so I don't have to worry about left P vs right P

"""

import re


y_chord = "KWH" # the 'y' in yet or the 'i' in genius
silent_linker = "KWR" # the 'linker' in genus


keysymbol_shorthands = {
    """
    There will be groups of keysymbols that come up again and again,
    so I'll define them once here
    """
    "long a": "a i",
    "schwa": "@",
    "any vowel": "(a|@)"
}

spelling_shorthands = {
    """
    There will be groups of letters that come up again and again,
    so I'll define them once here
    """
    "": "a i",
    "schwa": "@",
    "": ""
}

"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {

    "": [
        {"description": "silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": ".*[/STKPWHR]\*?((Aoe)|(AOeu)|(AOu)|(Ae)|(Aeu)|(O)|(Oe)|(Oeu))[*frpblgtsdz]+",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"}],


    "/S": [
        {"description": "S for initial s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": "",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

        {"description": "S for linking s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": "(.*[AOEUFRPBLGTSDZ]\*?)",
         "what does it affect": ['root', 'suffix', 'prefix','compound'],
         "steno theory": "WSI"},

        {"description": "S for linking vowel + s",
         "spelling": "[aeiouy]ss?",
         "pronunciation": keysymbol_shorthands["any vowel"] + " s ",
         "ambiguity": 1,
         "what must come before": "(.*[AOEUFRPBLGTSDZ]\*?)",
         "what does it affect": ['root', 'suffix', 'prefix','compound'],
         "steno theory": "WSI"}],

    "/S*": [
        {"description": "S* for initial s of a compound word",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": "(.*[AOEUFRPBLGTSDZ])*",
         "what does it affect": ['compound'],
         "steno theory": "WSI"}],


    "S": [

         {"description": "S for s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": "(.*/)*[TKPWHR]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

        {"description": "S for s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": ".*[/TKPWHR]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

        {"description": "S for soft c",
         "spelling": "c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": ".*[/TKPWHR]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

        {"description": "S for sc",
         "spelling": "sc",
         "pronunciation": " s ",
         "ambiguity": 2,
         "what must come before": ".*[/TKPWHR]+",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

        {"description": "S for s+vowel+consonant",
         "spelling": "sc",
         "pronunciation": " s "+keysymbol_shorthands["any vowel"]+ "( s )|( b )",
         "ambiguity": 3,
         "what must come before": ".*[/TKPWHR]+",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"}],


    "/K": [
        {"description": "K for initial/linking k",
         "spelling": "k",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 0,
         "what must come before": "",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

         {"description": "K for initial/linking hard c",
         "spelling": "c",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 1,
         "what must come before": "",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"}],

    "K": [
        {"description": "K for k",
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": ".*[/S]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

        {"description": "K for hard c",
         "spelling": "c",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": ".*[/S]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"}],


    "/"+silent_linker: [
        {"description": silent_linker + " for silent linker",
         "spelling": "",
         "pronunciation": " ((root)|(prefix)|(suffix)) ",
         "ambiguity": 0,
         "what must come before": ".*[frpblgtsdz]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "User preference"},

         {"description": silent_linker + " for silent linker that ignores word boundaries",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before": ".*[frpblgtsdz]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "User preference"}],

    "/"+y_chord: [
        {"description": y_chord + " for initial/linking y",
         "spelling": "y",
         "pronunciation": " ((root)|(prefix)|(suffix))?  iy ",
         "ambiguity": 0,
         "what must come before": ".*",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "User preference"}],

    "HR": [
        {"description": "HR for l",
         "spelling": "l",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": ".*[/STKPW]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},


        {"description": "HR for ll",
         "spelling": "ll",
         "pronunciation": " l ",
         "ambiguity": 1, #Alan Allan
         "what must come before": ".*[/STKPW]\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"}],

    "Ou": [
        {"description": "OU for ow said like ow",
         "spelling": "ow",
         "pronunciation": " ow ",
         "ambiguity": 0,
         "what must come before": ".*[STKPWHR]+\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"},

        {"description": "OU for ou said like ow",
         "spelling": "ou",
         "pronunciation": " ow ",
         "ambiguity": 1,
         "what must come before": ".*[STKPWHR]+\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"}],

    "eu": [
        {"description": "EU for y said like long e",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": ".*[STKPWHR]+\*?",
         "what does it affected": ['root', 'suffix', 'prefix'],
         "steno theory": "I think StenEd?"}],


    "d": [
        {"description": "-D for d",
         "spelling": "d",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": ".*[STKPWHRAOeu]+\*?",
         "what does it affect": ['root', 'suffix', 'prefix'],
         "steno theory": "WSI"}]

}

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
                "ambiguity":entry["built-up"]["ambiguity"]},

    return False


def add_a_chord_onto_each_incomplete_entry(initial_dictionary, target_pronunciation, target_spelling, never_seen_before_entries=[], every_complete_entry_generated=[]):

    dictionary_with_a_chord_added_to_each_entry =[]
    for entry in initial_dictionary:
        for chord in steno_chords_and_their_meanings:
            
            #Um actually it's fine to break steno order
            #if not is_steno_order.match(entry["built-up"]["steno outline"] + chord):
            #    next

            for chord_interpretation in steno_chords_and_their_meanings[chord]:

                chords = add_chord_to_chords(entry["built-up"]["steno outline"], chord, chord_interpretation["what must come before"])
                if not chords:
                    continue

                pronunciation = add_pronunciation_to_pronunciation(entry["built-up"]["pronunciation"], chord_interpretation["pronunciation"], target_pronunciation)
                if not pronunciation:
                    continue

                spelling = add_spelling_to_spelling(entry["built-up"]["spelling"], chord_interpretation["spelling"], target_spelling)
                if not spelling:
                    continue

                ambiguity = entry["built-up"]["ambiguity"] + chord_interpretation["ambiguity"]



                dictionary_with_a_chord_added_to_each_entry+=[{
                    "built-up":{
                        "steno outline":chords,
                        "pronunciation":pronunciation,
                        "spelling":spelling,
                        "ambiguity":ambiguity,},
                    "explanation of each chord":[]
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

    #if not list_of_incomplete_entries==[]:
    
    return(list_of_incomplete_entries)




#print(generate_write_outs("test"))
