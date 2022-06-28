import sys
from pathlib import Path

parent = Path.cwd().parent
dest = parent / Path('phonemes')
sys.path.insert(0, dest)



from   .. phonemes.word import  Word


w = Word('jad')
print(w)