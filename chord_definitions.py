import re

y_chord = "KWH" # the 'y' in yet or the 'i' in genius
silent_linker = "KWR" # the 'linker' in genus


custom_alphabet = "*QSTKPWHRAO-eufrpblgtsdz_"

keysymbol_shorthands = {
    """
    There will be groups of keysymbols that come up again and again,
    so I'll define them once here
    """
    "long a": "a i",
    "short vowels": " \[?(a4|u|@|i2|i7|i|e05|e5|e50|uh|a|o|a5|e|@r|a5/i2)\]? ",
    "short vowels but not a": " \[?(a4|u|@|i2|i7|i|e05|e5|uh|o|a5|e|@r|a5/i2)\]? ",
    "long vowels": " \[?(aa|ei|y  uu|iy)\]? ",
    "any vowel": " \[?(a4|a|ao|@|i2|i7|e05|eir|o|a5)\]? ",
    "long u": "( y )? (uu|ur|iu3) ",
    "pasta vowel": " ao "

}
#vowels like e5 are only found in suffixes?

spelling_shorthands = {
    """
    There will be groups of letters that come up again and again,
    so I'll define them once here
    """
    "": "a i",
    "schwa": "@",
    "long a": " ee "
}


#regex logic for what must come before
#hopefully compiling it all here makes it run faster since they'll be used
NothingRegex = re.compile(r'')
AtLeastOneCharacterRegex = re.compile(r'.+')
skipsAnEUInTheVowels = re.compile(r'[AO][frpblgtsdz]+')
unavailable_e_no_r = re.compile(r'.*[QSTKPWHR][AO]*[eu]+[fpblgtsdz]*')

A_to_g_yes_b_or_g = re.compile(r'.*[\-AOeufrp][bg][lg]*')
after_r = re.compile(r'.*[pblgtsdz]')

ends_in_t = re.compile(r'.*t')

upToQ = re.compile(r'.*[/Q]')
upToS = re.compile(r'.*[/QS]')
upToT = re.compile(r'.*[/QST]')
upToK = re.compile(r'.*[/QSTK]')
upToP = re.compile(r'.*[/QSTKP]')
upToW = re.compile(r'.*[/QSTKPW]')
upToH = re.compile(r'.*[/QSTKPWH]')
upToR = re.compile(r'.*[/QSTKPWHR]')

upToK_no_T = re.compile(r'.*[/QSK]')
upToW_no_T_not_just_k = re.compile(r'.*((K[PW]+)|([QST]K)|([/QSPW]))')
upToW_no_T = re.compile(r'.*[/QSKPW]')
upToW_no_P = re.compile(r'.*[/QSTKW]')


first_stroke_upToR = re.compile(r'[/QSTKPWHR]+')

A_to_u = re.compile(r'.*[\-AOeu]')
A_to_f = re.compile(r'.*[\-AOeuf]')
A_to_r = re.compile(r'.*[\-AOeufr]')
A_to_p = re.compile(r'.*[\-AOeufrp]')
A_to_b = re.compile(r'.*[\-AOeufrpb]')
A_to_l = re.compile(r'.*[\-AOeufrpbl]')
A_to_g = re.compile(r'.*[\-AOeufrpblg]')
A_to_t = re.compile(r'.*[\-AOeufrpblgt]')
A_to_s = re.compile(r'.*[\-AOeufrpblgts]')
A_to_d = re.compile(r'.*[\-AOeufrpblgtsd]')
A_to_z = re.compile(r'.*[\-AOeufrpblgtsdz]')


A_to_z_no_pbs = re.compile(r'.*[\-AOeufr][lgtdz]+')
A_to_z_no_plt = re.compile(r'.*[\-AOeufr][bgsdz]+')
A_to_t_no_g_end = re.compile(r'.*[\-AOeufrpbl]+(pblg)?(g?t)?')
A_to_d_no_t = re.compile(r'.*[\-AOeufrpblgs]+d?')
A_to_g_yes_t = re.compile(r'.*[\-AOeufrpblg]t')
yes_s = re.compile(r'.*s')

A_to_u_ = re.compile(r'.*[\-AOeu]_?')
A_to_f_ = re.compile(r'.*[\-AOeuf]_?')
A_to_r_ = re.compile(r'.*[\-AOeufr]_?')
A_to_p_ = re.compile(r'.*[\-AOeufrp]_?')
A_to_b_ = re.compile(r'.*[\-AOeufrpb]_?')
A_to_l_ = re.compile(r'.*[\-AOeufrpbl]_?')
A_to_g_ = re.compile(r'.*[\-AOeufrpblg]_?')
A_to_t_ = re.compile(r'.*[\-AOeufrpblgt]_?')
A_to_s_ = re.compile(r'.*[\-AOeufrpblgts]_?')
A_to_d_ = re.compile(r'.*[\-AOeufrpblgtsd]_?')
A_to_z_ = re.compile(r'.*[\-AOeufrpblgtsdz]_?')


A_to_z_no_pbs_ = re.compile(r'.*[\-AOeufr][lgtdz]+_?')
A_to_z_no_plt_ = re.compile(r'.*[\-AOeufr][bgsdz]+_?')


A_to_z_no_r = re.compile(r'.*[\-AOeuf][pblgtsdz]+')
A_to_z_no_p = re.compile(r'.*[\-AOeufr][blgtsdz]+')
A_to_z_no_b = re.compile(r'.*[\-AOeufrp][lgtsdz]+')
A_to_z_no_l = re.compile(r'.*[\-AOeufrpb][gtsdz]+')
A_to_z_no_g = re.compile(r'.*[\-AOeufrpbl][tsdz]+')
A_to_z_no_t = re.compile(r'.*[\-AOeufrpblg][sdz]+')
A_to_z_no_s = re.compile(r'.*[\-AOeufrpblgt][dz]+')
A_to_z_no_d = re.compile(r'.*[\-AOeufrpblgts][z]')


A_to_z_no_l_not_bg = re.compile(r'.*([\-AOeufrpb][tsdz]+)|([\-AOeufrp][gtsdz]+)')

slash_to_u = re.compile(r'.*[/][QSTKPWHR]*[\-AOeu]+')
slash_to_f = re.compile(r'.*[/][QSTKPWHR]*[\-AOeuf]+')
slash_to_r = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufr]+')
slash_to_p = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrp]+')
slash_to_b = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpb]+')
slash_to_l = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpbl]+')
slash_to_g = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblg]+')
slash_to_t = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgt]+')
slash_to_s = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgts]+')
slash_to_d = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgtsd]+')
slash_to_z = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgtsdz]+')

slash_to_r = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufr]')
slash_to_g_ = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblg]+_?')

slash_to_z_no_r = re.compile(r'.*[/][QSTKPWHR]*[\-AOeuf]+[pblgtsdz]+')
slash_to_z_no_p = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufr]+[blgtsdz]+')
slash_to_z_no_b = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrp]+[lgtsdz]+')
slash_to_z_no_l = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpb]+[gtsdz]+')
slash_to_z_no_g = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpbl]+[tsdz]+')
slash_to_z_no_t = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblg]+[sdz]+')
slash_to_z_no_s = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgt]+[dz]+')
slash_to_z_no_d = re.compile(r'.*[/][QSTKPWHR]*[\-AOeufrpblgts]+[z]')

"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {

    "": [
        #{"description": "silent e", #replaced with droppable e
        # "spelling": "e",
        # "pronunciation": "",
        # "ambiguity": 1, #maid/made
        # "what must come before": ".*[/QSTKPWHR]\*?([AOeu])[*frpblgtsdz]+",
        # "steno theory": "WSI"},
         
        #{"description": "droppable e", replaced with just putting e? in stuff
        # "spelling": "e",
        # "pronunciation": keysymbol_shorthands["short vowels"],
        # "ambiguity": 1,
        # "what must come before": ".*[/QSTKPWHR]\*?([AOeu]+)[*frpblgtsdz]+",
        # "steno theory": "I don't know"},
         
        #{"description": "droppable a",
        # "spelling": "a",
        # "pronunciation": keysymbol_shorthands["short vowels"],
        # "ambiguity": 1,
        # "what must come before": ".*[/QSTKPWHR]\*?([AOeu]+)[*frpblgtsdz]+",
        # "steno theory": "I don't know"},

        {"description": "drop short vowel",
         "spelling": "[aeiouy]",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 2,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"},

        {"description": "drop i that historically didn't exist anyway",
         "spelling": "",
         "pronunciation": " i ",
         "ambiguity": 2,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"},


        {"description": "drop long vowel",
         "spelling": "[aeiouy]",
         "pronunciation": keysymbol_shorthands["long vowels"],
         "ambiguity": 3,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"},

        {"description": "drop long u",
         "spelling": "u",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 3,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"},

        {"description": "drop the middle vowel in banana",
         "spelling": "a",
         "pronunciation": " oa ",
         "ambiguity": 3,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"},

        {"description": "ignoring a suffix border",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 1,
         "what must come before": AtLeastOneCharacterRegex,
         "steno theory": "I don't know"}],

    "/Q": [
        {"description": "^ for initial short a",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix)) " + keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "Josiah"},
         
        {"description": "^ for initial long a",
         "spelling": "a",
         "pronunciation": " (starting_)?((root)|(prefix))  ee ",
         "ambiguity": 1,
         "what must come before": NothingRegex,
         "steno theory": "Josiah"}],

    "/S": [
        {"description": "S for initial s",
         "spelling": "ss?",
         "pronunciation": " (starting_)?((root)|(prefix))  s ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "S for initial sc",
         "spelling": "sc",
         "pronunciation": " (starting_)?((root)|(prefix))  s ",
         "ambiguity": 1,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "S for linking s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        
        {"description": "S for linking sc",
         "spelling": "sc",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        #{"description": "S for linking vowel + s",
        # "spelling": "[aeiouy]ss?",
        # "pronunciation": keysymbol_shorthands["short vowels"] + " s ",
        # "ambiguity": 1,
        # "what must come before": A_to_z,
        # "steno theory": "WSI"}
        ],

    "/S*": [
        {"description": "S* for initial s of a compound word",
         "spelling": "ss?",
         "pronunciation": " compound  s ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "S* for initial sc of a compound word",
         "spelling": "sc",
         "pronunciation": " compound  s ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "S": [
        {"description": "S for s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": upToQ,
         "steno theory": "WSI"},

        {"description": "S for sc",
         "spelling": "sc",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": upToQ,
         "steno theory": "WSI"}],


    "/SKWR*": [
        {"description": "SKWR* for joining a compound word with j",
         "spelling": "j",
         "pronunciation": " compound  jh ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "/SKWR": [
        {"description": "SKWR for initial j",
         "spelling": "j",
         "pronunciation": " (starting_)((root)|(prefix))  jh ", 
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "SKWR for linking j",
         "spelling": "(j|dj|dge?)",
         "pronunciation": "( (root)|(prefix) )* jh ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "SKWR": [
        {"description": "SKWR for j",
         "spelling": "(j|dj|dge?)",
         "pronunciation": " jh ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "WSI"}],

    "/SR": [
        {"description": "SR for linker v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/SO*pb": [
        {"description": "SO*PB for 'son' where the o is silent",
         "spelling": "son",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/Se*pb": [
        {"description": "SE*PB for 'sen' where the e is silent",
         "spelling": "sen",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/S-pb": [
        {"description": "S-PB for 'son' where the o is silent",
         "spelling": "son",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"},

        {"description": "S-PB for 'sen' where the e is silent",
         "spelling": "sen",
         "pronunciation": " s  n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/T": [
        {"description": "T for initial t",
         "spelling": "t",
         "pronunciation": " (starting_)?((root)|(prefix))  t ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "T for linker t",
         "spelling": "tt?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? t ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/T*": [
        {"description": "T for compound linker t",
         "spelling": "t",
         "pronunciation": " compound  t ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwings"}],

    "T": [
        {"description": "T for t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],

    "/TK":[
        {"description": "TK for initial d",
         "spelling": "d",
         "pronunciation": " (starting_)((root)|(prefix)|(suffix))  d ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TK for linking d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "TK for linking d whilst ignoring boundaries",
         "spelling": "d",
         "pronunciation": " d  (suffix) ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "TK":[
        {"description": "TK for d",
         "spelling": "dd?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TKPW": [
        {"description": "TKPW for initial g",
         "spelling": "g",
         "pronunciation": " (starting_)?((root)|(prefix))  g ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TKPW for linker g",
         "spelling": "gg?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? g ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/TKPW*": [
        {"description": "TKPW for compound linker g",
         "spelling": "g",
         "pronunciation": " compound  g ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "TKPW": [
        {"description": "TKPW for g",
         "spelling": "gg?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TP": [
        {"description": "TP for initial f",
         "spelling": "f",
         "pronunciation": " (starting_)?((root)|(prefix))  f ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TP for linker f",
         "spelling": "ff?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? f ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/TP*": [
        {"description": "TP for compound linker f",
         "spelling": "f",
         "pronunciation": " compound  f ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "TP": [
        {"description": "T for f",
         "spelling": "ff?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TPH": [
        {"description": "TPH for initial n",
         "spelling": "n",
         "pronunciation": " (starting_)((root)|(prefix)|(suffix))  n ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TPH for linking n",
         "spelling": "nn?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/TPH*": [
        {"description": "TPH* for compound linker n",
         "spelling": "n",
         "pronunciation": " compound  n ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "TPH": [
        {"description": "TPH for n",
         "spelling": "nn?",
         "pronunciation": " n ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/TH": [
        {"description": "TH for initial th",
         "spelling": "th",
         "pronunciation": " (starting_)((root)|(prefix)|(suffix))  th ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "TH for linking th",
         "spelling": "th",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? th ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"}],

    "/K": [
        {"description": "K for initial k",
         "spelling": "kh?",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "K for linking k",
         "spelling": "kh?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? k ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

         {"description": "K for initial hard c",
         "spelling": "c",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 1,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "K for linking ch that sounds like k",
         "spelling": "ch",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? k ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "K for linking c that sounds like k",
         "spelling": "c",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? k ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "K": [
        {"description": "K for k",
         "spelling": "k(k|h)?",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": upToS,
         "steno theory": "WSI"},

        {"description": "K for hard c",
         "spelling": "c",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToS,
         "steno theory": "WSI"},

        {"description": "K for ch that sounds like k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": upToS,
         "steno theory": "WSI"}],


    "/KWH": [
        {"description": "KWH for linking y",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"},

        {"description": "KWH for linking i",
         "spelling": "i",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? ii ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],

    "/KWR": [
        {"description": "KWR for silent suffix linker",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "I think StenEd?"},

        {"description": "KWR for silent linker",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri"}],


    "/P": [
        {"description": "P for initial p",
         "spelling": "p",
         "pronunciation": " (starting_)?((root)|(prefix))  p ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "P for linker p",
         "spelling": "pp?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? p ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/P*": [
        {"description": "P for compound linker p",
         "spelling": "p",
         "pronunciation": " compound  p ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwings"}],

    "P": [
        {"description": "P for p",
         "spelling": "pp?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "steno theory": "WSI"}],

    "/PW*": [
        {"description": "PW* for joining a compound word with b",
         "spelling": "b",
         "pronunciation": " compound  b ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "/PW": [
        {"description": "PW for initial b",
         "spelling": "b",
         "pronunciation": " (starting_)((root)|(prefix))  b ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "PW for linking b",
         "spelling": "bb?",
         "pronunciation": "( ((root)|(prefix)) )? b ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "PW": [
        {"description": "PW for b",
         "spelling": "bb?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "WSI"}],

    "/PH*": [
        {"description": "PH* for joining a compound word with m",
         "spelling": "m",
         "pronunciation": " compound  m ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "/PH": [
        {"description": "PH for initial m",
         "spelling": "m",
         "pronunciation": " (starting_)((root)|(prefix))  m ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "PH for linking m",
         "spelling": "mm?",
         "pronunciation": "( (root)|(prefix) )* m ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "PH": [
        {"description": "PH for m",
         "spelling": "mm?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": upToK_no_T,
         "steno theory": "WSI"}],



    "/W*": [
        {"description": "W for compound linker w",
         "spelling": "w",
         "pronunciation": " compound  w ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "/W": [
        {"description": "W for initial w",
         "spelling": "w",
         "pronunciation": " (starting_)?((root)|(prefix))  w ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "W for linker w",
         "spelling": "ww?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? w ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "W": [
        {"description": "W for w",
         "spelling": "ww?",
         "pronunciation": " w ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "WSI"}],


    "/WA": [
        {"description": "WA for linking oir sound",
         "spelling": "oire?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Harri's Accent"}],
    
    "WA": [
        {"description": "WA for oir sound",
         "spelling": "oir?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 0,
         "what must come before": upToK,
         "steno theory": "Harri's Accent"},


        {"description": "WA for oir sound",
         "spelling": "oire?",
         "pronunciation": " w  ar  r ",
         "ambiguity": 1,
         "what must come before": upToK,
         "steno theory": "Harri's Accent"}],



    "/H*": [
        {"description": "H* for joining a compound word with h",
         "spelling": "h",
         "pronunciation": " compound  h ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "/H": [
        {"description": "H for initial h",
         "spelling": "h",
         "pronunciation": " (starting_)((root)|(prefix))  h ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "H for linking h",
         "spelling": "h",
         "pronunciation": "( (root)|(prefix) )* h ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

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
         "steno theory": "WSI"}],

    "/HR*": [
        {"description": "HR* for joining a compound word with l",
         "spelling": "l",
         "pronunciation": " compound  l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "/HR": [
        {"description": "HR for suffix linker l",
         "spelling": "ll?",
         "pronunciation": " suffix  l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "HR for linker l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"},

        {"description": "HR for vowel then suffix linker l",
         "spelling": "ll?",
         "pronunciation": keysymbol_shorthands["short vowels"] + " suffix  l ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],


    "HR": [
        {"description": "HR for l",
         "spelling": "l",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": upToW_no_T_not_just_k, #I just... THR → tl feels wrong. Oh this is kinda long, I also don't like k + space for vowel + l like #KHREU/TPORPB/KWHA
         "steno theory": "WSI"},


        {"description": "HR for ll",
         "spelling": "ll",
         "pronunciation": " l ",
         "ambiguity": 1, #Alan Allan
         "what must come before": upToW_no_T_not_just_k,
         "steno theory": "WSI"}],

    "/R": [
        {"description": "R for initial r",
         "spelling": "r",
         "pronunciation": " (starting_)?((root)|(prefix))  r ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "R for linker r", #doesn't have a fit for abjuration because jure secretly has an 'e'
         "spelling": "rr?",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? r ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "WSI"}],

    "/R*": [
        {"description": "R for compound linker r",
         "spelling": "r",
         "pronunciation": " compound  r ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "Lapwing"}],

    "R": [
        {"description": "R for r",
         "spelling": "rr?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": upToW,
         "steno theory": "WSI"}],

    "/A": [

        {"description": "A for initial a",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix))  a ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "A for initial schwa",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix)) " + keysymbol_shorthands["short vowels but not a"],
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"},

        {"description": "A for the initial pasta vowel",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix)) " + keysymbol_shorthands["pasta vowel"],
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "pasta is a short vowel"},

        {"description": "A for the initial drama vowel",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  aa ",
         "ambiguity": 1,
         "what must come before": NothingRegex,
         "steno theory": "drama is a short vowel"},

        {"description": "A for the initial middle a in banana",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  oa ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "banana is all short vowels"}],


    "A": [
        {"description": "A for short a",
         "spelling": "a",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},
         
        {"description": "A for the drama vowel",
         "spelling": "aa?",
         "pronunciation": " aa ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "drama is a short vowel"},


        {"description": "A for the middle a in banana",
         "spelling": "aa?",
         "pronunciation": " oa ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "banana is all short vowels"}],

    "AO": [
        {"description": "AO for oa said like abroad",
         "spelling": "oa",
         "pronunciation": " oo ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

    "AOe": [

        {"description": "AOE for long e spelt ee",
         "spelling": "ee",
         "pronunciation": " ii ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I don't know"},

        {"description": "AOE for long e spelt e",
         "spelling": "e",
         "pronunciation": " ii ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I don't know"},
        
        {"description": "AOE for long e spelt ea",
         "spelling": "ea",
         "pronunciation": " ii ",
         "ambiguity": 2,
         "what must come before": upToR,
         "steno theory": "I don't know"}],

    "AOeu": [
        {"description": "AOEU for long i",
         "spelling": "i",
         "pronunciation": " (ae|ai) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"}],


    "AOu": [
        {"description": "AOU for long u",
         "spelling": "u",
         "pronunciation": keysymbol_shorthands["long u"],
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I don't know"}],

    "AOr": [
        {"description": "AOR for oar",
         "spelling": "oar",
         "pronunciation": " our  r ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I don't know"}],

    "Ae": [ #need to add "/Ae" at some point? No you don't, you got KWR
        {"description": "AE for long e spelt ea, but only if it's the first stroke",
         "spelling": "ea",
         "pronunciation": " ii ",
         "ambiguity": 1,
         "what must come before": first_stroke_upToR,
         "steno theory": " I don't know"},

        {"description": "AE for long e spelt ae",
         "spelling": "ae",
         "pronunciation": " ii ",
         "ambiguity": 2,
         "what must come before": upToR,
         "steno theory": "Lapwing?"},

        {"description": "AE for long a spelt a_e, but only if it's the first stroke",
         "spelling": "a",
         "pronunciation": " ee ",
         "ambiguity": 2,
         "what must come before": first_stroke_upToR,
         "steno theory": " I don't know"},

         ],

    "/Aeu": [
        {"description": "AEU for initial long a",
         "spelling": "aa?y?",
         "pronunciation": " (starting_)?((root)|(prefix))  (ee|ei|eir) ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "WSI"}],

    "Aeu": [
        {"description": "AEU for long a",
         "spelling": "a(a|y|i)?",
         "pronunciation": " (ee|ei|eir) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "AEU for long a written with an e",
         "spelling": "ey?",
         "pronunciation": " (ee|ei|eir) ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I don't know"},

        {"description": "AEU for long a written with ei",
         "spelling": "ei",
         "pronunciation": " (ee|ei|eir) ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I don't know"}],

    "Aer": [
        {"description": "AER for -ary",
         "spelling": "ary",
         "pronunciation": " \(@r/~  e\)  r  iy ", #this looks like an error, 'cause it is, but if it ain't broke don't fitcecoc
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

    "Aepbs": [
        {"description": "AEPBS for -ency",
         "spelling": "ency",
         "pronunciation": " @  n  s  suffix  iy ", #this looks like an error, 'cause it is, but if it ain't broke don't fitcecoc
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

    "Ael": [
        {"description": "AEL for -ally",
         "spelling": "ally",
         "pronunciation": " l  suffix  iy ", #this looks like an error, 'cause it is, but if it ain't broke don't fitcecoc
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

    "/Au": [
        {"description": "AU for the initial drama vowel",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  aa ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "drama is a long vowel"},

        {"description": "AU for the initial daughter vowel",
         "spelling": "a(a|u)",
         "pronunciation": " (starting_)?((root)|(prefix))  oo ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "daughter is a long vowel"},

        {"description": "AU for initial al in false",
         "spelling": "all?",
         "pronunciation": " (starting_)?((root)|(prefix))  oo  l ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "false is AUL"}],

    "Au": [
        {"description": "AU for the daughter vowel",
         "spelling": "a(a|u)",
         "pronunciation": " oo ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "daughter is a long vowel"},

        {"description": "AU for al in false",
         "spelling": "all?",
         "pronunciation": " oo  l ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "false is AUL"},
         
         {"description": "AU for au",
         "spelling": "au",
         "pronunciation": " ow ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I don't know"},

        {"description": "AU for oa said like abroad",
         "spelling": "oa",
         "pronunciation": " oo ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],


    "/Ar": [

        {"description": "AR for initial long a followed by r",
         "spelling": "aa?re?",
         "pronunciation": " starting_((root)|(prefix))  ar  r ",
         "ambiguity": 0,
         "what must come before": NothingRegex,
         "steno theory": "Lapwing"}],

    "Ar": [
        {"description": "AR for long a followed by r",
         "spelling": "aa?re?",
         "pronunciation": " ar  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "Lapwing"}],


    "Al": [
        {"description": "AL for al (despite the silent a)",
         "spelling": "al",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI?"}],


    "Oe": [
        {"description": "OU for o said like owe",
         "spelling": "o",
         "pronunciation": " ou ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "Lapwing?"}],

    "O": [
        {"description": "O for o",
         "spelling": "o",
         "pronunciation": " (O|o|@|@r) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "O for o in Harri's accent",
         "spelling": "o",
         "pronunciation": " (au) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "Harri's accent"},

        {"description": "O for o (even though it's pronounced uh)",
         "spelling": "o",
         "pronunciation": " uh ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

        #{"description": "O for o, even though it's not pronounced",
        # "spelling": "o",
        # "pronunciation": "",
        # "ambiguity": 1,
        # "what must come before": upToR,
        # "steno theory": "WSI"}],

    "Ou": [
        {"description": "OU for ow said like ow",
         "spelling": "ow",
         "pronunciation": " ow ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "OU for ou said like ow",
         "spelling": "ou",
         "pronunciation": " ow ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "WSI"}],

    "Or": [
        {"description": "OR for long o followed by r",
         "spelling": "ore?",
         "pronunciation": " or  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "Lapwing"},

        {"description": "OR for oar",
         "spelling": "oar",
         "pronunciation": " our  r ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "I don't know"}],


    "e": [
        {"description": "E for unstressed e",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "E for short e spelt ea",
         "spelling": "ea",
         "pronunciation": " e ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": " I don't know"},

         {"description": "E for long e spelt just e", #abalone
          "spelling": "e",
          "pronunciation" : " iy ",
          "ambiguity": 1,
          "what must come before": upToR,
          "steno theory": "I don't know"}],

    "eu": [
        {"description": "EU for y said like long e",
         "spelling": "e?y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"},

        {"description": "EU for i",
         "spelling": "i",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"},

        {"description": "EU for y said like short i",
         "spelling": "y",
         "pronunciation": " i ",
         "ambiguity": 1, #honestly this might be 0
         "what must come before": upToR,
         "steno theory": "WSI"},
        
        {"description": "EU for y said like uh",
         "spelling": "y",
         "pronunciation": " i2 ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

    "eu/KWRe": [
        {"description": "EU/KWRE for ie",
         "spelling": "ie",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "I think StenEd?"}],

    "er": [
        {"description": "ER for er",
         "spelling": "er",
         "pronunciation": " @r  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "folding ER for suffix er when E is free",
         "spelling": "er",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 1,
         "what must come before": skipsAnEUInTheVowels, #replaced the logic ".*[AO](?!.*(.).*\1)[fpblgtsdz]*\*?"
         "steno theory": "Harri"}],

    "u": [

        {"description": "U for u",
         "spelling": "u",
         "pronunciation": " (@|uh) ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"},

        {"description": "U for ou said like country",
         "spelling": "ou",
         "pronunciation": " uh ",
         "ambiguity": 1,
         "what must come before": upToR,
         "steno theory": "WSI"}],

    "ur": [
        {"description": "UR for ur",
         "spelling": "ure?",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": upToR,
         "steno theory": "WSI"}],

    

    "f":[
        {"description": "-F for f",
         "spelling": "ff?e?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"},

         {"description": "-F for gh",
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I don't know"}],


    "f_":[ #there's logic where anything ending in a _ cannot be followed by a new stroke

        {"description": "-F for s",
         "spelling": "ss?e?",
         "pronunciation": " (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"},

        {"description": "-F for v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"}],




    #"fr":[
    #    {"description": "-FR for m",
    #     "spelling": "m",
    #     "pronunciation": " m ",
    #     "ambiguity": 2,
    #     "what must come before": A_to_u,
    #     "steno theory": "I think StenEd?"}],

    "frp":[
        {"description": "-FRP for mp",
         "spelling": "mp",
         "pronunciation": " m  p ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"}],

    "frpblg": [
        {"description": "-FRPBG for nkl",
         "spelling": "n(c|k)le?",
         "pronunciation": " ng  k  l ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"}],

    "frpbg": [
        {"description": "-FRPBG for nk",
         "spelling": "n(c|k)",
         "pronunciation": " ng  k ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"}],

    "frb":[
        {"description": "-FRB for mb",
         "spelling": "mb",
         "pronunciation": " m  b ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "I think StenEd?"}],

    "ft":[
        {"description": "-FT for ft",
         "spelling": "ft",
         "pronunciation": " f  t ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "WSI"},

        {"description": "-FT for st",
         "spelling": "st",
         "pronunciation": " s  t ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "WSI"}],

    #"fplt":[
    #    {"description": "-F for s then -PLT for suffix -ment",
    #     "spelling": "sement",
    #     "pronunciation": " s suffix  m  e5  n  t ",
    #     "ambiguity": 1,
    #     #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
    #     "what must come before": A_to_u,
    #     "steno theory": "I don't know"}],

    "fb":[
        {"description": "-FB for v",
         "spelling": "ve?",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": A_to_u,
         "steno theory": "Josiah?"}],

    "fg":[
        {"description": "-FG for gh",
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": A_to_u,
         "steno theory": "Harri"}],

    "r": [
        {"description": "-R for r",
         "spelling": "re?",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": A_to_f,
         "steno theory": "WSI"},

        {"description": "folding -R for suffix er when E is unavailable",
         "spelling": "er",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 2,
         "what must come before": unavailable_e_no_r,
         "steno theory": "Harri"},

        {"description": "folding -R for or? I'll do it when E is unavailable for some reason",
         "spelling": "or",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 3,
         "what must come before": unavailable_e_no_r, #reusing cause I'm lazy
         "steno theory": "Harri"}], 

    "rb": [
        {"description": "-RB for sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": A_to_f,
         "steno theory": "I don't know"}],

    "rbl": [
        {"description": "-RBL for -shable",
         "spelling": "shable",
         "pronunciation": " sh  suffix  @  b  l ",
         "ambiguity": 1,
         "what must come before": A_to_f,
         "steno theory": "Harri"}],

    "p": [
        {"description": "-P for p",
         "spelling": "pp?e?",
         "pronunciation": " p ",
         "ambiguity": 0,
         "what must come before": A_to_r_, #".*[AOeu](?!.*(.).*\1)[frblgtsdsz]*\*?"
         "steno theory": "WSI"}],

    "pb": [
        {"description": "-PB for n",
         "spelling": "(e|o)?nn?e?",
         "pronunciation": " n ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "WSI"}],





    "pbl": [
        {"description": "-PBL for nal (despite the silent a)",
         "spelling": "nall?", #abdominally
         "pronunciation": " n  l ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": "WSI?"}],

    "pblg": [
        {"description": "-PBLG for j sound",
         "spelling": "(j|dj|d?g)e?",
         "pronunciation": " jh ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": "WSI?"}],

    "pbg": [
        {"description": "-PBG for ng",
         "spelling": "ng?",
         "pronunciation": " ng ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "WSI"},

        {"description": "-PBG for ng and g",
         "spelling": "ng?",
         "pronunciation": " ng  g ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": "WSI"}],

    "/-pbs": [
        {"description": "-PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 0,
         "what must come before": A_to_z,
         "steno theory": "I think StenEd?"},

        {"description": "-PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|i2)  suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": A_to_z,
         "steno theory": "I think StenEd?"}],


    "pbs": [
        {"description": "-PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": A_to_r_,
         "steno theory": "I think StenEd?"},


         {"description": "-PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|i2)  suffix  n  E5  s ",
         "ambiguity": 2,
         "what must come before": A_to_r_,
         "steno theory": "I think StenEd?"},

        {"description": "folding -PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_pbs,
         "steno theory": "I think StenEd?"},

        {"description": "folding -PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|i2)  suffix  n  E5  s ",
         "ambiguity": 2,
         "what must come before": A_to_z_no_pbs,
         "steno theory": "I think StenEd?"}],

    "pl": [
        {"description": "-PL for m",
         "spelling": "m(b|m)?e?",
         "pronunciation": " m ",
         "ambiguity": 0,
         "what must come before": A_to_r_,
         "steno theory": "WSI"}],

    "*pz": [
        {"description": "*PZ for h",
         "spelling": "h",
         "pronunciation": "( h )?",
         "ambiguity": 0,
         "what must come before": slash_to_r,
         "steno theory": "Josiah"}],


    "/-plt":[
        {"description": "-PLT for suffix -ment", #maybe should make this only trigger if there's no space for a -PLT in the previous stroke?
         "spelling": "ment",
         "pronunciation": " suffix  m  e5  n  t ",
         "ambiguity": 0,
         "what must come before": after_r,
         "steno theory": "WSI"}],

    "plt":[
        {"description": "-PLT for suffix -ment",
         "spelling": "ment",
         "pronunciation": " suffix  m  e5  n  t ",
         "ambiguity": 1,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_r_,
         "steno theory": "I don't know"},

         {"description": "-PLT for t then suffix -ment",
         "spelling": "tment",
         "pronunciation": " t  suffix  m  e5  n  t ",
         "ambiguity": 2,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         "what must come before": A_to_r_,
         "steno theory": "I don't know"}],

         #{"description": "folding -PLT for suffix -ment",
         #"spelling": "ment",
         #"pronunciation": " suffix  m  e5  n  t ",
         #"ambiguity": 1,
         #"what must come before": ".*[AOeu]f?r?b?g?s?z\*?",
         #"what must come before": A_to_z_no_plt,
         #"steno theory": "I don't know"}],


    "b": [
        {"description": "-B for b",
         "spelling": "bb?e?",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": A_to_u, #this chord can only can after a vowel, so it's Josiah since `KAURB` → `carb`
         "steno theory": "Josiah"}],

    "bl": [
        {"description": "-BL for bil where the etymology is from 'able' (which doesn't have an i)",
         "spelling": "ble",
         "pronunciation": " b  i  l ",
         "ambiguity": 0,
         "what must come before": A_to_p_, 
         "steno theory": "Josiah"}],

        #{"description": "EU for i sound",
        # "spelling": "",
        # "pronunciation": " i ", #sorry I forgot what this actually was don't be mad
        # "ambiguity": 0,
        # "what must come before": upToR,
        # "steno theory": "I don't know"},

    "bg": [
        {"description": "-BG for k",
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "WSI"},

        {"description": "-BG for ck",
         "spelling": "ck",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "WSI"},

        {"description": "-BG for k sound spelt ch",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "WSI"},

        {"description": "-BG for c", #do I make *BG? pick pic?
         "spelling": "c",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": A_to_p_,
         "steno theory": "WSI?"}],

    "*bgs": [
        {"description": "*BGS for ction",
         "spelling": "ction",
         "pronunciation": " k  sh  suffix  n ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "Harri"}],

    "l":[
        {"description": "-L for l",
         "spelling": "ll?e?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": A_to_b_,
         "steno theory": "WSI"},

        {"description": "folding -L for l",
         "spelling": "ll?e?",
         "pronunciation": " l ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_l_not_bg,
         "steno theory": "I don't know"},

        {"description": "-L for -ly",
         "spelling": "ly",
         "pronunciation": " suffix  l  iy ",
         "ambiguity": 2,
         "what must come before": A_to_b_,
         "steno theory": "I don't know"},

        {"description": "folding -L for -ly",
         "spelling": "ly",
         "pronunciation": " suffix  l  iy ",
         "ambiguity": 2,
         "what must come before": A_to_z_no_l_not_bg, #*BLG → ckle
         "steno theory": "I don't know"}],

    #"/-ls":[
    #    {"description": "-LS for -less",
    #     "spelling": "less",
    #     "pronunciation": " suffix  l  E5  s ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],

    #"/-g":[
    #    {"description": "-G for -ing",
    #     "spelling": "ing",
    #     "pronunciation": " suffix  i  ng ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],

    "g":[
        {"description": "-G for g",
         "spelling": "gg?e?",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": A_to_p_,
         "steno theory": "WSI"},

        {"description": "-G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_p_,
         "steno theory": "WSI"},

        {"description": "folded -G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": A_to_z_no_g,
         "steno theory": "WSI"}],

    "gs":[
        {"description": "-GS for shion",
         "spelling": "(sh|te?)ion",
         "pronunciation": " sh ( suffix )? n ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "steno theory": "I think StenEd?"},

        {"description": "-GS for sion",
         "spelling": "deion", #listen I don't make the rules I just write them
         "pronunciation": " zh ( suffix )? n ",
         "ambiguity": 0,
         "what must come before": A_to_l_,
         "steno theory": "I think StenEd?"}],

    "t":[
        {"description": "-T for t",
         "spelling": "tt?e?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "steno theory": "WSI"},

        {"description": "-T for t even though it's pronounced with an sh sound",
         "spelling": "tt?e?",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": A_to_g_,
         "steno theory": "WSI"}],

    "*t":[
        {"description": "*T for th",
         "spelling": "the?",
         "pronunciation": " th ",
         "ambiguity": 0,
         "what must come before": slash_to_g_,
         "steno theory": "Lapwing"}],

    #"/-s":[
    #    {"description": "-S for plurals",
    #     "spelling": "s",
    #     "pronunciation": "( (suffix) ) z ",
    #     "ambiguity": 1,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],
        
    "s":[

        {"description": "-S for unvoiced s",
         "spelling": "ss?e?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": A_to_t_no_g_end, #no idea, this just feels right
         "steno theory": "WSI"},

        {"description": "-S for unvoiced c",
         "spelling": "ce?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": A_to_t_no_g_end, #maybe I'm traumatised from ABGS/HRERPL/TER → accelerometer
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
         "what must come before": slash_to_t,
         "steno theory": " Josiah"},

        #{"description": "*S for voiced s",
        # "spelling": "ss?e?",
        # "pronunciation": " z ",
        # "ambiguity": 0,
        # "what must come before": slash_to_t,
        # "steno theory": "Harri?"},
         
        {"description": "*S for suffix -ise",
         "spelling": "ise",
         "pronunciation": " suffix  ae  z ",
         "ambiguity": 1,
         "what must come before": slash_to_t,
         "steno theory": "Harri?"}],

    "/-d": [
        {"description": "-D for -ed",
         "spelling": "ed",
         "pronunciation": " suffix ( i7 )? (d|t) ",
         "ambiguity": 0,
         "what must come before": yes_s,
         "steno theory": "WSI"}],

    "d": [
        {"description": "-D for d",
         "spelling": "de?",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": A_to_t_,
         "steno theory": "WSI"},

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
         "spelling": "l?y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": slash_to_t,
         "steno theory": "Harri"},

        {"description": "*D for y (said like short i)",
         "spelling": "l?y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? i ",
         "ambiguity": 3,
         "what must come before": slash_to_t,
         "steno theory": "Harri"},

        {"description": "*D for dy",
         "spelling": "dy",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "what must come before": slash_to_t,
         "steno theory": "HelloChap? I can't remember"}],

    "dz": [
        {"description": "-DZ for suffix ing when G is taken",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": A_to_g_yes_b_or_g,
         "steno theory": "WSI"}],

    #"/-z":[
    #    {"description": "-Z for plurals",
    #     "spelling": "e?s",
    #     "pronunciation": "( (suffix) )( i7 )? (s|#z) ",
    #     "ambiguity": 0,
    #     "what must come before": A_to_z,
    #     "steno theory": "WSI"}],

    "z":[
        {"description": "-Z for plurals",
         "spelling": "e?s",
         "pronunciation": "( (suffix) )( i7 )? (s|z) ",
         "ambiguity": 1,
         "what must come before": A_to_d_no_t,
         "steno theory": "WSI"},

        #{"description": "-Z for voiced s", #this is only for onestrokes I think?
        # "spelling": "e?s",
        # "pronunciation": " (z) ",
        # "ambiguity": 1,
        # "what must come before": A_to_d_no_t,
        # "steno theory": "WSI"}
         ],


    "*z":[
        {"description": "*Z for z",
         "spelling": "ze?",
         "pronunciation": " z ",
         "ambiguity": 1,
         "what must come before": A_to_d_no_t,
         "steno theory": "Harri"}],

}
