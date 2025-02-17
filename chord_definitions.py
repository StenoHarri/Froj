import re



custom_alphabet = "QSTKPWHR-AOeufrpblgtsdz*_"
# individualistically::RB: { ~ i n =.= d I2 . v ~ i . d == y uu @ l }.> * i s t >.> i k >.> l iy > :{in==divid==ual}>ist>>ic>>ally>:0


keysymbol_shorthands = {
    """
    There will be groups of keysymbols that come up again and again,
    so I'll define them once here
    """
    "long a": "a i",
    "short vowels":           " \[?(@|@1|@r|a|a1|a4|a4/a1|a5|ae/i|ai/i|ar1|e|e05|e1|e5|a5/i2|e50|ee1|i|i1|i2|i5|i6|i7|ii/i|ii1|o|o1|o4|o5|o5/o|or1|our1|u|u/ouw|u/uu|uu/u|uh|uh/o|\(@r/e\))\]? ",
    # ii/i bidet/bistro
    "I don't know if these are long or short": " \[?(ao|eir)\]? ",

    "long a": " \[?(ee|ei|eir|eir1|aa/ee|ii/ee)\]? ",
    # ii/ee → beta

    "long o": " \[?(ou|ou1|ouw)\]? ",
    "long i": " \[?(ae|ae/i|ae/ii|aer|ai|ai/ei|ai/ii|ai1|ii/ae)\]? ",
    #regarding ai1, some Americans say long i, some skip it, but (most?) British people say long i, so for consistency I'm using long i
    "long vowels": " \[?(aa|ee|ei|ir|iy)\]? ",#adherence uses ir     #don't wanna drop y uu #\(@r/~  e\) is both long AND short

    "long u": "( y )? (iu|iu3|u/ouw|ur|uu|uu/uu|\(u/uu\)) ",
}
#vowels like e5 are only found in suffixes?

#regex logic for what must come before
#hopefully compiling it all here makes it run faster since they'll be used

A_to_z_or_nothing_at_all = re.compile(r'(.*[\-AOeufrpblgtsdz])?\*?$')
#NothingRegex = re.compile(r'')
#AtLeastOneCharacterRegex = re.compile(r'.+')
skipsAnEUInTheVowels_no_r = re.compile(r'[AO][fpblgtsdz]+\*?$')
unavailable_e_no_r = re.compile(r'[QSTKPWHR][AO]*[eu]+[fpblgtsdz]*\*?$') #fire

available_e_unavailable_r = re.compile(r'[AO]+f?r[pblgtsdz]*\*?$') # former farmer

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
ends_in_b_to_t_no_asterisk = re.compile(r'[blgt]_?$') #against
ends_in_g_to_t_no_asterisk = re.compile(r'[gt]\*?$')
ends_in_d_no_asterisk = re.compile(r'd$')
ends_in_d_no_asterisk_no_t = re.compile(r'[AO\-eufrpblg]d$')

any_letter = re.compile(r'[QSTKPWHRAO\-eufrpblgtsdz]\*?$')
any_letter_but_not_KWH = re.compile(r'((/(?!KWH$)[QSTKPWHR])|[AO\-eufrpblgtsdz])\*?$')
any_consonant = re.compile(r'[STKPWHRfrpblgtsdz]\*?$')
any_consonant_but_not_KWH = re.compile(r'(/(?!KWH$)[STKPWHR]+|[frpblgtsdz])\*?_?$') #(?! is for negative lookahead
SToR_but_not_KWH = re.compile(r'/(?!KWH$)[STKPWHR]+\*?_?$') #(?! is for negative lookahead


A_then_vowels_that_make_asterisk_plus_d_not_usable = re.compile(r'A([frpblgt]*[sdz]+|\*[frpblgtsdz]+)$')


g_and_dz = re.compile(r'g[ts]*[dz]+\*?$')


first_slash = re.compile(r'^/$')
slash_no_asterisk = re.compile(r'/_?$')
slash_no_asterisk_no__ = re.compile(r'/$')

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

upToK_not_just_K = re.compile(r'(/|[QST]K?)\*?_?$')

SToR = re.compile(r'[STKPWHR]\*?$')
SToR_ = re.compile(r'[STKPWHR]\*?_?$')
SToK = re.compile(r'[STK]\*?_?$')

SToR_or_nothing = re.compile(r'(^/|[STKPWHR]\*?|/\*)$') #or just an asterisk for compound words
#I'm getting rid of _? because "against"

upToK_no_T = re.compile(r'[/QSK]\*?_?$') # _? for #PWAOUD/PEFT
upToK_no_S = re.compile(r'[/QTK]\*?$')

upToW_not_just_T_not_just_k_or_just_w = re.compile(r'([STKPW]{2,}|[/QSKP])\*?_?$') #clink    _? for baudelair

upToW_not_just_s = re.compile(r'([/Q]|[TKPW])\*?_?$') #yes _ because actresses drops a boundary after t
upToH_not_just_s = re.compile(r'([/Q]|[TKPWH])\*?_?$') #yes _ because actresses drops a boundary after t
upToW_no_T = re.compile(r'[/QSKPW]\*?$')
upToW_no_P = re.compile(r'[/QSTKW]\*?$')

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

f_to_t_no_asterisk = re.compile(r'[\-AOeu][frpblgt]_?$')
r_ = re.compile(r'[\-AOeu]r\*?_?$')
r_no_asterisk = re.compile(r'[\-AOeu]r_?$')
l_ = re.compile(r'[\-AOeu]l\*?_?$')
l_no_asterisk = re.compile(r'[\-AOeu]l_?$')
t_no_pl = re.compile(r'[\-AOeufr]t\*?_?$')

f_to_z_ = re.compile(r'[frpblgtsdz]\*?_?$')
f_to_z = re.compile(r'[frpblgtsdz]\*?$')
f_to_z__not_just_t = re.compile(r'([frpblgtsdz]{2,}|[frpblgsdz])\*?$') #no _ because it has to follow a consonant
r_to_t__ = re.compile(r'[rpblgt]\*?_$')
p_to_z_ = re.compile(r'[pblgtsdz]\*?_?$')
p_to_z = re.compile(r'[pblgtsdz]\*?$')
l_to_z = re.compile(r'[lgtsdz]\*?$')

"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {

    "_": [


        {"description": "drop short vowel",
         "spelling": "[aeiouy]+",  #this may be a mistake adding the +, but my reasoning is ferrous, anxious, that `ou` is a short @
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 2,
         "what must come before": any_consonant_but_not_KWH,
         "steno theory": ""},

        #{"description": "drop i that historically didn't exist anyway",
        # "spelling": "",
        # "pronunciation": " i ",
        # "ambiguity": 2,
        # "what must come before": any_consonant_but_not_KWH,
        # "steno theory": ""},

        #{"description": "drop short vowel that starts a suffix",
        # "spelling": "[aeiouy]+",  #this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
        # "pronunciation": " suffix " + keysymbol_shorthands["short vowels"],
        # "ambiguity": 3,
        # "what must come before": any_consonant_but_not_KWH, #it was #just consonants, but then I saw: `PHER/SEUFL` → `merciful`
        # "steno theory": ""},



        #stuff like "awful" I'll just add
        #{"description": "ignore suffix boundaries after vowels??",
        # "spelling": "",  
        # "pronunciation": " suffix ",
        # "ambiguity": 3,
        # "what must come before": A_to_u,
        # "steno theory": ""},

        #{"description": "ignore suffix boundaries after anything???",
        # "spelling": "",
        # "pronunciation": " suffix ",
        # "ambiguity": 3,
        # "what must come before": any_letter_but_not_KWH,
        # "steno theory": ""},

        {"description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": keysymbol_shorthands["long vowels"],
         "ambiguity": 3,
         "what must come before": any_consonant_but_not_KWH,
         "steno theory": ""},


        #{"description": "drop long u",
        # "spelling": "ue?",
        # "pronunciation": keysymbol_shorthands["long u"],
        # "ambiguity": 3,
        # "what must come before": any_consonant_but_not_KWH,
        # "steno theory": ""},

        {"description": "drop the middle vowel in banana",
         "spelling": "a",
         "pronunciation": " oa ",
         "ambiguity": 3,
         "what must come before": any_consonant_but_not_KWH,
         "steno theory": ""},

         {"description": "drop silent vowel",
         "spelling": "[aiu]", #merciful, somethingcal
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before": any_consonant_but_not_KWH,
         "steno theory": ""},
        ],

    #"_": [

        #{"description": "ignoring a suffix boundary",
        # "spelling": "",
        # "pronunciation": " suffix ",
        # "ambiguity": 1,
        # "what must come before": any_letter,
        # "steno theory": ""},

        #{"description": "ignoring a non-suffix word boundary",
        # "spelling": "",
        # "pronunciation": " (prefix|root) ",
        # "ambiguity": 1,
        # "what must come before": any_letter,
        # "steno theory": ""}],

    "": [
        {"description": "ignore suffix boundaries after left hand consonants",
         "spelling": "", #algorithm+ics
         "pronunciation": " suffix ",
         "ambiguity": 3,
         "what must come before": SToR,
         "steno theory": ""},

        {"description": "ignore y sound that I don't have in my accent",
         "spelling": "", # bolognese
         "pronunciation": " \[y1\] ",
         "ambiguity": 0,
         "what must come before": SToR,
         "steno theory": ""},

    ],


    #"": [ # commenting out because it thinks the a in "against" is silent
    #    {"description": "drop silent vowel",
    #     "spelling": "[aiu]", #merciful, somethingcal
    #     "pronunciation": "",
    #     "ambiguity": 1,
    #     "what must come before": any_consonant_but_not_KWH,
    #     "steno theory": ""},
    #    ],

    "/": [
        {"description": "/",
         "spelling": "",
         "pronunciation": "( (prefix|root) )?",
         "ambiguity": 0,
         "what must come before": A_to_z_no_dash,
         "steno theory": ""}],

    "/_": [
        {"description": "/ for silent a",
         "spelling": "a",
         "pronunciation": "", #I made this empty instead of ( suffix )?
         "ambiguity": 1,
         "what must come before": f_to_z,
         "steno theory": ""},

        {"description": "/ for short vowel",
         "spelling": "[aeiouy]+",  #this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 2,
         "what must come before": f_to_z, #changed because meteorological was too big
         "steno theory": ""},

        {"description": "/ for i that historically didn't exist anyway",
         "spelling": "",
         "pronunciation": " i ",
         "ambiguity": 2,
         "what must come before": f_to_z,
         "steno theory": ""},

        {"description": "/ for short vowel that starts a suffix",
         "spelling": "[aeiouy]+",  #this may be a mistake adding the +, but my reasoning is ferrous, that `ou` is a short @
         "pronunciation": " suffix " + keysymbol_shorthands["short vowels"],
         "ambiguity": 3,
         "what must come before": f_to_z,
         "steno theory": ""},

        {"description": "/ for short vowel that starts a suffix, but I'm not sure about this one",
         "spelling": "[aeiouy]+",  #merciful
         "pronunciation": keysymbol_shorthands["short vowels"] + " suffix ",
         "ambiguity": 3,
         "what must come before": f_to_z,
         "steno theory": ""},

        #{"description": "/ for suffix boundary if it follows the left hand", #I actually have no idea what this means
        # "spelling": "",
        # "pronunciation": " suffix ",
        # "ambiguity": 3,
        # "what must come before": A_to_z_no_dash,
        # "steno theory": ""},

        {"description": "/ for long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": keysymbol_shorthands["long vowels"],
         "ambiguity": 3,
         "what must come before": f_to_z,
         "steno theory": ""},

        {"description": "/ for silent i?????????",
         "spelling": "i", #medicine
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before": f_to_z,
         "steno theory": "Harri?"},

        #{"description": "drop long u",
        # "spelling": "ue?",
        # "pronunciation": keysymbol_shorthands["long u"],
        # "ambiguity": 3,
        # "what must come before": any_consonant_but_not_KWH,
        # "steno theory": ""},

        {"description": "/ for the middle vowel in banana",
         "spelling": "a",
         "pronunciation": " oa ",
         "ambiguity": 3,
         "what must come before": f_to_z,
         "steno theory": ""}],

    "*": [
        {"description": "* for connecting a compound word",
         "spelling": "",
         "pronunciation": " compound ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing"},

        {"description": "* for a hyphen",
         "spelling": "\-",
         "pronunciation": "( compound )?",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing"},
        
        {"description": "* for apostrophe",
         "spelling": "'",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": any_letter,
         "steno theory": "Harri! Surprisingly"},

        #I would love to, but this is basically a whole new theory at this point
        # {"description": "* for connecting a suffix",
        # "spelling": "",
        # "pronunciation": " suffix ",
        # "ambiguity": 0,
        # "what must come before": slash_no_asterisk,
        # "steno theory": "Harriment"},
         ],


    #"Q": [
    #    {"description": "^ for short a",
    #     "spelling": "a",
    #     "pronunciation": keysymbol_shorthands["short vowels"],
    #     "ambiguity": 0,
    #     "what must come before": first_slash,
    #     "steno theory": "Josiah"},

    #    {"description": "^ for long a",
    #     "spelling": "a",
    #     "pronunciation": " (starting_)?((root)|(prefix))  ee ",
    #     "ambiguity": 1,
    #     "what must come before": first_slash,
    #     "steno theory": "Josiah"}],

    "S": [
        {"description": "S for s",
         "spelling": "ss?",
         "pronunciation": " s ", #( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"},

        {"description": "S for unvoiced s, but maybe you voice it",
         "spelling": "ss?",
         "pronunciation": " z/s ", #( \[y\] )? yeah you can add that
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""},

        {"description": "S for s with silent w", #answer
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI?"},

         {"description": "S for s with silent p", #conflicts with "uppsala" but psychotic has `HOT` → `hot` because of silent h so I don't mind
         "spelling": "ps",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI?"},

        {"description": "S for s spelt c (but historically had a y)", #the ce in pharmaceutical
         "spelling": "cc?e?",
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"},

        {"description": "S for voiced s",
         "spelling": "ss?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "steno theory": "WSI"},

        {"description": "S for soft c",
         "spelling": "s?c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "steno theory": "WSI?"},
        ],

    "STKPW": [
        {"description": "STKPW for z",
         "spelling": "zz?",
         "pronunciation": " z ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "I don't know but I seem to use it the most"}],

    #"ST-bg": [
    #    {"description": "ST-BG for -istic",
    #     "spelling": "istic",
    #     "pronunciation": " suffix  i  s  t  suffix  i  k ",
    #     "ambiguity": 0,
    #     "what must come before": slash,
    #     "steno theory": ""}],

    "SKWR": [
        {"description": "SKWR for j",
         "spelling": "j",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""},

        {"description": "SKWR for j sound",
         "spelling": "(g|dj|dgg?e?)",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""},

        {"description": "SKWR for zh sound spelt with a g/j",
         "spelling": "(d?jj?e?|d?gg?e?)",
         "pronunciation": " zh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "bonjour"},

        #{"description": "SKWR for d because Americans say j",
        # "spelling": "dd?",
        # "pronunciation": " d  y ",
        # "ambiguity": 0,
        # "what must come before": upToS,
        # "steno theory": ""}

        #{"description": "SKWR for d because Harri pronounces it j",
        # "spelling": "dd?",
        # "pronunciation": " d  \[y\] ",
        # "ambiguity": 1,
        # "what must come before": upToQ,
        # "steno theory": ""}
        ],

   "SKHR": [
        {"description": "SKHR for shr",
         "spelling": "shr",
         "pronunciation": " sh  r ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "Josiah"}],

    "SH": [
        {"description": "SH for sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"},

        {"description": "SH for sh sound with a weird spelling",
         "spelling": "((s|c|t|x)i|ce|che?|sc)", #sc like fascist?
         "pronunciation": " sh ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "steno theory": ""},

        {"description": "SH for ci that sounds like sh in Harri's accent",
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "Harri's accent"},

        {"description": "SH for s pronounced sh",
         "spelling": "ss?", #pressure
         "pronunciation": "( sh | s  y )",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"},

        {"description": "SH for s pronounced sh in Harri's accent (Essex?)",
         "spelling": "ss?", #assume
         "pronunciation": " s  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"},
         ],

    #"SHeup*": [
    #    {"description": "SH*EUP for -ship",
    #     "spelling": "sh",
    #     "pronunciation": " suffix  sh  i  p ",
    #     "ambiguity": 0,
    #     "what must come before": upToQ,
    #     "steno theory": "WSI"},
    #    ]_

    "SR": [
        {"description": "SR for v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"}],

    #"SO*pb": [
    #    {"description": "SO*PB for 'son' where the o is silent",
    #     "spelling": "son",
    #     "pronunciation": " s  n ",
    #     "ambiguity": 0,
    #     "what must come before": upToQ,
    #     "steno theory": "Harri"}],

    #"Se*pb": [
    #    {"description": "SE*PB for 'sen' where the e is silent",
    #     "spelling": "sen",
    #     "pronunciation": " s  n ",
    #     "ambiguity": 0,
    #     "what must come before": upToQ,
    #     "steno theory": "Harri"}],

    "S-pb": [
        {"description": "S-PB for 'son' where the o is silent",
         "spelling": "son",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "Harri"},

        {"description": "S-PB for 'sen' where the e is silent",
         "spelling": "sen",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "Harri"}],

    "T": [
        {"description": "T for t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"},
         
        {"description": "T for t even though Harri says ch",
         "spelling": "tt?", #attune
         "pronunciation": " t  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": ""}],

    #"Teu": [
    #    {"description": "TEU for suffix -ity",
    #     "spelling": "t?ty",
    #     "pronunciation": " suffix  @  t  iy ",
    #     "ambiguity": 0,
    #     "what must come before": upToS,

    #"Teuz": [
    #    {"description": "TEU for suffix -ity",
    #     "spelling": "t?ty",
    #     "pronunciation": " suffix  @  t  iy  suffix  z ",
    #     "ambiguity": 0,
    #     "what must come before": upToS

    "TK":[
        {"description": "TK for d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""},

        {"description": "TK for d even though Harri says j",
         "spelling": "dd?",
         "pronunciation": " d  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": ""}],

    "TKPW": [
        {"description": "TKPW for g",
         "spelling": "gg?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""}],

    "TKPH": [
        {"description": "TKPH for kn",
         "spelling": "kn",
         "pronunciation": " n ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "steno theory": ""}],

    "TP": [
        {"description": "TP for f",
         "spelling": "ff?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": upToK_no_T, #sphere
         "steno theory": ""},

        {"description": "TP for ph",
         "spelling": "ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": upToK_no_T, # sphere
         "steno theory": ""}],

    "TPW": [
        {"description": "TPW for inf",
         "spelling": "inf",
         "pronunciation": " i  n  f ",
         "ambiguity": 0,
         "what must come before": slash,
         "steno theory": "Josiah"}],

    "TPH": [
        {"description": "TPH for n",
         "spelling": "nn?",
         "pronunciation": " n ( \[y\] )?",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": ""},
         
         {"description": "TPH for g spelt gn",
         "spelling": "g?n",
         "pronunciation": " n ( y )?",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": ""}],

         #{"description": "TPH for ñ sound",
         #"spelling": "nn?",
         #"pronunciation": " n  y ",
         #"ambiguity": 1,
         #"what must come before": upToS,
         #"steno theory": ""}],

    "TH": [
        {"description": "TH for th",
         "spelling": "th",
         "pronunciation": " (th|dh) ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""}],

    "K": [
        {"description": "K for k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": ""},

        {"description": "K for hard c",
         "spelling": "cc?",  #acclimatise
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToS,
         "steno theory": ""},

        {"description": "K for hard c, maybe a y sound after depending on accent",
         "spelling": "cc?",  #barracuda
         "pronunciation": " k  \[y\] ",
         "ambiguity": 1,
         "what must come before": upToS,
         "steno theory": ""},

        {"description": "K for ch that sounds like k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToS,
         "steno theory": ""}],

    "KPW": [
        {"description": "KPW for imp",
         "spelling": "imp",
         "pronunciation": " i  m  p ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": ""},
        ],

    "KW": [
        {"description": "KW for q", #acquaint
         "spelling": "c?qu",  #combined with the `U` → `ui` in build, this is a nasty combination but I don't know a fix for it, I guess there's always two ways to read KWEU → qui
         "pronunciation": " k ( w )?", #briquette doesn't have a w
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": ""}],

    "KWR": [
        {"description": "KWR for y",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "StenEd?"},

        {"description": "KWR for y",
         "spelling": "y",
         "pronunciation": " y ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "StenEd?"},

        {"description": "KWR for y, but for some people it's silent???",
         "spelling": "y",
         "pronunciation": " \[y\] ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "StenEd?"},

        {"description": "KWR for i",
         "spelling": "i",
         "pronunciation": "( suffix )? (ii|ii2|y) ", #aerospacial
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""},

        {"description": "KWR for y (but this time it's a vowel??)",
         "spelling": "y",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "StenEd?"},

        {"description": "KWR for long e", #meteor the second e
         "spelling": "e",
         "pronunciation": " ii2 ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""}],

    "KWH": [
        {"description": "KWH for suffix",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 1,  # PWAEU/PWEU > PWAEUB/KWHEU
         "what must come before": slash_no_asterisk,
         "steno theory": "Harri"},

        {"description": "KWH instead of a consonant (Lapwing says you need a consonant to join to a previous stroke)",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 2,
         "what must come before": slash_no_asterisk_no__,
         "steno theory": "Harri"}],

    "KH": [
        {"description": "KH for ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": ""},

        {"description": "KH for t pronounced ch (even Americans do it for this word)",
         "spelling":"t",
         "pronunciation": " t ( suffix )? y ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "Harri?"}],


    "KHR": [ #because I've made HR illegal to follow K
        {"description": "KHR for cl",
         "spelling": "cc?l",
         "pronunciation": " k  l ",
         "ambiguity": 0,
         "what must come before": upToQ, #I just... THR → tl feels wrong. Oh this is kinda long, I also don't like k + space for vowel + l like #KHREU/TPORPB/KWHA... but it makes sense for collateral college collegial
         "steno theory": "WSI"},

        {"description": "KHR for coll",
         "spelling": "coll",
         "pronunciation": " k  (o|@)  l ",
         "ambiguity": 1,
         "what must come before": upToQ, #I just... THR → tl feels wrong. Oh this is kinda long, I also don't like k + space for vowel + l like #KHREU/TPORPB/KWHA... but it makes sense for collateral college collegial
         "steno theory": "WSI"}],

    #"Ka*l": [
    #    {"description": "KA*L for -ical",
    #     "spelling": "icall?",
    #     "pronunciation": " i  k  l ",
    #     "ambiguity": 0,
    #     "what must come before": slash,
    #     "steno theory": "Plover?"}],

    #"KA*el": [
    #    {"description": "KAEL for -ically, where the A is actually silent",
    #     "spelling": "ically",
    #     "pronunciation": " i  k  l  suffix  iy ",
    #     "ambiguity": 1,
    #     "what must come before": slash,
    #     "steno theory": "Lapwing (and this isn't a case of folding e, because `K-L` → `ical`"}],

    "P": [
        {"description": "P for p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "steno theory": "WSI"},

         {"description": "P for p (but British people say py?",
         "spelling": "pp?",
         "pronunciation": " p  \[y\] ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "steno theory": "WSI"}],

    "PW": [
        {"description": "PW for b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": upToK_no_S,
         "steno theory": "WSI"},
        ],

        #{"description": "PW for by spelt b", #butyl ?
        # "spelling": "bb?",
        # "pronunciation": " b  y ",
        # "ambiguity": 0,
        # "what must come before": ,upToK_no_S,
        # "steno theory": ""}],

    "PH": [
        {"description": "PH for m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "steno theory": "WSI"}],

    "W": [
        {"description": "W for w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "WSI"},

        {"description": "W for w written u",
         "spelling": "u",
         "pronunciation": " w ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "?"},
         
        {"description": "W for long u",
         "spelling": "u",
         "pronunciation": "( suffix )? y  uu ",
         "ambiguity": 0,
         "what must come before": upToK_not_just_K,
         "steno theory": "?"},

        {"description": "W for v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": SToK,
         "steno theory": ""},
        
        {"description": "folding W for w",
         "spelling": "ww?",
         "pronunciation": " (w|hw) ",
         "ambiguity": 1,
         "what must come before": H_to_R_no_W,
         "steno theory": "WSI"},],

    "WR": [
        {"description": "WR for wr (rite/right/write)",
         "spelling": "wr",
         "pronunciation": " r ",
         "ambiguity": 1,
         "what must come before": upToT,
         "steno theory": ""}],

    "WA": [
        {"description": "WA for oir sound",
         "spelling": "oir?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "Harri's Accent"},

        {"description": "WA for oir sound",
         "spelling": "oirr?e?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 1,
         "what must come before": upToK,
         "steno theory": "Harri's Accent"}],

    "H": [
        {"description": "H for h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "what must come before": upToW_no_P,
         "steno theory": "WSI"},

         {"description": "H for silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": upToW_no_P,
         "steno theory": "WSI"},


        {"description": "H for silent h depending on accent",
         "spelling": "h",
         "pronunciation": " \[h1\] ",
         "ambiguity": 0,
         "what must come before": upToW_no_P,
         "steno theory": "WSI"},
        ],

    "HR": [ #might be some logic for Commonwealth/United States spelling
        {"description": "HR for l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": upToW_not_just_T_not_just_k_or_just_w, #I just... THR → tl feels wrong. Oh this is kinda long, I also don't like k + space for vowel + l like #KHREU/TPORPB/KWHA... but it makes sense for collateral college collegial
         "steno theory": "WSI"},

        #{"description": "HR for ll",
        # "spelling": "ll",
        # "pronunciation": " l ",
        # "ambiguity": 1, #Alan Allan
        # "what must come before": upToW_no_T_not_just_k,
        # "steno theory": "WSI"},
         
        #{"description": "HR for suffix l",
        # "spelling": "ll?",
        # "pronunciation": " suffix  l ",
        # "ambiguity": 0,
        # "what must come before": slash, # ically is fine
        # "steno theory": ""},

        #{"description": "HR for al",
        # "spelling": "all?",
        # "pronunciation": " l ",
        # "ambiguity": 0,
        # "what must come before": slash, # ically is fine
        # "steno theory": ""}
        ],

    


    "R": [
        {"description": "R for r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": upToH_not_just_s,  #added up to H since THRU
         #personal opinion, but SR → s + r is ugly
         "steno theory": "WSI"},
         
        {"description": "R for rh",
         "spelling": "rr?h?",
         "pronunciation": " r ",
         "ambiguity": 1,
         "what must come before": upToH_not_just_s,  #added up to H since THRU
         #personal opinion, but SR → s + r is ugly
         "steno theory": ""}],

    "Re": [
        {"description": "RE for re",
         "spelling": "re",
         "pronunciation": " \(r  @/@r  r\) ",
         "ambiguity": 0,
         "what must come before": upToW,
         "steno theory": ""}],

    "A": [
        {"description": "A for short a",
         "spelling": "a",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "A for the pasta vowel",
         "spelling": "a",
         "pronunciation": " ao ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "pasta is a short vowel"},

        {"description": "A for the drama vowel",
         "spelling": "aa?",
         "pronunciation": " aa ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": "drama is a short vowel"},

        {"description": "A for the middle a in banana",
         "spelling": "aa?",
         "pronunciation": " oa ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "banana is all short vowels"},

        {"description": "A for silent a",
         "spelling": "a",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR, #guard shouldn't be "drop vowel, silent a"
         "steno theory": ""},
         
        {"description": "A for the a in graph (and actually I'm combining quite a few)",
         "spelling": "a",
         "pronunciation": " (ah|ah2) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing, #else AFT wouldn't be allowed
         "steno theory": ""},
         
        {"description": "A for short a (British accent, where Americans have long a)",
         "spelling": "a",
         "pronunciation": " (a/ee|ee/a) ", # ee/a patent/patent
         "ambiguity": 0,
         "what must come before": SToR_or_nothing, #else AFT wouldn't be allowed
         "steno theory": "British accent"}],

    "AO": [
        {"description": "AO for oa said like abroad",
         "spelling": "oa",
         "pronunciation": " oo ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": "I think StenEd?"},

        {"description": "AO for oa said like toad",
         "spelling": "oa",
         "pronunciation": " ou ",
         "ambiguity": 1, # toad/towed
         "what must come before": first_stroke_SToR_or_nothing,
         "steno theory": "I think StenEd?"},

        {"description": "AO for oo",
         "spelling": "oo",
         "pronunciation": " (u|uu) ", #uu is noon
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "I think StenEd?"}],

    "AOe": [
        {"description": "AOE for long e spelt ee",
         "spelling": "ee",
         "pronunciation": " (ii|ii2|ir) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e spelt ie",
         "spelling": "ie",
         "pronunciation": " (ii|ii2|ir) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e spelt i",
         "spelling": "i",
         "pronunciation": " (ii|ii2|ir) ",
         "ambiguity": 1, #why One? I don't know I can't think of any conflicts to be honest
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e spelt just e", #acne, aires
          "spelling": "e",
          "pronunciation" : " (ii|ii2|ir) ",
          "ambiguity": 1,
          "what must come before": SToR_or_nothing,
          "steno theory": ""},

        {"description": "AOE for long e spelt ea",
         "spelling": "ea",
         "pronunciation": " (ii|ii2|ir) ",
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e, but depending on your accent it could be a long i",
         "spelling": "(e?i|(a|e)y)",
         "pronunciation": " (ii/ae|ae/ii) ",
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e, but depending on your accent it could be a short e",
         "spelling": "e",
         "pronunciation": " (ii/e|eir/ir) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e spelt i, but depending on accent maybe you (*__*) pronounce it short i",
         "spelling": "i",
         "pronunciation": " (i/ii|ii/i) ", # n'ii/i'che b'ii/i'stro
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e, but depending on your accent it could be the vowel in bath?",
         "spelling": "a",
         "pronunciation": " aa/ei ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOE for long e but maybe it's two syllables?",
         "spelling": "ea",
         "pronunciation": " i@ ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},
         ],

    "AOeu": [
        {"description": "AOEU for long i",
         "spelling": "ie?", #acidifies
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "AOEU for long i spelt ei",
         "spelling": "ei", #acidifies
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "AOEU for long i spelt y",
         "spelling": "y",
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "StenEd?"},

        {"description": "AOEU for long i spelt ai", #Ainu, Aida, 
         "spelling": "ai",
         "pronunciation": keysymbol_shorthands["long i"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOEU for long i followed by a short e",
         "spelling": "ie",
         "pronunciation": keysymbol_shorthands["long i"] + " @ ",
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},
        ],


    #"AOeur": [
    #    {"description": "AOEUR for long i linked to an r",
    #     "spelling": "ia?rr?e?",
    #     "pronunciation": " aer  r ",
    #     "ambiguity": 0,
    #     "what must come before": SToR_or_nothing,
    #     "steno theory": ""}],

    "AOeu/KWRAOe": [
        {"description": "AOEU/KWRAOE for long i and long a spelt ai", #Ainu, Aida, 
         "spelling": "ai",
         "pronunciation": " ae  ii ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},
         ],

    "AOer": [
        {"description": "AOER for long e then r spelt ir",
         "spelling": "ir",
         "pronunciation": " ir  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""}],

    "AOu": [
        {"description": "AOU for long u",
         "spelling": "ue?",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

         {"description": "AOU for long u spelt ou",
         "spelling": "ou",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOU for long u spelt eau",
         "spelling": "eau",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOU for long u spelt ui",
         "spelling": "ui",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOU for long u spelt ew",
         "spelling": "ew",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 1, #nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AOU for long u spelt o (not using O for some reason)",
         "spelling": "o",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 1, #nute > nute, flew > flu, blew > blue... I do make the rules, and I'm power hungry
         "what must come before": SToR_or_nothing,
         "steno theory": "Lapwing"},
         ],

    "AOr": [
        {"description": "AOR for oar",
         "spelling": "oar",
         "pronunciation": " our  r ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": ""}],

    "Ae": [
        {"description": "AE for long e spelt ea, but only if it's the first stroke",
         "spelling": "ea",
         "pronunciation": " ii ",
         "ambiguity": 1,
         "what must come before": first_stroke_SToR_or_nothing,
         "steno theory": ""},

        {"description": "AE for short e spelt ea, but only if it's the first stroke",
         "spelling": "ea",
         "pronunciation": " e ",
         "ambiguity": 1,
         "what must come before": first_stroke_SToR_or_nothing,
         "steno theory": ""},

        {"description": "AE for short e spelt ea, but only if it's the first stroke",
         "spelling": "ea",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 1,
         "what must come before": first_stroke_SToR_or_nothing,
         "steno theory": ""},

        {"description": "AE for ae, ignoring pronunciation somewhat",
         "spelling": "ae",
         "pronunciation": " (ii|eir|ii/e) ",
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "steno theory": "Lapwing?"},

        {"description": "AE for long a spelt a_e, but only if it's the first stroke",
         "spelling": "a",
         "pronunciation": " ee ",
         "ambiguity": 2,
         "what must come before": first_stroke_SToR_or_nothing,
         "steno theory": " I don't know"},
         ],

    "Aeu": [
        {"description": "AEU for long a",
         "spelling": "a(a|ye?|i)?",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "AEU for the long a spelt with an e (I'm British)",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AEU for long a written et",
         "spelling": "ett?e?",
         "pronunciation": keysymbol_shorthands["long a"]+"$", #←←← look!!!! how cool!!!!!!   \($w$)/
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},


        {"description": "AEU for long a written with an e",
         "spelling": "ey?",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AEU for long a written with ei",
         "spelling": "ei",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AEU for long a written ea",
         "spelling": "ea",
         "pronunciation": keysymbol_shorthands["long a"],
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},
         ],


    #"Aer": [
    #    {"description": "AER for -ary",
    #     "spelling": "arr?(y|i)",
    #     "pronunciation": " \((@r/~  e|@r/e)\)  r  iy ", #this looks like an error, 'cause it is, but if it ain't broke don't fitcecoc
    #     "ambiguity": 1,
    #     "what must come before": SToR,
    #     "steno theory": "I think StenEd?"}],

    "Aer": [
        {"description": "AER for ary", #January actuary actuaries
         "spelling": "ar(y|ie)",
         "pronunciation": " \(@r/e\)  r  iy ",
         "ambiguity": 0,
         "what must come before": SToR,
         "steno theory": "I think StenEd?"}],


    "Au": [
        {"description": "AU for the vowel sound in daughter",
         "spelling": "aa?", #??? just keep it I guess
         "pronunciation": " oo ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AU for the au in because",
         "spelling": "au", #??? just keep it I guess
         "pronunciation": " (@|o/uh|o/oo) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "AU for the initial drama vowel",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  aa ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "drama is a long vowel"},

        {"description": "AU for a in alt",
         "spelling": "a",
         "pronunciation": " au ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "alt is AUL"},
         
        {"description": "AU for au spelling",
         "spelling": "au",
         "pronunciation": " (oo|ow|our) ", #`AU/RA` → `aura`
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},
        
        {"description": "AU for aw",
         "spelling": "awe?",
         "pronunciation": " (oo|ow|our) ", #`AU/RA` → `aura`
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        #{"description": "AU for al",
        # "spelling": "al",
        # "pronunciation": " aa ( \[l1\] )?",
        # "ambiguity": 0,
        # "what must come before": SToR_or_nothing,
        # "steno theory": ""},

        {"description": "AU for oa said like abroad",
         "spelling": "oa",
         "pronunciation": " oo ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri's accent"}],

    "Au_": [
        {"description": "AU for a in false",
         "spelling": "a",
         "pronunciation": " oo ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "false is AUL"}],

    "Aurb": [

        {"description": "AURB for arb",
         "spelling": "arb",
         "pronunciation": "("+keysymbol_shorthands["short vowels"]+"|"+keysymbol_shorthands["long vowels"]+")" + " r  b ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Josiah"}],

    "Af": [
        {"description": "AF for after", #I think this spills into raster
         "spelling": "after",
         "pronunciation": " ah  f  t  @r  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "StenEd?"}],

    "Afr/": [  # the / is there because of A*FRT/KWHOUGT → afterthought
        {"description": "AFR for the prefix after-",
         "spelling": "after",
         "pronunciation": " ah  f  t  @r  r  (compound|prefix) ",  #starting_root  ah  f  t  @r  r  suffix  w  @r  r  d 
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "StenEd?"}],

    "Ar": [
        {"description": "AR for long a followed by r",
         "spelling": "aa?rr?e?",
         "pronunciation": " ar  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Lapwing"},

        {"description": "AR for long a followed by r, spelt aur",
         "spelling": "uarr?e?",
         "pronunciation": " (ar|@r)  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Lapwing"},

        {"description": "AR for or sound spelt ar",
         "spelling": "arr?", #warring maybe?, athwart
         "pronunciation": " or  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Lapwing"},
        ],

    #"Al": [
    #    {"description": "AL for al (despite the silent a)",
    #     "spelling": "all?",
    #     "pronunciation": " l ",
    #     "ambiguity": 0,
    #     "what must come before": SToR_or_nothing,
    #     "steno theory": "WSI?"}],

    "O": [
        {"description": "O for o",
         "spelling": "o",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},


        {"description": "O for ow like knowledge",
         "spelling": "ow",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "O for o in Harri's accent",
         "spelling": "o",
         "pronunciation": " (au|our|our/or|o/uh) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri's accent"},

        {"description": "O for o (even though some people say owe)",
         "spelling": "o",
         "pronunciation": " oou ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri's accent"},

        {"description": "O for silent o",
         "spelling": "o",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        #{"description": "O for o even though it's pronounced with a schwa, discussion here: https://discord.com/channels/136953735426473984/1034561356361367683/1331201458279940178. However it's the same as almond, alopecia, and ameliorate, which I would do with a 'O'", #but   it's the same @ in "almond:", and alopecia, ameliorate
        # "spelling": "o",
        # "pronunciation": " @ ",
        # "ambiguity": 0,
        # "what must come before": SToR_or_nothing,
        # "steno theory": "Lapwing?"},

         ],

        #{"description": "O for o, even though it's not pronounced",
        # "spelling": "o",
        # "pronunciation": "",
        # "ambiguity": 1,
        # "what must come before": SToR_or_nothing,
        # "steno theory": "WSI"}],

    "Oe": [
        {"description": "OE for long o spelt o",
         "spelling": "oe?",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Lapwing?"},

        {"description": "OE for long o spelt ow",
         "spelling": "ow",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "OE for long o spelt au",
         "spelling": "au",  # baudelaire, aubergine
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri?"},

        {"description": "OE for long o spelt ou",
         "spelling": "ou",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 1, #bolder/boulder
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        #{"description": "OE for ough said like owe",
        # "spelling": "ough",
        # "pronunciation": " ouw ",
        # "ambiguity": 0,
        # "what must come before": SToR_or_nothing,
        # "steno theory": ""},

        {"description": "OE for oa said like owe",
         "spelling": "oa",
         "pronunciation": keysymbol_shorthands["long o"],
         "ambiguity": 0, #0 ambiguity because toad > towed... load >_< lode
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        # commenting out because of "tricotomy"?? # acrobatic?
        #{"description": "OE for unstressed o",
        # "spelling": "o",
        # "pronunciation": " @ ",
        # "ambiguity": 0,
        # "what must come before": SToR_or_nothing,
        # "steno is theory": "Lapwing?"}
        ],

    "Oeu": [
        {"description": "OEU for oi",
         "spelling": "oi",
         "pronunciation": " oi ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "OEU for oy",
         "spelling": "oy",
         "pronunciation": " oi ",
         "ambiguity": 1, #feel free to change this prioritisation
         "what must come before": SToR_or_nothing,
         "steno theory": ""}],

    "Oer": [
        {"description": "OER for -ory", #but some words like "auditory" it's not a . at all-grit micks suffix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
         "spelling": "or(y|ie)",
         "pronunciation": " \[our\]  r  iy ",
         "ambiguity": 1,
         "what must come before": SToR_but_not_KWH,
         "steno theory": "Harri?"},

        #{"description": "OER for the not a suffix -ory", #but some words like "auditory" it's not a suffix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # "spelling": "or(y|ie)",
        # "pronunciation": " \[our\]  r  iy ",
        # "ambiguity": 1,
        # "what must come before": just_KWH,
        # "steno theory": "Harri?"},
         ],

    "Oeg": [
        {"description": "OEG for ough said like owe",
         "spelling": "ough",
         "pronunciation": " ouw ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri?"},
         ],

    "O*u": [
        {"description": "O*U for owe in 'vowel'",
         "spelling": "owe",
         "pronunciation": " owr? ( e5 )?",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri"}],

    "Ou": [

        {"description": "OU for ou said like thought",
         "spelling": "ou",
         "pronunciation": " oo ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "OU for ow said like ow",
         "spelling": "ow",
         "pronunciation": " ow ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "OU for ou said like ow",
         "spelling": "ou",
         "pronunciation": " ow ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},
         ],

    "Or": [
        {"description": "OR for long o followed by r",
         "spelling": "orr?e?",
         "pronunciation": " or  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "OR for the 'or' in 'word'",
         "spelling": "or",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "OR for aur in dinosaur",
         "spelling": "aur?r",
         "pronunciation": " or  r ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": "Lapwing"},

        {"description": "OR for oar",
         "spelling": "oar?r",
         "pronunciation": " our  r ",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": ""}],

    "e": [
        {"description": "E for unstressed e",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""}, #not WSI because actresses that e is a @


        {"description": "E for short e spelt ea",
         "spelling": "ea",
         "pronunciation": " e ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": " I don't know"},

        #{"description": "E for a short long e spelt just e (I know that's confusing but it's an edge case", #abalone
        #commented this out because of the first e in meteor using it
        #  "spelling": "e",
        #  "pronunciation" : " ii ",
        #  "ambiguity": 1,
        #  "what must come before": SToR_or_nothing,
        #  "steno theory": "Harri"},

        {"description": "E for short e spelt ai (against)",
         "spelling": "ai",
         "pronunciation": " e ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": " I don't know"},

        {"description": "folding E for y (when *D is unusable)",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": A_then_vowels_that_make_asterisk_plus_d_not_usable,
         "steno theory": ""},


        {"description": "E folding for er when -R is already in use",
          "spelling": "err?",
          "pronunciation": "( suffix )? (@r|er)  r ",
          "ambiguity": 3,
          "what must come before": available_e_unavailable_r,
          "steno theory": ""},

        {"description": "E for short e, but depending on your accent it could be a long e",
         "spelling": "e",
         "pronunciation": " (ii/e|i/ii) ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},
          ],

    "e_": [
        {"description": "E for silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""}],

    "eu": [
        {"description": "EU for y said like long e",
         "spelling": "e?y",
         "pronunciation": " iy ", #(ii|ii2|ir)
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "I think StenEd?"},

        {"description": "EU for i said like long e, but like, short?",
         "spelling": "ee",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "EU for ii said like long e, but like, short?",
         "spelling": "ii",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "EU for i said like long e, but like, short?",
         "spelling": "ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "EU for i said like long e, but like, short?",
         "spelling": "i",
         "pronunciation": " iy ",
         "ambiguity": 1, #why One? I don't know I can't think of any conflicts to be honest
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "EU for i said like long e, but like, short?", #acne, aires
          "spelling": "e",
          "pronunciation" : " iy ",
          "ambiguity": 1,
          "what must come before": SToR_or_nothing,
          "steno theory": ""},

        {"description": "EU for i said like long e, but like, short?",
         "spelling": "ea",
         "pronunciation": " iy ",
         "ambiguity": 2,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "EU for i",
         "spelling": "i",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "I think StenEd?"},

        {"description": "EU for silent i",
         "spelling": "i",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        #{"description": "EU for i said like long e",
        # "spelling": "i",
        # "pronunciation": " (iy|ii|ii2|ir) ",
        # "ambiguity": 0,
        # "what must come before": SToR_or_nothing,
        # "steno theory": ""},

        {"description": "EU for y",
         "spelling": "y",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 1, #honestly this might be 0
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "EU for y said like uh",
         "spelling": "y",
         "pronunciation": " i2 ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "I think StenEd?"},

         {"description": "EU for short e spelt ui (is this just for build?)",
         "spelling": "ui",
         "pronunciation": " i ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": " I don't know"},
         
        {"description": "EU for short i but I think Americans use long a?",
         "spelling": "i",
         "pronunciation": " ai/i ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": " I don't know"},
        ],

    "eur": [
        {"description": "EUR for ir",
         "spelling": "ir",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR,
         "steno theory": ""}],

    #"eud": [
    #    {"description": "EUd for -ied",
    #     "spelling": "iedis",
    #     "pronunciation": " iy  suffix  d ",
    #     "ambiguity": 1,
    #     "what must come before": SToR,
    #     "steno theory": ""}],

    "euz": [
        {"description": "EUZ for -ies",
         "spelling": "ies",
         "pronunciation": " iy  suffix  z ",
         "ambiguity": 1,
         "what must come before": SToR,
         "steno theory": ""}
         ],

    "eu/KWHe": [
        {"description": "EU/KWHE for ie",
         "spelling": "ie",
         "pronunciation": " iy $",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri"}],

    "er": [
        {"description": "ER for er",
         "spelling": "err?",
         "pronunciation": "( (@r|er)  r | \(r  @/@r  r\) )", #sometimes (r  @/@r  r) like that whole thing is just in there
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "folding ER for er when E is free",
         "spelling": "err?",
         "pronunciation": "( suffix )?( (@r|er)  r | \(r  @/@r  r\) )",
         "ambiguity": 1,
         "what must come before": skipsAnEUInTheVowels_no_r, #replaced the logic ".*[AO](?!.*(.).*\1)[fpblgtsdz]*\*?"
         "steno theory": "Harri"}],

    "u": [
        {"description": "U for u",
         "spelling": "u",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI"},

        {"description": "U for ou in borough",
         "spelling": "ou",
         "pronunciation": " ouw?1 ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": "Harri"},

        {"description": "U for ou",
         "spelling": "ou",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": "WSI?"},
         
        {"description": "U for silent u",
         "spelling": "u",
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},
        ],

    "ur": [
        {"description": "UR for ur",
         "spelling": "urr?e?",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""},

        {"description": "UR for our",
         "spelling": "our",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": SToR_or_nothing,
         "steno theory": ""}],

    "-rb": [ #that - is part of it
        {"description": "-RB for 'shure'",
         "spelling": "(ss?|z)ure", #seizure, pleasure, measure, pressure, leisure
         "pronunciation": " (s|z)  y  @r  r ",
         "ambiguity": 1,
         "what must come before": SToR_but_not_KWH,
         "steno theory": "Harri theory"}],
         

    "f":[
        {"description": "-F for f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": A_to_u_, #`PHER/SEUFL` → `merciful`, with suffix=_
         "steno theory": "WSI"},

        {"description": "-F for gh", #laugh?
         "spelling": "ph",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": ""},

        #{"description": "-F for gh", #laugh?
        # "spelling": "gh",
        # "pronunciation": " f ",
        # "ambiguity": 1,
        # "what must come before": A_to_u,
        # "steno theory": ""},

        {"description": "folding -F for v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 1,
         "what must come before": l_,
         "steno theory": ""},
        ],

    "f_":[ #there's logic where anything ending in a _ cannot be followed by a new stroke
        {"description": "-F for s",
         "spelling": "ss?e?",
         "pronunciation": " (s|z) ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"},

        {"description": "-F for c",
         "spelling": "s?ce?",
         "pronunciation": " (s|z) ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"},

        {"description": "-F for v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"},

        {"description": "folding -F for s", #first accurst, but not saurus
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": r_,
         "steno theory": ""}
         ],

    "*f_":[
        {"description": "*F for z",
         "spelling": "zz?e?",
         "pronunciation": " (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "Harri"}],


    #"/-f":[
    #    {"description": "\-F for f",
    #     "spelling": "fe?",
    #     "pronunciation": " f ",
    #     "ambiguity": 0,
    #     "what must come before": l_,
    #     "steno theory": "It's in Main.json, TKWAR/-F"}
    #    ],

    "fr_":[
        {"description": "-FR for m",
         "spelling": "m",
         "pronunciation": " m ",
         "ambiguity": 2,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"}],

    #"frp":[
    #    {"description": "-FRP for mp",
    #     "spelling": "mp",
    #     "pronunciation": " m  p ",
    #     "ambiguity": 1,
    #     "what must come before": A_to_u,
    #     "steno theory": "I think StenEd?"}],

    "frpb": [
        {"description": "FRPB for nch (conflicts with -rch)",
         "spelling": "nche?",
         "pronunciation": " n  ch ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "StenEd?"}],

    "fpb": [
        {"description": "-FPB for ch following an r (conflicts with -nch)",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": r_,
         "steno theory": "StenEd?"}],


    #"frpblg": [
    #    {"description": "-FRPBG for nkl",
    #     "spelling": "n(c|k)le?",
    #     "pronunciation": " ng  k  l ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_u,
    #     "steno theory": "WSI"}],

    "frpbg": [
        {"description": "-FRPBG for nk",
         "spelling": "nk",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "Miff?"},

        {"description": "-FRPBG for nc",
         "spelling": "nc",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "Miff?"}],

    "frpbgs": [
        {"description": "-FRPBGS for nk + shn",
         "spelling": "nction",
         "pronunciation": " ng  k  sh  suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "Harri? I think I'm the only person to have thought of it?"},


        {"description": "-FRPBGS for nx",
         "spelling": "nx",
         "pronunciation": " ng  k  s ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "Harri? I think I'm the only person to have thought of it?"}
         ],

    "*fb":[
        {"description": "folding *FB after an -R for f sound",
         "spelling": "(f|ph)",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": r_no_asterisk,
         "steno theory": "Lapwing"}],

    #"ft":[
    #    {"description": "-FT for ft",
    #     "spelling": "ft",
    #     "pronunciation": " f  t ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_u,
    #     "steno theory": "WSI"},

    #    {"description": "-FT for st",
    #     "spelling": "st",
    #     "pronunciation": " s  t ",
    #     "ambiguity": 1,
    #     "what must come before": A_to_u,
    #     "steno theory": "WSI"}],
    "fp":[
        {"description": "-FP for ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": ""},

        {"description": "-FP for tch",
         "spelling": "tch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": ""}],

    "fpl":[
        {"description": "-FPL for -some suffix",
         "spelling": "some",
         "pronunciation": " suffix  s  m ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": ""}],

    #"fplt":[
    #    {"description": "-F for s then -PLT for suffix -ment",
    #     "spelling": "sement",
    #     "pronunciation": " s suffix  m  e5  n  t ",
    #     "ambiguity": 1,
    #     #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
    #     "what must come before": A_to_u,
    #     "steno theory": ""}],

    "fb":[
        {"description": "-FB for v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "Josiah?"}],

    #"/-fb":[
    #    {"description": "\-FB for v",
    #     "spelling": "ve?",
    #     "pronunciation": " v ",
    #     "ambiguity": 0,
    #     "what must come before": l_,
    #     "steno theory": "Harri"}
    #    ],

    "fl":[
        {"description": "-FL for -ful suffix",
         "spelling": "ful",
         "pronunciation": " suffix  f  l ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": ""}],

    "fg":[
        {"description": "-FG for gh",
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "Harri"}],

    "*fg":[
        {"description": "*FG for ghing",
         "spelling": "ghing",
         "pronunciation": " f  suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "Harri"}],

    #"fs":[
    #    {"description": "-FS for double s",
    #     "spelling": "ss",
    #     "pronunciation": " s ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_u, #no idea, this just feels right
    #     "steno theory": "Harri"}],

    "r": [
        {"description": "-R for r",
         "spelling": "rr?e?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": A_to_f_,
         "steno theory": "WSI"},

        {"description": "folding -R for re",
         "spelling": "re",
         "pronunciation": "( suffix )? (\(r  @/@r  r\)|@r  r) ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_r,
         "steno theory": ""},

        {"description": "folding -R for ro",  # acrobatics
         "spelling": "ro",
         "pronunciation": " r  @ ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_r,
         "steno theory": ""},

        {"description": "folding -R for suffix er when E is unavailable",
         "spelling": "err?",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 2,
         "what must come before": unavailable_e_no_r,
         "steno theory": "Harri"},


        {"description": "folding -R for ar? I'll do it when E is unavailable for some reason",
         "spelling": "arr?", # friar
         "pronunciation": " r ",
         "ambiguity": 3,
         "what must come before": unavailable_e_no_r, #reusing cause I'm lazy
         "steno theory": "Harri"},

        {"description": "folding -R for or? I'll do it when E is unavailable for some reason",
         "spelling": "orr?",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 3,
         "what must come before": unavailable_e_no_r, #reusing cause I'm lazy
         "steno theory": "Harri"}], 

    "rb": [
        {"description": "-RB for sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": A_to_f_,
         "steno theory": "StenEd?"},

        {"description": "-RB for ci that sounds like sh in Harri's accent", # aerospacial
         "spelling": "ci",
         "pronunciation": "( s ( suffix )? y | sh  \[ii\] )",
         "ambiguity": 0,
         "what must come before": A_to_f_,
         "steno theory": "Harri's accent"},

        {"description": "-RB for sh sound with a weird spelling",
         "spelling": "((s|c|t|x)i|ce|che?|sc)",
         "pronunciation": " sh ",
         "ambiguity": 1,
         "what must come before": A_to_f_,
         "steno theory": "StenEd?"},
         ],

    "rb_": [
        #conscious abstentious anxious?
        {"description": "-RB for nsh sound",
         "spelling": "n(sc|t|x)i", #x for anxious
         "pronunciation": " n  sh ",
         "ambiguity": 1,
         "what must come before": A_to_f_,
         "steno theory": "Harri"},

        {"description": "-RB for ngksh sound",
         "spelling": "n(sc|t|x)i", #xi for anxious,
         "pronunciation": " ng ( k )? sh ",
         "ambiguity": 1,
         "what must come before": A_to_f_,
         "steno theory": "Harri"},
         ],


    #"rbs": [  
        
    #    {"description": "-RBS for shus sound",
    #     "spelling": "(sc|t|x)ious", #x for anxious
    #     "pronunciation": " sh  @  s ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_u,
    #     "steno theory": "StenEd?"},
        
        
    #    {"description": "-RBS for vowel + nshus sound",
    #     "spelling": "n(sc|t|x)ious", #x for anxious
    #     "pronunciation": "( ng  k | n ) sh  @  s ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_u,
    #     "steno theory": "Plover?"}],

    "rbl": [
        {"description": "-RBL for -shable",
         "spelling": "shable?",
         "pronunciation": " sh  suffix  @  b  l ",
         "ambiguity": 1,
         "what must come before": A_to_f,
         "steno theory": "Harri"}],



    #"/-rbs": [
    #    {"description": "-RBS for shus sound",
    #     "spelling": "(sc|t|x)ious", #x for anxious
    #     "pronunciation": " sh  @  s ",
    #     "ambiguity": 0,
    #     "what must come before": after_f,
    #     "steno theory": "StenEd?"}],

    "p": [
        {"description": "-P for p",
         "spelling": "pp?e?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": A_to_r_, #".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "steno theory": ""}],

    "pb": [
        {"description": "-PB for n",
         "spelling": "(e|o)?nn?e?",
         "pronunciation": " n ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": ""},

        {"description": "-PB for suffix n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": ""},

        {"description": "-PB for gn",
         "spelling": "gn",
         "pronunciation": " n ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": ""},

        {"description": "folding -PB for suffix en",
         "spelling": "en",
         "pronunciation": " suffix  \[e5\]  n ",
         "ambiguity": 1,
         "what must come before": l_to_z_no_porb,
         "steno theory": ""}],

    "/-pb": [
        {"description": "-PB for suffix n",
         "spelling": "n",
         "pronunciation": " suffix  n ",
         "ambiguity": 0,
         "what must come before": after_r,
         "steno theory": "WSI?"}],

    #"pbl": [
    #    {"description": "-PBL for nal (despite the silent a)",
    #     "spelling": "nall?", #abdominally
    #     "pronunciation": " n  l ",
    #     "ambiguity": 1,
    #     "what must come before": A_to_r_,
    #     "steno theory": "WSI?"}],

    "pblg": [
        {"description": "-PBLG for j sound",
         "spelling": "(j|dj|d?gg?)e?",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": "WSI?"},

         {"description": "-PBLG for zh sound",
         "spelling": "(j|dj|d?gg?)e?",
         "pronunciation": " zh ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": ""}], #arbitrage


    "pbg": [
        {"description": "-PBG for ng",
         "spelling": "ng?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "WSI"},

        {"description": "-PBG for nge in singe", #funny example cause of course `SEUPBG` → `sing`, but `ORPBG` → `orange`
         "spelling": "nge?",
         "pronunciation": " n  jh ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": "WSI"},

        {"description": "-PBG for ng and g",
         "spelling": "ng?",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": "WSI"}],

    "pbgs": [
        {"description": "-PBGS for nx",
         "spelling": "nx",
         "pronunciation": " ng  g  z ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "WSI"}],

    "pbg/S": [
        {"description": "-PBG/S for nx",
         "spelling": "nx",
         "pronunciation": " ng  g  z ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "WSI"}],

    #"pb/SH": [
    #    {"description": "-PB/SH for nsh sound", #if there even is one?
    #     "spelling": "n(sc|t|x)i",
    #     "pronunciation": " n  sh ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_r_,
    #     "steno theory": ""}],
    "pbg/SH": [
        {"description": "-PBG/SH for ngsh sound", #if there even is one?
         "spelling": "n(sc|t|x)i",
         "pronunciation": " ng  sh ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": ""}],
    "frpbg/SH": [
        {"description": "-FRPBG/SH for ngksh sound", #if there even is one?
         "spelling": "n(sc|t|x)i",
         "pronunciation": " ng  k  sh ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": ""}],



    #"/-pbs": [
    #    {"description": "-PBS for suffix -ness",
    #     "spelling": "ness",
    #     "pronunciation": " suffix  n  E5  s ",
    #     "ambiguity": 0,
    #     "what must come before": after_r,
    #     "steno theory": "I think StenEd?"},

    #    {"description": "-PBS for suffix -y then suffix -ness",
    #     "spelling": "yness",
    #     "pronunciation": " suffix  (iy|i2)  suffix  n  E5  s ",
    #     "ambiguity": 1,
    #     "what must come before": after_r,
    #     "steno theory": "I think StenEd?"}],

    #"pbs": [
    #    {"description": "-PBS for suffix -ness",
    #     "spelling": "ness",
    #     "pronunciation": " suffix  n  E5  s ",
    #     "ambiguity": 1,
    #     "what must come before": A_to_r_,
    #     "steno theory": "I think StenEd?"},

    #     {"description": "-PBS for suffix -y then suffix -ness",
    #     "spelling": "yness",
    #     "pronunciation": " suffix  (iy|i2)  suffix  n  E5  s ",
    #     "ambiguity": 2,
    #     "what must come before": A_to_r_,
    #     "steno theory": "I think StenEd?"},

        #{"description": "folding -PBS for suffix -ness",
        # "spelling": "ness",
        # "pronunciation": " suffix  n  E5  s ",
        # "ambiguity": 1,
        # "what must come before": A_to_z_no_pbs,
        # "steno theory": "I think StenEd?"},

        #{"description": "folding -PBS for suffix -y then suffix -ness",
        # "spelling": "yness",
        # "pronunciation": " suffix  (iy|i2)  suffix  n  E5  s ",
        # "ambiguity": 2,
        # "what must come before": A_to_z_no_pbs,
        # "steno theory": "I think StenEd?"}
    #    ],

    "pl": [
        {"description": "-PL for m",
         "spelling": "mm?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "WSI"},

        {"description": "-PL for mb silent b",
         "spelling": "mb",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "StenEd?"},

        {"description": "-PL for mp silent p",
         "spelling": "mp",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "StenEd?"},

        {"description": "-PL for mn silent n",
         "spelling": "mn",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "StenEd?"},

        {"description": "-PL for lm silent l (has to follow AU)",
         "spelling": "lm",
         "pronunciation": "( \[l1\] )? m ",
         "ambiguity": 0,
         "what must come before": Au,
         "steno theory": "StenEd?"},

        {"description": "folding -PL for uhm sound",
         "spelling": "m(b|m)?e?",
         "pronunciation": " @  m ",
         "ambiguity": 0,
         "what must come before": t_no_pl,
         "steno theory": "WSI"},
         ],

    "*pz": [
        {"description": "*PZ for h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "what must come before": A_to_r_no_asterisk,
         "steno theory": "Josiah"},

        {"description": "*PZ for silent h",
         "spelling": "h",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": A_to_r_no_asterisk,
         "steno theory": "Josiah"}],

    "plt":[
        {"description": "-PLT for -ment",
         "spelling": "ment",
         "pronunciation": "( suffix )? m  e5  n  t ",
         "ambiguity": 0,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_r_,
         "steno theory": ""},

         {"description": "-PLT for t then suffix -ment",
         "spelling": "tment",
         "pronunciation": " t  suffix  m  e5  n  t ",
         "ambiguity": 2,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_r_,
         "steno theory": ""}],

         #{"description": "folding -PLT for suffix -ment",
         #"spelling": "ment",
         #"pronunciation": " suffix  m  e5  n  t ",
         #"ambiguity": 1,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         #"what must come before": A_to_z_no_plt,
         #"steno theory": ""}],

    "b": [
        {"description": "-B for b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": A_to_u, #this chord can only can after a vowel, so it's Josiah since `KAURB` → `carb`
         "steno theory": "Josiah"},

        {"description": "-B for b (following an -R)",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 1,
         "what must come before": ends_in_r,
         "steno theory": "WSI"}],

    "bl": [
        {"description": "-BL for bil where the etymology is from 'able' (which doesn't have an i)",
         "spelling": "ble?",
         "pronunciation": " b  i  l ",
         "ambiguity": 0,
         "what must come before": A_to_p_, 
         "steno theory": "Josiah"}],

        #{"description": "EU for i sound",
        # "spelling": "",
        # "pronunciation": " i ", #sorry I forgot what this actually was don't be mad
        # "ambiguity": 0,
        # "what must come before": SToR_or_nothing,
        # "steno theory": ""},

    "bg": [
        {"description": "-BG for k",
         "spelling": "k(k|e)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": ""},

        {"description": "-BG for ck",
         "spelling": "cke?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": ""},

        {"description": "-BG for k sound spelt ch",
         "spelling": "che?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": ""},

        {"description": "-BG for k sound, spelt lk (immediately after a vowel)",
         "spelling": "lk",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": ""},

        {"description": "-BG for c", #do I make *BG? pick pic?
         "spelling": "c(c|e)?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": A_to_p_,
         "steno theory": ""},

        {"description": "-BG for qu", #do I make *BG? pick pic?
         "spelling": "que?",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": A_to_p_,
         "steno theory": ""}],

    "bgs": [
        {"description": "-BGS for x",
         "spelling": "xe?", #axe
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": ""}],

    "*bgs": [
        {"description": "*BGS for ction",
         "spelling": "ction",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "Harri"}],

    "bg/S": [
        {"description": "-BG/S for x",
         "spelling": "x",
         "pronunciation": "( k  s | g  z )",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "Lapwing"}],

    "bg/TKPW": [ #blackguard
        {"description": "-BG/TKPW for ckg pronounced g",
         "spelling": "ckg",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "Harri"}],

    "bg/W": [
        {"description": "-BG/W for cqu", #`ABG/WAOE/KWHES` → `acquiesce`
         "spelling": "cqu",
         "pronunciation": " k  w ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": ""}],

    "l":[
        {"description": "-L for l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_b_not_just_p, #surely this should then work for "level"??
         "steno theory": "WSI"},

         {"description": "-L for le",
         "spelling": "ll?e",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_b_not_just_p, #surely this should then work for "level"??
         "steno theory": "WSI"},

         {"description": "-L for el",
         "spelling": "ell?e",
         "pronunciation": " l ",
         "ambiguity": 1,
         "what must come before": A_to_b_not_just_p, #surely this should then work for "level"??
         "steno theory": "WSI"},

         {"description": "-L for al",
         "spelling": "all?e?",
         "pronunciation": " @  l ", #silent a is already a thing
         "ambiguity": 1,
         "what must come before": A_to_b_not_just_p, #surely this should then work for "level"??
         "steno theory": "WSI"},

        {"description": "-L for suffix -al",
         "spelling": "al",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "what must come before": A_to_b_not_just_p,
         "steno theory": "WSI?"},


        {"description": "-L for suffix -l", #antibacterial
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "WSI?"},

        #{"description": "folding -L for l",
        # "spelling": "ll?e?",
        # "pronunciation": " l ",
        # "ambiguity": 1,
        # "what must come before": A_to_z_no_l_not_bg,
        # "steno theory": ""},

        #{"description": "-L for -ly",
        # "spelling": "ly",
        # "pronunciation": " suffix  l  iy ",
        # "ambiguity": 2,
        # "what must come before": A_to_b_not_just_p,
        # "steno theory": ""},

        #{"description": "folding -L for -ly",
        # "spelling": "ly",
        # "pronunciation": " suffix  l  iy ",
        # "ambiguity": 2,
        # "what must come before": A_to_z_no_l_not_bg, #*BLG → ckle
        # "steno theory": ""}
        ],


    "*l":[
        {"description": "*L for folding l",
         "spelling": "ll?e?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": after_l_no_asterisk_or_l,
         "steno theory": "Harri"},#*BLG → ckle

        #{"description": "*L for folding -ly",
        # "spelling": "ly",
        # "pronunciation": " suffix  l  iy ",
        # "ambiguity": 1,
        # "what must come before": after_l_no_asterisk_or_l, 
        # "steno theory": "Harri"}
        ],

    "-l":[
        {"description": "-L for -le",
         "spelling": "le",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": SToR, #cause this includes the -
         "steno theory": "Lapwing?"}],


    "/-l":[

        {"description": "/-L for -le",
         "spelling": "le",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": p_or_l_to_z,
         "steno theory": "Lapwing?"},

        #{"description": "-L for suffix l",
        # "spelling": "l",
        # "pronunciation": " suffix  l ",
        # "ambiguity": 0,
        # "what must come before": after_l_no_l,
        # "steno theory": "WSI"}
        ],

    "/-g":[
        {"description": "-G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": g_and_dz,
         "steno theory": "WSI"}],

    "*g":[
        {"description": "*G for gue", #mulch/mulk or something
         "spelling": "gue",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before":  A_to_r_no_asterisk, #picked to r... no particular reason
         "steno theory": "Harri"},

        {"description": "*G for k", #mulch/mulk or something
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": l_no_asterisk,
         "steno theory": "StenEd"},

        {"description": "*G for ch",
         "spelling": "ch",
         "pronunciation": " ch ",
         "ambiguity": 0,
         "what must come before": l_no_asterisk,
         "steno theory": "Harri"}],

    "g":[
        {"description": "-G for g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": A_to_l_not_just_b,
         "steno theory": "WSI"},

        {"description": "-G for g (pronounced j) following an l",
         "spelling": "gg?e?",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "what must come before": l_,
         "steno theory": "StenEd?"},

        {"description": "-G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_p_, #← look at that lack of _ at the end
         #okay the issue here is that maybe there's no issue
         "steno theory": "WSI"},

        {"description": "-G for silent gh",
         "spelling": "gh",
         "pronunciation": "",
         "ambiguity": 1,
         "what must come before":
         A_to_p,
         "steno theory": "Harri?"},

        {"description": "folded -G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": after_g_no_g,
         "steno theory": "WSI"}],

    "gt": [
        #{"description": "-GT for -ght",
        # "spelling": "ght",
        # "pronunciation": " t ",
        # "ambiguity": 0,
        # "what must come before": A_to_l_,
        # "steno theory": "Phoenix"},
        
        {"description": "-GT for -xt",
         "spelling": "xt",
         "pronunciation": " k  s  t ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "steno theory": "StenEd"},
         ],


    "gs": [
        {"description": "-GS for tion",
         "spelling": "tion",
         "pronunciation": "( suffix )? sh ( suffix )? n ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "steno theory": "I think StenEd?"},

        {"description": "-GS for sion",
         "spelling": "s?sion", #double s for accession
         "pronunciation": "( suffix )? (zh|sh|sh/zh) ( suffix )? n ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "steno theory": "I think StenEd?"},
         
         {"description": "-GS for cian",
         "spelling": "cian",
         "pronunciation": " s ( suffix )? y  @  n ", # beautician isn't with a suffix
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "steno theory": "I think StenEd?"}],

        #{"description": "-GS for sion",
        # "spelling": "deion", #listen I don't make the rules I just write them
        # "pronunciation": " zh ( suffix )? n ",
        # "ambiguity": 0,
        # "what must come before": A_to_l_,
        # "steno theory": "I think StenEd?"}],

    "t":[
        {"description": "-T for t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "steno theory": ""},

        {"description": "-T for t even though it's pronounced with an sh sound",
         "spelling": "tt?e?",
         "pronunciation": " sh ",
         "ambiguity": 2, #so it doesn't win against abtentious
         "what must come before": A_to_g_,
         "steno theory": ""}],

    "*t":[
        {"description": "*T for th",
         "spelling": "the?",
         "pronunciation": " (th|dh|dh/th) ",
         "ambiguity": 1, #giving it a 1 for personal reasons lol
         "what must come before": A_to_g_no_asterisk,
         "steno theory": "StenEd"},

         {"description": "*T for -th suffix",
         "spelling": "the?",
         "pronunciation": " suffix  (th|dh|dh/th) ",
         "ambiguity": 1, #giving it a 1 for personal reasons lol
         "what must come before": A_to_g_no_asterisk,
         "steno theory": "StenEd?"},
         ],

    "ts":[
        {"description": "-TS for t + s (when it's not a plural!)",
         "spelling": "tt?e?s",
         "pronunciation": " t  s ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "steno theory": ""}],

    "*td":[
        {"description": "*TD for dth",
         "spelling": "dthe?",
         "pronunciation": " (t|d)  (th|dh|dh/th) ",
         "ambiguity": 1, #giving it a 1 for personal reasons lol
         "what must come before": A_to_g_no_asterisk,
         "steno theory": "StenEd"},

        #worthy
        {"description": "*T for th, overlaid with *D for y",
         "spelling": "th(y|i)",
         "pronunciation": " (th|dh) ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": A_to_g_no_asterisk,
         "steno theory": "Harri?"}],


    #"/-s":[
    #    {"description": "-S for plurals",
    #     "spelling": "s",
    #     "pronunciation": "( (suffix) ) z ",
    #     "ambiguity": 1,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],
        
    "s":[
        {"description": "-S for se or ss",
         "spelling": "s(s|e)", #actresses?"
         "pronunciation": " s ",
         "ambiguity": 0,
         #cyclops
         "what must come before": A_to_t_, #A_to_t_no_g_end, #no idea, this just feels right. or maybe A_to_t_
         "steno theory": ""},

        {"description": "-S for s on its own immediately following a vowel",
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         #cyclops
         "what must come before": A_to_u_or__, #dis
         "steno theory": "cyclops with a -Z"},

         {"description": "-S for s on its own immediately following a vowel (I don't know if you voice it or not)",
         "spelling": "s",
         "pronunciation": " z/s ",
         "ambiguity": 0,
         #cyclops
         "what must come before": A_to_u_or__, #dis
         "steno theory": "cyclops with a -Z"},

        
        #{"description": "-Z for unvoiced s",
        # "spelling": "s",
        # "pronunciation": " s ",
        # "ambiguity": 0,
        # "what must come before": r_to_t__, #no idea, this just feels right
        # "steno theory": "WSI"},

         {"description": "-S for unvoiced s with silent t",
         "spelling": "ss?te?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_t_no_g_end, #no idea, this just feels right
         "steno theory": ""},

        {"description": "-S for s with silent w", #answer
         "spelling": "sw",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_t_no_g_end,
         "steno theory": ""},


        {"description": "-S for unvoiced c",
         "spelling": "s?ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": A_to_t_no_g_end, #maybe I'm traumatised from ABGS/HRERPL/TER → accelerometer
         "steno theory": "WSI"},

        {"description": "-S for maybe voiced s",
         "spelling": "ss?e?",
         "pronunciation": " z/s ",
         "ambiguity": 1,
         "what must come before": A_to_t, #no _ I think?
         "steno theory": "WSI"},

        {"description": "-S for voiced s",
         "spelling": "ss?e?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "what must come before": A_to_t, #no _ I think?
         "steno theory": "WSI"},

        {"description": "-S for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) ) (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_g_yes_t,
         "steno theory": "WSI"}],

    "*s":[
        {"description": "*S for 's",
         "spelling": "'s",
         "pronunciation": " suffix  (s|z) ",
         "ambiguity": 2,
         "what must come before": A_to_t_no_asterisk,
         "steno theory": " Josiah"},

        #{"description": "*S for voiced s",
        # "spelling": "ss?e?",
        # "pronunciation": " z ",
        # "ambiguity": 0,
        # "what must come before": A_to_t_no_asterisk,
        # "steno theory": "Harri?"},
         
        {"description": "*S for suffix -ise",
         "spelling": "ise?",
         "pronunciation": " suffix  ae  z ",
         "ambiguity": 1,
         "what must come before": A_to_t_no_asterisk,
         "steno theory": "Harri?"},

        {"description": "*S for st after a -G or -T",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 1,
         "what must come before": ends_in_b_to_t_no_asterisk,
         "steno theory": ""}
         ],

    "/-d": [
        {"description": "-D for -ed",
         "spelling": "ed",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 0,
         "what must come before": yes_s,
         "steno theory": "WSI"}],

    "d": [
        {"description": "-D for d",
         "spelling": "dd?e?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": A_to_t_,
         "steno theory": ""},

        {"description": "-D for d",
         "spelling": "dd?e?",
         "pronunciation": " d/t ",
         "ambiguity": 0,
         "what must come before": A_to_t_,
         "steno theory": ""},

        {"description": "-D for -ed",
         "spelling": "e?d",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 1,
         "what must come before": A_to_t,
         "steno theory": "WSI"}],

        #{"description": "folding -D for -ed",
        # "spelling": "e?d",
        # "pronunciation": " suffix ( i7 )? (d|t) ",
        # "ambiguity": 1,
        # "what must come before": A_to_z_no_d,
        # "steno theory": "WSI"}],

    "*d": [
        {"description": "*D for y",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": A_to_t_no_asterisk,
         "steno theory": "Harri"},

        {"description": "*D for y (said like short i)",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "what must come before": A_to_t_no_asterisk,
         "steno theory": "Harri"},

        {"description": "*D for dy",
         "spelling": "dd?y",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "what must come before": A_to_t_no_asterisk,
         "steno theory": "HelloChap? I can't remember"}],

    "dz": [
        {"description": "-DZ for d + s not a plural!",
         "spelling": "dd?e?s",
         "pronunciation": " d  z ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "steno theory": "WSI"},

        {"description": "-DZ for suffix ing when G is taken",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": A_to_g_yes_b_or_g,
         "steno theory": "WSI"}],

    #"/-z":[
    #    {"description": "-Z for plurals",
    #     "spelling": "s",
    #     "pronunciation": "( (suffix) )( i7 )? (s|#z) ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],

    "z":[
        {"description": "-Z for solo s following a consonant",
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": f_to_z__not_just_t, #dis
         "steno theory": "cyclops with a -Z"},

        {"description": "-Z for plurals", #actresses
         "spelling": "s",
         "pronunciation": " suffix ( i7 )? (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_d_no_t,
         "steno theory": "WSI"},

        #{"description": "-Z for what looks like a plural",
        # "spelling": "s", #"e?s"?
        # "pronunciation": " z $",
        # "ambiguity": 1,
        # "what must come before": A_to_d_no_t,
        # "steno theory": "WSI"},

        #{"description": "-Z for voiced s", #this is only for onestrokes I think?
        # "spelling": "e?s",
        # "pronunciation": " (z) ",
        # "ambiguity": 1,
        # "what must come before": A_to_d_no_t,
        # "steno theory": "WSI"}
         ],


    "*z":[
        {"description": "*Z for -st following -D",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 0,
         "what must come before": ends_in_d_no_asterisk,
         "steno theory": "Harri?"},

        {"description": "*Z for z",
         "spelling": "zz?e?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "what must come before": A_to_d_no_t,
         "steno theory": "Harri"},
         ],




























    #################### here's all the suffixes

    "SH*eur": [
        {"description": "SH*EUR for -shire (this feels like a suffix but it's actually not, also Americans overpronounce the  'ire' bit)",
         "spelling": "shire",
         "pronunciation": " sh  aer1  r ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Harri"}],

    "SH*eup": [
        {"description": "SH*EUP for -ship suffix",
         "spelling": "ship",
         "pronunciation": " suffix  sh  i  p ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing"}],

    "SO*pl": [
        {"description": "SO*PL for -some suffix",
         "spelling": "some",
         "pronunciation": " suffix  s  m ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing"}],

    "Seu": [
        {"description": "SEU for -cy suffix",
         "spelling": "c(y|ie)",
         "pronunciation": " suffix  s  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": ""}],

    "Teu": [
        {"description": "TEU for -ty suffix",
         "spelling": "t(ie|y)",
         "pronunciation": " suffix  t  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": ""}],

    "KHur": [
        {"description": "KHUR for -ture suffix",
         "spelling": "ture",
         "pronunciation": " suffix  t  y  @r  r ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing"}],

    "PWR*eu": [
        {"description": "PWR*EU for -berry suffix",
         "spelling": "berr(y|ie)",
         "pronunciation": " suffix  b  \(@r/e\)  r  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Harri"}],


    "WAO*eus": [
        {"description": "WAO*EUS for -wise suffix",
         "spelling": "wise",
         "pronunciation": " suffix  w  ae  z ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing"}],

    "WA*rd": [
        {"description": "WA*RD for -ward suffix",
         "spelling": "ward",
         "pronunciation": " suffix  w  @r  r  d ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "StenEd?"}],

    "WO*rtd": [
        {"description": "WO*RTD for -worthy suffix",
         "spelling": "worth(y|i)",
         "pronunciation": " suffix  w  @@r  r  dh  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Harri?"}],

    "WO*r/THeu": [
        {"description": "WO*R/THEU for -worthy suffix",
         "spelling": "worth(y|i)",
         "pronunciation": " suffix  w  @@r  r  dh  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing?"}],

    "HReu": [
        {"description": "HREU for -ly suffix",
         "spelling": "ly",
         "pronunciation": " suffix  l  iy ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "StenEd"}],

    "HAO*d": [
        {"description": "HAO*D for -hood suffix",
         "spelling": "hood",
         "pronunciation": " suffix  h  u  d ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory a": "StenEd"}],

    "HA*pl": [
        {"description": "HA*PL for -ham (this feels like a suffix but it's actually not, also Americans overpronounce the  'ha' bit)",
         "spelling": "ham",
         "pronunciation": " \(@/h  a\)  m ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Harri"}],

    "R*es": [
        {"description": "R*ES for -ress suffix", #actress
         "spelling": "ress",
         "pronunciation": " suffix  r  (e5|@)  s ",
         "ambiguity": 0,
         "what must come before": slash_no_asterisk,
         "steno theory": "Lapwing"}],

    "/-fl": [
        {"description": "-FL for suffix -ful",
         "spelling": "ful",
         "pronunciation": " suffix  f  l ",
         "ambiguity": 0,
         "what must come before": f_to_z,
         "steno theory": "StenEd?"}],

    "/-plt": [
        {"description": "/-PLT for -ment suffix", #adjournment
         "spelling": "ment",
         "pronunciation": " suffix  m  e5  n  t ",
         "ambiguity": 0,
         "what must come before": p_to_z,
         "steno theory": "StenEd?"}],

    "/-lt": [
        {"description": "/-LT for -let suffix", #armlet
         "spelling": "let",
         "pronunciation": " suffix  l  i7  t ",
         "ambiguity": 0,
         "what must come before": l_to_z,
         "steno theory": "StenEd?"}],
}

#missed audiotext
