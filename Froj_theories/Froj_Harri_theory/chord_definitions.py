import re

custom_alphabet = "QSTKPWHR-AOeufrpblgtsdz*_"
# individualistically::RB: { ~ i n =.= d I2 . v ~ i . d == y uu @ l }.> * i s t >.> i k >.> l iy > :{in==divid==ual}>ist>>ic>>ally>:0



"""
There will be groups of keysymbols that come up again and again,
so I'll define them once here
"""
keysymbol_shorthands = {

    "short vowels": " \[?(@|@1|@r|a|a/ee|a1|a4|a4/a|a4/a1|a5|a5/i2|aa|ae/i|ah|ah2|ai/i|ao|ar1|e|e/ee|e0|e05|e1|e5|e5/e|e50|ee/a|ee/o|ee1|ee5/ee|i|i/ai|i/e|i/ii|i1|i2|i5|i6|i7|ii/e|ii/i|ii1|o|o1|o4|o5|o5/o|o/uh|oa|or1|our1|u|u/ouw|u/uu|uu/u|uh|uh/o|\(@r/e\))\]? ",
    # ii/i bidet/bistro   #ou/o???

    "long a": " \[?(aa/ee|ee|ee/o|ei|eir|eir1|ii/ee|iy/ee|e/ee|ee5/ee)\]? ",
    # ii/ee → beta 

    "au": " \[?(oa|aa|ah|ah1|ah2|oo|o/oo)\]? ",
    #not au for me: ao  was o/uh   because o/oo   cross au

    "ou": " \[?(ow)\]? ",

    "long e": " \[?(aa/ei|ae/ii|eir/ir|i/ii|ii|ii/ae|ii/e|ii/i|ii2|ir|iy/ee)\]? ",
    "long o": " \[?(ou|ou/o|ou1|ouw)\]? ",
    "long i": " \[?(ae|ae/i|ae/ii|aer|ai|ai/ei|ai/ii|ai1|i/ai|ii/ae)\]? ",
    # regarding ai1, some Americans say long i, some skip it, but (most?) British people say long i, so for consistency I'm using long i
    "long vowels": " \[?(aa|ee|ei|ir|iy)\]? ",
    # adherence uses ir     #don't wanna drop y uu #\(@r/~  e\) is both long AND short

    "long u": "( y )? (iu|iu3|u/ouw|ur|uu|uu/uu|\(u/uu\)) ",
}
# vowels like e5 are only found in suffixes?

# regex logic for what must come before
# hopefully compiling it all here makes it run faster since they'll be used

A_to_z_or_nothing_at_all = re.compile(r'(.*[\-AOeufrpblgtsdz])?\*?$')
# NothingRegex = re.compile(r'')
# AtLeastOneCharacterRegex = re.compile(r'.+')
skipsAnEUInTheVowels_no_r = re.compile(r'[/QSTKPWHR][AO][fpblgtsdz]+\*?$')
unavailable_e_no_r = re.compile(r'[/QSTKPWHR][AO]*[eu]+[fpblgtsdz]*\*?$')  # fire

available_e_unavailable_r = re.compile(r'[AO]+f?r[pblgtsdz]*\*?$')  # former farmer

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

any_letter = re.compile(r'[QSTKPWHRAO\-eufrpblgtsdz]\*?$')
any_letter_but_not_KWH = re.compile(r'((/(?!KWH$)[QSTKPWHR])|[AO\-eufrpblgtsdz])\*?$')
any_consonant = re.compile(r'[STKPWHRfrpblgtsdz]\*?$')
any_consonant_but_not_KWH = re.compile(r'(/(?!KWH$)[STKPWHR]+|[frpblgtsdz])\*?_?$')  # (?! is for negative lookahead
SToR_but_not_KWH = re.compile(r'/(?!KWH$)[STKPWHR]+\*?_?$')  # (?! is for negative lookahead

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

SToR_or_nothing = re.compile(r'(^/|[STKPWHR]\*?|/\*)$')  # or just an asterisk for compound words
# I'm getting rid of _? because "against"

upToK_no_T = re.compile(r'[/QS]K?\*?_?$')  # _? for #PWAOUD/PEFT
upToK_no_S = re.compile(r'[/Q]T?K?\*?$')

upToW_not_just_T_not_just_k_or_just_w = re.compile(r'([STKPW]{2,}|[/QSKP])\*?_?$')  # clink    _? for baudelair

upToW_not_just_s = re.compile(r'([/QTKPW]S?|[/QTKP]H)\*?_?$')  # yes _ because actresses drops a boundary after t
upToH_not_just_s_or_sh_not_KWH = re.compile(
    r'([/QTKP]H?|W)\*?_?$')  # yes _ because actresses drops a boundary after t          shh

upToW_no_T = re.compile(r'[/QS]K?P?W?\*?$')
upToW_no_P = re.compile(r'[/QSTK]W?\*?$')

first_stroke_SToR_or_nothing = re.compile(r'^/[STKPWHR]*$')

H_to_R_no_W = re.compile(r'[/QSTKP]H?R?\*?_?$')

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

f_to_t_no_asterisk = re.compile(r'[\-AOeu][frpblgt]_?$')
r_ = re.compile(r'[\-AOeu]r\*?_?$')
r_no_asterisk = re.compile(r'[\-AOeu]r_?$')
l_ = re.compile(r'[\-AOeu]l\*?_?$')
l_no_asterisk = re.compile(r'[\-AOeu]l_?$')
t_no_pl = re.compile(r'[\-AOeufr]t\*?_?$')

f_to_z_ = re.compile(r'[frpblgtsdz]\*?_?$')
f_to_z = re.compile(r'[frpblgtsdz]\*?$')
f_to_z__not_just_t = re.compile(r'([frpblgtsdz]{2,}|[frpblgsdz])\*?$')  # no _ because it has to follow a consonant
r_to_t__ = re.compile(r'[rpblgt]\*?_$')
p_to_z_ = re.compile(r'[pblgtsdz]\*?_?$')
p_to_z = re.compile(r'[pblgtsdz]\*?$')
l_to_z = re.compile(r'[lgtsdz]\*?$')

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
         "what must come before": any_consonant_but_not_KWH,
         "theory": ""},

        {"chord": "",
         "description": "drop short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 2,
         "what must come before": any_consonant_but_not_KWH,
         "theory": ""},

        {"chord": "",
         "description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": keysymbol_shorthands["long vowels"],
         "ambiguity": 3,
         "what must come before": any_consonant_but_not_KWH,
         "theory": ""},


    ],


    "": [
        {"chord": "",
         "description": "ignore suffix boundaries after left hand consonants",
         "spelling": "",  # algorithm+ics
         "pronunciation": " suffix ",
         "ambiguity": 3,
         "what must come before": SToR,
         "theory": ""},

        {"chord": "",
         "description": "ignore y sound that I don't have in my accent",
         "spelling": "",  # bolognese
         "pronunciation": " \[y1\] ",
         "ambiguity": 0,
         "what must come before": SToR,
         "theory": ""},
    ],


    "/": [
        {"chord": "/",
         "description": "",
         "spelling": "",
         "pronunciation": "( (prefix|root) )?",
         "ambiguity": 0,
         "what must come before": A_to_z_no_dash,
         "theory": ""}],

    "/_": [
        {"chord": "/",
         "description": "/ silent a",
         "spelling": "a",
         "pronunciation": "",  # I made this empty instead of ( suffix )?
         "ambiguity": 1,
         "what must come before": f_to_z,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 2,
         "what must come before": f_to_z,  # changed because meteorological was too big
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix",
         "spelling": "[aeiouy]+",
         # this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": " suffix " + keysymbol_shorthands["short vowels"],
         "ambiguity": 3,
         "what must come before": f_to_z,
         "theory": ""},

        {"chord": "/",
         "description": "short vowel that starts a suffix, but I'm not sure about this one",
         "spelling": "[aeiouy]+",  # merciful
         "pronunciation": keysymbol_shorthands["short vowels"] + " suffix ",
         "ambiguity": 3,
         "what must come before": f_to_z,
         "theory": ""},

        {"chord": "/",
         "description": "long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": keysymbol_shorthands["long vowels"],
         "ambiguity": 3,
         "what must come before": f_to_z,
         "theory": ""},

        #{"chord": "/",
        # "description": "silent i?????????",
        # "spelling": "i",  # medicine
        # "pronunciation": "",
        # "ambiguity": 1,
        # "what must come before": f_to_z,
        # "theory": " (Theory: Harri?)"},

        # {"description": "drop long u",
        # "spelling": "ue?",
        # "pronunciation": keysymbol_shorthands["long u"],
        # "ambiguity": 3,
        # "what must come before": any_consonant_but_not_KWH,
        # "theory": ""},

        {"chord": "/",
         "description": "middle a in banana",
         "spelling": "a",
         "pronunciation": " oa ",
         "ambiguity": 3,
         "what must come before": f_to_z,
         "theory": ""}],

    "*": [
        {"chord": "*",
         "description": "compound word",
         "spelling": "",
         "pronunciation": " compound ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Lapwing"},

        {"chord": "*",
         "description": "hyphen",
         "spelling": "\-",
         "pronunciation": "( compound )?",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Harri"},

        {"chord": "*",
         "description": "apostrophe",
         "spelling": "'",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": any_letter,
         "theory": "Field"},

        # I would love to, but this is basically a whole new theory at this point
        # {"description": "* for connecting a suffix",
        # "spelling": "",
        # "pronunciation": " suffix ",
        # "ambiguity": 0,
        # "what must come before": slash_no_asterisk,
        # "steno theory": " (Theory: Harriment)"},
    ],

    # "Q": [
    #    {"description": "^ for short a",
    #     "spelling": "a",
    #     "pronunciation": keysymbol_shorthands["short vowels"],
    #     "ambiguity": 0,
    #     "what must come before": first_slash,
    #     "steno theory": " (Theory: Josiah)"},

    #    {"description": "^ for long a",
    #     "spelling": "a",
    #     "pronunciation": " (starting_)?((root)|(prefix))  ee ",
    #     "ambiguity": 1,
    #     "what must come before": first_slash,
    #     "steno theory": " (Theory: Josiah)"}],

    "S*": [ #left hand with an asterisk!!!
        {"chord": "S*",
         "description": "sus",
         "spelling": "sus",
         "pronunciation": f" s {keysymbol_shorthands['short vowels']} s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""}
    ],

    "S": [
        {"chord": "S",
         "description": "s",
         "spelling": "ss?",
         "pronunciation": " s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "S",
         "description": "s (maybe silent)",
         "spelling": "ss?",
         "pronunciation": " z/s ",  # ( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "S",
         "description": "sw silent w",  # answer 
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Plover"},

        {"chord": "S",
         "description": "ps silent p",
         # conflicts with "uppsala" but psychotic has `HOT` → `hot` because of silent h so I don't mind
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "S",
         "description": "c pronounced s or sy",  # the ce in pharmaceutical
         "spelling": "cc?e?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "S",
         "description": "s pronounced z",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "S",
         "description": "c pronounced s",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "theory": ""},
    ],

    "STK": [
        {"chord": "STK",
         "description": "des sound (optional c/t)", # dis/disc/dist/des/desc/dec
         "spelling": "d[ie][sc]+t?",
         "pronunciation": " d  (i|ii|e)  (s|z) ( root )?( (k|t) )?",
         "ambiguity": 1, # descend/distend
         "what must come before": upToQ,
         "theory": "?"}
    ],


    "STKPW": [
        {"chord": "STKPW",
         "description": "z",
         "spelling": "zz?",
         "pronunciation": " z ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"}
    ],


    # "ST-bg": [
    #    {"description": "ST-BG for -istic",
    #     "spelling": "istic",
    #     "pronunciation": " suffix  i  s  t  suffix  i  k ",
    #     "ambiguity": 0,
    #     "what must come before": slash,
    #     "steno theory": ""}],

    "STKH": [
        {"chord": "STKH",
         "description": "disch",
         "spelling": "disch",
         "pronunciation": " d  i  s ( root )? ch ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Josiah?"}
    ],

    "SKWR": [
        {"chord": "SKWR",
         "description": "j",
         "spelling": "j",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "SKWR",
         "description": "j sound",
         "spelling": "(g|dj|dgg?e?)",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "SKWR",
         "description": "g pronounced zh",
         "spelling": "(d?jj?e?|d?gg?e?)", #aubergine
         "pronunciation": " zh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"},

        {"chord": "SKWR",
         "description": "j pronounced zh", #bonjour
         "spelling": "(d?jj?e?|d?gg?e?)",
         "pronunciation": " zh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Plover?"},

        # {"description": "SKWR for d because Americans say j",
        # "spelling": "dd?",
        # "pronunciation": " d  y ",
        # "ambiguity": 0,
        # "what must come before": upToS,
        # "steno theory": ""}
    ],


    "SKHR": [
        {"chord": "SKHR",
         "description": "shr",
         "spelling": "shr",
         "pronunciation": " sh  r ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Phoenix"}
    ],

    "SPW": [
        {"chord": "SPW",
         "description": "int/ent",
         "spelling": "[ie]nt",
         "pronunciation": " (i|e|e0)  n ( root )? t ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "theory": "?"},

         {"chord": "SPW",
         "description": "enth",
         "spelling": "[ie]nth",
         "pronunciation": " (i|e|e0)  n ( root )? th ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "theory": "Plover"}
    ],


    "SH": [
        {"chord": "SH",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},


        {"chord": "SH",
         "description": "ci pronounced sh",
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"},

        {"chord": "SH",
         "description": "s pronounced sh",
         "spelling": "ss?",  # pressure
         "pronunciation": "( sh | s  y )",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "SH",
         "description": "s pronounced sh in Harri's accent (Essex?)",
         "spelling": "ss?",  # assume
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"},

        {"chord": "SH",
         "description": "sh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #sc like fascist
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "what must come before": upToQ,
         "theory": ""},


        {"chord": "SH",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "what must come before": upToQ,
         "theory": ""},
    ],


    "SR": [
        {"chord": "SR",
         "description": "v",
         "spelling": "vv?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""}
    ],


    "S-pb": [
        {"chord": "S-PB",
         "description": "son silent o",
         "spelling": "son",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"},

        {"chord": "S-PB",
         "description": "sen silent e",
         "spelling": "sen",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"}
    ],


    "T": [
        {"chord": "T",
         "description": "t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "T",
         "description": "t but Harri says ch",
         "spelling": "tt?",  # attune
         "pronunciation": " t  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToS,
         "theory": ""}
    ],


    "TK": [
        {"chord": "TK",
         "description": "d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "TK",
         "description": "d but Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToS,
         "theory": ""}
    ],


    "TKPW": [
        {"chord": "TKPW",
         "description": "g",
         "spelling": "gg?h?", #ghost can be TKPWOEFT or TKPWHOEFT
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""}
    ],


    "TKPH": [
        {"chord": "TKPH", #I could trade this rule for a silent k rule
         "description": "kn silent k",
         "spelling": "kn",
         "pronunciation": " n ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "theory": "I don't know"}
    ],


    "TP": [
        {"chord": "TP",
         "description": "f",
         "spelling": "ff?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,  # sphere
         "theory": ""},

        {"chord": "TP",
         "description": "ph pronounced f",
         "spelling": "p?ph", #sapphire
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": upToK_no_T,  # sphere
         "theory": "Plover?"}
    ],


    "TPW": [
        {"chord": "TPW",
         "description": "inf",
         "spelling": "inf",
         "pronunciation": " i  n  f ",
         "ambiguity": 0,
         "what must come before": slash,
         "theory": "Josiah?"}
    ],


    "TPH": [
        {"chord": "TPH",
         "description": "n",
         "spelling": "nn?",
         "pronunciation": " n ( \[y\] )?",
         "ambiguity": 0,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "TPH",
         "description": "gn silent g",
         "spelling": "g?n",
         "pronunciation": " n ( y )?",
         "ambiguity": 0,
         "what must come before": upToS,
         "theory": ""}
    ],


    "TH": [
        {"chord": "TH",
         "description": "th",
         "spelling": "th",
         "pronunciation": " (th|dh) ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""}
         ],


    "K": [
        {"chord": "K", #why does `KPHAOUPB` → `commune` not work????
         "description": "k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K",
         "description": "c pronounced k",
         "spelling": "cc?",  # acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K",
         "description": "k, maybe ky",
         "spelling": "cc?",  # barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K",
         "description": "ch pronounced k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToS,
         "theory": ""},

         {"chord": "K",
         "description": "ck",
         "spelling": "ck(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToS,
         "theory": ""},

        {"chord": "K", # connection, context
         "description": "con optional std",
         "spelling": "con[std]?",
         "pronunciation": " k  (@|o|o4)  n ( [st] )?",
         "ambiguity": 10,
         "what must come before": upToS,
         "theory": "Harri"}
    ],


    "K_": [ # combust, needs _ for stuff like command
        {"chord": "K", # connection, context
         "description": "com",
         "spelling": "com?",
         "pronunciation": " k  (@|o|o4)  m ",
         "ambiguity": 10,
         "what must come before": upToS,
         "theory": "Harri"}
    ],


    "KPW": [
        {"chord": "KPW",
         "description": "imp/emp",
         "spelling": "[ie]mp",
         "pronunciation": " (i|e|e0)  m ( root )? p ",
         "ambiguity": 2,
         "what must come before": upToS,
         "theory": "?"},

        {"chord": "KPW",
         "description": "impr/empr", #`KPWR` → `you` in my theory
         "spelling": "[ie]mpr",
         "pronunciation": " (i|e|e0)  m ( root )? p  r ",
         "ambiguity": 3,
         "what must come before": upToS,
         "theory": "Harri"},
    ],


    "KW": [
        {"chord": "KW",
         "description": "qu",  # acquaint
         "spelling": "c?qu",
         # combined with the `U` → `ui` in build, this is a nasty combination but I don't know a fix for it, I guess there's always two ways to read KWEU → qui
         "pronunciation": " k ( w )?",  # briquette doesn't have a w
         "ambiguity": 0,
         "what must come before": upToS,
         "theory": ""}
    ],


    "KWR": [
        {"chord": "KWR",
         "description": "y",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "KWR",
         "description": "y",
         "spelling": "y",
         "pronunciation": " y ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "KWR",
         "description": "y, but for some people it's silent???",
         "spelling": "y",
         "pronunciation": " \[y\] ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "KWR",
         "description": "i",
         "spelling": "i",
         "pronunciation": "( suffix )? (ii|ii2|y|iy) ",  # aerospacial ← who wrote that???, fancier has a iy
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"},

        {"chord": "KWR",
         "description": "y",
         "spelling": "y",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "KWR",
         "description": "long e",  # meteor the second e
         "spelling": "e",
         "pronunciation": " ii2 ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Harri"}
    ],


    "KWH": [
        {"chord": "KWH",
         "description": "suffix",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 2,  # PWAEU/PWEU > PWAEUB/KWHEU, I'd rather see `KPW` → `imp` than KWH showcased
         "what must come before": slash_no_asterisk,
         "theory": "Harri"},

        {"chord": "KWH",
         "description": "pretend consonant",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 3,
         "what must come before": slash_no_asterisk_no__,
         "theory": "Harri"}
    ],


    "KH": [
        {"chord": "KH",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "KH",
         "description": "cc pronounced ch",
         "spelling": "cc",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": ""},

        {"chord": "KH",
         "description": "t pronounced ch",
         "spelling": "t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "theory": "Plover?"}
    ],

    "KHR": [  # because I've made HR illegal to follow K
        {"chord": "KHR",
         "description": "cl",
         "spelling": "cc?l",
         "pronunciation": " k  l ",
         "ambiguity": 0,
         "what must come before": upToQ,
         # I just... THR → tl feels wrong. Oh this is kinda long, I also don't like k + space for vowel + l like #KHREU/TPORPB/KWHA... but it makes sense for collateral college collegial
         "theory": ""},

        {"chord": "KHR",
         "description": "coll",
         "spelling": "coll",
         "pronunciation": " k  (o|@)  l ",
         "ambiguity": 1,
         "what must come before": upToQ,
         # I just... THR → tl feels wrong. Oh this is kinda long, I also don't like k + space for vowel + l like #KHREU/TPORPB/KWHA... but it makes sense for collateral college collegial
         "theory": ""}
    ],


    "P": [
        {"chord": "P",
         "description": "p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "theory": ""},

        {"chord": "P",
         "description": "p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "theory": ""}
    ],


    "PW": [
        {"chord": "PW",
         "description": "b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": upToK_no_S,
         "theory": ""},
    ],


    "PH": [
        {"chord": "PH",
         "description": "m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "theory": ""}
    ],


    "W": [
        {"chord": "W",
         "description": "w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "what must come before": upToK,
         "theory": ""},

        {"chord": "W",
         "description": "u pronounced w",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "what must come before": upToK,
         "theory": ""},

        {"chord": "W",
         "description": "long u", #poplar / popular
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "what must come before": upToK_not_just_K,
         "theory": "Harri?"},

        {"chord": "W",
         "description": "w pronounced v",
         "spelling": "w",
         "pronunciation": " (v|v/w) ",
         "ambiguity": 0,
         "what must come before": upToK,
         "theory": ""},

        {"chord": "W",
         "description": "v (after SR is unavailable)",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": SToK,
         "theory": ""},

        {"chord": "W fold",
         "description": "W",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 1,
         "what must come before": H_to_R_no_W,
         "theory": ""}
    ],


    "WR": [
        {"chord": "WR",
         "description": "wr", #(rite/right/write)
         "spelling": "wr",
         "pronunciation": " r ",
         "ambiguity": 1,
         "what must come before": upToT,
         "theory": "StenEd"}
    ],


    "WA": [
        {"chord": "WA",
         "description": "oir",
         "spelling": "oir?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 0,
         "what must come before": upToK,
         "theory": "Harri"},

        {"chord": "WA",
         "description": "oir",
         "spelling": "oir[re]+",
         "pronunciation": " w  ar  r ",
         "ambiguity": 1,
         "what must come before": upToK,
         "theory": "Harri"}
    ],


    "WO": [
        {"chord": "WO",
         "description": "o pronounced wuh", # one
         "spelling": "o",
         "pronunciation": " w  uh ",
         "ambiguity": 0,
         "what must come before": upToK,
         "theory": "StenEd?"}
    ],


    "H": [
        {"chord": "H",
         "description": "h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "what must come before": upToW_no_P,
         "theory": ""},

        {"chord": "H",
         "description": "silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": upToQ_or_W,  # upToW_no_P  removed because of "school" I think
         "theory": "?"},

        {"chord": "H",
         "description": "silent h depending on accent",
         "spelling": "h",
         "pronunciation": " \[h1\] ",
         "ambiguity": 0,
         "what must come before": upToW_no_P,
         "theory": "?"},
    ],


    "HR": [  # might be some logic for Commonwealth/United States spelling
        {"chord": "HR",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": upToW_not_just_T_not_just_k_or_just_w,
         # I just... THR → tl feels wrong. Oh this is kinda long, I also don't like k + space for vowel + l like #KHREU/TPORPB/KWHA... but it makes sense for collateral college collegial
         "theory": ""},
    ],


    "R": [
        {"chord": "R",
         "description": "r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": upToH_not_just_s_or_sh_not_KWH,  # added up to H since THRU # personal opinion, but SR → s + r is ugly
         "theory": ""},

        {"chord": "R",
         "description": "rh silent h",
         "spelling": "rr?h?",
         "pronunciation": " r ",
         "ambiguity": 1,
         "what must come before": upToH_not_just_s_or_sh_not_KWH,  # added up to H since THRU
         # personal opinion, but SR → s + r is ugly
         "theory": ""}
    ],


    "Re": [
        {"chord": "RE",
         "description": "re",
         "spelling": "re",
         "pronunciation": " \(r  @/@r  r\) ",
         "ambiguity": 0,
         "what must come before": upToW,
         "theory": ""}
    ],


    "A": [
        {"chord": "A",
         "description": "short a",
         "spelling": "a",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "A",
         "description": "silent a",
         "spelling": "a",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR,  # guard shouldn't be "drop vowel, silent a"
         "theory": ""},
    ],


    "AO*": [
        {"chord": "AO*",
         "description": "ao",
         "spelling": "ao",
         "pronunciation": " ow ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"}
    ],


    "AO": [
        {"chord": "AO",
         "description": "oa said like abroad",
         "spelling": "oa",
         "pronunciation": " oo ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"},

        {"chord": "AO",
         "description": "oa said like toad",
         "spelling": "oa",
         "pronunciation": " ou ",
         "ambiguity": 1,  # toad/towed
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": "StenEd?"},

        {"chord": "AO",
         "description": "oo",
         "spelling": "oo",
         "pronunciation": " (u|uu) ",  # uu is noon
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"}
         ],


    "AOe": [
        {"chord": "AOE",
         "description": "ee pronounce long e",
         "spelling": "ee",
         "pronunciation": keysymbol_shorthands["long e"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "ie pronounce long e",
         "spelling": "ie",
         "pronunciation": keysymbol_shorthands["long e"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "i pronounce long e",
         "spelling": "i",
         "pronunciation": keysymbol_shorthands["long e"],
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "e pronounce long e",  # acne, aires
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["long e"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "ea pronounce long e",
         "spelling": "ea",
         "pronunciation": keysymbol_shorthands["long e"],
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "long e but maybe it's two syllables?",
         "spelling": "ea",
         "pronunciation": " i@ ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOE",
         "description": "ey pronounced long e",
         "spelling": "ey", #key
         "pronunciation": keysymbol_shorthands["long e"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"},
    ],

    "AOeu": [
        {"chord": "AOEU",
         "description": "long i",
         "spelling": "ie?",  # acidifies
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOEU",
         "description": "ei pronounced long i",
         "spelling": "ei",  # acidifies
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOEU",
         "description": "y pronounced long i",
         "spelling": "y",
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"},

        {"chord": "AOEU",
         "description": "ai pronounced long i",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOEU",
         "description": "long i followed by a short e",
         "spelling": "ie",
         "pronunciation": keysymbol_shorthands["long i"] + " @ ",
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "AOeur": [
        {"chord": "AOEUR",
         "description": "long i + r",
         "spelling": "irr?e?o?", # iron
         "pronunciation": " ae  @r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}
    ],


    "AOeu/KWHAOe": [
        {"chord": "AOEU/KWHAOE",
         "description": "ai pronounced long i + long a",  # Ainu, Aida,
         "spelling": "ai",
         "pronunciation": " ae  ii ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "AOer": [
        {"chord": "AOER",
         "description": "ir pronounced long e + r",
         "spelling": "ir",
         "pronunciation": " ir  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}
    ],


    "AOu": [
        {"chord": "AOU",
         "description": "long u",
         "spelling": "ue?",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "ou pronounced long u",
         "spelling": "ou",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "eau pronounced long u",
         "spelling": "eau",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "ui pronounced long u",
         "spelling": "ui",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AOU",
         "description": "ew pronounced long u",
         "spelling": "ew",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 1,  # nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "what must come before": SToR_or_nothing,
         "theory": "Harri?"},

        {"chord": "AOU (not O for some reason)",
         "description": "ou pronounced long u",
         "spelling": "o",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "Lapwing"},
    ],


    "AOr": [
        {"chord": "AOR",
         "description": "oar",
         "spelling": "oar",
         "pronunciation": " our  r ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"}
    ],


    "Ae": [
        {"chord": "AE",
         "description": "ea pronounced long e (first stroke only)",
         "spelling": "ea",
         "pronunciation": keysymbol_shorthands["long e"], #it was just ii before
         "ambiguity": 1,
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": "?"},

        {"chord": "AE",
         "description": "ea pronounced short e (first stroke only)",
         "spelling": "ea",
         "pronunciation": " e ", # earl?
         "ambiguity": 1,
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": "?"},

        {"chord": "AE",
         "description": "ea pronounced long a (first stroke only)",
         "spelling": "ea",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 1,
         "what must come before": first_stroke_SToR_or_nothing,
         "theory": "?"},

        {"chord": "AE",
         "description": "ae pronounced long e",
         "spelling": "ae",
         "pronunciation": keysymbol_shorthands["long e"], # eir?
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "theory": "Lapwing?"},
    ],


    "Aeu": [
        {"chord": "AEU",
         "description": "long a",
         "spelling": "a(a|ye?|i)?",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "e pronounced long a (I'm British)",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "et pronounced long a",
         "spelling": "ett?e?",
         "pronunciation": keysymbol_shorthands["long a"] + "$",  # ←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "ey pronounced long a",
         "spelling": "ey",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "ei pronounced long a",
         "spelling": "ei",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AEU",
         "description": "ea pronounced long a",
         "spelling": "ea",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],

    "Aeugs": [
        {"chord": "AEUGS",
         "description": "suffix -ation",
         "spelling": "ation",
         "pronunciation": " suffix  ee  sh ( suffix )? n ",
         "ambiguity": 2,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},
    ],


    "Aer": [
        {"chord": "AER",
         "description": "ary",  # January actuary actuaries
         "spelling": "ar(y|ie)",
         "pronunciation": " \(@r/e\)  r  iy ",
         "ambiguity": 0,
         "what must come before": SToR,
         "theory": "StenEd?"}
    ],


    "Au": [
        {"chord": "AU",
         "description": "sound southern Brits say for the 'a' in bath",
         "spelling": "o?a[auh]?",  # ??? just keep it I guess
         "pronunciation": keysymbol_shorthands["au"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AU",
         "description": "au",
         "spelling": "au",  # ??? just keep it I guess
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "AU",
         "description": "aw",
         "spelling": "awe?",
         "pronunciation": keysymbol_shorthands["au"],
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "Aurb": [
        {"chord": "AURB",
         "description": "arb",
         "spelling": "arb",
         "pronunciation": "(" + keysymbol_shorthands["short vowels"] + "|" + keysymbol_shorthands[
             "long vowels"] + ")" + " r  b ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Josiah"}
    ],


    "Ar": [
        {"chord": "AR",
         "description": "ar sound",
         "spelling": "aa?rr?e?",
         "pronunciation": " ar  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Lapwing?"},

        {"chord": "AR",
         "description": "aur pronounced ar sound",
         "spelling": "uarr?e?",
         "pronunciation": " (ar|@r)  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Lapwing"},

        {"chord": "AR",
         "description": "ar ponounced or",
         "spelling": "arr?",  # warring maybe?, athwart
         "pronunciation": " or  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Lapwing"},
    ],


    "O": [
        {"chord": "O",
         "description": "o",
         "spelling": "o",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "O",
         "description": "ow pronounced short", # Knowledge
         "spelling": "ow",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "O",
         "description": "o with Harri's accent",
         "spelling": "o",
         "pronunciation": " (au|our|our/or|o/uh) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},

        {"chord": "O",
         "description": "o (accent stuff)",
         "spelling": "o",
         "pronunciation": " oou ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},

        {"chord": "O",
         "description": "silent o",
         "spelling": "o",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "O*e": [
        {"chord": "O*E",
         "description": "weird spelling pronounced owe",
         "spelling": "e?aux?",  # baudelaire, aubergine beaux
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri?"}
    ],


    "Oe": [
        {"chord": "OE",
         "description": "long o",
         "spelling": "oe?",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}, #Lapwing

        {"chord": "OE",
         "description": "ow pronounced long o",
         "spelling": "owe?",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OE",
         "description": "au pronounced long o",
         "spelling": "au",  # baudelaire, aubergine beaux
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri?"},

        {"chord": "OE",
         "description": "final ot pronounced long o",
         "spelling": "ot$",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "?"},

        {"chord": "OE",
         "description": "ou pronounced long o",
         "spelling": "ou",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 1,  # bolder/boulder
         "what must come before": SToR_or_nothing,
         "theory": "?"},

        {"chord": "OE",
         "description": "oa pronounced owe",
         "spelling": "oa",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,  # 0 ambiguity because toad > towed... load >_< lode
         "what must come before": SToR_or_nothing,
         "theory": "?"},
    ],


    "Oeu": [
        {"chord": "OEU",
         "description": "oi",
         "spelling": "oi",
         "pronunciation": " oi ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OEU",
         "description": "oy",
         "spelling": "oye?",
         "pronunciation": " oi ",
         "ambiguity": 1,  # feel free to change this prioritisation
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
         "what must come before": SToR_but_not_KWH,
         "theory": "Harri?"},

        # {"description": "OER for the not a suffix -ory", #but some words like "auditory" it's not a suffix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # "spelling": "or(y|ie)",
        # "pronunciation": " \[our\]  r  iy ",
        # "ambiguity": 1,
        # "what must come before": just_KWH,
        # "steno theory": " (Theory: Harri?)"},
    ],


    #"Oeg": [
    #    {"description": "OEG for ough said like owe",
    #     "spelling": "ough",
    #     "pronunciation": " ouw ",
    #     "ambiguity": 0,
    #     "what must come before": SToR_or_nothing,
    #     "steno theory": " (Theory: Harri?)"},
    #],


    "O*u": [
        {"chord": "O*U",
         "description": "owe in 'vowel'",
         "spelling": "owe",
         "pronunciation": " owr? ( e5 )?",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"}
    ],


    "Ou": [
        {"chord": "OU",
         "description": "ou pronounced au sound", #thought
         "spelling": "ou",
         "pronunciation": keysymbol_shorthands["au"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OU",
         "description": "ow",
         "spelling": "ow",
         "pronunciation": " owr? ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OU",
         "description": "ou pronounced ow",
         "spelling": "ou",
         "pronunciation": " owr? ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OU",
         "description": "'ou' in 'your'",
         "spelling": "ou",
         "pronunciation": " or/ur ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "Or": [
        {"chord": "OR",
         "description": "long o + r",
         "spelling": "orr?e?",
         "pronunciation": " or  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OR",
         "description": "'or' in 'word'",
         "spelling": "or",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "OR",
         "description": "'aur' in 'dinosaur",
         "spelling": "aur?r",
         "pronunciation": " or  r ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "Lapwing"},

        {"chord": "OR",
         "description": "oar",
         "spelling": "oar?r",
         "pronunciation": " our  r ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""}
    ],

    "Ol": [
        {"chord": "OL",
         "description": "oll even though it's an OE sound",
         "spelling": "oll",
         "pronunciation": " ou  l ",
         "ambiguity": -1, # TROLZ > TROELZ
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"}],


    "e": [
        {"chord": "E",
         "description": "e",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},  # not WSI because actresses that e is a @

        {"chord": "E",
         "description": "ea pronounced e",
         "spelling": "ea",
         "pronunciation": " e ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "?"},

        # {"description": "E for a short long e spelt just e (I know that's confusing but it's an edge case", #abalone
        # commented this out because of the first e in meteor using it
        #  "spelling": "e",
        #  "pronunciation" : " ii ",
        #  "ambiguity": 1,
        #  "what must come before": SToR_or_nothing,
        #  "steno theory": " (Theory: Harri)"},

        {"chord": "E",
         "description": "ai pronounced short e", #against
         "spelling": "ai",
         "pronunciation": " e ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "?"},

        {"chord": "E fold",
         "description": "y (when *D is unusable)",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": A_then_vowels_that_make_asterisk_plus_d_not_usable,
         "theory": "StenEd?"},

        {"chord": "E fold",
         "description": "er (when -R is unusable)",
         "spelling": "err?",
         "pronunciation": "( suffix )? (@r|er)  r ",
         "ambiguity": 3,
         "what must come before": available_e_unavailable_r,
         "theory": "Harri?"},
    ],


    "e_": [
        {"chord": "E",
         "description": "silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}
    ],


    "eu": [
        {"chord": "EU",
         "description": "y pronounced i diphthong",
         "spelling": "e?y",
         "pronunciation": " iy ",  # (ii|ii2|ir)
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"},

        {"chord": "EU",
         "description": "ee pronounced i diphthong",
         "spelling": "ee",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "ii pronounced i diphthong",
         "spelling": "ii",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "ie pronounced i diphthong",
         "spelling": "ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "i",
         "spelling": "i",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "silent i",
         "spelling": "i",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "y",
         "spelling": "y",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 1,  # honestly this might be 0
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "i diphthong",
         "spelling": "i",
         "pronunciation": " iy ",
         "ambiguity": 1,  # why One? I don't know I can't think of any conflicts to be honest
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "EU",
         "description": "e pronounced i diphthong",  # acne, aires
         "spelling": "e",
         "pronunciation": " iy ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "Harri?"},

        {"chord": "EU",
         "description": "ea pronounced i diphthong",
         "spelling": "ea",
         "pronunciation": " iy ",
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "theory": "Harri?"},

        {"chord": "EU",
         "description": "i sound, weird spelling)", #busy, build
         "spelling": "ui?",
         "pronunciation": " i ",
         "ambiguity": -1, #`PWUS/KWHEU` < PWEUS/KWHEU
         "what must come before": SToR_or_nothing,
         "theory": "?"},
    ],


    "eur": [
        {"chord": "EUR",
         "description": "ir",
         "spelling": "ir",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR,
         "theory": "?"}
    ],


    "eupbg": [
        {"chord": "EUPBG",
         "description": "suffix -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": SToR_but_not_KWH,
         "theory": ""}
    ],


    "euz": [
        {"chord": "EUZ",
         "description": "-ies",
         "spelling": "ies",
         "pronunciation": " iy  suffix  z ",
         "ambiguity": 1,
         "what must come before": SToR,
         "theory": ""}
    ],


    "eu/KWHe": [
        {"chord": "EU/KWHE",
         "description": "ie",
         "spelling": "ie",
         "pronunciation": " iy $",
         "ambiguity": 0,
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
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "ER",
         "description": "suffix er",
         "spelling": "err?",
         "pronunciation": " suffix ( (@r|er)  r | \(r  @/@r  r\) )",
         # sometimes (r  @/@r  r) like that whole thing is just in there
         "ambiguity": 1,
         "what must come before": SToR_but_not_KWH,
         "theory": ""},

        {"chord": "ER",
         "description": "aer pronounced er",
         "spelling": "earr?",
         "pronunciation": "( (@r|er)  r | \(r  @/@r  r\) )",
         # sometimes (r  @/@r  r) like that whole thing is just in there
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?)"},

        {"chord": "ER fold",
         "description": "er (when E is free)",
         "spelling": "err?",
         "pronunciation": "( suffix )?( (@r|er)  r | \(r  @/@r  r\) )",
         "ambiguity": 1,
         "what must come before": skipsAnEUInTheVowels_no_r,  # replaced the logic ".*[AO](?!.*(.).*\1)[fpblgtsdz]*\*?"
         "theory": "Harri"}
    ],


    "u": [
        {"chord": "U",
         "description": "u",
         "spelling": "u",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "U",
         "description": "'ou' in 'borough'",
         "spelling": "ou",
         "pronunciation": " ouw?1 ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "Harri"},

        {"chord": "U",
         "description": "ou",
         "spelling": "ou",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},

        {"chord": "U",
         "description": "silent u",
         "spelling": "u",
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": ""},
    ],


    "ur": [
        {"chord": "UR",
         "description": "ur",
         "spelling": "urr?e?",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": "?"},

        {"chord": "UR",
         "description": "our",
         "spelling": "our",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "theory": ""}
    ],


    "-rb": [  # that - is part of it
        {"chord": "no vowel, -RB",
         "description": "'shure'",
         "spelling": "(ss?|z)ure",  # seizure, pleasure, measure, pressure, leisure
         "pronunciation": " (s|z) ( suffix )? y  @r  r ",
         "ambiguity": 1,
         "what must come before": SToR_but_not_KWH,
         "theory": "Harri"}
    ],


    "f": [
        {"chord": "-F",
         "description": "f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": A_to_u_,  # `PHER/SEUFL` → `merciful`, with suffix=_
         "theory": ""},

        {"chord": "-F",
         "description": "ph pronounced f",  # graph
         "spelling": "p?ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": "?"},

        # {"description": "-F for gh", #laugh?
        # "spelling": "gh",
        # "pronunciation": " f ",
        # "ambiguity": 1,
        # "what must come before": A_to_u,
        # "steno theory": ""},

        {"chord": "-F fold",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 1,
         "what must come before": l_,
         "theory": ""},
    ],


    "f_": [  # there's logic where anything ending in a _ cannot be followed by a new stroke
        {"chord": "-F",
         "description": "s",
         "spelling": "ss?e?",
         "pronunciation": " (s|z) ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "theory": "StenEd?"},

        {"chord": "-F",
         "description": "c",
         "spelling": "s?ce?",
         "pronunciation": " (s|z) ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "theory": "StenEd?"},

        {"chord": "-F",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "theory": "StenEd?"},

        {"chord": "-F fold",
         "description": "s",  # first accurst, but not saurus
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": r_,
         "theory": ""}
    ],


    "*f_": [
        {"chord": "*F",
         "description": "z",
         "spelling": "zz?e?",
         "pronunciation": " (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": "Harri"}
    ],


    "/-f":[
        {"chord": "/-F",
         "description": "final f",
         "spelling": "fe?$",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": l_,
         "theory": "Plover?"},

        {"chord": "/-F",
         "description": "final ph",
         "spelling": "p?phe?$",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": l_,
         "theory": "Plover?"}
    ],


    "fr_": [
        {"chord": "-FR",
         "description": "m",
         "spelling": "m",
         "pronunciation": " m ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "theory": "StenEd?"}
    ],


    "frpb": [
        {"chord": "-FRPB",
         "description": "nch (conflicts with -rch)",
         "spelling": "nche?",
         "pronunciation": " n  ch ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": "StenEd?"}
    ],


    "fpb": [
        {"chord": "-FRB",
         "description": "ch (following an r)",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": r_,
         "theory": "StenEd?"}
    ],


    "frpbg": [
        {"chord": "-FRPBG",
         "description": "nk",
         "spelling": "nk",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "Miff?"},

        {"chord": "-FRPBG",
         "description": "nc",
         "spelling": "nc",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "Miff??"}
    ],


    "frpbgs": [
        {"chord": "-FRPBGS",
         "description": "nk + shn sound",
         "spelling": "nction",
         "pronunciation": " ng  k  sh  suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "Harri"},

        {"chord": "-FRPBGS",
         "description": "nx",
         "spelling": "nx",
         "pronunciation": " ng  k  s ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "Harri"}
    ],


    "*fb": [
        {"chord": "*FB fold",
         "description": "f sound",
         "spelling": "(f|ph)",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": r_no_asterisk,
         "theory": "Lapwing"}
    ],


    "fp": [
        {"chord": "-FP",
         "description": "ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "?"},

        {"chord": "-FP",
         "description": "tch",
         "spelling": "tch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "?"}
    ],


    "fpl": [
        {"chord": "-FPL",
         "description": "suffix -some",
         "spelling": "some",
         "pronunciation": " suffix  s  m ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": "Magnum?"}
    ],


    "fb": [
        {"chord": "-FB",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "Phoenix"},

        {"chord": "-FB fold",
         "description": "v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 1,
         "what must come before": r_,
         "theory": "Harri"}
    ],


    "/-fb":[
        {"chord": "/-FB",
         "description": "v",
         "spelling": "ve?$",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": l_,
         "theory": "Harri"}
    ],


    "fbgt": [
        {"chord": "-FBGT",
         "description": "stic",
         "spelling": "stic",
         "pronunciation": " s  t  i  k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "Harri"}
    ],


    "fl": [
        {"chord": "-FL",
         "description": "suffix -ful",
         "spelling": "ful",
         "pronunciation": " suffix  f ( u )? l ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": ""}
    ],


    "*fg": [
        {"chord": "*FG",
         "description": "gh then suffix -ing",
         "spelling": "ghing",
         "pronunciation": " f  suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": "Harri"}
    ],

    # "fs":[
    #    {"description": "-FS for double s",
    #     "spelling": "ss",
    #     "pronunciation": " s ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_u, #no idea, this just feels right
    #     "steno theory": " (Theory: Harri)"}],

    "r": [
        {"chord": "-R",
         "description": "r",
         "spelling": "rr?e?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": A_to_f_,
         "theory": ""},

        {"chord": "-R fold",
         "description": "re",
         "spelling": "re",
         "pronunciation": "( suffix )? (\(r  @/@r  r\)|@r  r) ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_r,
         "theory": ""},

        {"chord": "-R fold",
         "description": "ro",  # acrobatics
         "spelling": "ro",
         "pronunciation": " r  @ ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_r,
         "theory": ""},

        {"chord": "-R fold",
         "description": "er (when E is unavailable)",
         "spelling": "err?",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 2,
         "what must come before": unavailable_e_no_r,
         "theory": "Harri"},

        {"chord": "-R fold",
         "description": "ar (when E is unavailable)",
         "spelling": "arr?",  # friar
         "pronunciation": " r ",
         "ambiguity": 3,
         "what must come before": unavailable_e_no_r,  # reusing cause I'm lazy
         "theory": "Harri"},

        {"chord": "-R fold",
         "description": "or (when E is unavailable)",
         "spelling": "orr?",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 3,
         "what must come before": unavailable_e_no_r,  # reusing cause I'm lazy
         "theory": "Harri"}
    ],


    "rb": [
        {"chord": "-RB",
         "description": "sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": A_to_f_,
         "theory": "StenEd?"},

        {"chord": "-RB",
         "description": "ci pronounced sh (Harri's accent)",  # aerospacial
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "what must come before": A_to_f_,
         "theory": "Harri"},

        {"chord": "-RB",
         "description": "sh sound",
         "spelling": "((s|t|x)i|ce|s?che?|sc|ss)",
         "pronunciation": "( sh | s ( suffix )? y )",
         "ambiguity": 1,
         "what must come before": A_to_f_,
         "theory": "StenEd?"},


        {"chord": "-RB",
         "description": "zh sound",
         "spelling": "((s|c|t|x)i|ce|s?che?|sc|ss)", #caucasia
         "pronunciation": "( zh | z ( suffix )? y )",
         "ambiguity": 1,
         "what must come before": A_to_f_,
         "theory": ""},
    ],


    "rb_": [
        # conscious abstentious anxious?
        {"chord": "-RB",
         "description": "nsh sound",
         "spelling": "n(sc|t|x)i",  # x for anxious
         "pronunciation": " n  sh ",
         "ambiguity": 1,
         "what must come before": A_to_f_,
         "theory": "Harri"},

        {"chord": "-RB",
         "description": "ngksh sound",
         "spelling": "n(sc|t|x)i",  # xi for anxious,
         "pronunciation": " ng ( k )? sh ",
         "ambiguity": 1,
         "what must come before": A_to_f_,
         "theory": "Harri"},
    ],

    "*rbl": [
        {"chord": "*RBL",
         "description": "rtial",
         "spelling": "rtial",
         "pronunciation": " s  y  @  l ",
         "ambiguity": 1,
         "what must come before": SToR_, #not a mistake
         "theory": "Harri"}
    ],

    "rbl": [
        {"chord": "-RBL",
         "description": "sh + suffix -able",
         "spelling": "shable?",
         "pronunciation": " sh  suffix  @  b  l ",
         "ambiguity": 1,
         "what must come before": A_to_f,
         "theory": "Harri"},

        {"chord": "-RBL",
         "description": "rrow",
         "spelling": "rr?ow?",
         "pronunciation": " r  ouw? ",
         "ambiguity": 1, #facial, faro
         "what must come before": A_to_f,
         "theory": "Harri"},
    ],


    "p": [
        {"chord": "-P",
         "description": "p",
         "spelling": "pp?e?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": A_to_r_,  # ".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "theory": ""}
    ],


    "/-p": [
        {"chord": "/-P",
         "description": "final p",
         "spelling": "pp?$",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": p_to_z,
         "theory": "StenEd"},
    ],

    "*pb": [
        {"chord": "*PB",
         "description": "ken sound",
         "spelling": "[ck]+[eo]n", # chicken, reckon, beacon
         "pronunciation": f" k {keysymbol_shorthands['short vowels']} n ", # y for the discontinuation
         "ambiguity": 1,
         "what must come before": A_to_r_no_asterisk,
         "theory": "Harri"}
    ],

    "pb": [
        {"chord": "-PB",
         "description": "n",
         "spelling": "(e|o)?nn?e?",
         "pronunciation": " n ", # y for the discontinuation
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": ""},

        {"chord": "-PB",
         "description": "suffix -n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": "?"},

        {"chord": "-PB",
         "description": "gn silent g",
         "spelling": "gn",
         "pronunciation": " n ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "theory": ""},

        {"chord": "-PB fold",
         "description": "suffix -en",
         "spelling": "en",
         "pronunciation": " suffix  \[e5\]  n ",
         "ambiguity": 1,
         "what must come before": l_to_z_no_porb,
         "theory": ""}
    ],


    "/-pb": [
        {"chord": "/-PB",
         "description": "suffix n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "what must come before": after_r,
         "theory": ""}
    ],


    "pblg": [
        {"chord": "-PBLG",
         "description": "j",
         "spelling": "d?je?",
         "pronunciation": " jh ",
         "ambiguity": 1, #Why 1? not 0?
         "what must come before": A_to_r_,
         "theory": ""},

        {"chord": "-PBLG",
         "description": "g pronounced j",
         "spelling": "d?gg?e?",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "theory": ""},

        {"chord": "-PBLG",
         "description": "zh sound",
         "spelling": "(j|dj|d?gg?)e?",
         "pronunciation": " zh ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "theory": ""}
    ],  # arbitrage


    "pbg": [
        {"chord": "-PBG",
         "description": "ng",
         "spelling": "ng?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": ""},

        {"chord": "-PBG",
         "description": "'nge' in 'singe'",
         # funny example cause of course `SEUPBG` → `sing`, but `ORPBG` → `orange`
         "spelling": "nge?",
         "pronunciation": " n  jh ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "theory": ""},

        {"chord": "-PBG",
         "description": "ng sound then g sound",
         "spelling": "ng?",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "theory": ""}
    ],


    "pbgs": [
        {"chord": "-PBGS",
         "description": "nx",
         "spelling": "nx",
         "pronunciation": " ng  g  z ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": "Harri?"}
        ],


    "pbg/S": [
        {"chord": "-PBG/S",
         "description": "nx",
         "spelling": "nx",
         "pronunciation": " ng  g  z ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": ""}
    ],


    "pbg/SH": [
        {"chord": "-PBG/SH",
         "description": "ngsh sound",  # if there even is one?
         "spelling": "n(sc|t|x)i",
         "pronunciation": " ng  sh ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": ""}
    ],


    "frpbg/SH": [
        {"chord": "-FRPBG/SH",
         "description": "ngksh sound",  # if there even is one?
         "spelling": "n(sc|t|x)i",
         "pronunciation": " ng  k  sh ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": ""}
    ],


    "pl": [
        {"chord": "-PL",
         "description": "m",
         "spelling": "mm?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": ""},

        {"chord": "-PL",
         "description": "mb silent b",
         "spelling": "mb",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": "StenEd?"},

        {"chord": "-PL",
         "description": "mp silent p",
         "spelling": "mp",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": "StenEd?"},

        {"chord": "-PL",
         "description": "mn silent n",
         "spelling": "mn",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "theory": "StenEd?"},

        {"chord": "-PL",
         "description": "lm silent l (has to follow AU)",
         "spelling": "lm",
         "pronunciation": "( \[l1\] )? m ",
         "ambiguity": 0,
         "what must come before": Au, #balm
         "theory": "StenEd?"},

        {"chord": "-PL fold",
         "description": "uhm sound",
         "spelling": "m(b|m)?e?",
         "pronunciation": " @  m ",
         "ambiguity": 0,
         "what must come before": t_no_pl,
         "theory": ""},
    ],


    "/-pl": [
        {"chord": "/-PL",
         "description": "final m",
         "spelling": "mm?$",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": p_to_z,
         "theory": "StenEd"},
    ],


    "*pz": [
        {"chord": "*PZ",
         "description": "h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "what must come before": A_to_r_no_asterisk,
         "theory": "Josiah"},

        {"chord": "*PZ",
         "description": "silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": A_to_r_no_asterisk,
         "theory": "Josiah?"}
    ],


    "plt": [
        {"chord": "-PLT",
         "description": "suffix -ment",
         "spelling": "ment",
         "pronunciation": "( suffix )? m  e5  n  t ",
         "ambiguity": 0,
         # "what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_r_,
         "theory": "?"},

        {"chord": "-PLT",
         "description": "t then suffix -ment",
         "spelling": "tment",
         "pronunciation": " t  suffix  m  e5  n  t ",
         "ambiguity": 2,
         # "what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_r_,
         "theory": "?"}
    ],


    "b": [
        {"chord": "-B",
         "description": "b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         # this chord can only can after a vowel, so it's Josiah since `KAURB` → `carb`
         "theory": ""},

        {"chord": "-B",
         "description": "b", 
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 1, #Following an R
         "what must come before": ends_in_r,
         "theory": ""}
    ],


    "/-b": [
        {"chord": "/-B",
         "description": "final b",
         "spelling": "bb?e?$",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": l_,
         "theory": "Lapwing"}
    ],


    "bl": [
        {"chord": "-BL",
         "description": "ble pronounced bil",
         "spelling": "ble?",
         "pronunciation": " b  i  l ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "Josiah?"},

        {"chord": "-BL",
         "description": "low",
         "spelling": "ll?ow?",
         "pronunciation": " l  ouw? ",
         "ambiguity": 1,
         "what must come before": A_to_p_,
         "theory": "Donna Urlaub"}
    ],


    "bg": [
        {"chord": "-BG",
         "description": "k",
         "spelling": "k(k|e)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "?"},

        {"chord": "-BG",
         "description": "ck",
         "spelling": "cke?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "?"},

        {"chord": "-BG",
         "description": "ch pronounced k",
         "spelling": "che?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "?"},

        {"chord": "-BG",
         "description": "ch pronounced x",
         "spelling": "che?",
         "pronunciation": " x ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "Harri"},

        {"chord": "-BG",
         "description": "lk silent l (immediately after a vowel)",
         "spelling": "lk",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "theory": ""},

        {"chord": "-BG",
         "description": "c pronounced k",  # do I make *BG? pick pic? $$$$
         "spelling": "c(c|e)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": A_to_p_,
         "theory": ""},

        {"chord": "-BG",
         "description": "qu",  # do I make *BG? pick pic? $$$$$$$?
         "spelling": "que?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": A_to_p_,
         "theory": ""}
    ],


    "bgs": [
        {"chord": "-BGS",
         "description": "x",
         "spelling": "xe?",  # axe
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": ""}
    ],


    "*bgs": [
        {"chord": "*BGS",
         "description": "ction",
         "spelling": "ction",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "Harri"}
    ],


    "bg/S": [
        {"chord": "-BG/S",
         "description": "x",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "Lapwing"}
    ],


    "bg/TKPW": [  # blackguard
        {"chord": "-BG/TKPW",
         "description": "ckg silent ck",
         "spelling": "ckg",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": "Harri"}
    ],


    "bg/W": [
        {"chord": "-BG/W",
         "description": "cqu",  # `ABG/WAOE/KWHES` → `acquiesce`
         "spelling": "cqu",
         "pronunciation": " k  w ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "theory": ""}
    ],


    "l": [
        {"chord": "-L",
         "description": "l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "le",
         "spelling": "ll?e",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "el",
         "spelling": "ell?e",
         "pronunciation": " l ",
         "ambiguity": 1,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "al",
         "spelling": "all?e?",
         "pronunciation": " @  l ",  # silent a is already a thing
         "ambiguity": 1,
         "what must come before": A_to_b_not_just_p,  # surely this should then work for "level"??
         "theory": ""},

        {"chord": "-L",
         "description": "suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "what must come before": A_to_b_not_just_p,
         "theory": ""},

        {"chord": "-L",
         "description": "suffix -l",  # antibacterial
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": ""},

         {"chord": "-L",
         "description": "silent -l after AU",  # antibacterial
         "spelling": "l", #PWAUL/-L → ball???
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "theory": ""},
    ],


    "*l": [
        {"chord": "*L fold",
         "description": "l",
         "spelling": "ll?e?",
         "pronunciation": " l ",
         "ambiguity": 1,
         "what must come before": after_l_no_asterisk_or_l,
         "theory": "Harri"},  # *BLG → ckle
    ],


    "-l": [
        {"chord": "- and -L",
         "description": "le",
         "spelling": "le",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": SToR_but_not_KWH,  # cause this includes the -
         "theory": "Lapwing?"}
    ],


    "/-l": [
        {"chord": "/-L",
         "description": "final le",
         "spelling": "ll?e$",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": p_or_l_to_z,
         "theory": "Lapwing?"},
    ],


    "/-g": [
        {"chord": "/-G",
         "description": "suffix -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": g_and_dz,
         "theory": ""}
    ],


    "*g": [
        {"chord": "*G",
         "description": "gue", #analogue
         "spelling": "gue",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": A_to_r_no_asterisk,  # picked to r... no particular reason
         "theory": "Harri"},

        {"chord": "*G",
         "description": "k (following an -L)",  # mulch/mulk or something
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": l_no_asterisk,
         "theory": "StenEd"},

        {"chord": "*G",
         "description": "ch (following an -L)",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": l_no_asterisk,
         "theory": "Harri"}],

    "g": [
        {"chord": "-G",
         "description": "g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": A_to_l_not_just_b,
         "theory": ""},

        {"chord": "-G",
         "description": "g pronounced j (following an -L)",
         "spelling": "gg?e?",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "what must come before": l_,
         "theory": "StenEd?"},

        {"chord": "-G",
         "description": "suffix -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_p_,  # ← look at that lack of _ at the end
         # okay the issue here is that maybe there's no issue
         "theory": ""},

         {"chord": "-G",
         "description": "suffix -ing after l",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 2,
         "what must come before": l_,  # ← look at that lack of _ at the end
         # okay the issue here is that maybe there's no issue
         "theory": ""},

        {"chord": "-G",
         "description": "silent gh",
         "spelling": "gh",
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before": A_to_p,
         "theory": "Harri?"},

        {"chord": "-G fold",
         "description": "suffix -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": after_g_no_g,
         "theory": ""}
    ],


    "gt": [
        {"chord": "-GT",
         "description": "xt",
         "spelling": "xt",
         "pronunciation": " k  s  t ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "theory": "StenEd"},
    ],


    "gs": [
        {"chord": "-GS",
         "description": "tion",
         "spelling": "tion",
         "pronunciation": "( suffix )? sh ( suffix )? n ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "theory": "StenEd"},

        {"chord": "-GS",
         "description": "sion",
         "spelling": "s?sion",  # double s for accession
         "pronunciation": "( suffix )? (zh|sh|sh/zh) ( suffix )? n ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "theory": "StenEd"},

        {"chord": "-GS",
         "description": "cian",
         "spelling": "cian",
         "pronunciation": " s ( suffix )? y  @  n ",  # beautician isn't with a suffix
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "theory": "StenEd"}
    ],


    "t": [
        {"chord": "-T",
         "description": "t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "theory": ""},

        {"chord": "-T",
         "description": "final dt pronounced t",
         "spelling": "dt$",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "theory": "Harri"},

        {"chord": "-T",
         "description": "t pronounced sh",
         "spelling": "tt?e?",
         "pronunciation": " sh ",
         "ambiguity": 2,  # so it doesn't win against abtentious
         "what must come before": A_to_g_,
         "theory": ""}
    ],


    "*t": [
        {"chord": "*T",
         "description": "th",
         "spelling": "the?",
         "pronunciation": " \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "what must come before": A_to_g_no_asterisk,
         "theory": "StenEd"},

        {"chord": "*T",
         "description": "suffix -th",
         "spelling": "the?",
         "pronunciation": " suffix  \[?(th|dh|dh/th)\]? ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "what must come before": A_to_g_no_asterisk,
         "theory": "StenEd?"},
    ],


    "ts": [
        {"chord": "-TS",
         "description": "t + s",
         "spelling": "tt?e?s",
         "pronunciation": " t  s ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "theory": ""}
    ],


    "*td": [
        {"chord": "*TD",
         "description": "dth",
         "spelling": "dthe?",
         "pronunciation": " (t|d)  (th|dh|dh/th) ",
         "ambiguity": 1,  # giving it a 1 for personal reasons lol
         "what must come before": A_to_g_no_asterisk,
         "theory": "StenEd"},

        # worthy
        {"chord": "*TD",
         "description": "th + y",
         "spelling": "th(y|ie?)",
         "pronunciation": " (th|dh) ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": A_to_g_no_asterisk,
         "theory": "Harri?"}
    ],


    "s": [
        {"chord": "-S",
         "description": "se",
         "spelling": "se",  # actresses?"
         "pronunciation": " (s|z) ",
         "ambiguity": 0,
         "what must come before": A_to_t_,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},

        {"chord": "-S",
         "description": "solo s following a vowel", #cyclops
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_u_or__,  # dis
         "theory": ""},

        {"chord": "-S",
         "description": "solo s following a vowel (maybe voiced)",
         "spelling": "s",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         # cyclops with a z
         "what must come before": A_to_u_or__,  # dis
         "theory": ""},

        {"chord": "-S",
         "description": "s silent t",
         "spelling": "ss?te?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_t_no_g_end,  # no idea, this just feels right
         "theory": ""},

        {"chord": "-S",
         "description": "s silent w",  # answer
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_t_no_g_end,
         "theory": ""},

        {"chord": "-S",
         "description": "ss",
         "spelling": "ss",  # actresses?"
         "pronunciation": " (s|z) ",
         "ambiguity": 1,
         # cyclops
         "what must come before": A_to_t_,  # A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "theory": ""},

        {"chord": "-S",
         "description": "c pronounced s",
         "spelling": "s?ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": A_to_t_no_g_end,  # maybe I'm traumatised from ABGS/HRERPL/TER → accelerometer
         "theory": ""},

        {"chord": "-S",
         "description": "s maybe voiced",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 1,
         "what must come before": A_to_t,  # no _ I think?
         "theory": ""},

        {"chord": "-S",
         "description": "s pronounced z",
         "spelling": "ss?e?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "what must come before": A_to_t,  # no _ I think?
         "theory": ""},

        {"chord": "-S",
         "description": "suffix -s",
         "spelling": "s",
         "pronunciation": "( (suffix) ) (s|z|z/s) ",
         "ambiguity": 1,
         "what must come before": A_to_g_yes_t,
         "theory": ""}
    ],


    "*s": [
        {"chord": "*S",
         "description": "suffix -'s",
         "spelling": "'s",
         "pronunciation": " suffix  (s|z|z/s) ",
         "ambiguity": 2,
         "what must come before": A_to_t_no_asterisk,
         "theory": "Josiah"},

        {"chord": "*S",
         "description": "suffix -ise",
         "spelling": "ise?",
         "pronunciation": " suffix  ae  z ",
         "ambiguity": 1,
         "what must come before": A_to_t_no_asterisk,
         "theory": "Harri?"},

        {"chord": "*S",
         "description": "st (following -G or -T)",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 1,
         "what must come before": ends_in_b_to_t_no_asterisk,
         "theory": ""}
    ],


    "/-d": [
        {"chord": "/-D",
         "description": "suffix -ed",
         "spelling": "ed",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 0,
         "what must come before": yes_s,
         "theory": ""}
    ],


    "d": [
        {"chord": "-D",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": A_to_t_,
         "theory": ""},

        {"chord": "-D",
         "description": "d",
         "spelling": "dd?e?",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "what must come before": A_to_t_,
         "theory": ""},

        {"chord": "-D",
         "description": "suffix -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 1,
         "what must come before": A_to_t,
         "theory": ""}
    ],


    "*d": [
        {"chord": "*D",
         "description": "y pronounced i diphthong",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": A_to_t_no_asterisk,
         "theory": "Harri?"},

        {"chord": "*D",
         "description": "y pronounced i",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "what must come before": A_to_t_no_asterisk,
         "theory": "Harri?"},

        {"chord": "*D",
         "description": "dy",
         "spelling": "dd?y",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "what must come before": A_to_t_no_asterisk,
         "theory": "HelloChap?"}
    ],


    "dz": [
        {"chord": "-DZ",
         "description": "d + s",
         "spelling": "dd?e?s",
         "pronunciation": " d  z ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "theory": ""},

        {"chord": "-DZ",
         "description": "suffix -ing (when G is unavailable)",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": A_to_g_yes_b_or_g,
         "theory": "Magnum"}
    ],


    "z": [
        {"chord": "-Z",
         "description": "solo s (following a consonant)",
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": f_to_z__not_just_t,  # dis
         "theory": "Harri"}, #cyclops

        {"chord": "-Z",
         "description": "plural",  # actresses
         "spelling": "s",
         "pronunciation": " suffix ( i7 )? (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_d_no_t,
         "theory": "?"},
    ],


    "*z": [
        {"chord": "*Z",
         "description": "-st (following -D)",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 0,
         "what must come before": ends_in_d_no_asterisk,
         "theory": "Harri?"},

        {"chord": "*Z",
         "description": "z",
         "spelling": "zz?e?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "what must come before": A_to_d_no_t,
         "theory": "Harri"},
    ],




    # prefixes
    "Af": [
        {"chord": "AF",
         "description": "after",  # I think this spills into rafter
         "spelling": "after",
         "pronunciation": " ah  f  t  @r  r ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"}
    ],


    "Afr/": [  # the / is there because of A*FRT/KWHOUGT → afterthought
        #however for compound words, the `/` means that it's not reordered :(
        {"chord": "AFR/",
         "description": "prefix after-",
         "spelling": "after",
         "pronunciation": " ah  f  t  @r  r  (compound|prefix) ",
         # starting_root  ah  f  t  @r  r  suffix  w  @r  r  d
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "theory": "StenEd?"}
    ],







    #################### here's all the suffixes

    "SH*eur": [
        {"chord": "SH*EUR",
         "description": "shire",
         "spelling": "shire",
         "pronunciation": " sh  aer1  r ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Harri"}
    ],


    "SH*eup": [
        {"chord": "SH*EUP",
         "description": "suffix -ship",
         "spelling": "ship",
         "pronunciation": " suffix  sh  i  p ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Lapwing"}
    ],


    "SO*pl": [
        {"chord": "SO*PL",
         "description": "suffix -some",
         "spelling": "some",
         "pronunciation": " suffix  s  m ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Lapwing"}
    ],


    "Seu": [
        {"chord": "SEU",
         "description": "suffix -cy",
         "spelling": "c(y|ie?)",
         "pronunciation": " suffix  s  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": ""}
    ],


    "Teu": [
        {"chord": "TEU",
         "description": "suffix -ty",
         "spelling": "t(y|ie?)",
         "pronunciation": " suffix  t  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": ""}
    ],


    "KHur": [
        {"chord": "KHUR",
         "description": "suffix -ture",
         "spelling": "ture",
         "pronunciation": " suffix  t  y  @r  r ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Lapwing"}
    ],


    "PWR*eu": [
        {"chord": "PWR*EU",
         "description": "suffix -berry",
         "spelling": "berr(y|ie?)",
         "pronunciation": " suffix  b  \(@r/e\)  r  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Harri"}
    ],


    "PHA*pb": [
        {"chord": "PHA*PB",
         "description": "suffix -man",
         "spelling": "man",
         "pronunciation": " suffix  m  (a5|@)  n ", #chairmanship with a @
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Plover?"}
    ],


    "PH*epb": [
        {"chord": "PH*EPB",
         "description": "suffix -men",
         "spelling": "men",
         "pronunciation": " suffix  m  e5  n ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Plover?"}
    ],


    "WAO*eus": [
        {"chord": "WAO*EUS",
         "description": "suffix -wise",
         "spelling": "wise",
         "pronunciation": " suffix  w  ae  z ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Lapwing"}
    ],


    "WA*rd": [
        {"chord": "WA*RD",
         "description": "suffix -ward",
         "spelling": "ward",
         "pronunciation": " suffix  w  @r  r  d ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "StenEd?"}
    ],


    "WO*rtd": [
        {"chord": "WO*RTD",
         "description": "suffix -worthy",
         "spelling": "worth(y|ie?)",
         "pronunciation": " suffix  w  @@r  r  dh  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Harri?"}
    ],


    "WO*r/THeu": [
        {"chord": "WO*R/THEU",
         "description": "suffix -worthy",
         "spelling": "worth(y|ie?)",
         "pronunciation": " suffix  w  @@r  r  dh  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Lapwing?"}
    ],


    "WO*pl": [
        {"chord": "WO*PL",
         "description": "suffix -woman",
         "spelling": "woman",
         "pronunciation": " suffix  w  u  m  (a5|@)  n ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Plover?"}
    ],


    "W*EUPL": [
        {"chord": "W*EUPL",
         "description": "suffix -women",
         "spelling": "woman",
         "pronunciation": " suffix  w  i  m  i  n ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Harri"}
    ],


    "HReu": [
        {"chord": "HREU",
         "description": "suffix -ly",
         "spelling": "l(y|ie?)",
         "pronunciation": " suffix  l  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "StenEd"}
    ],


    "HAO*d": [
        {"chord": "HAO*D",
         "description": "suffix -hood",
         "spelling": "hood",
         "pronunciation": " suffix  h  u  d ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "StenEd"}
    ],


    "HA*pl": [
        {"chord": "HA*PL",
         "description": "ham silent h",
         "spelling": "ham",
         "pronunciation": " \(@/h  a\)  m ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Harri"}
    ],


    "R*es": [
        {"chord": "R*ES",
         "description": "suffix -ress",  # actress
         "spelling": "ress",
         "pronunciation": " suffix  r  (e5|@)  s ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "theory": "Lapwing"}
    ],


    "Reu": [
        {"chord": "REU",
         "description": "suffix -ry",
         "spelling": "r(y|ie)",
         "pronunciation": " suffix  r  iy ",
         "ambiguity": 0,
         "what must come before": slash_or_T,
         "theory": "?"}
    ],



    "/-fl": [
        {"chord": "/-FL",
         "description": "suffix -ful",
         "spelling": "ful",
         "pronunciation": " suffix  f ( u )? l ", #canful
         "ambiguity": 0,
         "what must come before": f_to_z,
         "theory": "StenEd?"}
    ],


    "/-plt": [
        {"chord": "/-PLT",
         "description": "suffix -ment",  # adjournment
         "spelling": "ment",
         "pronunciation": " suffix  m  e5  n  t ",
         "ambiguity": 0,
         "what must come before": p_to_z,
         "theory": "StenEd?"}
    ],


    "/-lt": [
        {"chord": "/-LT",
         "description": "suffix -let",  # armlet
         "spelling": "let",
         "pronunciation": " suffix  l  i7  t ",
         "ambiguity": 0,
         "what must come before": l_to_z,
         "theory": "StenEd?"}
    ],

    "/-ls": [
        {"chord": "/-LT",
         "description": "suffix -less",  # armlet
         "spelling": "less",
         "pronunciation": " suffix  l  e5  s ",
         "ambiguity": 0,
         "what must come before": l_to_z,
         "theory": "StenEd?"}
    ],
}
