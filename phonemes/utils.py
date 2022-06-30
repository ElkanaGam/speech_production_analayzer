from colorsys import rgb_to_hls
from dataclasses import dataclass
from re import T
from xmlrpc.client import Boolean
from . word import Word
from . syllable import Syllable
import json


def _comp_length(x:any, y:any)-> Boolean:
    try: 
        if len(x) == len(y):
            return True
        else:
            return False
    except TypeError:
        print('types doesnt have len()')
    finally:
        return

with open('./phonemes/phonemes.json', 'r') as f:
    data = json.load(f)
    ALPHA_BET = data['ALPHABET']

def _foo():
    return ALPHA_BET['b']['type']

def match_syllable(target, production):
    target = Word(target)
    production = Word (production)
    matching_list =[]
    if _comp_length(target, production):
        matching(target, production, matching)
        return matching
    # ommition has ocuured
    index  = 0
    offset = len(target) - len(production) + 1
    roof = 100
    for i in range (offset):
        temp_sum = 0
        for j in range(len(production)):
            temp_sum += find_different(target.syllables_list[j+i], production.syllables_list[i])
        if temp_sum < roof:
            roof = temp_sum
            index  = i
        temp_sum = 0
    matching (target, production, index, matching_list)
    return matching_list


#total_list :[[(w1s1,w1s1),(w1s2,w1s2)],[(w2s1,w2s1),(w2s2,w2s2)]]
def matching(target:Word, production:Word, index: int, total_list: list) ->None:
    temp_list = []
    for i in range (0, index):
        part = (target.syllables_list[i], None)
        total_list.append(part)
    for i in range (index, target.get_syllables_num):
        part = (target.syllables_list[i], production.syllables_list[i])
        total_list.append(part)
    for i in range (index+production.get_syllables_num, target.get_syllables_num):
        part = (target.syllables_list[i], None)
        total_list.append(part)

def find_consonants_different(c1:str,c2:str)->int:
    total_score = 0
    characteristics = ['type','articulation_place','voicing']
    for c in characteristics:
        if ALPHA_BET[c1][c] != ALPHA_BET[c1][2]:
            total_score += 1
    total_score += abs(ALPHA_BET[c1]['sonorant_rank']-ALPHA_BET[c2]['sonorant_rank'])
    return total_score

def find_vowel_different(v1:str, v2: str) -> int:
    if v1 != v2:
        return 1
    else: 
        return 0

def find_cluster_different (s1:str, s2:str)->int:
    total_score = 0
    #production long than target
    if len(s2) > len (s1):
        total_score += 2
    # production length <= target length
    elif len (s1) != len(s2):
        total_score += 1
    for i in range(len(s2)):
        total_score += find_consonants_different(s1[i], s2[i])
    
def find_different (s1:Syllable, s2:Syllable)-> int:
    onset_diff = find_cluster_different(s1.parts['onset'], s2.parts['onset'])
    rhyme_diff = find_vowel_different(s1.parts['rhyme'], s2.parts['rhyme'])
    coda_diff = find_cluster_different(s1.parts['coda'], s2.parts['coda'])
    return onset_diff+rhyme_diff+coda_diff