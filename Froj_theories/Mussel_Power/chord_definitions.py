import re


try:
    from Froj_theories.Mussel_Power.vowel_categories import vowel_category
except ModuleNotFoundError:
    # Allow running as a script
    from vowel_categories import vowel_category


custom_alphabet = "12345678lrLR-AOEUabcdefghxXyY_"
valid_final_letter = r'[AOEUabcdefghxXyY]$' #Will need to come back to this for multi-strokes
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

ends_in_slash = re.compile(r'/$')
initial_slash_or_initial = re.compile(r'(^/|[12345678lLrR])$')
initial = re.compile(r'[12345678lLrR]$')
vowel_or_hyphen = re.compile(r'[AOEU\-]$')
final = re.compile(r'[abcdefghxXyY]$')
ends_in__ = re.compile(r'_$')
hyphen = re.compile(r'-$')
AU = re.compile(r'AU$')


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
         "what must come before": initial_slash_or_initial,
         "theory": ""},
    ],


    "/": [
        {"chord": "/",
         "description": "",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial,
         "theory": ""},

        {"chord": "/",
         "description": "drop silent vowel",
         "spelling": "[aiu]",  # merciful, somethingcal
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial,
         "theory": ""},

        {"chord": "/",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": initial,
         "theory": ""},

        {"chord": "/",
         "description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": initial,
         "theory": ""},
    ],


    "/-": [
        {"chord": "/",
         "description": "",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": final,
         "theory": ""},

        {"chord": "/",
         "description": "drop silent vowel",
         "spelling": "[aiu]",  # merciful, somethingcal
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": final,
         "theory": ""},

        {"chord": "/",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": final,
         "theory": ""},

        {"chord": "/",
         "description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": final,
         "theory": ""},
    ],


    "1": [
        {"chord": "1",
         "description": "r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # added up to H since THRU # personal opinion, but SR → s + r is ugly
         "theory": ""},

        {"chord": "1",
         "description": "r maybe silent",
         "spelling": "rr?",
         "pronunciation": " \[r\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # added up to H since THRU # personal opinion, but SR → s + r is ugly
         "theory": ""},

        {"chord": "1",
         "description": "rh silent h",
         "spelling": "rr?h",
         "pronunciation": " r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # added up to H since THRU
         # personal opinion, but SR → s + r is ugly
         "theory": ""}
    ],


    "1l": [
        {"chord": "1l",
         "description": "w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "1l",
         "description": "u pronounced w",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "1l",
         "description": "long u", #poplar / popular
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "Harri?"},

        {"chord": "1l",
         "description": "long u", #duet
         "spelling": "u",
         "pronunciation": "( suffix )? \[y\]  iu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "Harri?"},

        {"chord": "1l",
         "description": "w pronounced v",
         "spelling": "w",
         "pronunciation": " (v|v/w) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "1l",
         "description": "OE vowel",
         "spelling": "o",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "Harri"},

        {"chord": "1l",
         "description": "u",
         "spelling": "u",
         "pronunciation": " \(y uu/w\) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "1l",
         "description": "O",
         "spelling": "o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "Harri"},
    ],


    "1r": [
        {"chord": "1r",
         "description": "v",
         "spelling": "vv?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "1R": [
        {"chord": "1R", # connection, context
         "description": "com",
         "spelling": "comm?",
         "pronunciation": " k  (@|o|o4)  m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "1R", # connection, context
         "description": "com optional std",
         "spelling": "com[std]?",
         "pronunciation": " k  (@|o|o4)  m ( [std] )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "2": [
        {"chord": "2", #why does `KPHAOUPB` → `commune` not work????
         "description": "k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2",
         "description": "c pronounced k",
         "spelling": "cc?",  # acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2",
         "description": "k, maybe ky",
         "spelling": "cc?",  # barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2",
         "description": "ch pronounced k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2",
         "description": "ck",
         "spelling": "ck(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        # {"chord": "4", # connection, context
        #  "description": "con optional std",
        #  "spelling": "con[std]?",
        #  "pronunciation": " k  (@|o|o4)  n ( [st] )?",
        #  "ambiguity": 10,
        #  "orthoscore": 0,
        #  "what must come before": ends_in_slash,
        #  "theory": "Harri"}
    ],


    "2l": [
        {"chord": "2l",
         "description": "kr",
         "spelling": "k(k|h)?rr?",
         "pronunciation": " k  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2l",
         "description": "cr",
         "spelling": "cc?rr?",  # acclimatise
         "pronunciation": " k  r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2l",
         "description": "chr",
         "spelling": "chrr?",
         "pronunciation": " k  r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "spelling"},
    ],


    "2L": [
        {"chord": "2L",
         "description": "qu",  # acquaint
         "spelling": "c?qu",
         # combined with the `U` → `ui` in build, this is a nasty combination but I don't know a fix for it, I guess there's always two ways to read KWEU → qui
         "pronunciation": " k ( w )?",  # briquette doesn't have a w
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "2r": [
        {"chord": "2r", # connection, context
         "description": "con",
         "spelling": "conn?",
         "pronunciation": " k  (@|o|o4)  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2r", # connection, context
         "description": "con optional std",
         "spelling": "con[std]?",
         "pronunciation": " k  (@|o|o4)  n ( [std] )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "2r",
         "description": "im/em",
         "spelling": "[ie]m",
         "pronunciation": " (i|e|e0)  m ( root )?",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "2L": [
        {"chord": "2L",
         "description": "cl",
         "spelling": "cc?ll?",  # acclimatise
         "pronunciation": " k  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "3": [
        {"chord": "3",
         "description": "b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "3l": [
        {"chord": "3l",
         "description": "m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "3L": [
        {"chord": "3L",
         "description": "br",
         "spelling": "bb?rr?",
         "pronunciation": " b  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "3r": [
        {"chord": "3r",
         "description": "h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "3r",
         "description": "silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # upToW_no_P  removed because of "school" I think
         "theory": "?"},

        {"chord": "3r",
         "description": "silent h depending on accent",
         "spelling": "h",
         "pronunciation": " \[h1\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "?"},
    ],


    "3R": [
        {"chord": "3R",
         "description": "bl",
         "spelling": "bb?ll?",
         "pronunciation": " b  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "4": [
        {"chord": "4",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4",
         "description": "p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "4l": [
        {"chord": "4l",
         "description": "y",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4l",
         "description": "y",
         "spelling": "y",
         "pronunciation": " y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4l",
         "description": "y, but for some people it's silent???",
         "spelling": "y",
         "pronunciation": " \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4l",
         "description": "i",
         "spelling": "i",
         "pronunciation": "( suffix )? (ii|ii2|y|iy) ",  # aerospacial ← who wrote that???, fancier has a iy
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4l",
         "description": "y",
         "spelling": "y",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4l",
         "description": "long e?",  # meteor the second e
         "spelling": "e",
         "pronunciation": " ii2 ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4l",
         "description": "unspelt y",
         "spelling": "",
         "pronunciation": " y ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "4L": [
        {"chord": "4L",
         "description": "pr",
         "spelling": "pp?rr?",
         "pronunciation": " p  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "4r": [
        {"chord": "4r",
         "description": "pl",
         "spelling": "pp?ll?",
         "pronunciation": " p  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "4R": [
        {"chord": "4R",
         "description": "z",
         "spelling": "zz?",
         "pronunciation": "( z | t  s )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "4R",
         "description": "ex",
         "spelling": "[ei]xx?",
         "pronunciation": f"{vowel_category["short"]}( k  s | g  z )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "5": [
        {"chord": "5",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "5l": [
        {"chord": "5l",
         "description": "g",
         "spelling": "gg?h?", #ghost can be TKPWOEFT or TKPWHOEFT
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "5L": [
        {"chord": "5L",
         "description": "gr",
         "spelling": "gg?rr?",
         "pronunciation": " g  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5L",
         "description": "in",
         "spelling": "inn?e?",
         "pronunciation": f'{vowel_category["short"]} n ',
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5L",
         "description": "in",
         "spelling": "ynn?e?",
         "pronunciation": f'{vowel_category["short"]} n ',
         "ambiguity": 1,  # honestly this might be 0
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

    ],


    "5r": [
        {"chord": "5r",
         "description": "j",
         "spelling": "j",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5r",
         "description": "j sound",
         "spelling": "(g|dj|di|dgg?e?)", #soldier
         "pronunciation": " jh ",
         "ambiguity": 1, #jest>gest
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5r",
         "description": "g pronounced zh",
         "spelling": "(d?jj?e?|d?gg?e?)", #aubergine
         "pronunciation": " zh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5r",
         "description": "j pronounced zh", #bonjour
         "spelling": "(d?jj?e?|d?gg?e?)",
         "pronunciation": " zh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "5R": [
        {"chord": "5R",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5R",
         "description": "ci pronounced sh",
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "Harri"},

        {"chord": "5R",
         "description": "s pronounced sh",
         "spelling": "ss?",  # pressure
         "pronunciation": "( sh | s  y )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5R",
         "description": "s pronounced sh in Harri's accent (Essex?)",
         "spelling": "ss?",  # assume
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "5R",
         "description": "sh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #sc like fascist
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},


        {"chord": "SH",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "6": [
        {"chord": "6",
         "description": "d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "6",
         "description": "d but Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "6l": [
        {"chord": "6l",
         "description": "f",
         "spelling": "ff?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # sphere
         "theory": ""},

        {"chord": "TP",
         "description": "ph pronounced f",
         "spelling": "p?ph", #sapphire
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # sphere
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "a",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "a(a|ye?|i)",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1, # wave > waive
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a (you British?)",
         "spelling": "e",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ett?e?",
         "pronunciation": vowel_category["AEU"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ey",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ei", #inveigh, weigh
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": -1,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "AEU",
         "description": "suffix long a",
         "spelling": "a",
         "pronunciation": f' suffix {vowel_category["AEU"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "6L": [
        {"chord": "6L",
         "description": "fl",
         "spelling": "ff?ll?",
         "pronunciation": " f  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # sphere
         "theory": ""},

        {"chord": "6L",
         "description": "phl",
         "spelling": "p?phl", #sapphire
         "pronunciation": " f  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # sphere
         "theory": ""}
    ],


    "6r": [
        {"chord": "6r",
         "description": "dis/des sound", # dis/disc/dist/des/desc/dec
         "spelling": "d[ie][sc]+t?",
         "pronunciation": " d  (i|ii|e)  (s|z) ( root )?",
         "ambiguity": 1, # descend/distend
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "?"},

        {"chord": "6r",
         "description": "dis/des + consonant", # dis/disc/dist/des/desc/dec
         "spelling": "d[ie][sc]+[td]?",
         "pronunciation": " d  (i|ii|e)  (s|z) ( root )?( (k|t|d) )?",
         "ambiguity": 1, # descend/distend
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "?"},

        {"chord": "TH",
         "description": "th",
         "spelling": "th",
         "pronunciation": " (th|dh|dh/th) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "6R": [
        {"chord": "6R",
         "description": "fr",
         "spelling": "ff?rr?",
         "pronunciation": " f  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # sphere
         "theory": ""},

        {"chord": "6R",
         "description": "phr",
         "spelling": "p?phr", #sapphire
         "pronunciation": " f  r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,  # sphere
         "theory": ""}
    ],


    "7": [
        {"chord": "7",
         "description": "s",
         "spelling": "ss?",
         "pronunciation": " s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7",
         "description": "s (maybe silent)",
         "spelling": "ss?",
         "pronunciation": " z/s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7",
         "description": "sw silent w",  # answer 
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7",
         "description": "ps silent p",
         # conflicts with "uppsala" but psychotic has `HOT` → `hot` because of silent h so I don't mind
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7",
         "description": "c pronounced s or sy",  # the ce in pharmaceutical
         "spelling": "cc?e?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7",
         "description": "consumer",  # consumer
         "spelling": "s",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7",
         "description": "s pronounced z",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7",
         "description": "c pronounced s",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "7l": [
        {"chord": "7l",
         "description": "n",
         "spelling": "nn?",
         "pronunciation": " n ( \[y\] )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7l",
         "description": "gn silent g",
         "spelling": "g?n",
         "pronunciation": " n ( y )?",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "7l",
         "description": "i or e",
         "spelling": "[ie]",
         "pronunciation": " (i|e|e0) ( root )?",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "7L": [
        {"chord": "7L",
         "description": "sp",
         "spelling": "ss?pp?",
         "pronunciation": " s  p ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "7r": [
        {"chord": "7r",
         "description": "st",
         "spelling": "ss?tt?",
         "pronunciation": " s  t ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "7R": [
        {"chord": "7R",
         "description": "str",
         "spelling": "ss?tt?rr?",
         "pronunciation": " s  t  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "8": [
        {"chord": "8",
         "description": "t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "8",
         "description": "t but Harri says ch",
         "spelling": "tt?",  # attune
         "pronunciation": " t  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],

    "8l": [
        {"chord": "8l",
         "description": "short a",
         "spelling": "a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "spelling"},

        {"chord": "8l",
         "description": "short vowel", #villain... but not against?
         "spelling": "ai",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "spelling"},

        {"chord": "8l",
         "description": "short i",
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": ends_in_slash,
         "theory": "spelling"},
    ],


    "8L": [
        {"chord": "8l",
         "description": "an",
         "spelling": "ann?e?",
         "pronunciation": f'{vowel_category["short"]} n ',
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "8l",
         "description": "an",
         "spelling": "ainn?e?", #villain... but not against?
         "pronunciation": f'{vowel_category["short"]} n ',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "8l",
         "description": "an",
         "spelling": "inn?e?",
         "pronunciation": f'{vowel_category["EU"]} n ',
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": ends_in__,
         "theory": "spelling"},
    ],


    "8r": [
        {"chord": "8r",
         "description": "tr",
         "spelling": "tt?rr?",
         "pronunciation": " t  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},
    ],


    "8R": [
        {"chord": "8R",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "8R",
         "description": "cc pronounced ch",
         "spelling": "cc",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "8R",
         "description": "t pronounced ch",
         "spelling": "t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": "Plover?"},

        {"chord": "8R",
         "description": "ti pronounced ch", #congestion
         "spelling": "t",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": ends_in_slash,
         "theory": ""},

        {"chord": "8R",
         "description": "shr",
         "spelling": "shr",
         "pronunciation": " sh  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in_slash,
         "theory": ""}
    ],


    "A": [
        {"chord": "A",
         "description": "short vowel",
         "spelling": "a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "A",
         "description": "short vowel", #villain... but not against?
         "spelling": "ai",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "A",
         "description": "short i",
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": ends_in__,
         "theory": "spelling"},
    ],


    "AO": [
        {"chord": "AO",
         "description": "caught vowel",
         "spelling": "oa",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #coarse
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "AO",
         "description": "long o",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 1, #toad
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "AO",
         "description": "short vowel",
         "spelling": "oo",
         "pronunciation": vowel_category["short"] ,  # u is took I think?
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "AO",
         "description": "long u",
         "spelling": "oo",
         "pronunciation": vowel_category["AOU"],  # uu is noon
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "spelling"}
    ],


    "AOE": [
        {"chord": "AOE",
         "description": "long e",
         "spelling": "ee",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOE",
         "description": "long e",
         "spelling": "ie",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "phonetic"},

        {"chord": "AOE",
         "description": "long e",
         "spelling": "i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": -1, #Mozambique, Shiba
         "what must come before": ends_in__,
         "theory": "phonetic"},

        {"chord": "AOE",
         "description": "long e",  # acne, aires
         "spelling": "e",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #genotype
         "what must come before": ends_in__,
         "theory": "phonetic"},

        {"chord": "AOE",
         "description": "long e",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #read
         "what must come before": ends_in__,
         "theory": "phonetic"},

        {"chord": "AOE",
         "description": "long e but maybe it's two syllables?",
         "spelling": "ea",
         "pronunciation": " i@ ",
         "ambiguity": 1,
         "orthoscore": -1, #real
         "what must come before": ends_in__,
         "theory": "phonetic"},

        {"chord": "AOE",
         "description": "long e",
         "spelling": "ey",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #key
         "what must come before": ends_in__,
         "theory": "phonetic"},

        {"chord": "AOE",
         "description": "long e",
         "spelling": "oe",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #diarhoea
         "what must come before": ends_in__,
         "theory": "phonetic"},

        {"chord": "AOE",
         "description": "long e",
         "spelling": "eo", #theory
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "phonetic"},
    ],


    "AOEU": [
        {"chord": "AOEU",
         "description": "long i",
         "spelling": "ie?",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOEU",
         "description": "long i",
         "spelling": "ei",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOEU",
         "description": "long i",
         "spelling": "y",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "StenEd?"},

        {"chord": "AOEU",
         "description": "long i",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOEU",
         "description": "long i followed by a short e",
         "spelling": "ie",
         "pronunciation": vowel_category["AOEU"] + " @ ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOEU",
         "description": "long i as a suffix",
         "spelling": "i",
         "pronunciation": f' suffix {vowel_category["AOEU"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "AOU": [
        {"chord": "AOU",
         "description": "long u",
         "spelling": "e?ue?", # deuteronomy
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOU",
         "description": "long u",
         "spelling": "ou", 
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": -1, #soup
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOU",
         "description": "long u",
         "spelling": "eau",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOU",
         "description": "long u",
         "spelling": "ui",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOU",
         "description": "long u",
         "spelling": "ew",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,  # nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOU",
         "description": "long u",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": -1, #move
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOU", 
         "description": "long u",
         "spelling": "uu", #vacuum
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AOU", 
         "description": "long u + i",
         "spelling": "ui", #druid
         "pronunciation": f'{vowel_category["AOU"]} i ',
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "AE": [
        {"chord": "AE",
         "description": "long e",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"], #it was just ii before
         "ambiguity": 1,
         "orthoscore": 1, #read
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "AE",
         "description": "short e",
         "spelling": "ea",
         "pronunciation": " e ", # earl?
         "ambiguity": 2, #red
         "orthoscore": 1, #read
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "AE",
         "description": "long a",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 1,
         "what must come before": ends_in__,
         "theory": "spelling"},

        {"chord": "AE",
         "description": "AOE vowel spelt ae",
         "spelling": "ae",
         "pronunciation": vowel_category["AOE"], # eir?
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "Lapwing?"},
    ],


    "AEU": [
        {"chord": "AEU",
         "description": "long a",
         "spelling": "a",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "a(a|ye?|i)",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1, # wave > waive
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a (you British?)",
         "spelling": "e",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ett?e?",
         "pronunciation": vowel_category["AEU"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ey",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ei", #inveigh, weigh
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AEU",
         "description": "long a",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": -1,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AEU",
         "description": "suffix long a",
         "spelling": "a",
         "pronunciation": f' suffix {vowel_category["AEU"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "AU": [
        {"chord": "AU",
         "description": "caught vowel",
         "spelling": "a[auh]?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AU",
         "description": "caught vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": -1, #thought
         "what must come before": ends_in__,
         "theory": ""},

        #{"chord": "AU",
        # "description": "AU vowel spelt o",
        # "spelling": "o",
        # "pronunciation": vowel_category["AU"],
        # "ambiguity": 3,
        # "orthoscore": -1, #corp
        # "what must come before": ends_in__,
        # "theory": ""},

        {"chord": "AU",
         "description": "au",
         "spelling": "short vowel",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AU",
         "description": "ow vowel",
         "spelling": "au",
         "pronunciation": vowel_category["OU"], #Macau
         "ambiguity": 2,
         "orthoscore": 1,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "AU",
         "description": "caught vowel",
         "spelling": "awe?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],

    
    "O": [
        {"chord": "O",
         "description": "short vowel",
         "spelling": "o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "O",
         "description": "short vowel", # Knowledge
         "spelling": "ow",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},


        {"chord": "O",
         "description": "caught vowel",
         "spelling": "o",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #corp story
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "O",
         "description": "long u",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 1, #move,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "O",
         "description": "short o",
         "spelling": "a",
         "pronunciation": vowel_category["O"],
         "ambiguity": 1,
         "orthoscore": -1, #yacht
         "what must come before": ends_in__,
         "theory": "spelling"},
    ],


    "OE": [
        {"chord": "OE",
         "description": "long o",
         "spelling": "o[eu]?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "long o",
         "spelling": "owe?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "long o",
         "spelling": "au",  # baudelaire, aubergine beaux,
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": -1, #aubergine
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "long o",
         "spelling": "ot$",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OE",
         "description": "long o",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "orthoscore": -1, #toad
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "OEU": [
        {"chord": "OEU",
         "description": "oy vowel",
         "spelling": "oi",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OEU",
         "description": "oy vowel",
         "spelling": "oye?",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 1,  # feel free to change this prioritisation
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""}
    ],


    "OU": [
        {"chord": "OU",
         "description": "caught vowel", #thought
         "spelling": "ou",
         "pronunciation": vowel_category["AU"], # bolder/boulder  thought   " starting_root  th  oo  t  suffix  f  [u]  l ",
         "ambiguity": 0,
         "orthoscore": 1, #thought
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OU",
         "description": "ow vowel",
         "spelling": "ow",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "OU",
         "description": "long o",
         "spelling": "ou",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "Harri"},

        {"chord": "OU",
         "description": "short vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,  # colour
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "Harri"},

        {"chord": "OU",
         "description": "ow vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "E": [
        {"chord": "E",
         "description": "short vowel",
         "spelling": "e",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},  # not WSI because actresses that e is a @

        {"chord": "E",
         "description": "short e",
         "spelling": "ea",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "E",
         "description": "short e",  # against
         "spelling": "ai",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "E",
         "description": "short i",  # delicious
         "spelling": "e",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "E",
         "description": "short e", #friend
         "spelling": "ie",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "EU": [
        {"chord": "EU",
         "description": "y pronounced i diphthong",
         "spelling": "e?y",
         "pronunciation": " iy ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "StenEd?"},

        {"chord": "EU",
         "description": "ee pronounced i diphthong",
         "spelling": "ee",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "ii pronounced i diphthong",
         "spelling": "ii",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "ie pronounced i diphthong",
         "spelling": "ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "short i",
         "spelling": "i",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "short vowel",
         "spelling": "y",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,  # honestly this might be 0
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "i diphthong",
         "spelling": "i",
         "pronunciation": " iy ",
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "e pronounced i diphthong",  # acne, aires
         "spelling": "e",
         "pronunciation": " iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "Harri?"},

        {"chord": "EU",
         "description": "ea pronounced i diphthong",
         "spelling": "ea",
         "pronunciation": " iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "Harri?"},

        {"chord": "EU",
         "description": "short i", #busy
         "spelling": "u",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #busy
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "short i", #busy
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #garbage
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "EU",
         "description": "short i", #build
         "spelling": "ui?",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        #{"chord": "EU", commented out because of antidisestablishmentarianism, electrocardiography
        # "description": "EU vowel spelt e",  # delicious
        # "spelling": "e",
        # "pronunciation": vowel_category["EU"],
        # "ambiguity": 0,
        # "orthoscore": -1,
        # "what must come before": ends_in__,
        # "theory": ""},

        {"chord": "EU",
         "description": "long e",
         "spelling": "i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": 1, #Mozambique, Shiba
         "what must come before": ends_in__,
         "theory": ""},

         {"chord": "EU",
         "description": "suffix -y", #assembly
         "spelling": "(y|ie?)",
         "pronunciation": " suffix  iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "U": [
        {"chord": "U",
         "description": "short u",
         "spelling": "u",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},

        {"chord": "U",
         "description": "short u",
         "spelling": "ou",
         "pronunciation": vowel_category["U"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": "Harri"},

        {"chord": "U",
         "description": "short vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": ends_in__,
         "theory": ""},
    ],


    "a": [
        {"chord": "-1",
         "description": "solo s",
         "spelling": "s",
         "pronunciation": " (s|z) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-1",
         "description": "solo s",
         "spelling": "s",
         "pronunciation": " s/z ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-1",
         "description": "suffix -s",
         "spelling": "s",
         "pronunciation": "( (suffix) ) (s|z|z/s) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-1",
         "description": "plural",  # actresses
         "spelling": "es",
         "pronunciation": " suffix  i7  (s|z) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-1",
         "description": "whatever this is",
         "spelling": "is",
         "pronunciation": " i  s ", #halitosis
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri"},

        {"chord": "-1",
         "description": "s silent t",
         "spelling": "ss?te?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # no idea, this just feels right
         "theory": ""},

        {"chord": "-1",
         "description": "s silent w",  # answer
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "ax": [
        {"chord": "-1l",
         "description": "zz or ze",
         "spelling": "zz?e?",
         "pronunciation": "( z | t  s )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-1l",
         "description": "suffix -ize",
         "spelling": "ize?",
         "pronunciation": " suffix  ae  z ",
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "aX": [
        {"chord": "-1L",
         "description": "st",
         "spelling": "ss?tt?",
         "pronunciation": " (s|z)  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},
    ],


    "ay": [
        {"chord": "-1r",
         "description": "se",
         "spelling": "se",  # actresses?"
         "pronunciation": " (s|z) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},

        {"chord": "-1r",
         "description": "ss",
         "spelling": "ss",  # actresses?"
         "pronunciation": " (s|z) ",
         "ambiguity": 1,
         "orthoscore": 0,
         # cyclops
         "what must come before": vowel_or_hyphen,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},

        {"chord": "-1r",
         "description": "c pronounced s",
         "spelling": "s?ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # maybe I'm traumatised from ABGS/HRERPL/TER → accelerometer
         "theory": ""},

        {"chord": "-1r",
         "description": "se maybe voiced",
         "spelling": "ss?e",
         "pronunciation": " z/s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # no _ I think?
         "theory": ""},

        {"chord": "-1r",
         "description": "s pronounced z",
         "spelling": "ss?e?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # no _ I think?
         "theory": ""},
    ],


    "aY": [
        {"chord": "-8R",
         "description": "rse",
         "spelling": "rr?ss?e?",
         "pronunciation": " r  (s|z|s/z) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-8R",
         "description": "rce",
         "spelling": "rr?cc?e?",
         "pronunciation": " r  (s|z|s/z) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "b": [
        {"chord": "-2",
         "description": "ng",
         "spelling": "ng?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2",
         "description": "ngue", #tongue
         "spelling": "ngue",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2",
         "description": "ng with g",
         "spelling": "ng",
         "pronunciation": " ng ( \[?g\]? )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        # {"chord": "-2",
        #  "description": "'nge' in 'singe'",
        #  # funny example cause of course `SEUPBG` → `sing`, but `ORPBG` → `orange`
        #  "spelling": "nge?",
        #  "pronunciation": " n  jh ",
        #  "ambiguity": 1,
        #  "orthoscore": 0,
        #  "what must come before": vowel_or_hyphen,
        #  "theory": ""},

        {"chord": "-2",
         "description": "ng sound then g sound",
         "spelling": "ng?",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2",
         "description": "suffix -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # ← look at that lack of _ at the end
         # okay the issue here is that maybe there's no issue
         "theory": ""},
    ],


    "bx": [
        {"chord": "-2l",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2l",
         "description": "ci pronounced sh (Harri's accent)",  # aerospacial
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2l",
         "description": "sh sound",
         "spelling": "((s|t|x)i|c[ei]|s?che?|sc|ss)",
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2l",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        # conscious abstentious anxious?
        {"chord": "-2l",
         "description": "nsh sound",
         "spelling": "n(sc|t|x)i",  # x for anxious
         "pronunciation": " n  sh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri"},

        {"chord": "-2l",
         "description": "ngksh sound",
         "spelling": "n(sc|t|x)i",  # xi for anxious,
         "pronunciation": " ng ( k )? sh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri"},
    ],


    "bX": [
        {"chord": "-2L",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "?"},

        {"chord": "-2L",
         "description": "tch",
         "spelling": "tch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2L",
         "description": "ch spelt t",
         "spelling": "t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""}
    ],


    "by": [
        {"chord": "-2r",
         "description": "nk",
         "spelling": "nk",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2r",
         "description": "nc",
         "spelling": "nc",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2r",
         "description": "nic",
         "spelling": "nicc?",
         "pronunciation": " n  i  k ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-2r",
         "description": "short a",
         "spelling": "a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "spelling"},
    ],


    "bY": [
        {"chord": "-2R",
         "description": "b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},



        {"chord": "1l",
         "description": "w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "1l",
         "description": "u pronounced w",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "1l",
         "description": "long u", #poplar / popular
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "1l",
         "description": "long u", #duet
         "spelling": "u",
         "pronunciation": "( suffix )? \[y\]  iu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri?"},

        {"chord": "1l",
         "description": "w pronounced v",
         "spelling": "w",
         "pronunciation": " (v|v/w) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "1l",
         "description": "OE vowel",
         "spelling": "o",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri"},

        {"chord": "1l",
         "description": "u",
         "spelling": "u",
         "pronunciation": " \(y uu/w\) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "1l",
         "description": "O",
         "spelling": "o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri"},
    ],


    "c": [
        {"chord": "-3",
         "description": "y pronounced i diphthong",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3",
         "description": "y pronounced i diphthong",
         "spelling": "ie?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3",
         "description": "y pronounced i",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "cx": [
        {"chord": "-3l",
         "description": "g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3l",
         "description": "silent gh",
         "spelling": "gh",
         "pronunciation": "",
         "ambiguity": -1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri?"},

        {"chord": "-3l",
         "description": "ys pronounced i diphthong",
         "spelling": "ys",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ( (suffix) )? (s|z|z/s) ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3l",
         "description": "ys pronounced i diphthong",
         "spelling": "ie?s",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ( (suffix) )? (s|z|z/s) ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3l",
         "description": "ys pronounced i",
         "spelling": "ys",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ( (suffix) )? (s|z|z/s) ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "cX": [
        {"chord": "-3L",
         "description": "j",
         "spelling": "d?je?",
         "pronunciation": " jh ",
         "ambiguity": 1, #Why 1? not 0?
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3L",
         "description": "g pronounced j",
         "spelling": "d?gg?e?",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3L",
         "description": "zh sound",
         "spelling": "(j|dj|d?gg?)e?",
         "pronunciation": " zh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""}
    ],  # arbitrage


    "cy": [
        {"chord": "-3r",
         "description": "k",
         "spelling": "k(k|e)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3r",
         "description": "ck",
         "spelling": "cke?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3r",
         "description": "ch pronounced k",
         "spelling": "che?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3r",
         "description": "ch pronounced x",
         "spelling": "che?",
         "pronunciation": " x ",
         "ambiguity": 2, #lock/loch
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3r",
         "description": "lk silent l (immediately after a vowel)",
         "spelling": "lk",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3r",
         "description": "c pronounced k",  # do I make *BG? pick pic? $$$$
         "spelling": "c(c|e)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3r",
         "description": "qu",  # do I make *BG? pick pic? $$$$$$$?
         "spelling": "que?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "cY": [
        {"chord": "-3R",
         "description": "ble",
         "spelling": "bb?le?",
         "pronunciation": " b  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3R",
         "description": "ble pronounced bil",
         "spelling": "ble?",
         "pronunciation": " b  i  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3R",
         "description": "ction",
         "spelling": "ction",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-3R",
         "description": "cation",
         "spelling": "cation",
         "pronunciation": " k  ee  sh  suffix  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""}
    ],


    "d": [
        {"chord": "-4",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-4",
         "description": "le",
         "spelling": "ll?e",
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-4",
         "description": "el",
         "spelling": "ell?e?",#I added the final ? cause it looked wrong without it?
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-4",
         "description": "al",
         "spelling": "all?e?",
         "pronunciation": " @  l ",  # silent a is already a thing
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-4",
         "description": "suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-4",
         "description": "suffix -l",  # antibacterial
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

         #{"chord": "-L",
         #"description": "silent -l after AU",  # antibacterial
         #"spelling": "l", #PWAUL/-L → ball???
         #"pronunciation": "",
         #"ambiguity": 1,
         #"orthoscore": 0,
         #"what must come before": A_to_u,
         #"theory": ""},
    ],


    "dx": [
        {"chord": "-2l",
         "description": "ll?y",
         "spelling": "l(y|ie?)",
         "pronunciation": "( suffix )? l  iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""}
    ],


    "dX": [
        {"chord": "-4L",
         "description": "l + plural",
         "spelling": "ll?e?s",
         "pronunciation": " l  suffix  (s|z) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-4L",
         "description": "rch (conflicts with -nch)",
         "spelling": "rr?che?",
         "pronunciation": " r  ch ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""}
    ],


    "dy": [
        {"chord": "-4r",
         "description": "ld",
         "spelling": "ll?e?dd?",
         "pronunciation": " l  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-4r",
         "description": "ld",
         "spelling": "ll?e?dd?",
         "pronunciation": " l ( suffix ) d ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-2r",
         "description": "as",
         "spelling": "ass?",
         "pronunciation": f'{vowel_category["short"]}( (suffix) )? (s|z|z/s) ',
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "spelling"},
    ],


    "dY": [
        {"chord": "-4R",
         "description": "lt",
         "spelling": "ll?ett?",
         "pronunciation": " l  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-4R",
         "description": "suffix -ment",
         "spelling": "ment",
         "pronunciation": "( suffix )? m  e5  n  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-4R",
         "description": "t then suffix -ment",
         "spelling": "tment",
         "pronunciation": " t  suffix  m  e5  n  t ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""}
    ],


    "e": [
        {"chord": "-5",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-5",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-5",
         "description": "suffix -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""}
    ],


    "ex": [
        {"chord": "-5l",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0, #group > groupe
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # ".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "theory": ""},

        {"chord": "-5l",
         "description": "p",
         "spelling": "pp?e",
         "pronunciation": " p ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # ".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "theory": ""}
    ],


    "eX": [
        {"chord": "-5L",
         "description": "rm",
         "spelling": "rr?mm?e?",
         "pronunciation": " r  m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "ey": [
        {"chord": "-5r",
         "description": "m",
         "spelling": "mm?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-5r",
         "description": "mb silent b",
         "spelling": "mb",
         "pronunciation": " m ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-5r",
         "description": "mp silent p",
         "spelling": "mp",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-5r",
         "description": "mn silent n",
         "spelling": "mn",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-5r",
         "description": "lm silent l (has to follow AU)",
         "spelling": "lm",
         "pronunciation": "( \[l1\] )? m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": AU, #balm
         "theory": ""},

        {"chord": "-5r",
         "description": "uhm sound",
         "spelling": "m(b|m)?e?",
         "pronunciation": " @  m ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "eY": [
        {"chord": "-5R",
         "description": "mp",
         "spelling": "mm?e?pp?",
         "pronunciation": " m  p ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "f": [
        {"chord": "-6",
         "description": "n",
         "spelling": "nn?e?",
         "pronunciation": " n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "fx": [
        {"chord": "-6l",
         "description": "nd",
         "spelling": "nn?e?d",
         "pronunciation": " n  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-6l",
         "description": "nd",
         "spelling": "nn?e?d",
         "pronunciation": " n  suffix  d ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "fX": [
        {"chord": "-6L",
         "description": "ns",
         "spelling": "nn?e?ss?e?",
         "pronunciation": " n  s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-6L",
         "description": "ns",
         "spelling": "nn?e?cc?e?",
         "pronunciation": " n  s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-6L",
         "description": "suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  e5  s ", #aloofness
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-6L",
         "description": "mb",
         "spelling": "mm?bb?",
         "pronunciation": " m  b ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-6L",
         "description": "mb silent b",
         "spelling": "mb",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "spelling"},
    ],


    "fy": [
        {"chord": "-6r",
         "description": "nt",
         "spelling": "nn?e?tt?",
         "pronunciation": " n  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "fY": [
        {"chord": "-6R",
         "description": "n + plural",
         "spelling": "nn?e?s",
         "pronunciation": " n  suffix  (s|z) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # surely this should then work for "level"??
         "theory": ""},
    ],


    "g": [
        {"chord": "-7",
         "description": "t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7",
         "description": "final dt pronounced t",
         "spelling": "dt$",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri"},

        {"chord": "-7",
         "description": "t pronounced sh",
         "spelling": "tt?e?",
         "pronunciation": " sh ",
         "ambiguity": 2,  # so it doesn't win against abtentious
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7",
         "description": "ti pronounced ch", #congestion
         "spelling": "ti",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7", #variability
         "description": "suffix ity",
         "spelling": "ity",
         "pronunciation": " suffix  @  t  iy ",
         "ambiguity": 4, #ambiguity, versatility
         "orthostore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri?"}
    ],


    "gx": [
        {"chord": "-7l",
         "description": "f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,  # `PHER/SEUFL` → `merciful`, with suffix=_
         "theory": ""},

        {"chord": "-7l",
         "description": "ph pronounced f",  # graph
         "spelling": "p?ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "?"},

        {"chord": "-7l",
         "description": "gh pronounced f",  # graph
         "spelling": "p?ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "gX": [
        {"chord": "7L",
         "description": "th",
         "spelling": "the?",
         "pronunciation": " \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "7L",
         "description": "suffix -th",
         "spelling": "the?",
         "pronunciation": " suffix  \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "gy": [
        {"chord": "-7r",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7r",
         "description": "rv",
         "spelling": "rve?",
         "pronunciation": " r  v ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": "Harri"},
    ],


    "gY": [
        {"chord": "-7R",
         "description": "rk",
         "spelling": "rr?k(k|e)?",
         "pronunciation": " r  k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7R",
         "description": "rck",
         "spelling": "rr?cke?",
         "pronunciation": " r  k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7R",
         "description": "rch pronounced k",
         "spelling": "rr?che?",
         "pronunciation": " r  k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7R",
         "description": "rch pronounced rx",
         "spelling": "rr?che?",
         "pronunciation": " r  x ",
         "ambiguity": 2, #lock/loch
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7R",
         "description": "rc pronounced rk",  # do I make *BG? pick pic? $$$$
         "spelling": "rr?c(c|e)?",
         "pronunciation": " r  k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-7R",
         "description": "rqu",  # do I make *BG? pick pic? $$$$$$$?
         "spelling": "rr?que?",
         "pronunciation": " r  k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "h": [
        {"chord": "-8",
         "description": "r",
         "spelling": "rr?e?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "hx": [
        {"chord": "-8l",
         "description": "rt",
         "spelling": "rr?tt?e?",
         "pronunciation": " r  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},

        {"chord": "-8l",
         "description": "cket",
         "spelling": "c[kc]ett?e?",
         "pronunciation": f" k ( suffix )?({vowel_category["short"]})? t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "hX": [
        {"chord": "-8L",
         "description": "rd",
         "spelling": "rr?dd?e?",
         "pronunciation": " r  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "hy": [
        {"chord": "-8r",
         "description": "r + plural",
         "spelling": "rr?e?ss?",
         "pronunciation": " r  suffix ( i7 )? (s|z) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],


    "hY": [
        {"chord": "-8R",
         "description": "ry",
         "spelling": "rr?(y|ie?)",
         "pronunciation": " r ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": vowel_or_hyphen,
         "theory": ""},
    ],

}
