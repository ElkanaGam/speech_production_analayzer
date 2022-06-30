from doctest import script_from_examples
import sys
from pathlib import Path


# note : how to orgnaize importion, attention from where i run the script_from_example
# ask the different between the vs and the cmd

cwd = Path.cwd()
dest = cwd  / 'phonemes'

from phonemes import utils, word



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
    print (utils.match_syllable('banana', 'banana'))
    print('PASSED')



if __name__ == '__main__':
    print ('Enter data : struct | match ')
    test_input = input() 
    if test_input == 'struct':
        _test_structure()
    elif  test_input == 'match':
        _test_matching()
    else:
        print ('TEST WAS NOT EXECUTED')