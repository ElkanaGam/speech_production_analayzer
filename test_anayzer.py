import pandas as pd
from phonemes import analayse_consonants


WORDS_FOR_TEST = [[("Sul", "tul"),("xan", 'xan')], [("So","to"),("ko","ko"),("lad","lad")],[("o", "o"),("to","to"),("bus", "bus")],
                 [("o", "o"), ("fa", "fa"), ("no", "no"),("a", "a")], [("i","i"), ("ne", "ne")]]   


def _test_consonants_analisis():
    print('START TESTIN ANALYZER....\n')
    outcomes = pd.read_csv('./test_outcomes.csv', index_col=False)
    print('Data was imporeted')
    print(outcomes.head())
    print('ANALYZING')
    analayse_consonants.check_words(WORDS_FOR_TEST)
    print(analayse_consonants.df)






_test_consonants_analisis()
