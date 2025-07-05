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

any_consonant_but_not_SZN = re.compile(r'(((?!SZN$)[FSCZPN]+)|[npzcsf])$')

slash_ = re.compile(r'/$_?')


F_to_N_but_not_SZN_ = re.compile(r'((?!SZN$)[FSCZPN]+)_?$')
F_to_U_but_not_SZN_ = re.compile(r'((?!SZN$)[FSCZPN]+|[RXIU])$')
F_to_U_or_nothing = re.compile(r'(^/|[FSCZPNRXIU])$')


u_to_f = re.compile(r'[uieanpzcsf]$')
n_to_f = re.compile(r'[npzcsf]$')

u_to_a = re.compile(r'[uiea]$')


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
         "what must come before": any_consonant_but_not_SZN,
         "theory": ""},

        {"chord": "",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": any_consonant_but_not_SZN,
         "theory": ""},

        {"chord": "",
         "description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": any_consonant_but_not_SZN,
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


    "W": [
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
         "description": "OE vowel",
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
         "description": "OE vowel",
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
         "description": "AOE vowel spelt i",
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


    "n": [
        {"chord": "n",
         "description": "n",
         "spelling": "o?ne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "n",
         "description": "n", #gin
         "spelling": "o?nne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "n",
         "description": "suffix -n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "?"},

        {"chord": "n",
         "description": "gn silent g",
         "spelling": "gne?",
         "pronunciation": " n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "p": [
        {"chord": "p",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0, #group > groupe
         "orthoscore": 0,
         "what must come before": u_to_a,  # ".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "theory": ""},

        {"chord": "p",
         "description": "p",
         "spelling": "pp?e",
         "pronunciation": " p ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,  # ".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "theory": ""}
    ],


    "nz": [
        {"chord": "nz",
         "description": "y pronounced i diphthong",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "nz",
         "description": "y pronounced i diphthong",
         "spelling": "ie?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "nz",
         "description": "y pronounced i",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "nz",
         "description": "dy",
         "spelling": "dd?(y|ie?)",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "HelloChap?"}
    ],


    "pz": [
        {"chord": "pz",
         "description": "j",
         "spelling": "d?je?",
         "pronunciation": " jh ",
         "ambiguity": 1, #Why 1? not 0?
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pz",
         "description": "g pronounced j",
         "spelling": "d?gg?e?",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pz",
         "description": "zh sound",
         "spelling": "(j|dj|d?gg?)e?",
         "pronunciation": " zh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""}
    ],  # arbitrage


    "z": [
        {"chord": "z",
         "description": "s voiced",
         "spelling": "se?",
         "pronunciation": " z ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "z",
         "description": "s (maybe voiced)",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "z",
         "description": "ss voiced",
         "spelling": "sse?",  # actresses?"
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         # cyclops
         "what must come before": u_to_a,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},
    ],

 
    "nc": [
        {"chord": "nc",
         "description": "w????",
         "spelling": "ww?",
         "pronunciation": "( w | hw )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "pc": [
        {"chord": "pc",
         "description": "k",
         "spelling": "k(k|e)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "?"},

        {"chord": "pc",
         "description": "ck",
         "spelling": "cke?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pc",
         "description": "ch pronounced k",
         "spelling": "che?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "?"},

        {"chord": "pc",
         "description": "ch pronounced x",
         "spelling": "che?",
         "pronunciation": " x ",
         "ambiguity": 2, #lock/loch
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "Harri"},

        {"chord": "pc",
         "description": "lk silent l??)",
         "spelling": "lk",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pc",
         "description": "c pronounced k",
         "spelling": "c(c|e)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pc",
         "description": "qu",
         "spelling": "que?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "pc/S": [
        {"chord": "pc/S",
         "description": "x (sorry, too lazy for g+z)",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "pc/SP": [
        {"chord": "pc/SP",
         "description": "x (sorry, too lazy for g+zh)",
         "spelling": "xi?",
         "pronunciation": "( k  sh | g  zh )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "c": [
        {"chord": "c",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "c",
         "description": "ci pronounced sh (Harri's accent)",  # aerospacial
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "c",
         "description": "sh sound",
         "spelling": "((s|t|x)i|c[ei]|s?che?|sc|ss)",
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "c",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "ns": [
        {"chord": "ns",
         "description": "ng",
         "spelling": "ng?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ns",
         "description": "ngue", #tongue
         "spelling": "ngue",
         "pronunciation": " ng ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ns",
         "description": "ng with g",
         "spelling": "ng",
         "pronunciation": " ng ( \[?g\]? )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ns",
         "description": "'nge' in 'singe'",
         # funny example cause of course `SEUPBG` → `sing`, but `ORPBG` → `orange`
         "spelling": "nge?",
         "pronunciation": " n  jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ns",
         "description": "ng sound then g sound",
         "spelling": "ng?",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""}
    ],


    "ps": [
        {"chord": "ps",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "?"},

        {"chord": "ps",
         "description": "tch",
         "spelling": "tch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ps",
         "description": "ch spelt t",
         "spelling": "t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "nzs": [
        {"chord": "nzs",
         "description": "x",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "nzs",
         "description": "ction",
         "spelling": "ction",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "nzs",
         "description": "cation",
         "spelling": "cation",
         "pronunciation": " k  ee  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "Harri"}
    ],


    "pzs": [
        {"chord": "pzs",
         "description": "m",
         "spelling": "mm?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pzs",
         "description": "mb silent b",
         "spelling": "mb",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pzs",
         "description": "mp silent p",
         "spelling": "mp",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pzs",
         "description": "mn silent n",
         "spelling": "mn",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
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
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "ncs": [
        {"chord": "ncs",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncs",
         "description": "le",
         "spelling": "ll?e",
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncs",
         "description": "el",
         "spelling": "ell?e?", #I added the final ? cause it looked wrong without it?
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncs",
         "description": "al",
         "spelling": "all?e?",
         "pronunciation": " @  l ",  # silent a is already a thing
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncs",
         "description": "suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncs",
         "description": "suffix -l",  # antibacterial
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "pcs": [
        {"chord": "pcs",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pcs",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pcs",
         "description": "suffix -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""}
    ],



    "cs": [
        {"chord": "cs",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "cs",
         "description": "v",
         "spelling": "rve?",
         "pronunciation": " v ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "Harri"}
    ],


    "s": [
        {"chord": "s",
         "description": "unvoiced se",
         "spelling": "se",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},

        {"chord": "s",
         "description": "unvoiced s", #cyclops
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,  # dis
         "theory": ""},

        {"chord": "s",
         "description": "s (maybe voiced)",
         "spelling": "s",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,  # dis
         "theory": ""},

        {"chord": "s",
         "description": "s silent t",
         "spelling": "ss?te?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,  # no idea, this just feels right
         "theory": ""},

        {"chord": "s",
         "description": "s silent w",  # answer
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "s",
         "description": "ss",
         "spelling": "unvoiced ss",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "s",
         "description": "unvoiced s spelt c",
         "spelling": "s?ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "s",
         "description": "s maybe voiced",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,  # no _ I think?
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
         "what must come before": u_to_a,
         "theory": ""},
    ],

    "pcf": [
        {"chord": "pcf",
         "description": "b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "cf": [
        {"chord": "cf",
         "description": "h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "cf",
         "description": "silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},


        {"chord": "cf",
         "description": "st!",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "pf": [
        {"chord": "pf",
         "description": "t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pf",
         "description": "final dt pronounced t",
         "spelling": "dt$",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pf",
         "description": "t pronounced sh",
         "spelling": "tt?e?",
         "pronunciation": " sh ",
         "ambiguity": 2,  # so it doesn't win against abtentious
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pf",
         "description": "ti pronounced ch", #congestion
         "spelling": "ti",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pf", #variability
         "description": "suffix ity",
         "spelling": "ity",
         "pronunciation": " suffix  @  t  iy ",
         "ambiguity": 4, #ambiguity, versatility
         "orthostore": 0,
         "what must come before": u_to_a,
         "theory": ""}
    ],


    "nzf": [
        {"chord": "nzf",
         "description": "nt",
         "spelling": "nt",
         "pronunciation": " n ( root )? t ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "pzf": [
        {"chord": "pzf",
         "description": "g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "pzf",
         "description": "silent gh",
         "spelling": "gh",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "Harri"},
    ],


    "zf": [
        {"chord": "zf",
         "description": "th",
         "spelling": "the?",
         "pronunciation": " \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "zf",
         "description": "suffix -th",
         "spelling": "the?",
         "pronunciation": " suffix  \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],


    "ncf": [
        {"chord": "ncf",
         "description": "r",
         "spelling": "rr?e?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix? -re",
         "spelling": "re",
         "pronunciation": "( suffix )? (\(r  @/@r  r\)|@r  r) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix -r??", #secret
         "spelling": "r",
         "pronunciation": "( suffix ) r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix -er",
         "spelling": "err?",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "Harri"},

        {"chord": "ncf",
         "description": "ar???",
         "spelling": "arr?",  # friar
         "pronunciation": " r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "Harri"},

        {"chord": "ncf",
         "description": "suffix -or/-our???",
         "spelling": "ou?rr?",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": u_to_a,  # reusing cause I'm lazy
         "theory": "Harri"}
    ],


    "f": [
        {"chord": "f",
         "description": "f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": u_to_a,  # `PHER/SEUFL` → `merciful`, with suffix=_
         "theory": ""},

        {"chord": "f",
         "description": "ph pronounced f",  # graph
         "spelling": "p?ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": "?"},

        {"chord": "f",
         "description": "gh pronounced f",  # laugh
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": u_to_a,
         "theory": ""},
    ],

}