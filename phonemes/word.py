from . syllable import Syllable

class Word:
	def __init__(self, word:str) -> None:
		self.word = word.replace('sh', 'S').replace('ts', '&')
		self.syllables_list = self.slice_syllable()
   
   
	def get_syllables_num(self):
		vowels = {'a','e', 'i', 'o', 'u'}
		cnt = 0
		for v in vowels:
			cnt += self.word.count(v)
		return cnt
	
	def __len__ (self):
		return len(self.word)

   
	def slice_syllable(self):
		# pre_ussumeption!
		syllables = []
		num_of_syllables = self.get_syllables_num()
		word = self.word
		position  = 1
		left = 0
		rhyme_end = 0
		cursor = 0
		while cursor < len(word):
			while word[cursor] not in {'a','e', 'i', 'o', 'u'}:
				cursor += 1
			onset_end = cursor
			rhyme_start = cursor
			if word[cursor] in {'a','e', 'i', 'o', 'u'}:
				cursor += 1
			
			rhyme_end = cursor
			while (cursor < len(word) and word[cursor] not in {'a','e', 'i', 'o', 'u'}):
				cursor += 1
				# consider /maSpri&/ (=mashprits), so this break statment
				# allow only one con in the coda
				
			# coda is empty
			if cursor == rhyme_end:
				coda = cursor
			elif cursor == rhyme_end +1:
				coda = rhyme_end
			# tow vowels in a row
			else:
				coda = cursor -1
			if position == num_of_syllables:
				coda = len(word)
			
			syllables.append(Syllable(self.word[left:coda], position))
			left = coda
			position += 1
			cursor = left
		return syllables

	def __str__(self):
		data = [str(e) for e in self.syllables_list ]
		return '.'.join(data)

def _match_syllabe(targert, production):
	'''banana ->nana
		get data from the find_dif function
		mechanism: do match from the first syll not omited!
		helper do_match()
	'''

def _find_diff():
	'''
	get data from con_dif, vowel_diff
	'''
			
if __name__ == '__main__':
	words_pool = [Word(w) for w in ['masaijot', 'bakbuk','maftaex','jad', 'balon', 'shaon','mashprits']]
	for w in words_pool:
		print(w)