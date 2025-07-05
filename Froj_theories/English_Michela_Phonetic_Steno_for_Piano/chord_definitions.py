import re


try:
    from Froj_theories.English_Michela_Phonetic_Steno_for_Piano.vowel_categories import vowel_category
except ModuleNotFoundError:
    # Allow running as a script
    from vowel_categories import vowel_category


custom_alphabet = "QSTKPWHR-AOeufrpblgtsdz*_1"

custom_alphabet = "FSCZPNRXIUuieanpzcsf_"


"FSCZPN|RXIU|uiea|npzcsf|_"

#_ midway through a briefing technique


"""
Regex logic here
"""



slash_ = re.compile(r'/$_?')


F_to_N_but_not_SZN_ = re.compile(r'((?!SZN$)[FSCZPN]+)_?$')
F_to_N_or_nothing = re.compile(r'(^/|[FSCZPN])$')

F_to_U_but_not_SZN_ = re.compile(r'((?!SZN$)[FSCZPN]+|[RXIU])_?$')
F_to_U_or_nothing = re.compile(r'(^/|[FSCZPNRXIU])$')
F_to_U_but_not_a_vowel_before = re.compile(r'([npzcsf]/SZN|((?!SZN$)[FSCZPN]+)|[RXIU])$')

first_stroke_F_to_U_or_nothing = re.compile(r'(^/[FSCZPNRXIU]+)$')

u_to_f = re.compile(r'[uieanpzcsf]$')
n_to_f = re.compile(r'[npzcsf]$')

u_to_a_ = re.compile(r'[uiea]_?$')


any_consonant_but_not_KWH = re.compile(r'(/(?!KWH$)[STKPWHR]+|[frpblgtsdz])\*?_?$')  # (?! is for negative lookahead


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
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "",
         "description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},
    ],


    "/": [
        {"chord": "/",
         "description": "",
         "spelling": "",
         "pronunciation": "( (prefix|root) )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_f,
         "theory": ""}],

    "/_": [
        {"chord": "/",
         "description": "/ silent a",
         "spelling": "a",
         "pronunciation": "",  # I made this empty instead of ( suffix )?
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": n_to_f,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": n_to_f,  # changed because meteorological was too big
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": n_to_f,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix, but I'm not sure about this one",
         "spelling": "[aeiouy]+",  # merciful
         "pronunciation": vowel_category["short"] + " suffix ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": n_to_f,
         "theory": ""},

        {"chord": "/",
         "description": "long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": n_to_f,
         "theory": ""}],


    "F": [
        {"chord": "F",
         "description": "f",
         "spelling": "ff?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "F",
         "description": "ph pronounced f",
         "spelling": "p?ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "FC": [
        {"chord": "FC",
         "description": "h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "FC",
         "description": "silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "?"},

        {"chord": "FC",
         "description": "silent h depending on accent",
         "spelling": "h",
         "pronunciation": " \[h1\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "?"},
    ],


    "FCP": [
        {"chord": "FCP",
         "description": "b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "FCN": [
        {"chord": "FCN",
         "description": "r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "FCN",
         "description": "r maybe silent",
         "spelling": "rr?",
         "pronunciation": " \[r\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "FCN",
         "description": "rh silent h",
         "spelling": "rr?h",
         "pronunciation": " r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "FCR": [
        {"chord": "FCR",
         "description": "initial str",
         "spelling": "str",
         "pronunciation": " s  t  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "FCRI": [
        {"chord": "FCRI",
         "description": "initial spl",
         "spelling": "spl",
         "pronunciation": " s  p  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "FCIU": [
        {"chord": "FCIU",
         "description": "initial spr",
         "spelling": "spl",
         "pronunciation": " s  p  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],

    
    "FCXIU": [
        {"chord": "FCXIU",
         "description": "initial scr",
         "spelling": "scr",
         "pronunciation": " s  k  r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "FZ": [
        {"chord": "FZ",
         "description": "th",
         "spelling": "th",
         "pronunciation": " (th|dh|dh/th) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
         ],


    "FZP": [
        {"chord": "TKPW",
         "description": "g",
         "spelling": "gg?h?", #ghost can be TKPWOEFT or TKPWHOEFT
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "FZN": [
        {"chord": "FZN",
         "description": "int/ent",
         "spelling": "[ie]nt",
         "pronunciation": " (i|e|e0)  n ( root )? t ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "FZN",
         "description": "enth",
         "spelling": "[ie]nth",
         "pronunciation": " (i|e|e0)  n ( root )? th ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Plover"}
    ],


    "FP": [
        {"chord": "FP",
         "description": "t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "FP",
         "description": "t but Harri says ch",
         "spelling": "tt?",  # attune
         "pronunciation": " t  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "FN": [
        {"chord": "FN",
         "description": "nd????",
         "spelling": "ndd?",
         "pronunciation": " n  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "S": [
        {"chord": "S",
         "description": "s",
         "spelling": "ss?",
         "pronunciation": " s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "S",
         "description": "s (maybe voiced)",
         "spelling": "ss?",
         "pronunciation": " z/s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "S",
         "description": "sw silent w",  # answer 
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "S",
         "description": "ps silent p",
         # conflicts with "uppsala" but psychotic has `HOT` → `hot` because of silent h so I don't mind
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "S",
         "description": "c pronounced s or sy",  # the ce in pharmaceutical
         "spelling": "cc?e?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "S",
         "description": "consumer",  # consumer
         "spelling": "s",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": slash_,
         "theory": ""},

        #{"chord": "S",
        # "description": "s pronounced z",
        # "spelling": "ss?",
        # "pronunciation": " z ",
        # "ambiguity": 1,
        # "orthoscore": 0,
        # "what must come before": slash_,
        # "theory": ""},

        {"chord": "S",
         "description": "c pronounced s",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "SC": [
        {"chord": "SC",
         "description": "v",
         "spelling": "vv?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],

    "SCP": [
        {"chord": "SCP",
         "description": "d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "SCP",
         "description": "d but Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],

    "SCN": [
        {"chord": "SCN",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "SZ": [
        {"chord": "SZ",
         "description": "rd?????",
         "spelling": "rd",
         "pronunciation": " r  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "SZP": [
        {"chord": "SZP",
         "description": "m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],

    "SZN": [
        {"chord": "SZN",
         "description": "x (I was lazy here)",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],

    "SP": [
        {"chord": "SP",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "SP",
         "description": "cc pronounced ch",
         "spelling": "cc",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "SP",
         "description": "t pronounced ch",
         "spelling": "t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Plover?"},

        {"chord": "SP",
         "description": "ti pronounced ch", #congestion
         "spelling": "t",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": slash_,
         "theory": ""},
    ],


    "SN": [
        {"chord": "SN",
         "description": "ng???",
         "spelling": "ngg?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "C": [
        {"chord": "C",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "C",
         "description": "ci pronounced sh",
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "C",
         "description": "s pronounced sh",
         "spelling": "ss?",  # pressure
         "pronunciation": "( sh | s  y )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "C",
         "description": "s pronounced sh in Harri's accent (Essex?)",
         "spelling": "ss?",  # assume
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "C",
         "description": "sh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #sc like fascist
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},


        {"chord": "C",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],

    "CP": [
        {"chord": "CP",
         "description": "k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CP",
         "description": "c pronounced k",
         "spelling": "cc?",  # acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CP",
         "description": "k, maybe ky",
         "spelling": "cc?",  # barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CP",
         "description": "ch pronounced k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

         {"chord": "CP",
         "description": "ck",
         "spelling": "ck(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CP",
         "description": "q",
         "spelling": "c?q", #acquire
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CP", # connection, context
         "description": "con optional std",
         "spelling": "con[std]?",
         "pronunciation": " k  (@|o|o4)  n ( [st] )?",
         "ambiguity": 10,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Harri"}
    ],


    "CN": [
        {"chord": "CN",
         "description": "w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CN",
         "description": "u pronounced w",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CN",
         "description": "long u", #poplar / popular
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Harri?"},

        {"chord": "CN",
         "description": "long u", #duet
         "spelling": "u",
         "pronunciation": "( suffix )? \[y\]  iu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Harri?"},

        {"chord": "CN",
         "description": "w pronounced v",
         "spelling": "w",
         "pronunciation": " (v|v/w) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "CN",
         "description": "uie vowel",
         "spelling": "o",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Harri"}, #Lapwing

        {"chord": "CN",
         "description": "u",
         "spelling": "u",
         "pronunciation": " \(y uu/w\) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "Z": [
        {"chord": "Z",
         "description": "z",
         "spelling": "zz?",
         "pronunciation": "( z | t  s )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Harri"},

        {"chord": "Z",
         "description": "s (maybe voiced)",
         "spelling": "ss?",
         "pronunciation": " z/s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "Z",
         "description": "s pronounced z",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "ZP": [
        {"chord": "ZP",
         "description": "j",
         "spelling": "j",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZP",
         "description": "j sound",
         "spelling": "(g|dj|di|dgg?e?)", #soldier
         "pronunciation": " jh ",
         "ambiguity": 1, #jest>gest
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZP",
         "description": "g pronounced zh",
         "spelling": "(d?gg?e?)", #aubergine
         "pronunciation": " zh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Harri"},

        {"chord": "ZP",
         "description": "j pronounced zh", #bonjour
         "spelling": "(d?jj?e?)",
         "pronunciation": " zh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": "Harri"},
    ],


    "ZN": [
        {"chord": "ZN",
         "description": "y",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZN",
         "description": "y",
         "spelling": "y",
         "pronunciation": " y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZN",
         "description": "y, but for some people it's silent???",
         "spelling": "y",
         "pronunciation": " \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZN",
         "description": "i",
         "spelling": "i",
         "pronunciation": "( suffix )? (ii|ii2|y|iy) ",  # aerospacial ← who wrote that???, fancier has a iy
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZN",
         "description": "y",
         "spelling": "y",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZN",
         "description": "long e?",  # meteor the second e
         "spelling": "e",
         "pronunciation": " ii2 ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "ZN",
         "description": "unspelt y",
         "spelling": "",
         "pronunciation": " y ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
    ],


    "P": [
        {"chord": "P",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "P",
         "description": "p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""}
    ],


    "N": [
        {"chord": "N",
         "description": "n",
         "spelling": "nn?",
         "pronunciation": " n ( \[y\] )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        {"chord": "N",
         "description": "gn silent g",
         "spelling": "g?n",
         "pronunciation": " n ( y )?",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},

        #{"chord": "N",
        # "description": "in brief",
        # "spelling": "inn?",
        # "pronunciation": " i  n ( \[y\] )?",
        # "ambiguity": 10,
        # "orthoscore": 0,
        # "what must come before": slash_,
        # "theory": ""},
    ],


    # for the second series, I'm using `not SZN`, I just think it would create too many options?

    "R": [
        {"chord": "R",
         "description": "r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "R",
         "description": "r maybe silent",
         "spelling": "rr?",
         "pronunciation": " \[r\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "R",
         "description": "rh silent h",
         "spelling": "rr?h",
         "pronunciation": " r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""}
    ],


    "RI": [  # might be some logic for Commonwealth/United States spelling
        {"chord": "RI",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},
    ],


    "RIU": [
        {"chord": "RIU",
         "description": "t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "RIU",
         "description": "t but Harri says ch",
         "spelling": "tt?",  # attune
         "pronunciation": " t  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "SCP",
         "description": "d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "SCP",
         "description": "d but Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""}
    ],


    "RU": [
        {"chord": "RU",
         "description": "m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""}
    ],


    "X": [
        {"chord": "X",
         "description": "s",
         "spelling": "ss?",
         "pronunciation": " s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "X",
         "description": "s (maybe silent)",
         "spelling": "ss?",
         "pronunciation": " z/s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "X",
         "description": "sw silent w",  # answer 
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "X",
         "description": "ps silent p",
         # conflicts with "uppsala" but psychotic has `HOT` → `hot` because of silent h so I don't mind
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "X",
         "description": "c pronounced s or sy",  # the ce in pharmaceutical
         "spelling": "cc?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "X",
         "description": "s (maybe y too)",  # consumer
         "spelling": "s",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "X",
         "description": "s pronounced z",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "X",
         "description": "c pronounced s",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},
    ],


    "XI": [
        {"chord": "XI",
         "description": "Other languages stick w and f here, but we don't have f, and I'm sticking w on U",
         "spelling": "freeeeeeeeeeeeeeee???",
         "pronunciation": "freeeeeeeeeeee",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": "Harri"},
    ],


    "XIU": [
        {"chord": "XIU",
         "description": "k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "XIU",
         "description": "c pronounced k",
         "spelling": "cc?",  # acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "XIU",
         "description": "k, maybe ky",
         "spelling": "cc?",  # barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "XIU",
         "description": "ch pronounced k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

         {"chord": "XIU",
         "description": "ck",
         "spelling": "ck(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "XIU",
         "description": "q",
         "spelling": "c?q", #acquire
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "XIU", # connection, context
         "description": "con optional std",
         "spelling": "con[std]?",
         "pronunciation": " k  (@|o|o4)  n ( [st] )?",
         "ambiguity": 10,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": "Harri"},

        {"chord": "XIU",
         "description": "g",
         "spelling": "gg?h?", #ghost can be TKPWOEFT or TKPWHOEFT
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""}
    ],


    "XU": [
        {"chord": "TPH",
         "description": "n",
         "spelling": "nn?",
         "pronunciation": " n ( \[y\] )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "TPH",
         "description": "gn silent g",
         "spelling": "g?n",
         "pronunciation": " n ( y )?",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},
    ],


    "IU": [
        {"chord": "IU",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "IU",
         "description": "p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "IU",
         "description": "b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},
    ],


    "I": [
        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "I",
         "description": "y, but for some people it's silent???",
         "spelling": "y",
         "pronunciation": " \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "I",
         "description": "i",
         "spelling": "i",
         "pronunciation": "( suffix )? (ii|ii2|y|iy) ",  # aerospacial ← who wrote that???, fancier has a iy
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "I",
         "description": "long e?",  # meteor the second e
         "spelling": "e",
         "pronunciation": " ii2 ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "I",
         "description": "unspelt y",
         "spelling": "",
         "pronunciation": " y ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},
    ],


    "U": [
        {"chord": "U",
         "description": "w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": "Harri"},

        {"chord": "U",
         "description": "u pronounced w",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": "Harri"},

        {"chord": "U",
         "description": "long u", #poplar / popular
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "U",
         "description": "long u", #duet
         "spelling": "u",
         "pronunciation": "( suffix )? \[y\]  iu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},

        {"chord": "U",
         "description": "w pronounced v",
         "spelling": "w",
         "pronunciation": " (v|v/w) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": "Harri"},

        {"chord": "U",
         "description": "uie vowel",
         "spelling": "o",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": "Harri"}, #Lapwing

        {"chord": "U",
         "description": "u",
         "spelling": "u",
         "pronunciation": " \(y uu/w\) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_but_not_SZN_,
         "theory": ""},
    ],


    "Uu": [
        {"chord": "Uu",
         "description": "Uu vowel",
         "spelling": "a[auh]?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_or_nothing,
         "theory": ""},

        {"chord": "Uu",
         "description": "Uu vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": -1, #thought
         "what must come before": F_to_N_or_nothing,
         "theory": ""},

        {"chord": "Uu",
         "description": "Uu vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 3,
         "orthoscore": -1, #corp
         "what must come before": F_to_N_or_nothing,
         "theory": ""},

        {"chord": "Uu",
         "description": "au",
         "spelling": "short vowel spelt au",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_N_or_nothing,
         "theory": ""},

        {"chord": "Uu",
         "description": "ia vowel spelt au",
         "spelling": "au",
         "pronunciation": vowel_category["OU"], #Macau
         "ambiguity": 2,
         "orthoscore": 1,
         "what must come before": F_to_N_or_nothing,
         "theory": ""},

        {"chord": "Uu",
         "description": "Uu vowel",
         "spelling": "awe?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": F_to_N_or_nothing,
         "theory": ""},
    ],

    "Ii": [
        {"chord": "Ii",
         "description": "Ii vowel",
         "spelling": "oi",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_N_or_nothing,
         "theory": ""},

        {"chord": "Ii",
         "description": "Ii vowel",
         "spelling": "oye?",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 1,  # feel free to change this prioritisation
         "orthoscore": 0,
         "what must come before": F_to_N_or_nothing,
         "theory": ""}
    ],


    "u": [
        {"chord": "u",
         "description": "u",
         "spelling": "u",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "u",
         "description": "U vowel spelt ou",
         "spelling": "ou",
         "pronunciation": vowel_category["U"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": "Harri"},

        {"chord": "u",
         "description": "ou",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],


    "u_": [
        {"chord": "u",
         "description": "silent u",
         "spelling": "u",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_a_vowel_before,
         "theory": "Harri"},
    ],


    "ui": [
        {"chord": "ui",
         "description": "ui vowel",
         "spelling": "ie?",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ui",
         "description": "ui vowel",
         "spelling": "ei",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ui",
         "description": "ui vowel",
         "spelling": "y",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": "StenEd?"},

        {"chord": "ui",
         "description": "ui vowel",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ui",
         "description": "ui vowel followed by a short e",
         "spelling": "ie",
         "pronunciation": vowel_category["AOEU"] + " @ ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ui",
         "description": "suffix ui vowel",
         "spelling": "i",
         "pronunciation": f' suffix {vowel_category["AOEU"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_SZN_,
         "theory": ""},
    ],


    "i": [
        {"chord": "i",
         "description": "y pronounced i diphthong",
         "spelling": "e?y",
         "pronunciation": " iy ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "ee pronounced i diphthong",
         "spelling": "ee",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "ii pronounced i diphthong",
         "spelling": "ii",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "ie pronounced i diphthong",
         "spelling": "ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "i",
         "spelling": "i",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "y",
         "spelling": "y",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,  # honestly this might be 0
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "i diphthong",
         "spelling": "i",
         "pronunciation": " iy ",
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "e pronounced i diphthong",  # acne, aires
         "spelling": "e",
         "pronunciation": " iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": "Harri?"},

        {"chord": "i",
         "description": "ea pronounced i diphthong",
         "spelling": "ea",
         "pronunciation": " iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": "Harri?"},

        {"chord": "i",
         "description": "EU vowel spelt u", #busy
         "spelling": "u",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #busy
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "EU vowel spelt u", #busy
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #garbage
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "i",
         "description": "EU vowel spelt ui", #build
         "spelling": "ui?",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        #{"chord": "i", commented out because of antidisestablishmentarianism, electrocardiography
        # "description": "EU vowel spelt e",  # delicious
        # "spelling": "e",
        # "pronunciation": vowel_category["EU"],
        # "ambiguity": 0,
        # "orthoscore": -1,
        # "what must come before": SToR_or_nothing,
        # "theory": ""},

        {"chord": "i",
         "description": "ue vowel spelt i",
         "spelling": "i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": 1, #Mozambique, Shiba
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

         {"chord": "i",
         "description": "suffix -y", #assembly
         "spelling": "(y|ie?)",
         "pronunciation": " suffix  iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_SZN_,
         "theory": ""},
    ],


    "i_": [
        {"chord": "i",
         "description": "silent i",
         "spelling": "i",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_a_vowel_before,
         "theory": "Harri"},
    ],


    "ue": [
        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ee",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ie",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": -1, #Mozambique, Shiba
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",  # acne, aires
         "spelling": "e",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #genotype
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #read
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel but maybe it's two syllables?",
         "spelling": "ea",
         "pronunciation": " i@ ",
         "ambiguity": 1,
         "orthoscore": -1, #real
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ey",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #key
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "oe",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #diarhoea
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "eo", #theory
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],


    "uie": [
        {"chord": "uie",
         "description": "uie vowel",
         "spelling": "o[eu]?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel spelt ow",
         "spelling": "owe?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel spelt au",
         "spelling": "au",  # baudelaire, aubergine beaux,
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": -1, #aubergine
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel",
         "spelling": "ot$",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel spelt oa",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "orthoscore": -1, #toad
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],


    "ie": [
        {"chord": "ie",
         "description": "o",
         "spelling": "o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ie",
         "description": "short vowel spelt ow", # Knowledge
         "spelling": "ow",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ie",
         "description": "Uu vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #corp story
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ie",
         "description": "uia vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 1, #move,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ie",
         "description": "O vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["O"],
         "ambiguity": 1,
         "orthoscore": -1, #yacht
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],


    "ie_": [
        {"chord": "ie",
         "description": "silent o",
         "spelling": "o",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_a_vowel_before,
         "theory": "Harri"},
    ],


    "e": [
        {"chord": "e",
         "description": "e",
         "spelling": "e",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "e",
         "description": "E vowel spelt ea",
         "spelling": "ea",
         "pronunciation": vowel_category["E"],
         "ambiguity": 1,
         "orthoscore": -1,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "e",
         "description": "E vowel spelt ai",  # against
         "spelling": "ai",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "e",
         "description": "EU vowel spelt e",  # delicious
         "spelling": "e",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "e",
         "description": "E vowel", #friend
         "spelling": "ie",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],


    "e_": [
        {"chord": "E",
         "description": "silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_a_vowel_before,
         "theory": "Harri"}
    ],


    "ua": [
        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "a",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "a(a|ye?|i)",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1, # wave > waive
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel (are you British?)",
         "spelling": "e",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ett?e?",
         "pronunciation": vowel_category["AEU"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ey",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ei", #inveigh, weigh
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": -1,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ua",
         "description": "suffix ua vowel",
         "spelling": "a",
         "pronunciation": f' suffix {vowel_category["AEU"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_SZN_,
         "theory": ""},
    ],


    "uia": [
        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "e?ue?", # deuteronomy
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "ou", 
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": -1, #soup
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "eau",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "ui",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "ew",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,  # nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": -1, #move
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uia", 
         "description": "uia vowel",
         "spelling": "uu", #vacuum
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "uia", 
         "description": "uia vowel + another",
         "spelling": "ui", #druid
         "pronunciation": f'{vowel_category["AOU"]} i ',
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],

    "ia": [
        {"chord": "ia",
         "description": "Uu vowel spelt ou", #thought
         "spelling": "ou",
         "pronunciation": vowel_category["AU"], # bolder/boulder  thought   " starting_root  th  oo  t  suffix  f  [u]  l ",
         "ambiguity": 0,
         "orthoscore": 1, #thought
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ia",
         "description": "ia vowel",
         "spelling": "ow",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ia",
         "description": "uie vowel spelt OU??",
         "spelling": "ou",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": "Harri"},

        {"chord": "ia",
         "description": "short vowel spelt ou",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,  # colour
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": "Harri"},

        {"chord": "ia",
         "description": "ia vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],


    "iea": [
        {"chord": "iea",
         "description": "Uu vowel spelt ao",
         "spelling": "oa",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #coarse
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "iea",
         "description": "uie vowel spelt oa",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 1, #toad
         "what must come before": first_stroke_F_to_U_or_nothing,
         "theory": ""},

        {"chord": "iea",
         "description": "short vowel spelt oo",
         "spelling": "oo",
         "pronunciation": vowel_category["short"] ,  # u is took I think?
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "iea",
         "description": "uia vowel spelt oo",
         "spelling": "oo",
         "pronunciation": vowel_category["AOU"],  # uu is noon
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""}
    ],


    "ea": [
        {"chord": "ea",
         "description": "ue vowel spelt ea (first stroke only)",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"], #it was just ii before
         "ambiguity": 1,
         "orthoscore": 1, #read
         "what must come before": first_stroke_F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ea",
         "description": "ea pronounced short e (first stroke only)",
         "spelling": "ea",
         "pronunciation": " e ", # earl?
         "ambiguity": 2, #red
         "orthoscore": 1, #read
         "what must come before": first_stroke_F_to_U_or_nothing,
         "theory": ""},

        {"chord": "ea",
         "description": "ua vowel spelt ea (first stroke only)",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 1,
         "what must come before": first_stroke_F_to_U_or_nothing,
         "theory": "?"},

        {"chord": "ea",
         "description": "ue vowel spelt ae",
         "spelling": "ae",
         "pronunciation": vowel_category["AOE"], # eir?
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": "Lapwing?"},
    ],


    "a": [
        {"chord": "a",
         "description": "short a",
         "spelling": "a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "a",
         "description": "short a", #villain... but not against?
         "spelling": "ai",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": F_to_U_or_nothing,
         "theory": ""},

        {"chord": "a",
         "description": "EU vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": F_to_U_or_nothing,
         "theory": ""},
    ],


    "a_": [
        {"chord": "a",
         "description": "silent a",
         "spelling": "a",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": F_to_U_but_not_a_vowel_before,  # guard shouldn't be "drop vowel, silent a"
         "theory": "Harri"},
    ],


    "n": [
        {"chord": "n",
         "description": "n",
         "spelling": "o?ne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "n",
         "description": "n", #gin
         "spelling": "o?nne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "n",
         "description": "suffix -n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "?"},

        {"chord": "n",
         "description": "gn silent g",
         "spelling": "gne?",
         "pronunciation": " n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "p": [
        {"chord": "p",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0, #group > groupe
         "orthoscore": 0,
         "what must come before": u_to_a_,  # ".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "theory": ""},

        {"chord": "p",
         "description": "p",
         "spelling": "pp?e",
         "pronunciation": " p ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # ".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "theory": ""}
    ],


    "nz": [
        {"chord": "nz",
         "description": "y pronounced i diphthong",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "nz",
         "description": "y pronounced i diphthong",
         "spelling": "ie?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "nz",
         "description": "y pronounced i",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "nz",
         "description": "dy",
         "spelling": "dd?(y|ie?)",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "HelloChap?"}
    ],


    "pz": [
        {"chord": "pz",
         "description": "j",
         "spelling": "d?je?",
         "pronunciation": " jh ",
         "ambiguity": 1, #Why 1? not 0?
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pz",
         "description": "g pronounced j",
         "spelling": "d?gg?e?",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pz",
         "description": "zh sound",
         "spelling": "(j|dj|d?gg?)e?",
         "pronunciation": " zh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""}
    ],  # arbitrage


    "z": [
        {"chord": "z",
         "description": "s voiced",
         "spelling": "se?",
         "pronunciation": " z ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "z",
         "description": "s (maybe voiced)",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "z",
         "description": "ss voiced",
         "spelling": "sse?",  # actresses?"
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         # cyclops
         "what must come before": u_to_a_,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},
    ],

 
    "nc": [
        {"chord": "nc",
         "description": "w????",
         "spelling": "ww?",
         "pronunciation": "( w | hw )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "pc": [
        {"chord": "pc",
         "description": "k",
         "spelling": "k(k|e)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "?"},

        {"chord": "pc",
         "description": "ck",
         "spelling": "cke?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pc",
         "description": "ch pronounced k",
         "spelling": "che?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "?"},

        {"chord": "pc",
         "description": "ch pronounced x",
         "spelling": "che?",
         "pronunciation": " x ",
         "ambiguity": 2, #lock/loch
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "Harri"},

        {"chord": "pc",
         "description": "lk silent l??)",
         "spelling": "lk",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pc",
         "description": "c pronounced k",
         "spelling": "c(c|e)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pc",
         "description": "qu",
         "spelling": "que?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "pc/S": [
        {"chord": "pc/S",
         "description": "x (sorry, too lazy for g+z)",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "pc/SP": [
        {"chord": "pc/SP",
         "description": "x (sorry, too lazy for g+zh)",
         "spelling": "xi?",
         "pronunciation": "( k  sh | g  zh )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "c": [
        {"chord": "c",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "c",
         "description": "ci pronounced sh (Harri's accent)",  # aerospacial
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "c",
         "description": "sh sound",
         "spelling": "((s|t|x)i|c[ei]|s?che?|sc|ss)",
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "c",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "ns": [
        {"chord": "ns",
         "description": "ng",
         "spelling": "ng?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ns",
         "description": "ngue", #tongue
         "spelling": "ngue",
         "pronunciation": " ng ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ns",
         "description": "ng with g",
         "spelling": "ng",
         "pronunciation": " ng ( \[?g\]? )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ns",
         "description": "'nge' in 'singe'",
         # funny example cause of course `SEUPBG` → `sing`, but `ORPBG` → `orange`
         "spelling": "nge?",
         "pronunciation": " n  jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ns",
         "description": "ng sound then g sound",
         "spelling": "ng?",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""}
    ],


    "ps": [
        {"chord": "ps",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "?"},

        {"chord": "ps",
         "description": "tch",
         "spelling": "tch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ps",
         "description": "ch spelt t",
         "spelling": "t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "nzs": [
        {"chord": "nzs",
         "description": "x",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "nzs",
         "description": "ction",
         "spelling": "ction",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "nzs",
         "description": "cation",
         "spelling": "cation",
         "pronunciation": " k  ee  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "Harri"}
    ],


    "pzs": [
        {"chord": "pzs",
         "description": "m",
         "spelling": "mm?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pzs",
         "description": "mb silent b",
         "spelling": "mb",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pzs",
         "description": "mp silent p",
         "spelling": "mp",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pzs",
         "description": "mn silent n",
         "spelling": "mn",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        #{"chord": "pzs",
        # "description": "lm silent l (has to follow AU)",
        # "spelling": "lm",
        # "pronunciation": "( \[l1\] )? m ",
        # "ambiguity": 0,
        # "orthoscore": 0,
        # "what must come before": Au, #balm
        # "theory": ""},
    ],


    "zs": [
        {"chord": "zs",
         "description": "rd",
         "spelling": "rdd?",
         "pronunciation": " r  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "ncs": [
        {"chord": "ncs",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncs",
         "description": "le",
         "spelling": "ll?e",
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncs",
         "description": "el",
         "spelling": "ell?e?", #I added the final ? cause it looked wrong without it?
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncs",
         "description": "al",
         "spelling": "all?e?",
         "pronunciation": " @  l ",  # silent a is already a thing
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncs",
         "description": "suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncs",
         "description": "suffix -l",  # antibacterial
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "pcs": [
        {"chord": "pcs",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pcs",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pcs",
         "description": "suffix -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""}
    ],



    "cs": [
        {"chord": "cs",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "cs",
         "description": "v",
         "spelling": "rve?",
         "pronunciation": " v ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "Harri"}
    ],


    "s": [
        {"chord": "s",
         "description": "unvoiced se",
         "spelling": "se",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},

        {"chord": "s",
         "description": "unvoiced s", #cyclops
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # dis
         "theory": ""},

        {"chord": "s",
         "description": "s (maybe voiced)",
         "spelling": "s",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # dis
         "theory": ""},

        {"chord": "s",
         "description": "s silent t",
         "spelling": "ss?te?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # no idea, this just feels right
         "theory": ""},

        {"chord": "s",
         "description": "s silent w",  # answer
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "s",
         "description": "ss",
         "spelling": "unvoiced ss",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "s",
         "description": "unvoiced s spelt c",
         "spelling": "s?ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "s",
         "description": "s maybe voiced",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # no _ I think?
         "theory": ""},


        #{"chord": "s",
        # "description": "suffix -s",
        # "spelling": "s",
        # "pronunciation": "( (suffix) ) (s|z|z/s) ",
        # "ambiguity": 1,
        # "orthoscore": 0,
        # "what must come before": A_to_g_yes_t,
        # "theory": ""}
    ],

    "nf": [
        {"chord": "nd",
         "description": "nd",
         "spelling": "ndd?",
         "pronunciation": " n  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],

    "pcf": [
        {"chord": "pcf",
         "description": "b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "cf": [
        {"chord": "cf",
         "description": "h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "cf",
         "description": "silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},


        {"chord": "cf",
         "description": "st!",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "pf": [
        {"chord": "pf",
         "description": "t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pf",
         "description": "final dt pronounced t",
         "spelling": "dt$",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pf",
         "description": "t pronounced sh",
         "spelling": "tt?e?",
         "pronunciation": " sh ",
         "ambiguity": 2,  # so it doesn't win against abtentious
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pf",
         "description": "ti pronounced ch", #congestion
         "spelling": "ti",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pf", #variability
         "description": "suffix ity",
         "spelling": "ity",
         "pronunciation": " suffix  @  t  iy ",
         "ambiguity": 4, #ambiguity, versatility
         "orthostore": 0,
         "what must come before": u_to_a_,
         "theory": ""}
    ],


    "nzf": [
        {"chord": "nzf",
         "description": "nt",
         "spelling": "nt",
         "pronunciation": " n ( root )? t ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "pzf": [
        {"chord": "pzf",
         "description": "g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "pzf",
         "description": "silent gh",
         "spelling": "gh",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "Harri"},
    ],


    "zf": [
        {"chord": "zf",
         "description": "th",
         "spelling": "the?",
         "pronunciation": " \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "zf",
         "description": "suffix -th",
         "spelling": "the?",
         "pronunciation": " suffix  \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],


    "ncf": [
        {"chord": "ncf",
         "description": "r",
         "spelling": "rr?e?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix? -re",
         "spelling": "re",
         "pronunciation": "( suffix )? (\(r  @/@r  r\)|@r  r) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix -r??", #secret
         "spelling": "r",
         "pronunciation": "( suffix ) r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix -er",
         "spelling": "err?",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "Harri"},

        {"chord": "ncf",
         "description": "ar???",
         "spelling": "arr?",  # friar
         "pronunciation": " r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "Harri"},

        {"chord": "ncf",
         "description": "suffix -or/-our???",
         "spelling": "ou?rr?",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # reusing cause I'm lazy
         "theory": "Harri"}
    ],


    "f": [
        {"chord": "f",
         "description": "f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a_,  # `PHER/SEUFL` → `merciful`, with suffix=_
         "theory": ""},

        {"chord": "f",
         "description": "ph pronounced f",  # graph
         "spelling": "p?ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": "?"},

        {"chord": "f",
         "description": "gh pronounced f",  # laugh
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a_,
         "theory": ""},
    ],

}