import re


try:
    from Froj_theories.Mussel_Power.vowel_categories import vowel_category
except ModuleNotFoundError:
    # Allow running as a script
    from vowel_categories import vowel_category


custom_alphabet = "QSTKPWHR-AOeufrpblgtsdz*_1"
valid_final_letter = r'[AOeufrpblgtsdz]\*?$'


"FSCZPN|RXIU|uiea|npzcsf|_"


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

A_to_z_or_nothing_at_all = re.compile(r'(.*[\-AOeufrpblgtsdz])?\*?$')
# NothingRegex = re.compile(r'')
# AtLeastOneCharacterRegex = re.compile(r'.+')
skipsAnEUInTheVowels_no_r = re.compile(r'[/QSTKPWHR][AO][fpblgtsdz]+\*?$')
unavailable_e_no_r = re.compile(r'[/QSTKPWHR]([AO]*[eu]|AO)+[fpblgtsdz]*\*?$')  # fire

available_e_unavailable_r = re.compile(r'[AO]+f?r[pblgtsdz]*\*?$')  # former farmer
unavailable_e_unavailable_r_no_asterisk = re.compile(r'[AO][eu]+f?rp?b?l?g?t?s?d?z?$')


A_to_g_yes_b_or_g = re.compile(r'[\-AOeufrp][bg][lg]*\*?$')
l_to_z_no_f = re.compile(r'[\-AOeu][rpb]*[lgtsdz]+\*?$')
l_to_z_no_porb = re.compile(r'[\-AOeu]r?[lgtsdz]+\*?$')
p_or_l_to_z = re.compile(r'[\-AOeu][plgtsdz]+\*?$')
A_to_z_no_r = re.compile(r'[\-AOeu][fpblgtsdz]*\*?_?$')

after_f = re.compile(r'[rpblgtsdz]\*?$')
after_r = re.compile(r'[pblgtsdz]\*?$')
after_l_no_l = re.compile(r'/[QSTKPWHRAO\-eufrpb]+[gtsdz]+\*?$')
after_l_no_asterisk_or_l = re.compile(r'/[QSTKPWHRAO\-eufrpb]+[gtsdz]+$')
after_g_no_g = re.compile(r'/[QSTKPWHRAO\-eufrpbl]+[tsdz]\*?$')

ends_in_r = re.compile(r'r\*?$')
ends_in_t = re.compile(r't\*?$')
ends_in_b_to_t_no_asterisk = re.compile(r'[blgt]_?$')  # against
ends_in_g_to_t_no_asterisk = re.compile(r'[gt]\*?$')
ends_in_d_no_asterisk = re.compile(r'd$')
ends_in_d_no_asterisk_no_t = re.compile(r'[AO\-eufrpblg]d$')

any_letter_or_nothing = re.compile(r'(^/|[QSTKPWHRAO\-eufrpblgtsdz])$')
#any_letter_but_not_KWH = re.compile(r'((/(?!KWH$)[QSTKPWHR])|[AO\-eufrpblgtsdz])\*?$')
any_consonant = re.compile(r'[STKPWHRfrpblgtsdz]\*?$')
any_consonant_but_not_KWH = re.compile(r'(/(?!KWH$)[STKPWHR]+|[frpblgtsdz])\*?_?$')  # (?! is for negative lookahead
SToR_but_not_KWH = re.compile(r'/(?!KWH$)[STKPWHR]+\*?$')  # (?! is for negative lookahead  no _ because the cheeky little `TKPWEUPBG` → "going"

A_then_vowels_that_make_asterisk_plus_d_not_usable = re.compile(r'A([frpblgt]*[sdz]+|\*[frpblgtsdz]+)$')

g_and_dz = re.compile(r'g[ts]*[dz]+\*?$')

first_slash = re.compile(r'^/$')
slash_no_asterisk = re.compile(r'/_?$')
slash_no_asterisk_no__ = re.compile(r'/$')
slash_or_T = re.compile(r'/T?$')


just_KWH = re.compile(r'/KWH$')

slash = re.compile(r'/\*?_?$')
upToQ = re.compile(r'[/Q]\*?_?$')
upToS = re.compile(r'[/QS]\*?_?$')
upToT = re.compile(r'[/QST]\*?_?$')
upToK = re.compile(r'[/QSTK]\*?_?$')
upToP = re.compile(r'[/QSTKP]\*?_?$')
upToW = re.compile(r'[/QSTKPW]\*?_?$')
upToH = re.compile(r'[/QSTKPWH]\*?_?$')
upToR = re.compile(r'[/QSTKPWHR]\*?_?$')


upToQ_or_W = re.compile(r'[/QW]\*?_?$')

upToK_not_just_K = re.compile(r'(/|[QST]K?)\*?_?$')

SToR = re.compile(r'[STKPWHR]\*?$')
SToR_ = re.compile(r'[STKPWHR]\*?_?$')
SToK = re.compile(r'[STK]\*?_?$')

SToR_but_not_a_vowel_before = re.compile(r'([FRPBLGTSDZ]/KWH|([STKPR]H?|W))\*?$')

SToR_or_nothing = re.compile(r'(^/|[STKPWHR]\*?|/\*)$')  # or just an asterisk for compound words
# I'm getting rid of _? because "against"

upToK_no_T = re.compile(r'[/QS]K?\*?_?$')  # _? for #PWAOUD/PEFT
upToK_no_S = re.compile(r'[/Q]T?K?\*?$')

upToW_not_just_T_not_just_k_or_just_w = re.compile(r'([STKPW]{2,}|[/QSKP])\*?_?$')  # clink    _? for baudelair

upToW_not_just_s = re.compile(r'([/QTKPW]S?|[/QTKP]H)\*?_?$')  # yes _ because actresses drops a boundary after t
upToH_not_just_s_or_sh_not_KWH = re.compile(r'([/QTKP]H?|W)\*?_?$')  # yes _ because actresses drops a boundary after t          shh

upToW_no_T = re.compile(r'[/QS]K?P?W?\*?$')
upToW_no_P = re.compile(r'[/QSTK](P?W)?\*?$') #`PWHOELD` → `behold` needs a p

first_stroke_SToR_or_nothing = re.compile(r'^/[STKPWHR]*$')

H_to_R_no_W = re.compile(r'[/QSTKP][HR]+\*?_?$')

A_to_u = re.compile(r'[\-AOeu]\*?$')
A_to_f = re.compile(r'[\-AOeuf]\*?$')
A_to_r = re.compile(r'[\-AOeufr]\*?$')
A_to_p = re.compile(r'[\-AOeufrp]\*?$')
A_to_b = re.compile(r'[\-AOeufrpb]\*?$')
A_to_l = re.compile(r'[\-AOeufrpbl]\*?$')
A_to_g = re.compile(r'[\-AOeufrpblg]\*?$')
A_to_t = re.compile(r'[\-AOeufrpblgt]\*?$')
A_to_s = re.compile(r'[\-AOeufrpblgts]\*?$')
A_to_d = re.compile(r'[\-AOeufrpblgtsd]\*?$')
A_to_z = re.compile(r'[\-AOeufrpblgtsdz]\*?$')
A_to_z_no_dash = re.compile(r'[AOeufrpblgtsdz]\*?$')

A_to_u_or__ = re.compile(r'[\-AOeu]([frpblgt]+_)?\*?$')

A_to_z_no_pbs = re.compile(r'[\-AOeufr][lgtdz]+\*?$')
A_to_z_no_plt = re.compile(r'[\-AOeufr][bgsdz]+\*?$')
A_to_t_no_g_end = re.compile(r'[\-AOeufrpbl]+(pblg)?(g?t)?\*?$')
A_to_d_no_t = re.compile(r'[\-AOeufrpblgs]+d?\*?$')
A_to_g_yes_t = re.compile(r'[\-AOeufrpblg]t\*?$')
yes_s = re.compile(r's\*?$')

Au = re.compile(r'Au\*?$')  # it can be in compound words
A_to_u_ = re.compile(r'[\-AOeu]\*?_?$')
A_to_f_ = re.compile(r'[\-AOeuf]\*?_?$')
A_to_r_ = re.compile(r'[\-AOeufr]\*?_?$')
A_to_p_ = re.compile(r'[\-AOeufrp]\*?_?$')
A_to_b_ = re.compile(r'[\-AOeufrpb]\*?_?$')
A_to_l_ = re.compile(r'[\-AOeufrpbl]\*?_?$')
A_to_g_ = re.compile(r'[\-AOeufrpblg]\*?_?$')
A_to_t_ = re.compile(r'[\-AOeufrpblgt]\*?_?$')
A_to_s_ = re.compile(r'[\-AOeufrpblgts]\*?_?$')
A_to_d_ = re.compile(r'[\-AOeufrpblgtsd]\*?_?$')
A_to_z_ = re.compile(r'[\-AOeufrpblgtsdz]\*?_?$')

A_to_z_no_pbs_ = re.compile(r'[\-AOeufr][lgtdz]+\*?_?$')
A_to_z_no_plt_ = re.compile(r'[\-AOeufr][bgsdz]+\*?_?$')
A_to_b_not_just_p = re.compile(r'[\-AOeu]([fr]+p|[fr]*pb|[frb]*)\*?_?$')
A_to_l_not_just_b = re.compile(r'[\-AOeu](([frpbl]{2,})?|[frpl])\*?_?$')

A_to_z_no_r = re.compile(r'[\-AOeuf][pblgtsdz]+\*?$')
A_to_z_no_p = re.compile(r'[\-AOeufr][blgtsdz]+\*?$')
A_to_z_no_b = re.compile(r'[\-AOeufrp][lgtsdz]+\*?$')
A_to_z_no_l = re.compile(r'[\-AOeufrpb][gtsdz]+\*?$')
A_to_z_no_g = re.compile(r'[\-AOeufrpbl][tsdz]+\*?$')
A_to_z_no_t = re.compile(r'[\-AOeufrpblg][sdz]+\*?$')
A_to_z_no_s = re.compile(r'[\-AOeufrpblgt][dz]+\*?$')
A_to_z_no_d = re.compile(r'[\-AOeufrpblgts][z]\*?$')

A_to_u_no_asterisk = re.compile(r'[\-AOeu]$')
A_to_z_no_l_not_bg = re.compile(r'(([\-AOeufrpb][tsdz]+)|([\-AOeufrp][gtsdz]+))\*?_?$')
A_to_r_no_asterisk = re.compile(r'[\-AOeufr]_?$')
A_to_g_no_asterisk = re.compile(r'[\-AOeufrpblg]_?$')
A_to_t_no_asterisk = re.compile(r'[\-AOeufrpblgt]_?$')

f_to_r = re.compile(r'[\-AOeu][frpblgt]\*?$')
f_to_t_no_asterisk = re.compile(r'[\-AOeu][frpblgt]_?$')
r_ = re.compile(r'[\-AOeu]r\*?_?$')
r_no_asterisk = re.compile(r'[\-AOeu]r_?$')
l_ = re.compile(r'[\-AOeu]l\*?_?$')
l_no_asterisk = re.compile(r'[\-AOeu]l_?$')
t_no_pl = re.compile(r'[\-AOeufr]t\*?_?$')

f_to_z_ = re.compile(r'[frpblgtsdz]\*?_?$')
f_to_z = re.compile(r'[frpblgtsdz]\*?$')
f_to_z__not_just_t = re.compile(r'([frpblgtsdz]{2,}|[frpblgsdz])\*?$')  # no _ because it has to follow a consonant
f_to_z_no_fb = re.compile(r'[\-AOeu][bplgtsdz]+\*?$')
r_to_t__ = re.compile(r'[rpblgt]\*?_$')
r_to_z = re.compile(r'[rpblgtsdz]\*?$')
p_to_z_ = re.compile(r'[pblgtsdz]\*?_?$')
p_to_z = re.compile(r'[pblgtsdz]\*?$')
b_to_z = re.compile(r'[blgtsdz]\*?$')
b_to_z_no_bg_ = re.compile(r'[\-AOeufrp][ltsdz]+\*?_?$')
l_to_z = re.compile(r'[lgtsdz]\*?$')
s = re.compile(r's\*?$')

































































































































































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
         "what must come before": any_consonant_but_not_KWH,
         "theory": ""},

        {"chord": "",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": any_consonant_but_not_KWH,
         "theory": ""},

        {"chord": "",
         "description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": any_consonant_but_not_KWH,
         "theory": ""},
    ],


    "": [
        {"chord": "",
         "description": "ignore suffix boundaries after left hand consonants",
         "spelling": "",  # algorithm+ics
         "pronunciation": " suffix ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": SToR,
         "theory": ""},

        {"chord": "",
         "description": "ignore y sound that I don't have in my accent",
         "spelling": "",  # bolognese
         "pronunciation": vowel_category["silent"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR,
         "theory": ""},
    ],


    "/": [
        {"chord": "/",
         "description": "",
         "spelling": "",
         "pronunciation": "( (prefix|root) )?",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": A_to_z_no_dash,
         "theory": ""}],

    "/_": [
        {"chord": "/",
         "description": "/ silent a",
         "spelling": "a",
         "pronunciation": "",  # I made this empty instead of ( suffix )?
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": f_to_z,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": vowel_category["short"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": f_to_z,  # changed because meteorological was too big
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": " suffix " + vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": f_to_z,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix, but I'm not sure about this one",
         "spelling": "[aeiouy]+",  # merciful
         "pronunciation": vowel_category["short"] + " suffix ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": f_to_z,
         "theory": ""},

        {"chord": "/",
         "description": "long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": f'({vowel_category["AOE"]}|{vowel_category["AOEU"]}|{vowel_category["AOU"]}|{vowel_category["AOU"]}|{vowel_category["AEU"]}|{vowel_category["AU"]}|{vowel_category["OE"]}|{vowel_category["OEU"]}|{vowel_category["OU"]}|{vowel_category["EU"]})',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": f_to_z,
         "theory": ""}],



    "K": [
        {"chord": "K", #why does `KPHAOUPB` → `commune` not work????
         "description": "k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K",
         "description": "c pronounced k",
         "spelling": "cc?",  # acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K",
         "description": "k, maybe ky",
         "spelling": "cc?",  # barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K",
         "description": "ch pronounced k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": upToS,
         "theory": ""},

         {"chord": "K",
         "description": "ck",
         "spelling": "ck(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K", # connection, context
         "description": "con optional std",
         "spelling": "con[std]?",
         "pronunciation": " k  (@|o|o4)  n ( [st] )?",
         "ambiguity": 10,
         "orthoscore": 0,
         "what must come before": upToS,
         "theory": "Harri"}
    ],




    "A_": [
        {"chord": "A",
         "description": "silent a",
         "spelling": "a",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_a_vowel_before,  # guard shouldn't be "drop vowel, silent a"
         "theory": ""},
    ],

    "A": [
        {"chord": "A",
         "description": "short a",
         "spelling": "a",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "A",
         "description": "short a", #villain... but not against?
         "spelling": "ai",
         "pronunciation": vowel_category["short"],
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},


        {"chord": "A",
         "description": "EU vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1, #garbage
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "AO*": [
        {"chord": "AO*",
         "description": "OU vowel spelt ao",
         "spelling": "ao",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"}
    ],


    "AO": [
        {"chord": "AO",
         "description": "AU vowel spelt ao",
         "spelling": "oa",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #coarse
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AO",
         "description": "OE vowel spelt oa",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 1, #toad
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": ""},

        {"chord": "AO",
         "description": "short vowel spelt oo",
         "spelling": "oo",
         "pronunciation": vowel_category["short"] ,  # u is took I think?
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AO",
         "description": "AOU vowel spelt oo",
         "spelling": "oo",
         "pronunciation": vowel_category["AOU"],  # uu is noon
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}
         ],

    "AO*e": [
        {"chord": "AO*E",
         "description": "AOE vowel spelt oe",
         "spelling": "oe",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": 1, #diarrhoea
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AO*E",
         "description": "AOE vowel + another vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"] + vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": 1, #create
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],

    "AOe": [
        {"chord": "AOE",
         "description": "AOE vowel",
         "spelling": "ee",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel",
         "spelling": "ie",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel",
         "spelling": "i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": -1, #Mozambique, Shiba
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel",  # acne, aires
         "spelling": "e",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #genotype
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #read
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel but maybe it's two syllables?",
         "spelling": "ea",
         "pronunciation": " i@ ",
         "ambiguity": 1,
         "orthoscore": -1, #real
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel",
         "spelling": "ey",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": -1, #key
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel",
         "spelling": "oe",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": -1, #diarhoea
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "AOE vowel",
         "spelling": "eo", #theory
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "AO*eu": [
        {"chord": "AO*EU",
         "description": "AOEU vowel, but two syllables", #diary, diagram, liar
         "spelling": "ia",
         "pronunciation": f'{vowel_category["AOEU"]}( suffix )?{vowel_category["short"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},
    ],

    "AOeu": [
        {"chord": "AOEU",
         "description": "AOEU vowel",
         "spelling": "ie?",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOEU",
         "description": "AOEU vowel",
         "spelling": "ei",  # acidifies
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOEU",
         "description": "AOEU vowel",
         "spelling": "y",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"},

        {"chord": "AOEU",
         "description": "AOEU vowel",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": vowel_category["AOEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOEU",
         "description": "AOEU vowel followed by a short e",
         "spelling": "ie",
         "pronunciation": vowel_category["AOEU"] + " @ ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOEU",
         "description": "suffix AOEU vowel",
         "spelling": "i",
         "pronunciation": f' suffix {vowel_category["AOEU"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "AOeur": [
        {"chord": "AOEUR",
         "description": "long i + r",
         "spelling": "irr?e?o?", # iron
         "pronunciation": " ae  @r ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}
    ],


    "AOeu/KWHAOe": [
        {"chord": "AOEU/KWHAOE",
         "description": "ai pronounced long i + long a",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": " ae  ii ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "AOu": [
        {"chord": "AOU",
         "description": "AOU vowel",
         "spelling": "e?ue?", # deuteronomy
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "AOU vowel",
         "spelling": "ou", 
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": -1, #soup
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "AOU vowel",
         "spelling": "eau",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "AOU vowel",
         "spelling": "ui",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "AOU vowel",
         "spelling": "ew",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,  # nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "AOU vowel",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": -1, #move
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU", 
         "description": "AOU vowel",
         "spelling": "uu", #vacuum
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU", 
         "description": "AOU vowel + another",
         "spelling": "ui", #druid
         "pronunciation": f'{vowel_category["AOU"]} i ',
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "AO*u": [
        {"chord": "AO*U",
         "description": "AOU vowel, but two syllables", #rune/ruin
         "spelling": "ui",
         "pronunciation": f'{vowel_category["AOU"]}( suffix )?{vowel_category["short"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},
    ],


    "AOr": [
        {"chord": "AOR",
         "description": "oar",
         "spelling": "oar",
         "pronunciation": " our  r ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "?"}
    ],


    "Ae": [
        {"chord": "AE",
         "description": "AOE vowel spelt ea (first stroke only)",
         "spelling": "ea",
         "pronunciation": vowel_category["AOE"], #it was just ii before
         "ambiguity": 1,
         "orthoscore": 1, #read
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": ""},

        {"chord": "AE",
         "description": "ea pronounced short e (first stroke only)",
         "spelling": "ea",
         "pronunciation": " e ", # earl?
         "ambiguity": 2, #red
         "orthoscore": 1, #read
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": ""},

        {"chord": "AE",
         "description": "AEU vowel spelt ea (first stroke only)",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 1,
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": "?"},

        {"chord": "AE",
         "description": "AOE vowel spelt ae",
         "spelling": "ae",
         "pronunciation": vowel_category["AOE"], # eir?
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Lapwing?"},
    ],


    "A*eur": [
        {"chord": "A*EUR",
         "description": "AOEUR vowel, but two syllables", #lair/layer
         "spelling": "ayer",
         "pronunciation": f'{vowel_category["AOEU"]}( suffix )?{vowel_category["short"]} r ',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},
    ],


    "Aeu": [
        {"chord": "AEU",
         "description": "AEU vowel",
         "spelling": "a",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "AEU vowel",
         "spelling": "a(a|ye?|i)",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1, # wave > waive
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "AEU vowel (are you British?)",
         "spelling": "e",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "AEU vowel",
         "spelling": "ett?e?",
         "pronunciation": vowel_category["AEU"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "AEU vowel",
         "spelling": "ey",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "AEU vowel",
         "spelling": "ei", #inveigh, weigh
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "AEU vowel",
         "spelling": "ea",
         "pronunciation": vowel_category["AEU"],
         "ambiguity": 2,
         "orthoscore": -1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "suffix AEU vowel",
         "spelling": "a",
         "pronunciation": f' suffix {vowel_category["AEU"]}',
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "Aeur": [
        {"chord": "AEUR",
         "description": "suffix -ar", #vexatious
         "spelling": "ar",
         "pronunciation": " suffix  eir  r ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "Aeurbs": [
        {"chord": "AEURBS",
         "description": "suffix -atious", #vexatious
         "spelling": "atious",
         "pronunciation": " suffix  ee  sh  @  s ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "Aeugs": [
        {"chord": "AEUGS",
         "description": "suffix -ation",
         "spelling": "ation",
         "pronunciation": " suffix  ee  sh ( suffix )? n ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "Aer": [
        {"chord": "AER",
         "description": "ary",  # January actuary actuaries
         "spelling": "ar(y|ie)",
         "pronunciation": " \(@r/e\)  r  iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR,
         "theory": "StenEd?"}
    ],


    "Au": [
        {"chord": "AU",
         "description": "AU vowel",
         "spelling": "a[auh]?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AU",
         "description": "AU vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": -1, #thought
         "what must come before": SToR_or_nothing,
         "theory": ""},

        #{"chord": "AU",
        # "description": "AU vowel spelt o",
        # "spelling": "o",
        # "pronunciation": vowel_category["AU"],
        # "ambiguity": 3,
        # "orthoscore": -1, #corp
        # "what must come before": SToR_or_nothing,
        # "theory": ""},

        {"chord": "AU",
         "description": "au",
         "spelling": "short vowel spelt au",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AU",
         "description": "OU vowel spelt au",
         "spelling": "au",
         "pronunciation": vowel_category["OU"], #Macau
         "ambiguity": 2,
         "orthoscore": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AU",
         "description": "AU vowel",
         "spelling": "awe?",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],

    "Al": [
        {"chord": "AL",
         "description": "suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "O_": [
        {"chord": "O",
         "description": "silent o",
         "spelling": "o",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_a_vowel_before,
         "theory": ""},
    ],


    "O": [
        {"chord": "O",
         "description": "o",
         "spelling": "o",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "O",
         "description": "short vowel spelt ow", # Knowledge
         "spelling": "ow",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},


        {"chord": "AU",
         "description": "AU vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AU"],
         "ambiguity": 1,
         "orthoscore": 1, #corp story
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "O",
         "description": "AOU vowel spelt o",
         "spelling": "o",
         "pronunciation": vowel_category["AOU"],
         "ambiguity": 1,
         "orthoscore": 1, #move,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "O",
         "description": "O vowel spelt a",
         "spelling": "a",
         "pronunciation": vowel_category["O"],
         "ambiguity": 1,
         "orthoscore": -1, #yacht
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "O*e": [
        {"chord": "O*E",
         "description": "OE vowel... spelt weird",
         "spelling": "e?aux?",  # baudelaire, aubergine beaux
         "pronunciation": vowel_category["OE"],
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},

        {"chord": "O*E",
         "description": "OE vowel spelt ow",
         "spelling": "ow",  # baudelaire, aubergine beaux
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": 1,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"}
    ],


    "Oe": [
        {"chord": "OE",
         "description": "OE vowel",
         "spelling": "o[eu]?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel spelt ow",
         "spelling": "owe?",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel spelt au",
         "spelling": "au",  # baudelaire, aubergine beaux,
         "pronunciation": vowel_category["OE"],
         "ambiguity": 1,
         "orthoscore": -1, #aubergine
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel",
         "spelling": "ot$",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OE",
         "description": "OE vowel spelt oa",
         "spelling": "oa",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "orthoscore": -1, #toad
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "Oeu": [
        {"chord": "OEU",
         "description": "OEU vowel",
         "spelling": "oi",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OEU",
         "description": "OEU vowel",
         "spelling": "oye?",
         "pronunciation": vowel_category["OEU"],
         "ambiguity": 1,  # feel free to change this prioritisation
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}
    ],


    "Oer": [
        {"chord": "OER",
         "description": "-ory",
         # but some words like "auditory" it's not a . at all-grit micks suffix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
         "spelling": "or(y|ie)",
         "pronunciation": "( suffix )? \[our\]  r  iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": "Harri?"},
    ],


    "O*u": [
        {"chord": "O*U",
         "description": "owe in 'vowel'",
         "spelling": "owe",
         "pronunciation": " owr? ( e5 )?",
         "ambiguity": 4,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"}
    ],


    "Ou": [
        {"chord": "OU",
         "description": "AU vowel spelt ou", #thought
         "spelling": "ou",
         "pronunciation": vowel_category["AU"], # bolder/boulder  thought   " starting_root  th  oo  t  suffix  f  [u]  l ",
         "ambiguity": 0,
         "orthoscore": 1, #thought
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OU",
         "description": "OU vowel",
         "spelling": "ow",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OU",
         "description": "OE vowel spelt OU??",
         "spelling": "ou",
         "pronunciation": vowel_category["OE"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},

        {"chord": "OU",
         "description": "short vowel spelt ou",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,  # colour
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},

        {"chord": "OU",
         "description": "OU vowel",
         "spelling": "ou",
         "pronunciation": vowel_category["OU"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "Ous": [
        {"chord": "OUS",
         "description": "suffix -ous",
         "spelling": "ous",
         "pronunciation": " suffix  @  s ",
         "ambiguity": 2,
         "orthoscore": 1, #glamorous
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "Or": [
        {"chord": "OR",
         "description": "suffix -or",
         "spelling": "orr?",
         "pronunciation": " suffix  @r  r ",
         "ambiguity": 0,
         "orthosuccor": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "Ol": [
        {"chord": "OL",
         "description": "oll even though it's an OE sound",
         "spelling": "oll",
         "pronunciation": " ou  l ",
         "ambiguity": -1, # TROLZ > TROELZ
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"}],


    "e": [
        {"chord": "E",
         "description": "e",
         "spelling": "e",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},  # not WSI because actresses that e is a @

        {"chord": "E",
         "description": "E vowel spelt ea",
         "spelling": "ea",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "E",
         "description": "E vowel spelt ai",  # against
         "spelling": "ai",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": -1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "E",
         "description": "EU vowel spelt e",  # delicious
         "spelling": "e",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0,
         "orthoscore": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "E",
         "description": "E vowel", #friend
         "spelling": "ie",
         "pronunciation": vowel_category["E"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "E fold",
         "description": "y (when *D is unusable)",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": A_then_vowels_that_make_asterisk_plus_d_not_usable,
         "theory": "StenEd?"},

        {"chord": "E fold",
         "description": "er (when -R is unusable)",
         "spelling": "err?",
         "pronunciation": "( suffix )? (@r|er)  r ",
         "ambiguity": 3,
         "orthoscore": 0,
         "what must come before": available_e_unavailable_r,
         "theory": "Harri?"},
    ],


    "e_": [
        {"chord": "E",
         "description": "silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_a_vowel_before,
         "theory": ""}
    ],


    "eu_": [
        {"chord": "EU",
         "description": "silent i",
         "spelling": "i",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_a_vowel_before,
         "theory": ""},
    ],

    "eu": [
        {"chord": "EU",
         "description": "y pronounced i diphthong",
         "spelling": "e?y",
         "pronunciation": " iy ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"},

        {"chord": "EU",
         "description": "ee pronounced i diphthong",
         "spelling": "ee",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "ii pronounced i diphthong",
         "spelling": "ii",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "ie pronounced i diphthong",
         "spelling": "ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "i",
         "spelling": "i",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "y",
         "spelling": "y",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,  # honestly this might be 0
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "i diphthong",
         "spelling": "i",
         "pronunciation": " iy ",
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "e pronounced i diphthong",  # acne, aires
         "spelling": "e",
         "pronunciation": " iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri?"},

        {"chord": "EU",
         "description": "ea pronounced i diphthong",
         "spelling": "ea",
         "pronunciation": " iy ",
         "ambiguity": 2,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri?"},

        {"chord": "EU",
         "description": "EU vowel spelt u", #busy
         "spelling": "u",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #busy
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "EU vowel spelt u", #busy
         "spelling": "a",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": -1, #garbage
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "EU vowel spelt ui", #build
         "spelling": "ui?",
         "pronunciation": vowel_category["EU"],
         "ambiguity": 0, #`PWUS/KWHEU` < PWEUS/KWHEU
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        #{"chord": "EU", commented out because of antidisestablishmentarianism, electrocardiography
        # "description": "EU vowel spelt e",  # delicious
        # "spelling": "e",
        # "pronunciation": vowel_category["EU"],
        # "ambiguity": 0,
        # "orthoscore": -1,
        # "what must come before": SToR_or_nothing,
        # "theory": ""},

        {"chord": "EU",
         "description": "AOE vowel spelt i",
         "spelling": "i",
         "pronunciation": vowel_category["AOE"],
         "ambiguity": 2,
         "orthoscore": 1, #Mozambique, Shiba
         "what must come before": SToR_or_nothing,
         "theory": ""},

         {"chord": "EU",
         "description": "suffix -y", #assembly
         "spelling": "(y|ie?)",
         "pronunciation": " suffix  iy ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "eufpl": [
        {"chord": "EUFPL",
         "description": "suffix -ism",
         "spelling": "ism",
         "pronunciation": " suffix  i  s  m ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": "StenEd?"},
    ],


    "eufb": [
        {"chord": "EUFB",
         "description": "suffix -ive",
         "spelling": "ive?",
         "pronunciation": " suffix  i  v ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "eupbg": [
        {"chord": "EUPBG",
         "description": "suffix -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""}
    ],


    "euz": [
        {"chord": "EUZ",
         "description": "-ies",
         "spelling": "ies",
         "pronunciation": " iy  suffix  z ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR,
         "theory": ""}
    ],


    "eu/KWHe": [
        {"chord": "EU/KWHE",
         "description": "ie",
         "spelling": "ie",
         "pronunciation": " iy $",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"}
    ],


    "er": [
        {"chord": "ER",
         "description": "er",
         "spelling": "err?",
         "pronunciation": "( (@r|er)  r | \(r  @/@r  r\) )",
         # sometimes (r  @/@r  r) like that whole thing is just in there
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "ER",
         "description": "suffix er",
         "spelling": "err?",
         "pronunciation": " suffix ( (@r|er)  r | \(r  @/@r  r\) )",
         # sometimes (r  @/@r  r) like that whole thing is just in there
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},

        {"chord": "ER",
         "description": "aer pronounced er",
         "spelling": "earr?",
         "pronunciation": "( (@r|er)  r | \(r  @/@r  r\) )",
         # sometimes (r  @/@r  r) like that whole thing is just in there
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?)"},

        {"chord": "ER fold",
         "description": "er (when E is free)",
         "spelling": "err?",
         "pronunciation": "( suffix )?( (@r|er)  r | \(r  @/@r  r\) )",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": skipsAnEUInTheVowels_no_r,  # replaced the logic ".*[AO](?!.*(.).*\1)[fpblgtsdz]*\*?"
         "theory": "Harri"}
    ],


    "u_": [
        {"chord": "U",
         "description": "silent u",
         "spelling": "u",
         "pronunciation": "",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_a_vowel_before,
         "theory": ""},
    ],

    "u": [
        {"chord": "U",
         "description": "u",
         "spelling": "u",
         "pronunciation": vowel_category["short"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "U",
         "description": "U vowel spelt ou",
         "spelling": "ou",
         "pronunciation": vowel_category["U"],
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},

        {"chord": "U",
         "description": "ou",
         "spelling": "ou",
         "pronunciation": vowel_category["short"],
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "l": [
        {"chord": "-L",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "le",
         "spelling": "ll?e",
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "el",
         "spelling": "ell?e?",#I added the final ? cause it looked wrong without it?
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "al",
         "spelling": "all?e?",
         "pronunciation": " @  l ",  # silent a is already a thing
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": A_to_b_not_just_p,
         "theory": ""},

        {"chord": "-L",
         "description": "suffix -l",  # antibacterial
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": A_to_u,
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


    "*l": [
        {"chord": "*L fold",
         "description": "l",
         "spelling": "ll?e?",
         "pronunciation": " l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": after_l_no_asterisk_or_l,
         "theory": "Harri"},  # *BLG → ckle


        {"chord": "*L fold",
         "description": "l",
         "spelling": "ll?e?",
         "pronunciation": " a5  l ",
         "ambiguity": 1,
         "orthoscore": 0,
         "what must come before": after_l_no_asterisk_or_l,
         "theory": "Harri"},  # *BLG → vocal
    ],


    "-l": [
        {"chord": "- and -L",
         "description": "le",
         "spelling": "le",
         "pronunciation": " l ",
         "ambiguity": 0,
         "orthoscore": 0,
         "what must come before": SToR_but_not_KWH,  # cause this includes the -
         "theory": "Lapwing?"}
    ],

}

