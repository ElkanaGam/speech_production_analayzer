from ctypes import util
import sys
from pathlib import Path

parent = Path.cwd().parent
sys.path.append('..')
from phonemes import utils

utils._is_here()