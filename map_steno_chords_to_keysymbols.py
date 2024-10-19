"""
Using the layout

STKPWHRAO*eufrpblgtsds
Making the right hand lowercase so I don't have to worry about left P vs right P

"""

steno_chords_and_their_meanings={
    """
    Chord: [[spelling,          sound,          briefiness]]
    """

    "S" : [["s",                "s",            0],
           ["c",                "s",            1],
           ["sc",               "s",            2],
           ["[sc][aeiou][sc]",  "s[aeiou]s",    3]],


    "T" : [["t",                "t",            0],
           ["t[aeiou]",         "t[aeiou]",     3]],

    "TK": [["d",                "d",            0],
           ["d[aeiou]",         "d[aeiou]",     3]],


    "A" : [["a",        "a",    0]],

    "AOe": [["ee",     "ii", 0],
            ["e(consonant)?(vowel)", "ii", 1]], #but for something like adhesive, um, just read it

    "e" : [["e",    "e",    0],
           ["e",    "E",    1]], #alphabEtise

    "eu": [["i",    "i",    0],
           ["y",    "i",    1]]


}

