from doctest import script_from_examples
import sys
from pathlib import Path


# note : how to orgnaize importion, attention from where i run the script_from_example
# ask the different between the vs and the cmd

cwd = Path.cwd()
dest = cwd  / 'phonemes'

from phonemes import utils, word, analayse_consonants , Syllable



print ('SRTARTIN TEST')

def _test_structure():
    ## tetsing word and syllable modules
    print('tetsing word and syllable modules')
    with open (dest / Path ('sklton_test.py'), 'r')  as f:
        text = f.readlines()
    for l in text:
        raw_data = l.split('->')
        raw_word  = raw_data[0].strip()[2:]
        processed_word = raw_data[1].strip()[:]
        print (f'Now testing {raw_word} as word')
        assert str (word.Word(raw_word)) == processed_word
        
    print('PASSED')

## testing utils module
## testing matchin modules
def _test_matching():
    print ('TESTING MATCHIN MECHANISM')
    assert utils.match_syllable('banana', 'banana') == [('ba', 'ba'), ('na', 'na'), ('na', 'na')]
    assert (utils.match_syllable('banana', 'nana')) == [('ba', None), ('na', 'na'), ('na', 'na')]
    assert (utils.match_syllable('otobus', 'bus'))  == [('o', None), ('to', None), ('bus', 'bus')]
    assert (utils.match_syllable('otobus', 'us'))  == [('o', None), ('to', None), ('bus', 'us')]
    print('PASSED')



def _test_compare_part():
    print ('TESTING COMPRASION MECHANISM')
    analayse_consonants.compare('b','b')
    analayse_consonants.compare('b','p')
    print(analayse_consonants.df)
    print(analayse_consonants.ERRORS_TABLE)


if __name__ == '__main__':
    print ('Enter data : struct | match | compare ')
    test_input = input() 
    if test_input == 'struct':
        _test_structure()
    elif  test_input == 'match':
        _test_matching()
    elif test_input == 'compare':
        _test_compare_part()
    else:
        print ('TEST WAS NOT EXECUTED')