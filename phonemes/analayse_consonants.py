import json
import string
import pandas as pd
import numpy as np
from . syllable import Syllable 

# create empty table for the conconants analyzing section

abc = list(string.ascii_lowercase[:26])
for c in ['c','q', 'w','y']:
    abc.remove(c)
# adding ts , sh
abc += ['S', '&']
target = 'target_occurance'.upper()
production = 'production_occurance'.upper()
df = pd.DataFrame(np.zeros((len(abc),2)), index = abc, columns=[target, production])
ERRORS_TABLE = {}



with open('./phonemes/phonemes.json', 'r') as f:
    data = json.load(f)
    ALPHA_BET = data['ALPHABET']


## how to check cluster?
## currently (9.7.22): cluster are not compared, becoyse probably if err it will envolve
## prosodic process
def check_consonant_in_word(processed_word:list)->None:      
    for pos, syllable in enumerate(processed_word):
        target = Syllable(syllable[0], pos)
        # if all syllable was omitted so this function dont need to take care
        # about this error, it is prosodic error
        if syllable[1] == None:
            break

        prod  = Syllable(syllable[1], pos)
        # onest checking
        if target.has_onset:
            if not target.is_cluster:
                compare(target, prod, 'onset')
        # rhyme checking
        compare(target, prod, 'rhyme')

        # coda checking
        if not target.is_open:
            if  not prod.is_open:
                compare(target, prod, 'coda')


def compare(target:Syllable, prod:Syllable, part_name:str):
    target_part = target.syllable_parts[part_name]
    prod_part = prod.syllable_parts[part_name]
    df.loc[target_part, 'target_occurance'.upper()] += 1
    
    # omittion -> will be review at prosodic part
    if prod_part == '':
        return
    # correct production 
    elif target_part == prod_part:
        df.loc[target_part, 'production_occurance'.upper()] += 1
    
    # subtitution
    else:
        type_of_err = f'{target_part}->{prod_part}'
        if part_name == 'rhyme':
            type_of_err = 'vowel changes'
        if type_of_err in ERRORS_TABLE:    
            ERRORS_TABLE[type_of_err] += 1
        else:
            ERRORS_TABLE[type_of_err] = 1


def check_words (word_list:list):
    for w in word_list:
        check_consonant_in_word(w)



def errors_classifyer(dict_of_err:dict):
    ERRORS_TYPE = set()
    for k in dict_of_err.keys():
        # unpacked phonmes
        t, p = k.split('->')
        if ALPHA_BET[t]['class'] == 'consonants':
            if  ALPHA_BET[t]['type'] == 'fricative' and ALPHA_BET[p]['type'] == 'plosive':
                ERRORS_TYPE.add('stoping')
            if (ALPHA_BET[t]['voicing'] == True) and ALPHA_BET[p]['voicing'] == False:
                ERRORS_TYPE.add('devoicing')
            if ALPHA_BET[t]['frontization'] > ALPHA_BET[p]['frontization']:
                ERRORS_TYPE.add('backing')
            if ALPHA_BET[t]['frontization'] < ALPHA_BET[p]['frontization']:
                ERRORS_TYPE.add('fronting')
    return list(ERRORS_TYPE)