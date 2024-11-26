

y_chord = "KWH" # the 'y' in yet or the 'i' in genius
silent_linker = "KWR" # the 'linker' in genus


keysymbol_shorthands = {
    """
    There will be groups of keysymbols that come up again and again,
    so I'll define them once here
    """
    "long a": "a i",
    "short vowels": " \[?(@|E5|I2|I7|E05|a)\]? ",
    "any vowel": " \[?(a|ao|@|E5|I2|I7|E05|aa|eir)\]? ",
    "pasta vowel": " ao "
}

spelling_shorthands = {
    """
    There will be groups of letters that come up again and again,
    so I'll define them once here
    """
    "": "a i",
    "schwa": "@",
    "long a": " ee "
}

"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {

    "": [
        {"description": "silent e",
         "spelling": "e",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": ".*[/QSTKPWHR]\*?((Aoe)|(AOeu)|(AOu)|(Ae)|(Aeu)|(O)|(Oe)|(Oeu))[*frpblgtsdz]+",
         "steno theory": "WSI"},
         
        {"description": "droppable e",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": ".*[/QSTKPWHR]\*?([AOeu]+)[*frpblgtsdz]+",
         "steno theory": "I don't know"},
         
        {"description": "droppable a",
         "spelling": "a",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 1,
         "what must come before": ".*[/QSTKPWHR]\*?([AOeu]+)[*frpblgtsdz]+",
         "steno theory": "I don't know"},

        {"description": "ignoring a suffix border",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 1,
         "what must come before": ".*[/QSTKPWHR]\*?([AOeu]+)[*frpblgtsdz]+",
         "steno theory": "I don't know"}],

    "/Q": [
        {"description": "^ for initial short a",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix)) " + keysymbol_shorthands["any vowel"],
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "Josiah"},
         
        {"description": "^ for initial long a",
         "spelling": "a",
         "pronunciation": " (starting_)?((root)|(prefix))  ee ",
         "ambiguity": 1,
         "what must come before": "",
         "steno theory": "Josiah"}],

    "/S": [
        {"description": "S for initial s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "WSI"},

        {"description": "S for linking s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": "(.*[AOeufrpblgtsdz]\*?)",
         "steno theory": "WSI"},

        {"description": "S for linking vowel + s",
         "spelling": "[aeiouy]ss?",
         "pronunciation": keysymbol_shorthands["short vowels"] + " s ",
         "ambiguity": 1,
         "what must come before": "(.*[AOeufrpblgtsdz]\*?)",
         "steno theory": "WSI"}],

    "/S*": [
        {"description": "S* for initial s of a compound word",
         "spelling": "ss?",
         "pronunciation": " compound  s ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]\*?",
         "steno theory": "WSI"}],


    "S": [

         {"description": "S for s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": "(.*/)*[TKPWHR]\*?",
         "steno theory": "WSI"},

        {"description": "S for s",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": ".*[/TKPWHR]\*?",
         "steno theory": "WSI"},

        {"description": "S for soft c",
         "spelling": "c",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": ".*[/TKPWHR]\*?",
         "steno theory": "WSI"},

        {"description": "S for sc",
         "spelling": "sc",
         "pronunciation": " s ",
         "ambiguity": 2,
         "what must come before": ".*[/TKPWHR]+",
         "steno theory": "WSI"},

        {"description": "S for s+vowel+consonant",
         "spelling": "sc",
         "pronunciation": " s "+keysymbol_shorthands["any vowel"]+ "( s )|( b )",
         "ambiguity": 3,
         "what must come before": ".*[/TKPWHR]+",
         "steno theory": "WSI"}],

    "/SR": [
        {"description": "SR for linker v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": ".*[/AOeufrpblgtsdz*]\*?",
         "steno theory": "I think StenEd?"}],

    "/TK":[
        {"description": "TK for initial d",
         "spelling": "d",
         "pronunciation": " (starting_)((root)|(prefix)|(suffix))  d ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "WSI"},


        {"description": "TK for linking d whilst ignoring boundaries",
         "spelling": "d",
         "pronunciation": " d  (suffix) ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgtsdz]\*?",
         "steno theory": "WSI"}],

    "TK":[
        {"description": "TK for d",
         "spelling": "d",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": ".*[QS]",
         "steno theory": "WSI"}],

    "/K": [
        {"description": "K for initial k",
         "spelling": "k",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "WSI"},

         {"description": "K for initial hard c",
         "spelling": "c",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 1,
         "what must come before": "",
         "steno theory": "WSI"},

        {"description": "K for linking ch that sounds like k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgtsdz]\*?",
         "steno theory": "WSI"}],

    "K": [
        {"description": "K for k",
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": ".*[/QS]\*?",
         "steno theory": "WSI"},

        {"description": "K for hard c",
         "spelling": "c",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": ".*[/QS]\*?",
         "steno theory": "WSI"},

        {"description": "K for ch that sounds like k",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": ".*[/QS]\*?",
         "steno theory": "WSI"}],


    "/KWH": [
        {"description": "KWH for initial/linking y",
         "spelling": "y",
         "pronunciation": " ((root)|(prefix)|(suffix))?  iy ",
         "ambiguity": 0,
         "what must come before": ".*[frpblgtsdz]+\*?",
         "steno theory": "Harri"}],

    "/KWR": [
        {"description": "KWR for silent suffix linker",
         "spelling": "",
         "pronunciation": " suffix ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "I think StenEd?"},

        {"description": "KWR for silent linker",
         "spelling": "",
         "pronunciation": "",
         "ambiguity": 0,
         "what must come before": ".*[frpblgtsdz]+\*?",
         "steno theory": "Harri"}],



    "/PW*": [
        {"description": "PW* for joining a compound word with b",
         "spelling": "b",
         "pronunciation": " compound  b ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "Lapwing"}],


    "/PW": [
        {"description": "PW for initial b",
         "spelling": "b",
         "pronunciation": " (starting_)((root)|(prefix))  b ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "Lapwing"},

        {"description": "PW for linking b",
         "spelling": "b",
         "pronunciation": "( (root)|(prefix) )* b ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "Lapwing"}],

    "PW": [
        {"description": "PW for b",
         "spelling": "b",
         "pronunciation": " b ",
         "ambiguity": 0,
         "what must come before": ".*[/QS]\*?",
         "steno theory": "WSI"}],

    "/H": [
        {"description": "H for linking h",
         "spelling": "h",
         "pronunciation": "( (root)|(prefix) )* h ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "WSI"}],

    "H": [
        {"description": "H for h",
         "spelling": "h",
         "pronunciation": " h ",
         "ambiguity": 0,
         "what must come before": ".*[/QSTKPW]\*?",
         "steno theory": "WSI"}],

    "/HR*": [
        {"description": "HR* for joining a compound word with l",
         "spelling": "l",
         "pronunciation": " compound  l ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "Lapwing"}],

    "/HR": [
        {"description": "HR for suffix linker l",
         "spelling": "l",
         "pronunciation": " suffix  l ",
         "ambiguity": 0,
         "what must come before": ".*[/AOeufrpblgtsdz]\*?",
         "steno theory": "WSI"},


        {"description": "HR for vowel then suffix linker l",
         "spelling": "l",
         "pronunciation": keysymbol_shorthands["short vowels"] + " suffix  l ",
         "ambiguity": 0,
         "what must come before": ".*[/AOeufrpblgtsdz]\*?",
         "steno theory": "WSI"}],


    "HR": [
        {"description": "HR for l",
         "spelling": "l",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": ".*[/QSTKPW]\*?",
         "steno theory": "WSI"},


        {"description": "HR for ll",
         "spelling": "ll",
         "pronunciation": " l ",
         "ambiguity": 1, #Alan Allan
         "what must come before": ".*[/QSTKPW]\*?",
         "steno theory": "WSI"}],

    "/A": [

        {"description": "A for initial a",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix))  a ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "WSI"},

        {"description": "A for initial schwa",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix)) " + keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "WSI"},

        {"description": "A for the initial pasta vowel",
         "spelling": "a",
         "pronunciation": " (starting_)((root)|(prefix)) " + keysymbol_shorthands["pasta vowel"],
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "Harri's accent"},


        {"description": "A for the initial drama vowel",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  aa ",
         "ambiguity": 1,
         "what must come before": "",
         "steno theory": "drama is a short vowel"}],

    "A": [
        {"description": "A for short a",
         "spelling": "a",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "WSI"}],



    "AOe": [
        {"description": "AOE for long e spelt ea",
         "spelling": "ea",
         "pronunciation": " ii ",
         "ambiguity": 2,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "I don't know"}],


    "AOu": [
        {"description": "AOU for long u",
         "spelling": "u",
         "pronunciation": "( y )? (uu|UU) ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "I don't know"}],


    "Ae": [
        {"description": "AE for long e spelt ea",
         "spelling": "ea",
         "pronunciation": " ii ",
         "ambiguity": 2,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": " I don't know"}],

    "/Aeu": [
        {"description": "AEU for initial long a",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  (ee|ei|eir) ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "WSI"}],


    "/Au": [
        {"description": "AU for the initial drama vowel",
         "spelling": "aa?",
         "pronunciation": " (starting_)?((root)|(prefix))  aa ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "drama is a long vowel"},

        {"description": "AU for the initial daughter vowel",
         "spelling": "a(a|u)",
         "pronunciation": " (starting_)?((root)|(prefix))  oo ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "daughter is a long vowel"},

        {"description": "AU for initial al in false",
         "spelling": "all?",
         "pronunciation": " (starting_)?((root)|(prefix))  oo  l ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "false is AUL"}],

    "Au": [
        {"description": "AU for the daughter vowel",
         "spelling": "a(a|u)",
         "pronunciation": " oo ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "daughter is a long vowel"},

        {"description": "AU for al in false",
         "spelling": "all?",
         "pronunciation": " oo  l ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "false is AUL"}],


    "/Ar": [

        {"description": "AR for initial long a followed by r",
         "spelling": "aa?r",
         "pronunciation": " starting_((root)|(prefix))  ar  r ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "Lapwing"}],

    "Ar": [
        {"description": "AR for long a followed by r",
         "spelling": "aa?r",
         "pronunciation": " ar  r ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "Lapwing"}],


    "Oe": [
        {"description": "OU for o said like owe",
         "spelling": "o",
         "pronunciation": " ou ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "Lapwing?"}],

    "O": [
        {"description": "O for o",
         "spelling": "o",
         "pronunciation": " (O|@) ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "WSI"}],

    "Ou": [
        {"description": "OU for ow said like ow",
         "spelling": "ow",
         "pronunciation": " ow ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "WSI"},

        {"description": "OU for ou said like ow",
         "spelling": "ou",
         "pronunciation": " ow ",
         "ambiguity": 1,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "WSI"}],

    "Or": [
        {"description": "OR for long o followed by r",
         "spelling": "or",
         "pronunciation": " or  r ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "Lapwing"}],


    "e": [
        {"description": "E for unstressed e",
         "spelling": "e",
         "pronunciation": keysymbol_shorthands["short vowels"],
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "I don't know"},

        {"description": "E for unstressed e whilst ignoring boundaries",
         "spelling": "e",
         "pronunciation": " (suffix|prefix|root|compound) "+keysymbol_shorthands["short vowels"],
         "ambiguity": 1,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "I don't know"}],

    "eu": [
        {"description": "EU for y said like long e",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "I think StenEd?"},

        {"description": "EU for i",
         "spelling": "i",
         "pronunciation": " i ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "I think StenEd?"},
        
        {"description": "EU for y said like uh",
         "spelling": "y",
         "pronunciation": " I2 ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "I think StenEd?"}],

    "er": [
        {"description": "ER for er",
         "spelling": "er",
         "pronunciation": " @r  r ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "WSI"},

        {"description": "folding ER for suffix er when E is free",
         "spelling": "er",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 1,
         "what must come before": ".*[QSTKPWHR]+([AOfpblgtsdz*]*)\*?",
         "steno theory": "Harri"}],

    "u": [
        {"description": "U for ou said like country",
         "spelling": "ou",
         "pronunciation": " uh ",
         "ambiguity": 1,
         "what must come before": ".*[QSTKPWHR]+\*?",
         "steno theory": "I don't know"}],

    "ur": [
        {"description": "UR for ur",
         "spelling": "ur",
         "pronunciation": " @@r  r ",
         "ambiguity": 0,
         "what must come before": ".*[QSTKPWHR]\*?",
         "steno theory": "WSI"}],


    "f":[
        {"description": "-F for f",
         "spelling": "ff?",
         "pronunciation": " f ",
         "ambiguity": 0,
         "what must come before": ".*[AOeu]+\*?",
         "steno theory": "WSI"},
         
        {"description": "-F for v",
         "spelling": "f",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": ".*[AOeu]+\*?",
         "steno theory": "WSI"},

        {"description": "-F for s",
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 1,
         "what must come before": ".*[AOeu]+\*?",
         "steno theory": "I think StenEd?"},

        {"description": "-F for v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 1,
         "what must come before": ".*[AOeu]+\*?",
         "steno theory": "I think StenEd?"},

        {"description": "folding -F for s",
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 2,
         "what must come before": ".*[AOeu]r?p?b?l?g?t?s?d?z?\*?",
         "steno theory": "I think StenEd?"},

         {"description": "-F for gh",
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": ".*[AOeurpblgtsdz]+\*?",
         "steno theory": "I don't know"}],

    "fb":[
        {"description": "-FB for v",
         "spelling": "v",
         "pronunciation": " v ",
         "ambiguity": 0,
         "what must come before": ".*[AOeu]+\*?",
         "steno theory": "Josiah?"}],

    "fg":[
        {"description": "-FG for gh",
         "spelling": "gh",
         "pronunciation": " f ",
         "ambiguity": 1,
         "what must come before": ".*[AOeu]+\*?",
         "steno theory": "Harri"}],

    "r": [
        {"description": "-R for r",
         "spelling": "r",
         "pronunciation": " r ",
         "ambiguity": 0,
         "what must come before": ".*[AOeu]+\*?",
         "steno theory": "WSI"},


        {"description": "folding R for suffix er when E is unavailable",
         "spelling": "er",
         "pronunciation": "( suffix )? @r  r ",
         "ambiguity": 2,
         "what must come before": ".*[QSTKPWHR]+([AO]*[eu]+[fpblgtsdz*]*)\*?",
         "steno theory": "Harri"}],

    "rb": [
        {"description": "-RB for sh",
         "spelling": "sh",
         "pronunciation": " sh ",
         "ambiguity": 0,
         "what must come before": ".*[AOeuf]+\*?",
         "steno theory": "I don't know"}],

    "pb": [
        {"description": "-PB for n",
         "spelling": "(e|o)?n",
         "pronunciation": " n ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufr]+\*?",
         "steno theory": "WSI"}],

         


    "/-pbs": [
        {"description": "-PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "I think StenEd?"},

        {"description": "-PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|I2)  suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "I think StenEd?"}],


    "pbs": [
        {"description": "folding -PBS for suffix -ness",
         "spelling": "ness",
         "pronunciation": " suffix  n  E5  s ",
         "ambiguity": 1,
         "what must come before": "(.*/)?[QSTKPWHR]*\*?[AO\-eu]+[frlgt*]*",
         "steno theory": "I think StenEd?"},

        {"description": "folding -PBS for suffix -y then suffix -ness",
         "spelling": "yness",
         "pronunciation": " suffix  (iy|I2)  suffix  n  E5  s ",
         "ambiguity": 2,
         "what must come before": "(.*/)?[QSTKPWHR]*[AO\-eu]+[frlgt*]*",
         "steno theory": "I think StenEd?"}],


    "bg": [
        {"description": "-BG for k",
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrp]+\*?",
         "steno theory": "WSI"},

        {"description": "-BG for ck",
         "spelling": "ck",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrp]+\*?",
         "steno theory": "WSI"},

        {"description": "-BG for k sound spelt ch",
         "spelling": "ch",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrp]+\*?",
         "steno theory": "WSI"}],

    "l":[
        {"description": "-L for l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": ".*[AOeu]f?r?p?b?\*?",
         "steno theory": "I don't know"},

        {"description": "folding -L for l",
         "spelling": "ll?",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": ".*[AOeu]f?r?p?b?g?t?s?d?z?\*?",
         "steno theory": "I don't know"},

        {"description": "folding -L for -ly",
         "spelling": "ly",
         "pronunciation": " suffix  l  iy ",
         "ambiguity": 2,
         "what must come before": ".*[AOeu]f?r?p?b?g?t?s?d?z?\*?",
         "steno theory": "I don't know"}],

    "/-ls":[
        {"description": "-LS for -less",
         "spelling": "less",
         "pronunciation": " suffix  l  E5  s ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "WSI"}],


    "/-g":[
        {"description": "-G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "WSI"}],

    "g":[
        {"description": "-G for g",
         "spelling": "g",
         "pronunciation": " g ",
         "ambiguity": 0,
         "what must come before": "(.*/)?[QSTKPWHR]*[AO\-eu]+[frpbl*]*",
         "steno theory": "WSI"},

        {"description": "folded -G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": "(.*/)?[QSTKPWHR]*[AO\-eu]+[frpblgtsdz*]*",
         "steno theory": "WSI"}],


    "t":[

        {"description": "-T for t",
         "spelling": "tt?",
         "pronunciation": " t ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblg]+\*?",
         "steno theory": "WSI"}],

    #"/-s":[
    #    {"description": "-S for plurals",
    #     "spelling": "s",
    #     "pronunciation": "( (suffix) ) z ",
    #     "ambiguity": 1,
    #     "what must come before": ".*[AOeufrpblgtsdz]+\*?",
    #     "steno theory": "WSI"}],
        
    "s":[

        {"description": "-S for unvoiced s",
         "spelling": "s",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgt]+\*?",
         "steno theory": "WSI"},


        {"description": "folded -S for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) ) (s|z) ",
         "ambiguity": 1,
         "what must come before": ".*t[AOeufrpblg*]*\*?",
         "steno theory": "WSI"}],

    "*s":[
        {"description": "*S for 's",
         "spelling": "'s",
         "pronunciation": " suffix  z ",
         "ambiguity": 2,
         "what must come before": ".*[AOeufrpblgt]+\*?",
         "steno theory": " Josiah"},],

    "/-d": [
        {"description": "-D for -ed",
         "spelling": "ed",
         "pronunciation": " suffix ( I7 )? d ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "WSI"}],

    "d": [
        {"description": "-D for d",
         "spelling": "d",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgts]+\*?",
         "steno theory": "WSI"},

        {"description": "folding -D for -ed",
         "spelling": "ed",
         "pronunciation": " suffix ( I7 )? d ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgts]+\*?",
         "steno theory": "WSI"}],

    "*d": [
        {"description": "*D for y",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": ".*[AOeufrpblgts]+\*?",
         "steno theory": "Harri"},

        {"description": "*D for dy",
         "spelling": "dy",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "what must come before": ".*[AOeufrpblgt]+\*?",
         "steno theory": "HelloChap? I can't remember"}],



    "/-z":[
        {"description": "-Z for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) ) (s|z) ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "WSI"}],

    "z":[
        {"description": "folded -Z for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) ) (s|z) ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgsd]+\*?",
         "steno theory": "WSI"}],
    
    

}
