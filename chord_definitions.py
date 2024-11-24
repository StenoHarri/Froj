

y_chord = "KWH" # the 'y' in yet or the 'i' in genius
silent_linker = "KWR" # the 'linker' in genus


keysymbol_shorthands = {
    """
    There will be groups of keysymbols that come up again and again,
    so I'll define them once here
    """
    "long a": "a i",
    "schwa": "@",
    "any vowel": "(a|@)"
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
         "what must come before": ".*[/STKPWHR]\*?((Aoe)|(AOeu)|(AOu)|(Ae)|(Aeu)|(O)|(Oe)|(Oeu))[*frpblgtsdz]+",
         "steno theory": "WSI"}],


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
         "what must come before": "(.*[AOEUFRPBLGTSDZ]\*?)",
         "steno theory": "WSI"},

        {"description": "S for linking vowel + s",
         "spelling": "[aeiouy]ss?",
         "pronunciation": keysymbol_shorthands["any vowel"] + " s ",
         "ambiguity": 1,
         "what must come before": "(.*[AOEUFRPBLGTSDZ]\*?)",
         "steno theory": "WSI"}],

    "/S*": [
        {"description": "S* for initial s of a compound word",
         "spelling": "ss?",
         "pronunciation": " s ",
         "ambiguity": 0,
         "what must come before": "(.*[AOEUFRPBLGTSDZ])*",
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


    "/K": [
        {"description": "K for initial/linking k",
         "spelling": "k",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 0,
         "what must come before": "",
         "steno theory": "WSI"},

         {"description": "K for initial/linking hard c",
         "spelling": "c",
         "pronunciation": " (starting_)?((root)|(prefix)|(suffix))  k ",
         "ambiguity": 1,
         "what must come before": "",
         "steno theory": "WSI"}],

    "K": [
        {"description": "K for k",
         "spelling": "k",
         "pronunciation": " k ",
         "ambiguity": 0,
         "what must come before": ".*[/S]\*?",
         "steno theory": "WSI"},

        {"description": "K for hard c",
         "spelling": "c",
         "pronunciation": " k ",
         "ambiguity": 1,
         "what must come before": ".*[/S]\*?",
         "steno theory": "WSI"}],


    "/KWH": [
        {"description": "KWH for initial/linking y",
         "spelling": "y",
         "pronunciation": " ((root)|(prefix)|(suffix))?  iy ",
         "ambiguity": 0,
         "what must come before": ".*[frpblgtsdz]+\*?",
         "steno theory": "User preference"}],

    "/KWR": [
        {"description": "KWR for initial/linking k",
         "spelling": "",
         "pronunciation": " ((root)|(prefix)|(suffix)) ",
         "ambiguity": 0,
         "what must come before": ".*[frpblgtsdz]+\*?",
         "steno theory": "WSI"}],


    "HR": [
        {"description": "HR for l",
         "spelling": "l",
         "pronunciation": " l ",
         "ambiguity": 0,
         "what must come before": ".*[/STKPW]\*?",
         "steno theory": "WSI"},


        {"description": "HR for ll",
         "spelling": "ll",
         "pronunciation": " l ",
         "ambiguity": 1, #Alan Allan
         "what must come before": ".*[/STKPW]\*?",
         "steno theory": "WSI"}],

    "/Aeu": [
        {"description": "AEU for initial long a",
         "spelling": "a",
         "pronunciation": " (starting_)?((root)|(prefix))  ee ",
         "ambiguity": 0,
         "what must come before": ".*",
         "steno theory": "WSI"}],

    "Ou": [
        {"description": "OU for ow said like ow",
         "spelling": "ow",
         "pronunciation": " ow ",
         "ambiguity": 0,
         "what must come before": ".*[STKPWHR]+\*?",
         "steno theory": "WSI"},

        {"description": "OU for ou said like ow",
         "spelling": "ou",
         "pronunciation": " ow ",
         "ambiguity": 1,
         "what must come before": ".*[STKPWHR]+\*?",
         "steno theory": "WSI"}],

    "eu": [
        {"description": "EU for y said like long e",
         "spelling": "y",
         "pronunciation": " iy ",
         "ambiguity": 0,
         "what must come before": ".*[STKPWHR]+\*?",
         "steno theory": "I think StenEd?"}],


    "pb": [
        {"description": "-PB for n",
         "spelling": "n",
         "pronunciation": " n ",
         "ambiguity": 0,
         "what must come before": ".*[STKPWHRAOeufr]+\*?",
         "steno theory": "WSI"}],

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
        {"description": "folded -G for -ing",
         "spelling": "ing",
         "pronunciation": " suffix  i  ng ",
         "ambiguity": 1,
         "what must come before": "(.*/)?[STKPWHR]*[AO\-eu]+[frpblgtsdz*]*",
         "steno theory": "WSI"}],


    "/-s":[
        {"description": "-S for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) ) z ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "WSI"}],
        
    "s":[
        {"description": "folded -S for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) ) z ",
         "ambiguity": 2,
         "what must come before": ".*[AOeufrpblgt]+\*?",
         "steno theory": "WSI"}],


    "d": [
        {"description": "-D for d",
         "spelling": "d",
         "pronunciation": " d ",
         "ambiguity": 0,
         "what must come before": ".*[STKPWHRAOeu]+\*?",
         "steno theory": "WSI"}],

    "*d": [
        {"description": "*D for y",
         "spelling": "y",
         "pronunciation": "( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 2,
         "what must come before": ".*[STKPWHRAOeu]+\*?",
         "steno theory": "Harri"},

        {"description": "*D for dy",
         "spelling": "dy",
         "pronunciation": " d ( ((root)|(prefix)|(suffix)) )? iy ",
         "ambiguity": 4,
         "what must come before": ".*[STKPWHRAOeu]+\*?",
         "steno theory": "HelloChap? I can't remember"}],



    "z":[
        {"description": "folded -Z for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) )? z ",
         "ambiguity": 1,
         "what must come before": ".*[AOeufrpblgtsd]+\*?",
         "steno theory": "WSI"}],
    
    "/-z":[
        {"description": "-Z for plurals",
         "spelling": "s",
         "pronunciation": "( (suffix) )? z ",
         "ambiguity": 0,
         "what must come before": ".*[AOeufrpblgtsdz]+\*?",
         "steno theory": "WSI"}],

}
