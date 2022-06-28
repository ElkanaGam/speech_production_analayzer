from dataclasses import dataclass
import json 
from . word import Word





with open('./phonemes/phonemes.json', 'r') as f:
    data = json.load(f)
    ALPHA_BET = data['ALPHABET']

def _foo():
    return ALPHA_BET['b']['type']

def match_syllab(target, production):
    target = Word(target)
    production = Word (production)
    



#total_list :[[(w1s1,w1s1),(w1s2,w1s2)],[(w2s1,w2s1),(w2s2,w2s2)]]
def matching(target:Word, production:Word, index: int, total_list: list) ->None:
    temp_list = []
    for i in range (0, index):
        part = (target.syllables_list[i], None)
        total_list.append(part)
    for i in range (index, target.get_syllables_num):
        part = (target.syllables_list[i], production.syllables_list[i])
    
    for i in range (index, production.get_syllables_num):
        part = (target.syllables_list[i], production.syllables_list[i])
    
    for i in range (index+production.get_syllables_num, target.get_syllables_num):
        part = (target.syllables_list[i], None)

def find_consonants_different(c1:str,c2:str)->int:
    total_score = 0
    if ALPHA_BET[c1]['type'] != ALPHA_BET[c1]['type']:
        total_score += 1
