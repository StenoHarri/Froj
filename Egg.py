"""
questions for professor
why is pancake pang+cake
but suncream sun+cream not sung+cream?
or ingcorporate

If the unilex is meant to be used for natural speech, how does it deal with when neighbouring words in a sentence do this?
"I think my son g could do that. (and if it's not noticeable, then why do it for pang cake?)
"""

from convert_unilex_into_readable_lists import (
    full_entry_pattern,
    make_boundaries_into_list)

from map_steno_chords_to_keysymbols import generate_write_outs





def make_input_into_dictionary_entry(input):
    word = full_entry_pattern.fullmatch(input).groupdict()

    word['pronunciation'           ] = make_boundaries_into_list(word['pronunciation'])
    word['word_boundaries'         ] = make_boundaries_into_list(word['word_boundaries'])
    #print(word)
    word['full write outs'         ] = generate_write_outs(word)
    word['briefs within boundaries'] = "still need to code this"
    word['briefs across boundaries'] = "still need to code this"

    #print(word)
    return {word['word']:word}






#do everything simultaneously, however it's quiet if it doesn't find anything.
#with (open("Smol.txt", "r", encoding="utf-8")) as txt_dictionary:
#    result = list(map(lambda x: full_entry_pattern.fullmatch(x).groupdict(), txt_dictionary.readlines()))

    #matches = full_entry_pattern.findall(txt_dictionary.readlines())

#print(result)
dictionary={}



with (open("big.txt", "r", encoding="utf-8")) as txt_dictionary:


    something={}
    for outline in txt_dictionary:
        something.update(make_input_into_dictionary_entry(outline))
        #print("\n")


    """
    for entry in something:
        print(
                f"{something[entry]['word']:15}"
                +"\n      pronunciation:  "
                +f"{str(something[entry]['pronunciation']):<45}"
                +"\n      word boundaries:"
                +f"{str(something[entry]['word_boundaries']):20}"
                +"\n      full write outs:"
                +str(something[entry]['full write outs'])
                )
        print("")
    """



"""

dictionary['["seriously"],["RB"]'] = [

            #phonetics
            [[[["s"] ["*"] ["ir"] ["."] ["r"] ["ii"] ["@"] ["s"]],["root"]],[["l iy"],["suffix"]]],

            #orthography
            [[["serious"],["root"]],          [["ly"],["suffix"]]],

            #write outs
            ["SAOER/KWRAOE/KWRUS/HREU" 1],

            #briefing within word boundaries
            ["SAOER/KWHUS/HREU" 1, "SAO*ERD/KWRUS/HREU" 2,"SAOERS/HREU" 3],

            #briefing between word boundaries
            ["SAOER/KWRAOE/KWRULS" 2, "SAOER/KWHULS" 3, "SAO*ERD/KWRULS" 3,"SAOER/KWRULS" 4,"SAO*ERLSZ" 5, "SAOERLS" 5,"SHRAOERLS" 6]]


"""
