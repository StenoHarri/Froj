import re


try:
    from Froj_theories.Mussel_Power.vowel_categories import vowel_category
except ModuleNotFoundError:
    # Allow running as a script
    from vowel_categories import vowel_category


custom_alphabet = "12345678lrLR-AOEU12345678lLrR_"
valid_final_letter = r'[\-AOEU]([12345678lLrR]+)?$' #Will need to come back to this for multi-strokes
does_theory_pay_attention_to_stress_markers = True



#_ to say "don't skip a series"


"""
Regex logic here
"""
"""
There will be groups of keysymbols that come up again and again,
so I'll define them once here
"""

# regex logic for what must come before
# hopefully compiling it all here makes it run faster since they'll be used

# A_to_z_or_nothing_at_all = re.compile(r'(.*[\-AOeufrpblgtsdz])?\*?$')
# NothingRegex = re.compile(r'')
# AtLeastOneCharacterRegex = re.compile(r'.+')

initial_slash = re.compile(r'^/$')
ends_in__ = re.compile(r'_$')



"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {

    "_": [
        {"chord": "",
         "description": "stress",
         "spelling": "",
         "pronunciation": " stressed ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "OE": [
        {"chord": "OE",
         "description": "OE vowel",
         "spelling": "o[eu]?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel spelt ow",
         "spelling": "owe?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel spelt au",
         "spelling": "au",  # baudelaire, aubergine beaux,
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": -1, #aubergine
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel",
         "spelling": "ot$",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel spelt oa",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "orthoscore": -1, #toad
         "what must come before": ends_in__,
         "theory": ""},
    ],

}

