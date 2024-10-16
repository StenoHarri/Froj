
import re

keysymbol_to_steno_chord={

    #assuming the steno layout is stkpwhrao*EUFRPBLGTSTZ
    #I made the second half capitalised cause it's easier for distinguishing stuff like left vs right "S"

    "s" : ["s"],
    "z" : ["stkpw"],
    "z" : ["stkpw"],
    "jh" : ["skwr"],
    "sh" : ["sh"],
    "zh" : ["sh"],
    "sh r" : ["skhr"],

    "t" : ["t"],
    "d" : ["tk"],
    "g" : ["tkpw"],
    "g w" : ["tkpw"],

    "k" : ["k"],
    "y" : ["kwr"], 

    "" : ["kwr"],
    "b" : ["pw"],
    "w" : ["w","wh"],   #must include wh

    "h" : ["h"],        #must include h
    "l" : ["hr"],

    "r" : ["r"],

    "a" : ["a"],
    "@" : ["a"],        #must include a
    "o" : ["a"],        #must include a
    "ah" : ["a"],
    "aa" : ["a"],
    "uu" : ["ao"],      #must include oo
    "ii" : ["aoE"],
    "ir r" : ["aoER"],
    "ai" : ["aoEU"],
    "ae" : ["aoEU"],
    "iu3" : ["aoU"],
    #"aE" : ", but this
    "ee" : ["aEU"],#yeah I understand,
    "eir r" : ["aEUR"],
    "oo" : ["aU"],
    "ar r b" : ["aURB"],
    "ar r ch" : ["aFRPB"],
    "ar r" : ["aR"],
    "@r r" : ["aR"],

    "o" : ["o"],
    "@" : ["o"],        #must include o
    "ou" : ["oE"],
    "oi" : ["oEU"],
    "ow" : ["oU"],
    "@@r r" : ["oR"],

    "ng k" : ["*PBG"],
    "ng k sh n" : ["*PBGS"],
    "th" : ["*T"],
    "dh" : ["*T"],
    "z" : ["*Z"],

    "e" : ["E"],
    "@r r" : ["ER"],
    "i" : ["EU"],
    "ii" : ["EU"],      #must include i, without an e within 2 letters afterwards
    "@@r r" : ["EUR"],

    "uh" : ["U"],
    "@@ r v" : ["UFRB"],
    "@@r r" : ["UR"],

    "f" : ["F"],
    "ch" : ["FP"],
    "n ch" : ["FRPB"],

    "sh" : ["RB"],

    "p" : ["P"],
    "n" : ["PB"],
    "jh" : ["PBLG"],
    "ng" : ["PBG"],
    "m" : ["PL"],

    "b" : ["B"],
    "ouw" : ["B"],
    "k" : ["BG"],
    "k sh n" : ["BGS"],

    "l" : ["L"],

    "g" : ["G"],
    "k s t" : ["GT"],   #xt
    "sh n" : ["GS"],
    "zh n" : ["GS"],

    "t" : ["T"],

    "s" : ["S"],
    "z" : ["S"],

    "d" : ["D"],
    "s" : ["Z"]

}







def construct_every_combination(path_direction):
    """
    Given a set of options, left or right, up or down.
    Will return all combinations:
    left+up, left+down, right+up, right+down, etc.
    """
    every_combination = [[]]  # Initialize with empty list
    for length_of_combination in range(len(path_direction)):
        current_options = path_direction[length_of_combination]
        new_combinations = []  # Temporary list to store updated combinations

        for option in current_options:
            for existing_combination in every_combination:
                new_combination = existing_combination + [option]
                new_combinations.append(new_combination)

        every_combination = (new_combinations)  # Add new combinations

    every_valid_combination = []
    for combination in every_combination:
        valid_combination=re.fullmatch(r'(s?t?k?p?w?h?r?a?o?\*?E?\*?U?\*?F?\*?R?\*?P?\*?B?\*?L?\*?G?\*?T?\*?S?\*?D?\*?Z?)',"".join(combination))
        if valid_combination:
            every_valid_combination.append(valid_combination[0])

    return every_valid_combination





word = "w i ng k "
word =["w","i","ng","k"]
word =["red", "orange",["blue", "green"],"yellow"]
word =["w","i","ng","k"]


def listed_word_validator(word_parts):
        steno=[]
        try:
            for word_part in word_parts:
                steno+=([keysymbol_to_steno_chord[word_part]])
        except KeyError:
            return
        

        return construct_every_combination(steno)
#from more_itertools import locate



def generate_every_split_of_a_morpheme_via_syllables(morpheme):
    

    combinations_to_search_with=[]
    for position_of_sound in range(2**(len(morpheme)-1)):
        # Generate binary masks for the morpheme
        bin_mask = "1"+(format(position_of_sound, '{fill}{width}b'.format(width= len(morpheme)-1, fill=0)))
        if bin_mask=="10":
            bin_mask="1"
        
        #inefficient, as these could have been simply not generated in the first space
        is_split_already_in_the_correct_spot = True
        for position in range(len(bin_mask)):
            if morpheme[position]==('.'):
                if not (bin_mask[position] == "1" and bin_mask[position+1] == "1"):
                    is_split_already_in_the_correct_spot=False
        if not is_split_already_in_the_correct_spot:
            continue


        
        # Combine the binary mask with the morpheme
        combination_to_search_with = []
        for position in range(len(bin_mask)):

            if morpheme[position] == ".":
                continue
            
            #if it's 1, add the morpheme ["i"]+["d"] = ["i"]+["d"]
            if bin_mask[position]=="1" or morpheme[position-1] == ".":
                combination_to_search_with+=([morpheme[position]])

            #if it's O, add the morpheme  ["i"]+["d"] = ["i d"]
            else:
                combination_to_search_with[-1]+=" "+morpheme[position]
        combinations_to_search_with+=[combination_to_search_with]
    return combinations_to_search_with



def generate_write_outs(pronunciation):
    print(pronunciation)
    for morpheme in pronunciation: # morpheme[0] is what makes the morpheme, morpheme[1] is the type
        morpheme_text = morpheme[0]
        morpheme_type = morpheme[1]
        
        every_split_of_morpheme = generate_every_split_of_a_morpheme_via_syllables(morpheme_text)
        print("something else")
        


        

        ####I need to add logic here, one for splitting at the . and one for splitting at the ==



        #Split each combination using 'O'
        #listed_pronunciation = (combination_to_search_with.split('0'))

        #look up what each combination maps to
        #listed_pronunciations=listed_word_validator(listed_pronunciation)
        #if listed_pronunciations:
        #    for listed_pronunciation in listed_pronunciations:
        #        print("".join(pronunciation) + " maps to " + listed_pronunciation)

#generate_write_outs([[['i', '.', 'd', 'ii', '@', '.', 's', 'iy'], ['root']], [['z'], ['suffix']]])