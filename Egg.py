from regex_patterns import full_entry_pattern, pronunciation_pattern, make_boundaries_into_list
from generate_steno import generate_write_outs





def make_input_into_dictionary_entry(input):
    word = full_entry_pattern.fullmatch(input).groupdict()

    word['pronunciation'           ] = make_boundaries_into_list(word['pronunciation'])
    word['word_boundaries'         ] = make_boundaries_into_list(word['word_boundaries'])
    print(word)
    word['full write outs'         ] = generate_write_outs(word['pronunciation'])#, word['word_boundaries'])
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



with (open("smol.txt", "r", encoding="utf-8")) as txt_dictionary:
    print ("\n\n"+f"{'word':15}"+" || "+f"{'type':<5}"+" | "+f"{'pronunciation':<45}"+" | "+f"{'word boundaries':20}"+" | "+"commonness\n")
    something={}
    for outline in txt_dictionary:
        something.update(make_input_into_dictionary_entry(outline))
        print("\n\n\n\n")
        for entry in something:
            print(f"{something[entry]['word']:15}"+" || "+f"{str(something[entry]['pronunciation']):<45}"+" | "+f"{str(something[entry]['word_boundaries']):20}"+" | "+"commonness\n"+str(something[entry]['full write outs'])+"\n")
        print(something)



"""



dictionary['["seriously"],["RB"]'] = [
            
            #phonetics
            [[[["s"] ["*"] ["ir"] ["."] ["r"] ["ii"] ["@"] ["s"]],["root"]],[["l iy"],["suffix"]]],

            #orthography
            [[["serious"],["root"]],          [["ly"],["suffix"]]],

            #write outs
            ["SAOER/KWRAOE/KWRUS/HREU"],

            #briefing within word boundaries
            ["SAO*ERD/KWRUS/HREU","SAOER/KWRUS/HREU","SAOERS/HREU"],

            #briefing between word boundaries
            ["SAOER/KWRAOE/KWRULS", "SAO*ERD/KWRULS","SAOER/KWRULS","SAOERLS","SHRAOERLS"]]

"""