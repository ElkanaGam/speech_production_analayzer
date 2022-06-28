import json


with open ('phonemes.json') as f:
    data = json.load(f)
    ALPHABET = data['ALPHABET']

def is_vowel(c):
    return  ALPHABET[c]['class'] == 'vowel'

def not_vowel(c):
    return  ALPHABET[c]['class'] == 'consonants'




class Syllable:

    def __init__(self, word_part, position) -> None:
        self.parts = ['onset',  'rhyme','coda']
        self.syllable_parts = self.craeate_syllable(word_part) 
        self.position = position
        self.is_cluster = len(self.syllable_parts['onset']) > 1 
        self.is_open = len(self.syllable_parts['coda']) == 0
        self.has_onset = len(self.syllable_parts['onset']) > 0 


    def craeate_syllable(self,word_part):
        syllable_parts = {'onset':'', "rheyme":'', "coda":''}
        i  = 0
        j = 0
        while not_vowel(word_part[i]):
            i += 1
        j = i
        while j < len(word_part) and is_vowel(word_part[j]):
            j += 1
        syllable_parts['onset'] = word_part[0:i]
        syllable_parts['rhyme'] = word_part[i:j]
        syllable_parts['coda'] = word_part[j:]
        
        return syllable_parts

    def __repr__(self) -> str:
        return ''.join([self.syllable_parts[p] for p in self.parts]) 
        
        





   


if __name__ == "__main__":
    # s = Syllable ('bik', 1)
    # print(s)
    # for p in s.parts:
    #     print(s.syllable_parts[p])


    l = [[[]],[]],[],[[[],[]]]

    f= []
    # shalow_copy(l, 0,f)
    costume_copy(l,[0],f)
    print(f)