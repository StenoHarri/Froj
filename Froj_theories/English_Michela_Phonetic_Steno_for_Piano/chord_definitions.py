import re


try:
    from Froj_theories.English_Michela_Phonetic_Steno_for_Piano.vowel_categories import vowel_category
except ModuleNotFoundError:
    # Allow running as a script
    from vowel_categories import vowel_category


custom_alphabet = "FSCZPNRXIUuieanpzcsf_"
valid_final_letter = r'(^/[RXIU]+|[uieanpzcsf])$'


"FSCZPN|RXIU|uiea|npzcsf|_"


#_ to say "don't skip a series"


"""
Regex logic here
"""
initial_slash = re.compile(r'^/$')
slash_ = re.compile(r'/$_?')


slash_or_first_series = re.compile(r'[/FSCZPN]$')

first_series = re.compile(r'[FSCZPN]$')

#no ? on purpose
first_series_ = re.compile(r'[FSCZPN]_$')


#first_stroke_2nd_or_3rd_to_4th = 

initial_first_or_second_series = re.compile(r'(^/[FSCZPNRXIU]+)$')

initial_second_series_or_third_or_fourth = re.compile(r'((/[RXIU])|[uieanpzcsf])$')

slash_or_first_or_second_series = re.compile(r'[FSCZPNRXIU]$')

not_initial_slash_or_first_or_second_series_ = re.compile(r'(./|[FSCZPNRXIU]_?)$')


fourth_before_slash_or_first_or_second_series = re.compile(r'([npzcsf]/|[FSCZPNRXIU])$')


fourth_series = re.compile(r'[npzcsf]$')


#Can't think of a good way to describe this, here's a link to the discussion https://discord.com/channels/136953735426473984/452550775592321054/1393999334755926130
consonanted_consonant_OR_initial_second_OR_third_ = re.compile(
    r'([npzcsf]/[FSCZPN]+|(^/|[FSCZPN])[RXIU]+|[uiea]_?)')


initial_slash_or_anything_else = re.compile(r'(^/|[FSCZPNRXIUuieanpzcsf])$')

initial_slash_or_anything_else_ = re.compile(r'(^/|[FSCZPNRXIUuieanpzcsf])_$') #intensional lack of ?



































































































































































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
         "what must come before": first_series,
         "theory": ""},

        {"chord": "",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "",
         "description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "",
         "description": "drop short vowel + consonant!",
         "spelling": "[aeiouy][bcdfghjklmnpqrstvwxyz]",
         "pronunciation": f'{vowel_category["short"]}( [bcdfghjklmnpqrstvwxyz]+ )',
         "ambiguity": 15,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": "?"},
    ],


    "/": [
        {"chord": "/",
         "description": "",
         "spelling": "",
         "pronunciation": "( (prefix|root) )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},

        {"chord": "/",
         "description": "suffix",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},
    ],


    "/_": [
        {"chord": "/",
         "description": "/ silent a",
         "spelling": "a",
         "pronunciation": "",  # I made this empty instead of ( suffix )?
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,  # changed because meteorological was too big
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix, but I'm not sure about this one",
         "spelling": "[aeiouy]+",  # merciful
         "pronunciation": vowel_category["short"] + " suffix ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/",
         "description": "long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": fourth_series,
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
         "theory": ""},

        {"chord": "FC",
         "description": "silent h depending on accent",
         "spelling": "h",
         "pronunciation": " \[h1\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
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
        {"chord": "FZP",
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
         "theory": ""}
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
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": slash_,
         "theory": ""},
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
         "theory": ""},

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
         "spelling": "ww?h?",
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
         "theory": ""},

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


    "R": [
        {"chord": "R",
         "description": "r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "R",
         "description": "r maybe silent",
         "spelling": "rr?",
         "pronunciation": " \[r\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "R",
         "description": "rh silent h",
         "spelling": "rr?h",
         "pronunciation": " r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "R",
         "description": "initial a",
         "spelling": "^a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "R",
         "description": "initial short a", #villain... but not against?
         "spelling": "^ai",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "R",
         "description": "initial EU vowel spelt a",
         "spelling": "^a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": initial_slash,
         "theory": ""},
    ],

    
    "R_": [
        {"chord": "R",
         "description": "r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "R",
         "description": "r maybe silent",
         "spelling": "rr?",
         "pronunciation": " \[r\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "R",
         "description": "rh silent h",
         "spelling": "rr?h",
         "pronunciation": " r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "RX": [
        {"chord": "RX",
         "description": "initial ue vowel spelt ea (first stroke only)",
         "spelling": "^ea",
         "pronunciation": vowel_category["AOE"], #it was just ii before
         "ambiguity": 1,
         "orthoscore": 1, #read
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RX",
         "description": "ea pronounced short e (first stroke only)",
         "spelling": "^ea",
         "pronunciation": " e ", # earl?
         "ambiguity": 2, #red
         "orthoscore": 1, #read
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RX",
         "description": "ua vowel spelt ea (first stroke only)",
         "spelling": "^e", # made
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": 1,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RX",
         "description": "ue vowel spelt ae",
         "spelling": "^ae",
         "pronunciation": vowel_category["AOE"], # eir?
         "ambiguity": 3, # made > mead
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "RXI": [
        {"chord": "RXI",
         "description": "initial Uu vowel spelt ao",
         "spelling": "^oa",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #coarse
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RXI",
         "description": "initial uie vowel spelt oa",
         "spelling": "^oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 1, #toad
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RXI",
         "description": "initial short vowel spelt oo",
         "spelling": "^oo",
         "pronunciation": vowel_category["short"] ,  # u is took I think?
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RXI",
         "description": "initial uia vowel spelt oo",
         "spelling": "^oo",
         "pronunciation": vowel_category["AOU"],  # uu is noon
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""}
    ],


    "RI": [  # might be some logic for Commonwealth/United States spelling
        {"chord": "RI",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "RI",
         "description": "initial Uu vowel spelt ou", #thought
         "spelling": "^ou",
         "pronunciation": vowel_category["AU"], # bolder/boulder  thought   " starting_root  th  oo  t  suffix  f  [u]  l ",
         "ambiguity": 0,
         "orthoscore": 1, #thought
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RI",
         "description": "initial ia vowel",
         "spelling": "^ow",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RI",
         "description": "initial uie vowel spelt OU??",
         "spelling": "^ou",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": "Harri"},

        {"chord": "RI",
         "description": "initial short vowel spelt ou",
         "spelling": "^ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,  # colour
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": "Harri"},

        {"chord": "RI",
         "description": "initial ia vowel",
         "spelling": "^ou",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "RI_": [  # might be some logic for Commonwealth/United States spelling
        {"chord": "RI",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "RIU": [
        {"chord": "RIU",
         "description": "t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "RIU",
         "description": "t but Harri says ch",
         "spelling": "tt?",  # attune
         "pronunciation": " t  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "SCP",
         "description": "d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "SCP",
         "description": "d but Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "SCP",
         "description": "initial uia vowel",
         "spelling": "^e?ue?", # deuteronomy
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "SCP",
         "description": "initial uia vowel",
         "spelling": "^ou", 
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": -1, #soup
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "SCP",
         "description": "initial uia vowel",
         "spelling": "^eau",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "SCP",
         "description": "initial uia vowel",
         "spelling": "^ui",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "SCP",
         "description": "initial uia vowel",
         "spelling": "^ew",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,  # nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "SCP",
         "description": "initial uia vowel",
         "spelling": "^o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": -1, #move
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "SCP", 
         "description": "initial uia vowel",
         "spelling": "^uu", #vacuum
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "SCP", 
         "description": "initial uia vowel + another",
         "spelling": "^ui", #druid
         "pronunciation": f'{vowel_category["AOU"]} i ',
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "RIU_": [
        {"chord": "RIU",
         "description": "t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "RIU",
         "description": "t but Harri says ch",
         "spelling": "tt?",  # attune
         "pronunciation": " t  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
         
         {"chord": "SCP",
         "description": "d but Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "RU": [
        {"chord": "RU",
         "description": "m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "RU",
         "description": "intial ua vowel",
         "spelling": "^a",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RU",
         "description": "initial ua vowel",
         "spelling": "^a(a|ye?|i)",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1, # wave > waive... I take this back, maid > made, can you use AE
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RU",
         "description": "initial ua vowel (are you British?)",
         "spelling": "^e",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RU",
         "description": "initial ua vowel",
         "spelling": "^ett?e?",
         "pronunciation": vowel_category["AEU"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RU",
         "description": "initial ua vowel",
         "spelling": "^ey",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RU",
         "description": "initial ua vowel",
         "spelling": "^ei", #inveigh, weigh
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "RU",
         "description": "initial ua vowel",
         "spelling": "^ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": -1,
         "what must come before": initial_slash,
         "theory": ""},
    ],

    "RU_": [
        {"chord": "RU",
         "description": "m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],

    "X": [
        {"chord": "X",
         "description": "s",
         "spelling": "ss?",
         "pronunciation": " s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "s (maybe silent)",
         "spelling": "ss?",
         "pronunciation": " z/s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "sw silent w",  # answer 
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "ps silent p",
         # conflicts with "uppsala" but psychotic has `HOT` → `hot` because of silent h so I don't mind
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "c pronounced s or sy",  # the ce in pharmaceutical
         "spelling": "cc?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "s (maybe y too)",  # consumer
         "spelling": "s",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "s pronounced z",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "c pronounced s",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "X",
         "description": "initial e",
         "spelling": "^e",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "X",
         "description": "initial E vowel spelt ea",
         "spelling": "^ea",
         "pronunciation": vowel_category["E"],
         "ambiguity": 1,
         "orthoscore": -1,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "X",
         "description": "initial E vowel spelt ai",  # against
         "spelling": "^ai",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "X",
         "description": "initial EU vowel spelt e",  # delicious
         "spelling": "^e",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "X",
         "description": "initial E vowel", #friend
         "spelling": "^ie",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "X_": [
        {"chord": "X",
         "description": "s",
         "spelling": "ss?",
         "pronunciation": " s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "X",
         "description": "s (maybe silent)",
         "spelling": "ss?",
         "pronunciation": " z/s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "X",
         "description": "sw silent w",  # answer 
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "X",
         "description": "ps silent p",
         # conflicts with "uppsala" but psychotic has `HOT` → `hot` because of silent h so I don't mind
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "X",
         "description": "c pronounced s or sy",  # the ce in pharmaceutical
         "spelling": "cc?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "X",
         "description": "s (maybe y too)",  # consumer
         "spelling": "s",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "X",
         "description": "s pronounced z",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "X",
         "description": "c pronounced s",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "XI": [
        {"chord": "XI",
         "description": "Other languages stick w and f here, but we don't have f, and I'm sticking w on U",
         "spelling": "freeeeeeeeeeeeeeee???",
         "pronunciation": "freeeeeeeeeeee",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": "Harri"},

        {"chord": "XI",
         "description": "initial o",
         "spelling": "^o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XI",
         "description": "initial short vowel spelt ow", # Knowledge
         "spelling": "^ow",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XI",
         "description": "initial Uu vowel spelt o",
         "spelling": "^o",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #corp story
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XI",
         "description": "initial uia vowel spelt o",
         "spelling": "^o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 1, #move,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XI",
         "description": "initial O vowel spelt a",
         "spelling": "^a",
         "pronunciation": vowel_category["O"],
         "ambiguity": 1,
         "orthoscore": -1, #yacht
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "XIU": [
        {"chord": "XIU",
         "description": "k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XIU",
         "description": "c pronounced k",
         "spelling": "cc?",  # acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XIU",
         "description": "k, maybe ky",
         "spelling": "cc?",  # barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XIU",
         "description": "ch pronounced k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

         {"chord": "XIU",
         "description": "ck",
         "spelling": "ck(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XIU",
         "description": "q",
         "spelling": "c?q", #acquire
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XIU", # connection, context
         "description": "con optional std",
         "spelling": "con[std]?",
         "pronunciation": " k  (@|o|o4)  n ( [st] )?",
         "ambiguity": 10,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": "Harri"},

        {"chord": "XIU",
         "description": "g",
         "spelling": "gg?h?", #ghost can be TKPWOEFT or TKPWHOEFT
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XIU",
         "description": "initial uie vowel",
         "spelling": "^o[eu]?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XIU",
         "description": "initial uie vowel spelt ow",
         "spelling": "^owe?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XIU",
         "description": "initial uie vowel spelt au",
         "spelling": "^au",  # baudelaire, aubergine beaux,
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": -1, #aubergine
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XIU",
         "description": "initial uie vowel",
         "spelling": "^ot$",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XIU",
         "description": "initial uie vowel spelt oa",
         "spelling": "^oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "orthoscore": -1, #toad
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "XIU_": [
        {"chord": "XIU",
         "description": "k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "XIU",
         "description": "c pronounced k",
         "spelling": "cc?",  # acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "XIU",
         "description": "k, maybe ky",
         "spelling": "cc?",  # barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "XIU",
         "description": "ch pronounced k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

         {"chord": "XIU",
         "description": "ck",
         "spelling": "ck(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "XIU",
         "description": "q",
         "spelling": "c?q", #acquire
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "XIU", # connection, context
         "description": "con optional std",
         "spelling": "con[std]?",
         "pronunciation": " k  (@|o|o4)  n ( [st] )?",
         "ambiguity": 10,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": "Harri"},

        {"chord": "XIU",
         "description": "g",
         "spelling": "gg?h?", #ghost can be TKPWOEFT or TKPWHOEFT
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "XInz": [
        {"chord": "XInz",
         "description": "initial ienz vowel",
         "spelling": "oi",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XInz",
         "description": "initial ienz vowel",
         "spelling": "oye?",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 0,  # feel free to change this prioritisation
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""}
    ],


    "XU": [
        {"chord": "XU",
         "description": "n",
         "spelling": "nn?",
         "pronunciation": " n ( \[y\] )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XU",
         "description": "gn silent g",
         "spelling": "g?n",
         "pronunciation": " n ( y )?",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",
         "spelling": "^ee",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",
         "spelling": "^ie",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",
         "spelling": "^i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": -1, #Mozambique, Shiba
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",  # acne, aires
         "spelling": "^e",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #genotype
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",
         "spelling": "^ea",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #read
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel but maybe it's two syllables?",
         "spelling": "^ea",
         "pronunciation": " i@ ",
         "ambiguity": 1,
         "orthoscore": -1, #real
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",
         "spelling": "^ey",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #key
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",
         "spelling": "^oe",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #diarhoea
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "XU",
         "description": "initial ue vowel",
         "spelling": "^eo", #theory
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "XU_": [
        {"chord": "XU",
         "description": "n",
         "spelling": "nn?",
         "pronunciation": " n ( \[y\] )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "XU",
         "description": "gn silent g",
         "spelling": "g?n",
         "pronunciation": " n ( y )?",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "I": [
        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "I",
         "description": "y, but for some people it's silent???",
         "spelling": "y",
         "pronunciation": " \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "I",
         "description": "i",
         "spelling": "i",
         "pronunciation": "( suffix )? (ii|ii2|y|iy) ",  # aerospacial ← who wrote that???, fancier has a iy
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "I",
         "description": "long e?",  # meteor the second e
         "spelling": "e",
         "pronunciation": " ii2 ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "I",
         "description": "unspelt y",
         "spelling": "",
         "pronunciation": " y ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},


        #uhhh this bit is kinda weird, coincidence? On purpouse? Idk

        {"chord": "I",
         "description": "initial y pronounced i diphthong",
         "spelling": "^e?y",
         "pronunciation": " iy ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "initial ee pronounced i diphthong",
         "spelling": "^ee",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "initial ii pronounced i diphthong",
         "spelling": "^ii",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "initial ie pronounced i diphthong",
         "spelling": "^ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "initial i",
         "spelling": "^i",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "inital y",
         "spelling": "^y",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,  # honestly this might be 0
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "inital i diphthong",
         "spelling": "^i",
         "pronunciation": " iy ",
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "inital e pronounced i diphthong",  # acne, aires
         "spelling": "^e",
         "pronunciation": " iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": "Harri?"},

        {"chord": "I",
         "description": "inital ea pronounced i diphthong",
         "spelling": "^ea",
         "pronunciation": " iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": "Harri?"},

        {"chord": "I",
         "description": "inital EU vowel spelt u", #busy
         "spelling": "^u",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #busy
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "inital EU vowel spelt u", #busy
         "spelling": "^a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #garbage
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "I",
         "description": "inital EU vowel spelt ui", #build
         "spelling": "^ui?",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        #{"chord": "I", commented out because of antidisestablishmentarianism, electrocardiography
        # "description": "EU vowel spelt e",  # delicious
        # "spelling": "^e",
        # "pronunciation": vowel_category["EU"],
        # "ambiguity": 0,
        # "orthoscore": -1,
        # "what must come before": SToR_or_nothing,
        # "theory": ""},

        {"chord": "I",
         "description": "inital ue vowel spelt i",
         "spelling": "^i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": 1, #Mozambique, Shiba
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "I_": [
        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "I",
         "description": "y, but for some people it's silent???",
         "spelling": "y",
         "pronunciation": " \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "I",
         "description": "i",
         "spelling": "i",
         "pronunciation": "( suffix )? (ii|ii2|y|iy) ",  # aerospacial ← who wrote that???, fancier has a iy
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "I",
         "description": "y",
         "spelling": "y",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "I",
         "description": "long e?",  # meteor the second e
         "spelling": "e",
         "pronunciation": " ii2 ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "I",
         "description": "unspelt y",
         "spelling": "",
         "pronunciation": " y ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "IU": [
        {"chord": "IU",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "IU",
         "description": "p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "IU",
         "description": "b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "IU",
         "description": "initial ui vowel",
         "spelling": "^ie?",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "IU",
         "description": "initial ui vowel",
         "spelling": "^ei",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "IU",
         "description": "initial ui vowel",
         "spelling": "^y",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "IU",
         "description": "initial ui vowel",  # Ainu, Aida,
         "spelling": "^ai",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "IU",
         "description": "initial ui vowel followed by a short e",
         "spelling": "^ie",
         "pronunciation": vowel_category["AOEU"] + " @ ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "IU_": [
        {"chord": "IU",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "IU",
         "description": "p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "IU",
         "description": "b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "U": [
        {"chord": "U",
         "description": "w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": "Harri"},

        {"chord": "U",
         "description": "u pronounced w",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": "Harri"},

        {"chord": "U",
         "description": "long u", #poplar / popular
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "U",
         "description": "long u", #duet
         "spelling": "u",
         "pronunciation": "( suffix )? \[y\]  iu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "U",
         "description": "w pronounced v",
         "spelling": "w",
         "pronunciation": " (v|v/w) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": "Harri"},

        {"chord": "U",
         "description": "uie vowel",
         "spelling": "o",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": "Harri"}, #Lapwing

        {"chord": "U",
         "description": "u",
         "spelling": "u",
         "pronunciation": " \(y uu/w\) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series,
         "theory": ""},

        {"chord": "u",
         "description": "initial u",
         "spelling": "^u",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},

        {"chord": "u",
         "description": "initial u vowel spelt ou",
         "spelling": "^ou",
         "pronunciation": vowel_category["U"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": "Harri"},

        {"chord": "u",
         "description": "initial ou",
         "spelling": "^ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_slash,
         "theory": ""},
    ],


    "U_": [
        {"chord": "U",
         "description": "w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": "Harri"},

        {"chord": "U",
         "description": "u pronounced w",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": "Harri"},

        {"chord": "U",
         "description": "long u", #poplar / popular
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "U",
         "description": "long u", #duet
         "spelling": "u",
         "pronunciation": "( suffix )? \[y\]  iu ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},

        {"chord": "U",
         "description": "w pronounced v",
         "spelling": "w",
         "pronunciation": " (v|v/w) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": "Harri"},

        {"chord": "U",
         "description": "uie vowel",
         "spelling": "o",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": "Harri"}, #Lapwing

        {"chord": "U",
         "description": "u",
         "spelling": "u",
         "pronunciation": " \(y uu/w\) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": first_series_,
         "theory": ""},
    ],


    "Uu_": [
        {"chord": "Uu",
         "description": "Uu vowel",
         "spelling": "a[auh]?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": slash_or_first_series,
         "theory": ""},

        {"chord": "Uu",
         "description": "Uu vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 3,
         "orthoscore": -1, #thought
         "what must come before": slash_or_first_series,
         "theory": ""},

        #{"chord": "Uu",
        # "description": "Uu vowel spelt o",
        # "spelling": "o",
        # "pronunciation": vowel_category["AU"],
        # "ambiguity": 3,
        # "orthoscore": -1, #corp
        # "what must come before": F_to_N_or_nothing,
        # "theory": ""},

        {"chord": "Uu",
         "description": "au",
         "spelling": "short vowel spelt au",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": slash_or_first_series,
         "theory": ""},

        {"chord": "Uu",
         "description": "ia vowel spelt au",
         "spelling": "au",
         "pronunciation": vowel_category["OU"], #Macau
         "ambiguity": 4,
         "orthoscore": 1,
         "what must come before": slash_or_first_series,
         "theory": ""},

        {"chord": "Uu",
         "description": "Uu vowel",
         "spelling": "awe?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": slash_or_first_series,
         "theory": ""},
    ],


    "Ii_": [
        {"chord": "Ii",
         "description": "Ii vowel",
         "spelling": "oi",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": slash_or_first_series,
         "theory": ""},

        {"chord": "Ii",
         "description": "Ii vowel",
         "spelling": "oye?",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 4,  # feel free to change this prioritisation
         "orthoscore": 0,
         "what must come before": slash_or_first_series,
         "theory": ""}
    ],


    "u": [
        {"chord": "u",
         "description": "u",
         "spelling": "u",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "u",
         "description": "U vowel spelt ou",
         "spelling": "ou",
         "pronunciation": vowel_category["U"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri"},

        {"chord": "u",
         "description": "ou",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "u",
         "description": "suffix u",
         "spelling": "u",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "u",
         "description": "suffix U vowel spelt ou",
         "spelling": "ou",
         "pronunciation": " suffix " + vowel_category["U"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri"},

        {"chord": "u",
         "description": "suffix ou",
         "spelling": "ou",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "u_": [
        {"chord": "u",
         "description": "silent u",
         "spelling": "u",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"},
    ],


    "u/_": [
        {"chord": "u",
         "description": "silent u",
         "spelling": "u",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"},
    ],


    "ui": [
        {"chord": "ui",
         "description": "ui vowel",
         "spelling": "ie?",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "ui vowel",
         "spelling": "ei",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "ui vowel",
         "spelling": "y",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "ui vowel",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "ui vowel followed by a short e",
         "spelling": "ie",
         "pronunciation": vowel_category["AOEU"] + " @ ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        #{"chord": "ui",
        # "description": "suffix ui vowel",
        # "spelling": "i",
        # "pronunciation": f' suffix {vowel_category["AOEU"]}',
        # "ambiguity": 3,
        # "orthoscore": 0,
        # "what must come before": not_initial_slash_or_first_or_second_series_,
        # "theory": ""},

        {"chord": "ui",
         "description": "suffix ui vowel",
         "spelling": "ie?",  # acidifies
         "pronunciation": " suffix " + vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "suffix ui vowel",
         "spelling": "ei",  # acidifies
         "pronunciation": " suffix " + vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "suffix ui vowel",
         "spelling": "y",
         "pronunciation": " suffix " + vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "suffix ui vowel",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": " suffix " + vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ui",
         "description": "suffix ui vowel followed by a short e",
         "spelling": "ie",
         "pronunciation": " suffix " + vowel_category["AOEU"] + " @ ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "i": [
        {"chord": "i",
         "description": "y pronounced i diphthong",
         "spelling": "e?y",
         "pronunciation": " iy ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "ee pronounced i diphthong",
         "spelling": "ee",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "ii pronounced i diphthong",
         "spelling": "ii",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "ie pronounced i diphthong",
         "spelling": "ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "i",
         "spelling": "i",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "y",
         "spelling": "y",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,  # honestly this might be 0
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "i diphthong",
         "spelling": "i",
         "pronunciation": " iy ",
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "e pronounced i diphthong",  # acne, aires
         "spelling": "e",
         "pronunciation": " iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri?"},

        {"chord": "i",
         "description": "ea pronounced i diphthong",
         "spelling": "ea",
         "pronunciation": " iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri?"},

        {"chord": "i",
         "description": "EU vowel spelt u", #busy
         "spelling": "u",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #busy
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "EU vowel spelt a", #busy
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #garbage
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "EU vowel spelt ui", #build
         "spelling": "ui?",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
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
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix y pronounced i diphthong",
         "spelling": "e?y",
         "pronunciation": " suffix " + " iy ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix ee pronounced i diphthong",
         "spelling": "ee",
         "pronunciation": " suffix " + " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix ii pronounced i diphthong",
         "spelling": "ii",
         "pronunciation": " suffix " + " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix ie pronounced i diphthong",
         "spelling": "ie",
         "pronunciation": " suffix " + " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix i",
         "spelling": "i",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix y",
         "spelling": "y",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 1,  # honestly this might be 0
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix i diphthong",
         "spelling": "i",
         "pronunciation": " suffix " + " iy ",
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix e pronounced i diphthong",  # acne, aires
         "spelling": "e",
         "pronunciation": " suffix " + " iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri?"},

        {"chord": "i",
         "description": "suffix ea pronounced i diphthong",
         "spelling": "ea",
         "pronunciation": " suffix " + " iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri?"},

        {"chord": "i",
         "description": "suffix EU vowel spelt u", #busy
         "spelling": "u",
         "pronunciation": " suffix " + vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #busy
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix EU vowel spelt a", #busy
         "spelling": "a",
         "pronunciation": " suffix " + vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #garbage
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "i",
         "description": "suffix EU vowel spelt ui", #build
         "spelling": "ui?",
         "pronunciation": " suffix " + vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
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
         "description": "suffix ue vowel spelt i",
         "spelling": "i",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": 1, #Mozambique, Shiba
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "i_": [
        {"chord": "i",
         "description": "silent i",
         "spelling": "i",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"},
    ],


    "i/_": [
        {"chord": "i",
         "description": "silent i",
         "spelling": "i",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"},
    ],


    "ue": [
        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ee",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ie",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": -1, #Mozambique, Shiba
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",  # acne, aires
         "spelling": "e",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #genotype
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #read
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel but maybe it's two syllables?",
         "spelling": "ea",
         "pronunciation": " i@ ",
         "ambiguity": 1,
         "orthoscore": -1, #real
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "ey",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #key
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "oe",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #diarhoea
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "ue vowel",
         "spelling": "eo", #theory
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

         {"chord": "ue",
         "description": "suffix ue vowel",
         "spelling": "ee",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel",
         "spelling": "ie",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel",
         "spelling": "i",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": -1, #Mozambique, Shiba
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel",  # acne, aires
         "spelling": "e",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #genotype
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel",
         "spelling": "ea",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #read
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel but maybe it's two syllables?",
         "spelling": "ea",
         "pronunciation": " suffix " + " i@ ",
         "ambiguity": 1,
         "orthoscore": -1, #real
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel",
         "spelling": "ey",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #key
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel",
         "spelling": "oe",
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #diarhoea
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ue",
         "description": "suffix ue vowel",
         "spelling": "eo", #theory
         "pronunciation": " suffix " + vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "uie": [
        {"chord": "uie",
         "description": "uie vowel",
         "spelling": "o[eu]?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel spelt ow",
         "spelling": "owe?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel spelt au",
         "spelling": "au",  # baudelaire, aubergine beaux,
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": -1, #aubergine
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel",
         "spelling": "ot$",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "uie vowel spelt oa",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "orthoscore": -1, #toad
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "suffix uie vowel",
         "spelling": "o[eu]?",
         "pronunciation": " suffix " + vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "suffix uie vowel spelt ow",
         "spelling": "owe?",
         "pronunciation": " suffix " + vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "suffix uie vowel spelt au",
         "spelling": "au",  # baudelaire, aubergine beaux,
         "pronunciation": " suffix " + vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": -1, #aubergine
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "suffix uie vowel",
         "spelling": "ot$",
         "pronunciation": " suffix " + vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uie",
         "description": "suffix uie vowel spelt oa",
         "spelling": "oa",
         "pronunciation": " suffix " + vowel_category["OE"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "orthoscore": -1, #toad
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "ie": [
        {"chord": "ie",
         "description": "o",
         "spelling": "o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "short vowel spelt ow", # Knowledge
         "spelling": "ow",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "Uu vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #corp story
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "uia vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 1, #move,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "O vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["O"],
         "ambiguity": 1,
         "orthoscore": -1, #yacht
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "suffix o",
         "spelling": "o",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "suffix short vowel spelt ow", # Knowledge
         "spelling": "ow",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "suffix Uu vowel spelt o",
         "spelling": "o",
         "pronunciation": " suffix " + vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #corp story
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "suffix uia vowel spelt o",
         "spelling": "o",
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 1, #move,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ie",
         "description": "suffix O vowel spelt a",
         "spelling": "a",
         "pronunciation": " suffix " + vowel_category["O"],
         "ambiguity": 1,
         "orthoscore": -1, #yacht
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "ie_": [
        {"chord": "ie",
         "description": "silent o",
         "spelling": "o",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"},
    ],


    "ie/_": [
        {"chord": "ie",
         "description": "silent o",
         "spelling": "o",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"},
    ],


    "ienz": [
        {"chord": "ienz",
         "description": "ienz vowel",
         "spelling": "oi",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ienz",
         "description": "ienz vowel",
         "spelling": "oye?",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 0,  # feel free to change this prioritisation
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""}
    ],


    "e": [
        {"chord": "e",
         "description": "e",
         "spelling": "e",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "E vowel spelt ea",
         "spelling": "ea",
         "pronunciation": vowel_category["E"],
         "ambiguity": 1,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "E vowel spelt ai",  # against
         "spelling": "ai",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "EU vowel spelt e",  # delicious
         "spelling": "e",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "E vowel", #friend
         "spelling": "ie",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "suffix e",
         "spelling": "e",
         "pronunciation": " suffix " +vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "suffix E vowel spelt ea",
         "spelling": "ea",
         "pronunciation": " suffix " +vowel_category["E"],
         "ambiguity": 1,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "suffix E vowel spelt ai",  # against
         "spelling": "ai",
         "pronunciation": " suffix " +vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "suffix EU vowel spelt e",  # delicious
         "spelling": "e",
         "pronunciation": " suffix " +vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "e",
         "description": "suffix E vowel", #friend
         "spelling": "ie",
         "pronunciation": " suffix " + vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "e_": [
        {"chord": "e",
         "description": "silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"}
    ],


    "e/_": [
        {"chord": "e",
         "description": "silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,
         "theory": "Harri"}
    ],


    "ua": [
        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "a",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "a(a|ye?|i)",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1, # wave > waive... I take this back, maid > made, can you use AE
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel (are you British?)",
         "spelling": "e",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ett?e?",
         "pronunciation": vowel_category["AEU"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ey",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ei", #inveigh, weigh
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "ua vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        #{"chord": "ua",
        # "description": "suffix ua vowel",
        # "spelling": "a",
        # "pronunciation": f' suffix {vowel_category["AEU"]}',
        # "ambiguity": 3,
        # "orthoscore": 0,
        # "what must come before": not_initial_slash_or_first_or_second_series_,
        # "theory": ""},

         {"chord": "ua",
         "description": "suffix ua vowel",
         "spelling": "a",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "suffix ua vowel",
         "spelling": "a(a|ye?|i)",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1, # wave > waive... I take this back, maid > made, can you use AE
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "suffix ua vowel (are you British?)",
         "spelling": "e",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "suffix ua vowel",
         "spelling": "ett?e?",
         "pronunciation": vowel_category["AEU"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "suffix ua vowel",
         "spelling": "ey",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "suffix ua vowel",
         "spelling": "ei", #inveigh, weigh
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ua",
         "description": "suffix ua vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": -1,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        #{"chord": "ua",
        # "description": "suffix ua vowel",
        # "spelling": "a",
        # "pronunciation": f' suffix {vowel_category["AEU"]}',
        # "ambiguity": 3,
        # "orthoscore": 0,
        # "what must come before": not_initial_slash_or_first_or_second_series_,
        # "theory": ""},
    ],


    "uia": [
        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "e?ue?", # deuteronomy
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "ou", 
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": -1, #soup
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "eau",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "ui",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "ew",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,  # nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "uia vowel",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": -1, #move
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia", 
         "description": "uia vowel",
         "spelling": "uu", #vacuum
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia", 
         "description": "uia vowel + another",
         "spelling": "ui", #druid
         "pronunciation": f'{vowel_category["AOU"]} i ',
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

         {"chord": "uia",
         "description": "suffix uia vowel",
         "spelling": "e?ue?", # deuteronomy
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "suffix uia vowel",
         "spelling": "ou", 
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": -1, #soup
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "suffix uia vowel",
         "spelling": "eau",
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "suffix uia vowel",
         "spelling": "ui",
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "suffix uia vowel",
         "spelling": "ew",
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 1,  # nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia",
         "description": "suffix uia vowel",
         "spelling": "o",
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": -1, #move
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia", 
         "description": "suffix uia vowel",
         "spelling": "uu", #vacuum
         "pronunciation": " suffix " + vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "uia", 
         "description": "suffix uia vowel + another",
         "spelling": "ui", #druid
         "pronunciation": " suffix " + f'{vowel_category["AOU"]} i ',
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "ia": [
        {"chord": "ia",
         "description": "Uu vowel spelt ou", #thought
         "spelling": "ou",
         "pronunciation": vowel_category["AU"], # bolder/boulder  thought   " starting_root  th  oo  t  suffix  f  [u]  l ",
         "ambiguity": 0,
         "orthoscore": 1, #thought
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ia",
         "description": "ia vowel",
         "spelling": "ow",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ia",
         "description": "uie vowel spelt OU??",
         "spelling": "ou",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri"},

        {"chord": "ia",
         "description": "short vowel spelt ou",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,  # colour
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri"},

        {"chord": "ia",
         "description": "ia vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ia",
         "description": "suffix Uu vowel spelt ou", #thought
         "spelling": "ou",
         "pronunciation": " suffix " + vowel_category["AU"], # bolder/boulder  thought   " starting_root  th  oo  t  suffix  f  [u]  l ",
         "ambiguity": 0,
         "orthoscore": 1, #thought
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ia",
         "description": "suffix ia vowel",
         "spelling": "ow",
         "pronunciation": " suffix " + vowel_category["OU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "ia",
         "description": "suffix uie vowel spelt OU??",
         "spelling": "ou",
         "pronunciation": " suffix " + vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri"},

        {"chord": "ia",
         "description": "suffix short vowel spelt ou",
         "spelling": "ou",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 0,  # colour
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": "Harri"},

        {"chord": "ia",
         "description": "suffix ia vowel",
         "spelling": "ou",
         "pronunciation": " suffix " + vowel_category["OU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "iea": [
        {"chord": "iea",
         "description": "Uu vowel spelt ao",
         "spelling": "oa",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #coarse
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "iea",
         "description": "uie vowel spelt oa",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 1, #toad
         "what must come before": initial_first_or_second_series,
         "theory": ""},

        {"chord": "iea",
         "description": "short vowel spelt oo",
         "spelling": "oo",
         "pronunciation": vowel_category["short"] ,  # u is took I think?
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "iea",
         "description": "uia vowel spelt oo",
         "spelling": "oo",
         "pronunciation": vowel_category["AOU"],  # uu is noon
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "iea",
         "description": "suffix Uu vowel spelt ao",
         "spelling": "oa",
         "pronunciation": " suffix " + vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #coarse
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "iea",
         "description": "suffix uie vowel spelt oa",
         "spelling": "oa",
         "pronunciation": " suffix " + vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 1, #toad
         "what must come before": initial_first_or_second_series,
         "theory": ""},

        {"chord": "iea",
         "description": "suffix short vowel spelt oo",
         "spelling": "oo",
         "pronunciation": " suffix " + vowel_category["short"] ,  # u is took I think?
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "iea",
         "description": "suffix uia vowel spelt oo",
         "spelling": "oo",
         "pronunciation": " suffix " + vowel_category["AOU"],  # uu is noon
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "ea": [
        {"chord": "ea",
         "description": "ue vowel spelt ea (first stroke only)",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"], #it was just ii before
         "ambiguity": 1,
         "orthoscore": 1, #read
         "what must come before": initial_first_or_second_series,
         "theory": ""},

        {"chord": "ea",
         "description": "ea pronounced short e (first stroke only)",
         "spelling": "ea",
         "pronunciation": " e ", # earl?
         "ambiguity": 2, #red
         "orthoscore": 1, #read
         "what must come before": initial_first_or_second_series,
         "theory": ""},

        {"chord": "ea",
         "description": "ua vowel spelt ea (first stroke only)",
         "spelling": "e", # made
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": 1,
         "what must come before": initial_first_or_second_series,
         "theory": ""},

        {"chord": "ea",
         "description": "ue vowel spelt ae",
         "spelling": "ae",
         "pronunciation": vowel_category["AOE"], # eir?
         "ambiguity": 3, # made > mead
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        #{"chord": "ea",
        # "description": "suffix ue vowel spelt ea (first stroke only)",
        # "spelling": "ea",
        # "pronunciation": vowel_category["AOE"], #it was just ii before
        # "ambiguity": 1,
        # "orthoscore": 1, #read
        # "what must come before": initial_first_or_second_series,
        # "theory": ""},

        #{"chord": "ea",
        # "description": "suffix ea pronounced short e (first stroke only)",
        # "spelling": "ea",
        # "pronunciation": " e ", # earl?
        # "ambiguity": 2, #red
        # "orthoscore": 1, #read
        # "what must come before": initial_first_or_second_series,
        # "theory": ""},

        #{"chord": "ea",
        # "description": "suffix ua vowel spelt ea (first stroke only)",
        # "spelling": "e", # made
        # "pronunciation": vowel_category["AEU"],
        # "ambiguity": 2,
        # "orthoscore": 1,
        # "what must come before": initial_first_or_second_series,
        # "theory": ""},

        {"chord": "ea",
         "description": "suffix ue vowel spelt ae",
         "spelling": "ae",
         "pronunciation": " suffix " + vowel_category["AOE"], # eir?
         "ambiguity": 3, # made > mead
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "a": [
        {"chord": "a",
         "description": "short a",
         "spelling": "a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "a",
         "description": "short a", #villain... but not against?
         "spelling": "ai",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "a",
         "description": "EU vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "a",
         "description": "suffix short a",
         "spelling": "a",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "a",
         "description": "suffix short a", #villain... but not against?
         "spelling": "ai",
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},

        {"chord": "a",
         "description": "suffix EU vowel spelt a",
         "spelling": "a",
         "pronunciation": " suffix " + vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": not_initial_slash_or_first_or_second_series_,
         "theory": ""},
    ],


    "a_": [
        {"chord": "a",
         "description": "silent a",
         "spelling": "a",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,  # guard shouldn't be "drop vowel, silent a"
         "theory": "Harri"},
    ],


    "a/_": [
        {"chord": "a",
         "description": "silent a",
         "spelling": "a",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_before_slash_or_first_or_second_series,  # guard shouldn't be "drop vowel, silent a"
         "theory": "Harri"},
    ],


    "n": [
        {"chord": "n",
         "description": "n",
         "spelling": "o?ne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "n",
         "description": "n", #gin
         "spelling": "o?nne?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "n",
         "description": "suffix -n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "n",
         "description": "gn silent g",
         "spelling": "gne?",
         "pronunciation": " n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "p": [
        {"chord": "p",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0, #group > groupe
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "p",
         "description": "p",
         "spelling": "pp?e",
         "pronunciation": " p ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""}
    ],


    "nz": [
        {"chord": "nz",
         "description": "y pronounced i diphthong",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "nz",
         "description": "y pronounced i diphthong",
         "spelling": "ie?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "nz",
         "description": "y pronounced i",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "nz",
         "description": "dy",
         "spelling": "dd?(y|ie?)",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "HelloChap?"}
    ],


    "pz": [
        {"chord": "pz",
         "description": "j",
         "spelling": "d?je?",
         "pronunciation": " jh ",
         "ambiguity": 1, #Why 1? not 0?
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pz",
         "description": "g pronounced j",
         "spelling": "d?gg?e?",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pz",
         "description": "zh sound",
         "spelling": "(j|dj|d?gg?)e?",
         "pronunciation": " zh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""}
    ],  # arbitrage


    "z": [
        {"chord": "z",
         "description": "s voiced",
         "spelling": "se?",
         "pronunciation": " z ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "z",
         "description": "s (maybe voiced)",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "z",
         "description": "ss voiced",
         "spelling": "sse?",  # actresses?"
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         # cyclops
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],

 
    "nc": [
        {"chord": "nc",
         "description": "w????",
         "spelling": "ww?",
         "pronunciation": "( w | hw )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "pc": [
        {"chord": "pc",
         "description": "k",
         "spelling": "k(k|e)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pc",
         "description": "ck",
         "spelling": "cke?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pc",
         "description": "ch pronounced k",
         "spelling": "che?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pc",
         "description": "ch pronounced x",
         "spelling": "che?",
         "pronunciation": " x ",
         "ambiguity": 2, #lock/loch
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "Harri"},

        {"chord": "pc",
         "description": "lk silent l??)",
         "spelling": "lk",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pc",
         "description": "c pronounced k",
         "spelling": "c(c|e)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pc",
         "description": "qu",
         "spelling": "que?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "pc/S": [
        {"chord": "pc/S",
         "description": "x (sorry, too lazy for g+z)",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "pc/SP": [
        {"chord": "pc/SP",
         "description": "x (sorry, too lazy for g+zh)",
         "spelling": "xi?",
         "pronunciation": "( k  sh | g  zh )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "c": [
        {"chord": "c",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "c",
         "description": "ci pronounced sh (Harri's accent)",  # aerospacial
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "c",
         "description": "sh sound",
         "spelling": "((s|t|x)i|c[ei]|s?che?|sc|ss)",
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "c",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "ns": [
        {"chord": "ns",
         "description": "ng",
         "spelling": "ng?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ns",
         "description": "ngue", #tongue
         "spelling": "ngue",
         "pronunciation": " ng ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ns",
         "description": "ng with g",
         "spelling": "ng",
         "pronunciation": " ng ( \[?g\]? )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ns",
         "description": "'nge' in 'singe'",
         # funny example cause of course `SEUPBG` → `sing`, but `ORPBG` → `orange`
         "spelling": "nge?",
         "pronunciation": " n  jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ns",
         "description": "ng sound then g sound",
         "spelling": "ng?",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""}
    ],


    "ps": [
        {"chord": "ps",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ps",
         "description": "tch",
         "spelling": "tch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ps",
         "description": "ch spelt t",
         "spelling": "t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "nzs": [
        {"chord": "nzs",
         "description": "x",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "nzs",
         "description": "ction",
         "spelling": "ction",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "nzs",
         "description": "cation",
         "spelling": "cation",
         "pronunciation": " k  ee  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "Harri"}
    ],


    "pzs": [
        {"chord": "pzs",
         "description": "m",
         "spelling": "mm?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pzs",
         "description": "mb silent b",
         "spelling": "mb",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pzs",
         "description": "mp silent p",
         "spelling": "mp",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pzs",
         "description": "mn silent n",
         "spelling": "mn",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
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
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "ncs": [
        {"chord": "ncs",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncs",
         "description": "le",
         "spelling": "ll?e",
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncs",
         "description": "el",
         "spelling": "ell?e?", #I added the final ? cause it looked wrong without it?
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncs",
         "description": "al",
         "spelling": "all?e?",
         "pronunciation": " @  l ",  # silent a is already a thing
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncs",
         "description": "suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncs",
         "description": "suffix -l",  # antibacterial
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "pcs": [
        {"chord": "pcs",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pcs",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pcs",
         "description": "suffix -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""}
    ],


    "cs": [
        {"chord": "cs",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "cs",
         "description": "rv",
         "spelling": "rve?",
         "pronunciation": " r  v ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "Harri"}
    ],


    "s": [
        {"chord": "s",
         "description": "unvoiced se",
         "spelling": "se",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "s",
         "description": "unvoiced s", #cyclops
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "s",
         "description": "s (maybe voiced)",
         "spelling": "s",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "s",
         "description": "s silent t",
         "spelling": "ss?te?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "s",
         "description": "s silent w",  # answer
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "s",
         "description": "ss",
         "spelling": "unvoiced ss",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "s",
         "description": "unvoiced s spelt c",
         "spelling": "s?ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "s",
         "description": "s maybe voiced",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
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
        {"chord": "nf",
         "description": "nd",
         "spelling": "ndd?",
         "pronunciation": " n  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "pcf": [
        {"chord": "pcf",
         "description": "b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "cf": [
        {"chord": "cf",
         "description": "h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "cf",
         "description": "silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},


        {"chord": "cf",
         "description": "st!",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "pf": [
        {"chord": "pf",
         "description": "t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pf",
         "description": "final dt pronounced t",
         "spelling": "dt$",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pf",
         "description": "t pronounced sh",
         "spelling": "tt?e?",
         "pronunciation": " sh ",
         "ambiguity": 2,  # so it doesn't win against abtentious
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pf",
         "description": "ti pronounced ch", #congestion
         "spelling": "ti",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pf", #variability
         "description": "suffix ity",
         "spelling": "ity",
         "pronunciation": " suffix  @  t  iy ",
         "ambiguity": 4, #ambiguity, versatility
         "orthostore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""}
    ],


    "nzf": [
        {"chord": "nzf",
         "description": "nt",
         "spelling": "nt",
         "pronunciation": " n ( root )? t ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "pzf": [
        {"chord": "pzf",
         "description": "g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "pzf",
         "description": "silent gh",
         "spelling": "gh",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "Harri"},
    ],


    "zf": [
        {"chord": "zf",
         "description": "th",
         "spelling": "the?",
         "pronunciation": " \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "zf",
         "description": "suffix -th",
         "spelling": "the?",
         "pronunciation": " suffix  \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],


    "ncf": [
        {"chord": "ncf",
         "description": "r",
         "spelling": "rr?e?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix? -re",
         "spelling": "re",
         "pronunciation": "( suffix )? (\(r  @/@r  r\)|@r  r) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix -r??", #secret
         "spelling": "r",
         "pronunciation": "( suffix ) r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "ncf",
         "description": "suffix -er",
         "spelling": "err?",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "Harri"},

        {"chord": "ncf",
         "description": "ar???",
         "spelling": "arr?",  # friar
         "pronunciation": " r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "Harri"},

        {"chord": "ncf",
         "description": "suffix -or/-our???",
         "spelling": "ou?rr?",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": "Harri"}
    ],


    "f": [
        {"chord": "f",
         "description": "f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "f",
         "description": "ph pronounced f",  # graph
         "spelling": "p?ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},

        {"chord": "f",
         "description": "gh pronounced f",  # laugh
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": consonanted_consonant_OR_initial_second_OR_third_,
         "theory": ""},
    ],



    ##now to dupe everything below, but make it pressable as a second final




































































































































































































    "/n": [
        {"chord": "/n",
         "description": "final n",
         "spelling": "o?ne?$",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/n",
         "description": "final n", #gin
         "spelling": "o?nne?$",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/n",
         "description": "final suffix -n",
         "spelling": "n$",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "?"},

        {"chord": "/n",
         "description": "final gn silent g",
         "spelling": "gne?$",
         "pronunciation": " n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/p": [
        {"chord": "/p",
         "description": "final p",
         "spelling": "pp?$",
         "pronunciation": " p ",
         "ambiguity": 0, #group > groupe
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/p",
         "description": "final p",
         "spelling": "pp?e$",
         "pronunciation": " p ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""}
    ],


    "/nz": [
        {"chord": "/nz",
         "description": "final y pronounced i diphthong",
         "spelling": "y$",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},

        {"chord": "/nz",
         "description": "final y pronounced i diphthong",
         "spelling": "ie?$",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},

        {"chord": "/nz",
         "description": "final y pronounced i",
         "spelling": "y$",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/nz",
         "description": "final dy",
         "spelling": "dd?(y|ie?)$",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "HelloChap?"}
    ],


    "/pz": [
        {"chord": "/pz",
         "description": "final j",
         "spelling": "d?je?$",
         "pronunciation": " jh ",
         "ambiguity": 1, #Why 1? not 0?
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pz",
         "description": "final g pronounced j",
         "spelling": "d?gg?e?$",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pz",
         "description": "final zh sound",
         "spelling": "(j|dj|d?gg?)e?$",
         "pronunciation": " zh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""}
    ],  # arbitrage


    "/z": [
        {"chord": "/z",
         "description": "final s voiced",
         "spelling": "se?$",
         "pronunciation": " z ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/z",
         "description": "final s (maybe voiced)",
         "spelling": "ss?e?$",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/z",
         "description": "final ss voiced",
         "spelling": "sse?$",  # actresses?"
         "pronunciation": " z ",
         "ambiguity": 1,
         "orthoscore": 0,
         # cyclops
         "what must come before": fourth_series,
         "theory": ""},
    ],

 
    "/nc": [
        {"chord": "/nc",
         "description": "final w????",
         "spelling": "ww?$",
         "pronunciation": "( w | hw )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/pc": [
        {"chord": "/pc",
         "description": "final k",
         "spelling": "k(k|e)?$",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "?"},

        {"chord": "/pc",
         "description": "final ck",
         "spelling": "cke?$",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pc",
         "description": "final ch pronounced k",
         "spelling": "che?$",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "?"},

        {"chord": "/pc",
         "description": "final ch pronounced x",
         "spelling": "che?$",
         "pronunciation": " x ",
         "ambiguity": 2, #lock/loch
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "Harri"},

        {"chord": "/pc",
         "description": "final lk silent l??)",
         "spelling": "lk$",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pc",
         "description": "final c pronounced k",
         "spelling": "c(c|e)?$",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pc",
         "description": "final qu",
         "spelling": "que?$",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "pc/S": [
        {"chord": "/pc/S",
         "description": "final x (sorry, too lazy for g+z)",
         "spelling": "x$",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "pc/SP": [
        {"chord": "/pc/SP",
         "description": "final x (sorry, too lazy for g+zh)",
         "spelling": "xi?$",
         "pronunciation": "( k  sh | g  zh )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/c": [
        {"chord": "/c",
         "description": "final sh",
         "spelling": "sh$",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/c",
         "description": "final ci pronounced sh (Harri's accent)",  # aerospacial
         "spelling": "ci$",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/c",
         "description": "final sh sound",
         "spelling": "((s|t|x)i|c[ei]|s?che?|sc|ss)$",
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/c",
         "description": "final zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)$", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/ns": [
        {"chord": "/ns",
         "description": "final ng",
         "spelling": "ng?$",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ns",
         "description": "final ngue", #tongue
         "spelling": "ngue$",
         "pronunciation": " ng ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ns",
         "description": "final ng with g",
         "spelling": "ng$",
         "pronunciation": " ng ( \[?g\]? )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ns",
         "description": "final 'nge' in 'singe'",
         # funny example cause of course `SEUPBG` → `sing`, but `ORPBG` → `orange`
         "spelling": "nge?$",
         "pronunciation": " n  jh ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ns",
         "description": "final ng sound then g sound",
         "spelling": "ng?$",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""}
    ],


    "/ps": [
        {"chord": "/ps",
         "description": "final ch",
         "spelling": "ch$",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "?"},

        {"chord": "/ps",
         "description": "final tch",
         "spelling": "tch$",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ps",
         "description": "final ch spelt t",
         "spelling": "t$",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/nzs": [
        {"chord": "/nzs",
         "description": "final x",
         "spelling": "x$",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/nzs",
         "description": "final ction",
         "spelling": "ction$",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/nzs",
         "description": "final cation",
         "spelling": "cation$",
         "pronunciation": " k  ee  sh  suffix  n ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "Harri"}
    ],


    "/pzs": [
        {"chord": "/pzs",
         "description": "final m",
         "spelling": "mm?e?$",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pzs",
         "description": "final mb silent b",
         "spelling": "mb$",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pzs",
         "description": "final mp silent p",
         "spelling": "mp$",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pzs",
         "description": "final mn silent n",
         "spelling": "mn$",
         "pronunciation": " m ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        #{"chord": "/pzs",
        # "description": "final lm silent l (has to follow AU)",
        # "spelling": "lm$",
        # "pronunciation": "( \[l1\] )? m ",
        # "ambiguity": 0,
        # "orthoscore": 0,
        # "what must come before": Au, #balm
        # "theory": ""},
    ],


    "/zs": [
        {"chord": "/zs",
         "description": "final rd",
         "spelling": "rdd?$",
         "pronunciation": " r  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/ncs": [
        {"chord": "/ncs",
         "description": "final l",
         "spelling": "ll?$",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ncs",
         "description": "final le",
         "spelling": "ll?e$",
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ncs",
         "description": "final el",
         "spelling": "ell?e?$", #I added the final ? cause it looked wrong without it?
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ncs",
         "description": "final al",
         "spelling": "all?e?$",
         "pronunciation": " @  l ",  # silent a is already a thing
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ncs",
         "description": "final suffix -al",
         "spelling": "al$",
         "pronunciation": " suffix  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},

        {"chord": "/ncs",
         "description": "final suffix -l",  # antibacterial
         "spelling": "l$",
         "pronunciation": " suffix  l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},
    ],


    "/pcs": [
        {"chord": "/pcs",
         "description": "final d",
         "spelling": "dd?e?$",
         "pronunciation": " d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pcs",
         "description": "final d",
         "spelling": "dd?e?$",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pcs",
         "description": "final suffix -ed",
         "spelling": "e?d$",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""}
    ],



    "/cs": [
        {"chord": "/cs",
         "description": "final v",
         "spelling": "ve?$",
         "pronunciation": " v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/cs",
         "description": "final v",
         "spelling": "rve?$",
         "pronunciation": " v ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "Harri"}
    ],


    "/s": [
        {"chord": "/s",
         "description": "final unvoiced se",
         "spelling": "se$",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/s",
         "description": "final unvoiced s", #cyclops
         "spelling": "s$",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/s",
         "description": "final s (maybe voiced)",
         "spelling": "s$",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/s",
         "description": "final s silent t",
         "spelling": "ss?te?$",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/s",
         "description": "final s silent w",  # answer
         "spelling": "sw$",
         "pronunciation": " s ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/s",
         "description": "final ss",
         "spelling": "unvoiced ss$",  # actresses?"
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/s",
         "description": "final unvoiced s spelt c",
         "spelling": "s?ce?$",
         "pronunciation": " s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/s",
         "description": "final s maybe voiced",
         "spelling": "ss?e?$",
         "pronunciation": " z/s ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},


        {"chord": "/s",
         "description": "final suffix -s",
         "spelling": "s$",
         "pronunciation": "( (suffix) ) (s|z|z/s) ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""}
    ],

    "/nf": [
        {"chord": "/nd",
         "description": "final nd",
         "spelling": "ndd?$",
         "pronunciation": " n  d ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],

    "/pcf": [
        {"chord": "/pcf",
         "description": "final b",
         "spelling": "bb?e?$",
         "pronunciation": " b ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/cf": [
        {"chord": "/cf",
         "description": "final h",
         "spelling": "h$",
         "pronunciation": " h ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/cf",
         "description": "final silent h",
         "spelling": "h$",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},


        {"chord": "/cf",
         "description": "final st!",
         "spelling": "st$",
         "pronunciation": " s  t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/pf": [
        {"chord": "/pf",
         "description": "final t",
         "spelling": "tt?e?$",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pf",
         "description": "final final dt pronounced t",
         "spelling": "dt$$",
         "pronunciation": " t ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pf",
         "description": "final t pronounced sh",
         "spelling": "tt?e?$",
         "pronunciation": " sh ",
         "ambiguity": 2,  # so it doesn't win against abtentious
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pf",
         "description": "final ti pronounced ch", #congestion
         "spelling": "ti$",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pf", #variability
         "description": "final suffix ity",
         "spelling": "ity$",
         "pronunciation": " suffix  @  t  iy ",
         "ambiguity": 3, #ambiguity, versatility
         "orthostore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""}
    ],


    "/nzf": [
        {"chord": "/nzf",
         "description": "final nt",
         "spelling": "nt$",
         "pronunciation": " n ( root )? t ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],


    "/pzf": [
        {"chord": "/pzf",
         "description": "final g",
         "spelling": "gg?e?$",
         "pronunciation": " g ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/pzf",
         "description": "final silent gh",
         "spelling": "gh$",
         "pronunciation": "",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "Harri"},
    ],


    "/zf": [
        {"chord": "/zf",
         "description": "final th",
         "spelling": "the?$",
         "pronunciation": " \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/zf",
         "description": "final suffix -th",
         "spelling": "the?$",
         "pronunciation": " suffix  \[?(th|dh|dh/th)\]? ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},
    ],


    "/ncf": [
        {"chord": "/ncf",
         "description": "final r",
         "spelling": "rr?e?$",
         "pronunciation": " r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/ncf",
         "description": "final suffix? -re",
         "spelling": "re$",
         "pronunciation": "( suffix )? (\(r  @/@r  r\)|@r  r) ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},

        {"chord": "/ncf",
         "description": "final suffix -r??", #secret
         "spelling": "r$",
         "pronunciation": "( suffix ) r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": ""},

        {"chord": "/ncf",
         "description": "final suffix -er",
         "spelling": "err?$",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": "Harri"},

        {"chord": "/ncf",
         "description": "final ar???",
         "spelling": "arr?$",  # friar
         "pronunciation": " r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "Harri"},

        {"chord": "/ncf",
         "description": "final suffix -or/-our???",
         "spelling": "ou?rr?$",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": initial_second_series_or_third_or_fourth,
         "theory": "Harri"}
    ],


    "/f": [
        {"chord": "/f",
         "description": "final f",
         "spelling": "ff?e?$",
         "pronunciation": " f ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},

        {"chord": "/f",
         "description": "final ph pronounced f",  # graph
         "spelling": "p?ph$",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": "?"},

        {"chord": "/f",
         "description": "final gh pronounced f",  # laugh
         "spelling": "gh$",
         "pronunciation": " f ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": fourth_series,
         "theory": ""},
    ],






















































































# Suffixes
















}