british_accent = {

    #short, just pay attention to spelling
    #`PRE/TEU` → "pretty"
    #`PWU/SEU` → "busy"
    "short": " \[?(@|@@r|@1|@r|a|a/ee|a1|a4|a4/a|a4/a1|a5|a5/i2|aa|aa1|ae/i|ah|ah1|ah2|ai/i|ao|ar/@@r|ar1|au|e|e/ee|e/ei|e/ii|e0|e0/e|e05|e1|e5|e5/e|e50|ee/a|ee/o|ee1|ee5/ee|i|i/@@r|i/ai|i/e|i/ii|i1|i2|i5|i6|i7|ii/e|ii/i|ii1|o|o/a|o/oo|o/uh|o1|o4|o5|o5/o|oa|oou|or1|our1|ouw1|u|u/@@r|u/ouw|u/uu|uu/u|uh|uh/o|\(@r/e\))\]? ",
    # ii/i bidet/bistro   #ou/o???
    "short r coloured": "none",

    "silent": " \[y1\] ",


    #phonetic, you can ignore spelling
    #`PREU/TEU` → "pretty"
    #`PWEU/SEU` → "busy"
    "A": " \[?(a|ah|ao|oa)\]? ",
    "O": " \[?(au|o|oou)\]? ",  #some of these?@@r|or|our|our/or
    "E": " \[?(e)\]? ",
    #"EU": " \[?(i|iy)\]? ",
    "U": " \[?(uh|ouw?1)\]? ",
    #interestingly enough, there are some vowels that aren't phonetic! Like "u", found in "book" and "bully"


    "AOE": " \[?(aa/ei|ae/ii|e/ii|eir/ir|i/ii|ii|ii/ae|ii/e|ii/i|ii2|ir|iy/ee)\]? ",
    "AOER": "none",



    "AOEU": " \[?(ae|ae/i|ae/ii|aer|ai|ai/ei|ai/ii|ai1|i/ai|ii/ae)\]? ",
    "AOEUR": "none",
    # regarding ai1, some Americans say long i, some skip it, but (most?) British people say long i, so for consistency I'm using long i


    "AOU": "( y )? (iu|iu3|u/ouw|ur|uu|uu/uu|\(u/uu\)) ",
    "AOUR": "none",

    "AEU": " \[?(aa/ee|ee|ee/o|e/ei|ei|eir|eir1|ii/ee|iy/ee|e/ee|ee5/ee)\]? ",
    "AEUR": "none",
    # ii/ee → beta 

    #water, NOT father!!!!!
    #For Brits AU is /ɔː/, not /ɑː/
    "AU": " \[?(oo|o/oo|or|or/ur)\]? ",
    #not au for me: ao  was o/uh   because o/oo   cross au

    "OE": " \[?(ou|ou/o|ou1|ouw)\]? ",

    "OEU": " oi ",

    "OU": " \[?(ow|owr)\]? ",
    "OUR": "none",

    "EU": " \[?(iy)\]? ",
}


american_accent = {

    "short": " \[?(@|@1|@r|a|a/ee|a1|a4|a4/a|a4/a1|a5|a5/i2|aa|ae/i|ah|ah2|ai/i|ao|ar/@@r|ar1|au|e|e/ee|e/ei|e/ii|e0|e05|e1|e5|e5/e|e50|ee/a|ee/o|ee1|ee5/ee|i|i/ai|i/e|i/ii|i1|i2|i5|i6|i7|ii/e|ii/i|ii1|o|o/a|o/uh|o1|o4|o5|o5/o|oa|oou|or1|our1|ouw1|u|u/ouw|u/uu|uu/u|uh|uh/o|\(@r/e\))\]? ",
    # ii/i bidet/bistro   #ou/o???

    "long a": " \[?(aa/ee|ee|ee/o|e/ei|ei|eir|eir1|ii/ee|iy/ee|e/ee|ee5/ee)\]? ",
    # ii/ee → beta 

    "au": " \[?(oa|aa|aa1|ah|ah1|ah2|oo|o/oo)\]? ",
    #not au for me: ao  was o/uh   because o/oo   cross au

    "ow! Sound": " \[?(ow|owr)\]? ",


    "long e": " \[?(aa/ei|ae/ii|e/ii|eir/ir|i/ii|ii|ii/ae|ii/e|ii/i|ii2|ir|iy/ee)\]? ",
    "long o": " \[?(ou|ou/o|ou1|ouw)\]? ",
    "long i": " \[?(ae|ae/i|ae/ii|aer|ai|ai/ei|ai/ii|ai1|i/ai|ii/ae)\]? ",
    # regarding ai1, some Americans say long i, some skip it, but (most?) British people say long i, so for consistency I'm using long i
    "long vowels": " \[?(aa|ee|ei|ir|iy)\]? ",
    # adherence uses ir     #don't wanna drop y uu #\(@r/~  e\) is both long AND short

    "long u": "( y )? (iu|iu3|u/ouw|ur|uu|uu/uu|\(u/uu\)) ",
}



# f'({keysymbol_shorthands["AOE"]}|{keysymbol_shorthands["AOEU"]}|{keysymbol_shorthands["AOU"]}|{keysymbol_shorthands["AOU"]}|{keysymbol_shorthands["AEU"]}|{keysymbol_shorthands["AU"]}|{keysymbol_shorthands["OE"]}|{keysymbol_shorthands["OEU"]}|{keysymbol_shorthands["OU"]}|{keysymbol_shorthands["EU"]})'


vowel_category = british_accent