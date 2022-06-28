from doctest import script_from_examples
import sys
from pathlib import Path

# note : how to oranaize impirtion, attention from where i run the script_from_example
# ask the different between the vs and the cmd

parent = Path.cwd().parent
dest = parent / Path('phonemes')
sys.path.insert(0, dest)

from phonemes import utils



print ('start..')
assert utils._foo() == 'plosive'
print('PASSED')