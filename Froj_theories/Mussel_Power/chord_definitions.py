import re


try:
    from Froj_theories.Mussel_Power.vowel_categories import vowel_category
except ModuleNotFoundError:
    # Allow running as a script
    from vowel_categories import vowel_category


custom_alphabet = "12345678lrLR-AOEU12345678lLrR_"
valid_final_letter = r'[\-AOEU]([12345678lLrR]+)?$' #Will need to come back to this for multi-strokes
does_theory_pay_attention_to_stress_markers = True



#_ to say "don't skip a series"


"""
Regex logic here
"""
"""
There will be groups of keysymbols that come up again and again,
so I'll define them once here
"""

# regex logic for what must come before
# hopefully compiling it all here makes it run faster since they'll be used

# A_to_z_or_nothing_at_all = re.compile(r'(.*[\-AOeufrpblgtsdz])?\*?$')
# NothingRegex = re.compile(r'')
# AtLeastOneCharacterRegex = re.compile(r'.+')




"""
Chord: [[spelling,          sound,          briefiness, theory]]
"""
steno_chords_and_their_meanings = {



}

