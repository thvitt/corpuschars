import inspect
import numpy as np
import pandas as pd
from collections import defaultdict
import os
def write_file_list(liste):
    """
    :param liste:List der Dateinamen im Arbeitsverzeichnis der Werke
    :return: Nichts
    """
    filelist = open("dateinamen.txt","a")
    for x in liste:
        filelist.write(x+"\n")
    filelist.close()

os.chdir(r"C:\users\Eickelpasch\documents\corpuschars\Romane_test")
files=os.listdir()
print(files)
#ich schreibe erst diese Liste, um später die gleiche Reihenfolge und
# Existenz der files sicherstellen zu können


write_file_list(files)
anzahl_files = len(files)
print("es gibt "+ str(anzahl_files) + " Dateien")
#for i in range(anzahl_files):
#    with open(files[i]) as werk:
with open(files[1]) as werk:
        text=werk.read()
        print('Textlänge in Zeichen = ',len(text) )
        #print('der Inhalt Nr.',i,' ist : ', text )
        chars = defaultdict(int)

        for char in text:
            chars[char] += 1
            char_table = pd.DataFrame.from_dict(chars, orient= 'index')
#, orient= 'index', columns=['character', 'char_count'])
#char_table.columns = ['character', 'char_count']
print(chars)
char_table = char_table._rename(columns={0: 'count'})
char_table.index.name= 'character'
char_table.sort_values(by='count', kind = 'mergesort', ascending=True, inplace=True)
print(char_table.head (n=20))
#print(char_table.columns)
#print(char_table['a'])
#char_table.info()
