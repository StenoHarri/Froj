
import json
import re

lookup = {}

with open("Froj_theories/Froj_Harri_theory/best_of_word_to_entry_lookup.json", "r") as f:
    lookup['word_lookup'] = json.load(f)

with open("Froj_theories/Froj_Harri_theory/Froj_verbose_lookup.json", "r") as f:
    lookup['entry_lookup'] = json.load(f)


is_raw_steno = re.compile(r'^(S?T?K?P?W?H?R?[AO*\-EU]+F?R?P?B?L?G?T?S?D?Z?)(/S?T?K?P?W?H?R?[AO*\-EU]+F?R?P?B?L?G?T?S?D?Z?)*$')



def get_annotation_level(word_to_find):

    if word_to_find.startswith(":>>"):
        return word_to_find.replace(":>>","").strip(), True

    else: # it must be :>
        return word_to_find.replace(":>","").strip(), False


def get_response( user_input:str) -> str:

    word_to_find, complexity = get_annotation_level(user_input)

    if word_to_find == '':
        return 'you can do :> for lookup, :>> for annotated lookup'


    if re.search(is_raw_steno, word_to_find):

        type_of_lookup = 'entry lookup'
    else:
        type_of_lookup = 'word lookup'
        word_to_find = word_to_find.lower()


    



    if 'hello' in word_to_find:
        return f"Hi friend (ΘoΘ )"
    elif 'froj' in word_to_find:
        return f"That's me! How can I help?"
    elif 'shrimp' in word_to_find:
        return "🦐"
    elif 'crazy' in word_to_find:
        return "I was crazy once"
    elif type_of_lookup == 'entry lookup' and word_to_find in lookup['entry_lookup']:
        return f"hi"
    elif type_of_lookup == 'word lookup' and f"{word_to_find}:" in lookup['word_lookup']:
        return f"hello"

        response = ""
        response+= f'found `{word_to_find}` in Tad theory'



        if best_words[word_to_find+':']['text'] == "showing the best 0 out of 0 entries":
            return "Sorry, Harri hasn't written all the rules to make that word. Removing suffixes *might* help"

        response+= f"\n{best_words[word_to_find+':']['text']}"

        for entry in reversed(best_words[word_to_find+':']['entries']):
            response+=f"```"

            thingie = (entry['raw steno']
                   .replace('Z*','*Z')
                   .replace('D*','*D')
                   .replace('S*','*S')
                   .replace('T*','*T')
                   .replace('G*','*G')
                   .replace('L*','*L')
                   .replace('B*','*B')
                   .replace('P*','*P')
                   .replace('R*','*R')
                   .replace('F*','*F')
                   .replace('U*','*U')
                   .replace('E*','*E')
                   .replace('-*','*'))

            response+= (f"\n{thingie}")
            if complexity == 'complex':
                for chord in entry['explanation']:
                    left_spaces = ''
                    right_spaces = ''
                    for space_to_add in range(10 - len(chord['theory'])):
                        left_spaces+=' '

                    for space_to_add in range(10 - len(chord['chord'])):
                        right_spaces+=' '

                    response+= f"\n{chord['theory']}{left_spaces}{chord['chord']}{right_spaces}{chord['description']}"
            response+= f"```"

        return response

    else:
        return "```ANSI\n\033[31mHello\033[0mSorry, I'm missing the pronunciation data for that word :(```"



