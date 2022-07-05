from colorsys import rgb_to_hls
from dataclasses import dataclass
from re import T
from xmlrpc.client import Boolean
from . word import Word
from . syllable import Syllable
import json


def _is_here():
    print('Imporeted')

def _comp_length(x:any, y:any)-> Boolean:
    try: 
        if len(x) == len(y):
            return True
        else:
            return False
    except TypeError:
        print('types doesnt have len()')
    

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
        matching(target, production,0, matching_list)
        return matching_list
    # ommition has ocuured
    offset = target.get_syllables_num() - production.get_syllables_num() + 1
    temp_match  = 100
    index = 0
    i = 0
    while i < offset:
        if find_different(target.syllables_list[i], production.syllables_list[0]) < temp_match :
            index= i
            temp_match = find_different(target.syllables_list[i], production.syllables_list[0])
        i += 1
    matching (target, production, index, matching_list)
    return matching_list


#total_list :[[(w1s1,w1s1),(w1s2,w1s2)],[(w2s1,w2s1),(w2s2,w2s2)]]
def matching(target:Word, production:Word, index: int, total_list: list) ->None:
    temp_list = []
    for i in range (0, index):
        part = (str(target.syllables_list[i]), None)
        total_list.append(part)
    for i in range (production.get_syllables_num()):
        part = (str(target.syllables_list[i+index]), str(production.syllables_list[i]))
        total_list.append(part)
    for i in range (index+production.get_syllables_num(), target.get_syllables_num()):
        part = (str(target.syllables_list[i]), None)
        total_list.append(part)

def find_consonants_different(c1:str,c2:str)->int:
    total_score = 0
    characteristics = ['type','articulation_place','voicing']
    for c in characteristics:
        if ALPHA_BET[c1][c] != ALPHA_BET[c2][c]:
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
        return total_score
    # production length <= target length
    elif len (s1) != len(s2):
        total_score += 1
    for i in range(len(s2)):
        total_score += find_consonants_different(s1[i], s2[i])
    return total_score


def find_different (s1:Syllable, s2:Syllable)-> int:
    onset_diff = find_cluster_different(s1.syllable_parts['onset'], s2.syllable_parts['onset'])
    rhyme_diff = find_vowel_different(s1.syllable_parts['rhyme'], s2.syllable_parts['rhyme'])
    coda_diff = find_cluster_different(s1.syllable_parts['coda'], s2.syllable_parts['coda'])
    return  (onset_diff+rhyme_diff+coda_diff)