from collections import Counter
#from collections import OrderedDict
import timeit

#from time  import Timer

import pandas as pd
from pathlib import Path
import glob
#defaultdict wuerd ersetzt
import numpy as np
import sys
import pprint


corpus_dir_name = 'Romane2'
projekt_pfad = 'C:\\users\\Eickelpasch\\Documents\\corpuschars'
corpus_pfad = projekt_pfad + '\\' + corpus_dir_name
#print (corpus_pfad)
cp = Path(corpus_pfad)
print (cp)
t_start = timeit.default_timer()

corpusfiles = list(cp.glob("*.txt")) #  gab immer den gesamten pfad zurueck
def erzeuge_liste_corpusflenames (corpusfiles):
    """
    erzeuge eine liste mit den corpusfile names
    :param corpusfiles:
    :return: corpusfilename: liste mit den corpusfile names.
    """
    corpusfilename = []
    for i in range(len(corpusfiles)):
        corpusfilename.append(Path(corpusfiles[i]).name)
    return corpusfilename
corpusfilenames = erzeuge_liste_corpusflenames(corpusfiles)
print (corpusfilenames)
char_matrix = pd.DataFrame()
for j in range(len(corpusfiles)):
    cp_file  = Path(corpusfiles[j])
    text = cp_file.read_text("locale")
   # text = cp_file.read_text(encoding = "UTF-8")
    '''
    "locale" sthet für das encoding- defautl ist wohl utf-8 , das einen Fehler erzeugte
    aber auch fand ich in 'Hauff,-Wilhelm_Die Bettlerin vom Pont des Arts.txt' die
    gleiche Fehlermeldung. Genauer wurde gemeldet
    File "C:\Users\Eickelpasch\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 815560: character maps to <undefined>
Eine Position 815560 gibt es aber nicht ( 231 220 ist die letze laut notepad++ und
0x81 wird in notepad++ nicht gefunden.
    '''
    cnt = Counter()
    for character in text:
        cnt[character] += 1
    if j == 0 :
        char_matrix = pd.DataFrame.from_dict(cnt, orient= 'index',columns = [0])
        print (char_matrix)
    else:
        char_matrix_r = pd.DataFrame.from_dict(cnt, orient= 'index',columns = [j])
        char_matrix = char_matrix.join(char_matrix_r,on=None,how='outer')

char_matrix.fillna(0,inplace=True)
char_matrix['Summe'] = char_matrix.sum(axis=1)
charmatrix_sorted = char_matrix.sort_values(by='Summe', ascending=True)
t_stop = timeit.default_timer()
print (charmatrix_sorted.shape)
print ("Gesamtlaufzeit = " + str(t_stop - t_start))
#print (cnt)