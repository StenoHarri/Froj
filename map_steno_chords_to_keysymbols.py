"""
Using the layout

STKPWHRAO*eufrpblgtsds
Making the right hand lowercase so I don't have to worry about left P vs right P

"""

keysymbol_shorthands={
    """
    There will be groups of keysymbols that come up again and again,
    so I'll define them once here
    """
    "long a":"a i",
    "schwa" :"@",
    "any vowel" : "(a|@)"
}

spelling_shorthands={
    """
    There will be groups of letters that come up again and again,
    so I'll define them once here
    """
    "":"a i",
    "schwa" :"@",
    "":""
}


steno_chords_and_their_meanings={
    """
    Chord: [[spelling,          sound,          briefiness, theory]]
    """

    "S" : [["s",                "s",            0,  "WSI"],
           ["c",                "s",            1,  "WSI"],
           ["sc",               "s",            2,  "WSI"],
           ["[sc][aeiou][scb]", "s[aeiou][sb]", 3,  "WSI"]],


    "T" : [["t",                "t",            0,  "WSI"],
           ["t[aeiou]",         "t[aeiou]",     3,  "WSI"]],

    "TK": [["d",                "d",            0,  "WSI"],
           ["d[aeiou]",         "d[aeiou]",     3,  "WSI"]],


    "K": [["k",                 "k",            0,  "WSI"],
          ["c",                 "k",            1,  "WSI"]],


    "HR":[["l",                 "l",            0,  "WSI"],
          ["ll",                "l",            1,  "WSI"]], #Alan vs Allan

    "A" : [["a",        "a",    0]],

    "AOe": [["ee",     "ii", 0],
            ["e(consonant)?(vowel)", "ii", 1]], #but for something like adhesive, um, just read it

    "Ou":[["ou",                "ow",           0,  "WSI"],
          ["ow",                "ow",           1,  "WSI"]],



    "e" : [["e",    "e",    0, "WSI"],
           ["e",    "E",    1, "WSI"]], #alphabEtise

    "eu": [["i",    "i",    0, "WSI"],
           ["y",    "i",    1, "WSI"]]

    "pb":[["n",                 "n",            0,  "WSI"]],


    "d":[["d",                  "d",            0,  "WSI"]]
    


}

