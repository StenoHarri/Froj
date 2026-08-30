import re


try:
    from Froj_theories.English_Michela_Phonetic_Steno_for_Piano.vowel_categories import vowel_category
except ModuleNotFoundError:
    # Allow running as a script
    from vowel_categories import vowel_category


custom_alphabet = "SBKPTNFRLHYWIOAUE-gbsltnw*_"
valid_final_letter = r'[IOAUEgbsltnw]\*?$'


#_ to act as memory if you wanna add briefing techniques later"


"""
Regex logic here
"""
initial_slash = re.compile(r'^/$')
slash = re.compile(r'/$')
slash_ = re.compile(r'/_?$')


first_bank = re.compile(r'[SBKPTNFRLHYW]$')
slash_or_first_bank = re.compile(r'[/SBKPTNFRLHYW]$')


slash_or_first_bank_no_S = re.compile(r'/[BKPTNFRLHYW]*_?$')
slash_or_first_bank_no_B = re.compile(r'/[SKPTNFRLHYW]*_?$')

slash_or_first_bank_no_BT = re.compile(r'/[SKPNFRLHYW]*_?$')
slash_or_first_bank_no_K = re.compile(r'/[SBPTNFRLHYW]*_?$')
slash_or_first_bank_no_P = re.compile(r'/[SBKTNFRLHYW]*_?$')


slash_or_first_bank_no_R = re.compile(r'/[SBKPTNFLHYW]*_?$')



vowel_bank = re.compile(r'[IOAUE]$')


final_bank = re.compile(r'[gbsltnw]$')

vowel_or_final_bank = re.compile(r'[IOAUEgbsltnw]$')


vowel_or_final_bank_no_bt = re.compile(r'[IOAUE\-][gslnw]*$')
vowel_or_final_bank_no_n = re.compile(r'[IOAUE\-][gbsltw]*$')
























"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {

    "_": [
        {"chord": "",
         "description": "drop silent vowel",
         "spelling": "[aiu]",  # merciful, somethingcal
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_bank,
         "theory": ""},

        {"chord": "",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": first_bank,
         "theory": ""},
    ],


    "/": [
        {"chord": "/",
         "description": "",
         "spelling": "",
         "pronunciation": "( (prefix|root) )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank,
         "theory": ""},
    ],

    "/-": [
        {"chord": "/-",
         "description": "",
         "spelling": "",
         "pronunciation": "( (prefix|root|suffix) )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": final_bank,
         "theory": ""},
    ],


    "/_": [
        {"chord": "/",
         "description": "/ silent a",
         "spelling": "a",
         "pronunciation": "",  # I made this empty instead of ( suffix )?
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": final_bank,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": final_bank,  # changed because meteorological was too big
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": final_bank,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix, but I'm not sure about this one",
         "spelling": "[aeiouy]+",  # merciful
         "pronunciation": vowel_category["short"] + " suffix ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": final_bank,
         "theory": ""},

        {"chord": "/",
         "description": "long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]})', #{vowel_category["EU"]}
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": final_bank,
         "theory": ""}],



    "S": [
        {"chord": "S",
         "description": "s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_S,
         "theory": ""},

        {"chord": "S",
         "description": "s (maybe silent)",
         "spelling": "ss?",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_S,
         "theory": ""},

        {"chord": "S",
         "description": "sw silent w",
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": slash_or_first_bank_no_S,
         "theory": ""},

        {"chord": "S",
         "description": "ps silent p",
         # conflicts with "uppsala"
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_S,
         "theory": ""},

        {"chord": "S",
         "description": "c pronounced s or sy",  # the ce in pharmaceutical
         "spelling": "cc?e?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_S,
         "theory": ""},

        {"chord": "S",
         "description": "s pronounced z",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_S,
         "theory": ""},

        {"chord": "S",
         "description": "c pronounced s",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_S,
         "theory": ""},
    ],


    "BT": [
        {"chord": "BT",
         "description": "d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_BT,
         "theory": ""},

        {"chord": "BT",
         "description": "d but Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_BT,
         "theory": ""}
    ],


    "P": [
        {"chord": "P",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_P,
         "theory": ""},

        {"chord": "P",
         "description": "p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_P,
         "theory": ""}
    ],



    "R": [
        {"chord": "R",
         "description": "r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_R,
         "theory": ""},

        {"chord": "R",
         "description": "r maybe silent",
         "spelling": "rr?",
         "pronunciation": " \[r\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_R,
         "theory": ""},

        {"chord": "R",
         "description": "rh silent h",
         "spelling": "rr?h",
         "pronunciation": " r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank_no_R,
         "theory": ""}
    ],





    "O": [
        {"chord": "O",
         "description": "o",
         "spelling": "o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank,
         "theory": ""},

        {"chord": "O",
         "description": "short vowel spelt ow", # Knowledge
         "spelling": "ow",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank,
         "theory": ""},


        {"chord": "AU",
         "description": "AU vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #corp story
         "what must come before": slash_or_first_bank,
         "theory": ""},

        {"chord": "O",
         "description": "AOU vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 1, #move,
         "what must come before": slash_or_first_bank,
         "theory": ""},

        {"chord": "O",
         "description": "O vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["O"],
         "ambiguity": 1,
         "orthoscore": -1, #yacht
         "what must come before": slash_or_first_bank,
         "theory": ""},
    ],




    "A": [
        {"chord": "A",
         "description": "short a",
         "spelling": "a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank,
         "theory": ""},

        {"chord": "A",
         "description": "short a", #villain... but not against?
         "spelling": "ai",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank,
         "theory": ""},


        {"chord": "A",
         "description": "EU vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": slash_or_first_bank,
         "theory": ""},
    ],



    "E": [
        {"chord": "E",
         "description": "e",
         "spelling": "e",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank,
         "theory": ""}, 

        {"chord": "E",
         "description": "E vowel spelt ea",
         "spelling": "ea",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": slash_or_first_bank,
         "theory": ""},

        {"chord": "E",
         "description": "E vowel spelt ai",  # against
         "spelling": "ai",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": slash_or_first_bank,
         "theory": ""},

        {"chord": "E",
         "description": "EU vowel spelt e",  # delicious
         "spelling": "e",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": slash_or_first_bank,
         "theory": ""},

        {"chord": "E",
         "description": "E vowel", #friend
         "spelling": "ie",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_or_first_bank,
         "theory": ""},
    ],




    "bt": [
        {"chord": "-bt",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_bt,
         "theory": ""},

        {"chord": "-bt",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_bt,
         "theory": ""},

        {"chord": "-bt",
         "description": "suffix -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_bt,
         "theory": ""}
    ],


   "n": [
        {"chord": "-n",
         "description": "n",
         "spelling": "o?ne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_n,
         "theory": ""},

        {"chord": "-n",
         "description": "n", #gin
         "spelling": "o?nne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_n,
         "theory": ""},

        {"chord": "-n",
         "description": "en",
         "spelling": "enn?e?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_n,
         "theory": ""},

        {"chord": "-n",
         "description": "suffix -n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_n,
         "theory": "?"},

        {"chord": "-n",
         "description": "gn silent g",
         "spelling": "gne?",
         "pronunciation": " n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_final_bank_no_n,
         "theory": ""},
    ],


}





"""


    "Abl": [
        {"chord": "ABL",
         "description": "suffix -able",
         "spelling": "able?",
         "pronunciation": " suffix  @  b  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""}
    ],


    "Olg": [
        {"chord": "OLG",
         "description": "suffix -ology",
         "spelling": "olog[yi]",
         "pronunciation": "( suffix )? o  l  @  jh  iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""}
    ],


    "eupb": [
        {"chord": "EUPB",
         "description": "suffix -ine",
         "spelling": "ine",
         "pronunciation": " suffix  ai/i  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""}
    ],


        {"chord": "-PBS",
         "description": "suffix -ence",
         "spelling": "ence?",
         "pronunciation": " suffix  (@|e5)  s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": A_to_r,
         "theory": ""},
    ],



    ],
}
"""