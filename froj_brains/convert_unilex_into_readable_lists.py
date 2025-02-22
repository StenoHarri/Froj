import re



full_entry_pattern = re.compile(r"""
                #Spelling:
                (?P<word>
                    ([a-z'-.]+?)    #the . is needed literally just for dot.com
                    :
                    (([0-9]*?),?(.*?)) #with homonyms, they each get numbers.
                ) 
                :

                #word class (like is it a noun or something)
                (?P<word_class>
                [A-Z/|$]+?
                )
                :\           #Trailing whitespace

                #pronunciation
                #((\{[a-z *@.]+\})*|(\>[a-z *@.]+\>)*.*)           #group 3
                (?P<pronunciation>
                .*?
                #   ((?P<prefix>:?\<.*?\<)|(?P<root>:?\{.*?\})|(?P<suffix>:?\>.*?\>)|\.?)+
                )
                \ :

                #word boundaries
                (?P<word_boundaries>
                .*?
                )
                :                #delete formatting
                #frequency
                (?P<frequency>
                [0-9]*
                )         #group 5
                \n               #delete formatting
                """, re.X)




two_vowels_together = re.compile(r"""
                (\ (?:ii|i|ie|e|a|uh|aa|aai|o|oo|u|uu|uw|@@|@|ei|ai|oi|au|ou|ouw|oul|uul|ah|
                ah2|iy|ow|oow|ou|oou|ao|oa|ir|er|ar|or|our|ur|i@|ae|iu3|@r|I2|E0|I7|@@r|
                eir|iu|A4|O4|UH4|A5|EE5|EI5|O5|I6|I4|E5|O6|O3|I5|@@r2|@@r3|aer|owr|oir|
                OU5|ii|uu|ur|ir|ii2|ee|EE1|eh|UH|OO1|EI|EE|iir|OUW1|E50|E05|iur|UW)\ )

                (ii|i|ie|e|a|uh|aa|aai|o|oo|u|uu|uw|@@|@|ei|ai|oi|au|ou|ouw|oul|uul|ah|
                ah2|iy|ow|oow|ou|oou|ao|oa|ir|er|ar|or|our|ur|i@|ae|iu3|@r|I2|E0|I7|@@r|
                eir|iu|A4|O4|UH4|A5|EE5|EI5|O5|I6|I4|E5|O6|O3|I5|@@r2|@@r3|aer|owr|oir|
                OU5|ii|uu|ur|ir|ii2|ee|EE1|eh|UH|OO1|EI|EE|iir|OUW1|E50|E05|iur|UW)

                #\        #hoping it's just greedy
                                               """, re.X)

r_following_an_r_affected_vowel = re.compile(r"""
                                             
                \ (ir|er|ar|or|our|ur|i@|ae|iu3|@r|@@r|eir|@@r2|@@r3|aer|owr|oir|ur|ir|ii2|iir|iur)
                . r

                                             """, re.X)


pronunciation_pattern = re.compile(r"""
                                    (?P<prefix>:?\<.*?\<)|
                                    (?P<root>:?\{.*?\})|
                                    (?P<suffix>:?\>.*?\>)|\.
                                   """, re.X)


def make_target_pronunciation_into_string(target_list):
    string=" starting__"
    for morpheme in target_list:
        #print(morpheme[1][0]) would print stuff like root root root root
        string+=' '+morpheme[1][0] + "  " + "  ".join(morpheme[0]) + " "
    return string.replace('_ ','')



def make_target_spelling_into_string(target_list):
    #ended up removing a lot of the features, since you can just arse contain
    string=""
    for morpheme in target_list:
        string+="Something went wrong".join(morpheme[0])
    return string

def make_boundaries_into_list(full_pronunciation):
    #print (pronunciation_pattern.split(full_pronunciation))
    morphemes = []

    last_word_was_a_root=False
    for morpheme in pronunciation_pattern.split(full_pronunciation):
        if not morpheme:
            continue

        # Stuff to note:
        # the $ symbol is for like run-on morphemes


        if morpheme.startswith("<"):
            morpheme_type = "prefix"
            morpheme = morpheme.replace("<","")
            last_word_was_a_root=False
        elif morpheme.startswith("{"):
            if last_word_was_a_root:
                morpheme_type = "compound"
            else:
                morpheme_type = "root"
                last_word_was_a_root =True
            morpheme = morpheme.replace("{","").replace("}","")
        elif morpheme.startswith(">"):
            morpheme_type = "suffix"
            morpheme = morpheme.replace(">","")
            #last_word_was_a_root=False `TKULTS/O*EPBL` → `adult {^s} {^-only}` the `{^s}` doesn't stop it being a root
        else:
            #print("error")
            "error"

        new_morpheme=""
        
        for each_instance_of_two_vowels_together in two_vowels_together.split(morpheme.strip()):
            #looking back on this a few months later, I think what this is doing is separating out the vowels because then I can start a new stroke cleanly
            if each_instance_of_two_vowels_together=="":
                "do nothing because you're now following after a diphthong at the end of a word, nothing comes after it"
            else:
                if each_instance_of_two_vowels_together[-1] == " ":
                    new_morpheme+= each_instance_of_two_vowels_together+". "
                    #print(each_instance_of_two_vowels_together)
                else:
                    new_morpheme+= each_instance_of_two_vowels_together
        
        morpheme = " "+new_morpheme+" " #I'll just remove this again after removing the replace stuff below



        morphemes.append([morpheme
                           .replace(" ~/*","")
                           .replace(" */~","")
                           .replace(" *","") #remove stress marker
                           .replace("* ","")#[*  e]
                           .replace(" ~","") #secondary stress (for compound words)
                           .replace("~ ","") #[~ a]
                           .replace(" •","") #stress again
                           .replace(" /","")
                           .replace("/ ","")
                           .replace(" -","") #no idea what this does, but I don't want it
                           .replace(" $","") #dunno what this is either
                           #.replace(" . ","") #syllable
                           .replace(". ","") #syllable boundaries
                           .replace(" .1","")
                           .replace(" ==","") #morpheme
                           .replace(" =.=","")
                           .replace("==","") #gotta do this since it's in the spelling section too
                           #.replace("= ","") #morpheme he
                           .replace(" [*]","")
                           .replace(" [*1]","")
                           .replace(" [~]","")
                           .replace(" [~1]","") #accent dependent stress markers
                           .lower()
                           .strip()
                           .split(" ")       # make it a list of sounds
                           ,
                          [morpheme_type]])
    #print(morphemes)
        

    return morphemes
    return make_target_pronunciation_into_string(morphemes)



#print("something")
