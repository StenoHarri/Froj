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

def make_boundaries_into_list(full_pronunciation):
    #print (pronunciation_pattern.split(full_pronunciation))
    morphemes = []
    for morpheme in pronunciation_pattern.split(full_pronunciation):
        if not morpheme:
            continue

        # Stuff to note:
        # the $ symbol is for like run-on morphemes


        if morpheme.startswith("<"):
            morpheme_type = "prefix"
            morpheme = morpheme.replace("<","")
        elif morpheme.startswith("{"):
            morpheme_type = "root"
            morpheme = morpheme.replace("{","").replace("}","")
        elif morpheme.startswith(">"):
            morpheme_type = "suffix"
            morpheme = morpheme.replace(">","")
        else:
            print("error")

        new_morpheme=""
        for each_instance_of_two_vowels_together in two_vowels_together.split(morpheme.strip()):
            if each_instance_of_two_vowels_together[-1] == " ":
                new_morpheme+= each_instance_of_two_vowels_together+". "
            else:
                new_morpheme+= each_instance_of_two_vowels_together
        
        morpheme = " "+new_morpheme+" " #I'll just remove this again after removing the replace stuff below
            

        
        
        morphemes.append([morpheme
                           .replace(" *","") #remove stress marker
                           .replace(" ~","") #I think this is stress too?•
                           .replace(" •","") #stress again
                           .replace(" /","")
                           .replace("/ ","")
                           .replace(" -","") #no idea what this does, but I don't want it
                           .strip()
                           .split(" ")       # make it a list of sounds
                           ,
                          [morpheme_type]])
    print(morphemes)
    return morphemes



#print("something")
