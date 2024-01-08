#import random
#import json
import os
from os import path
import re
#import math
#import operator
from collections import Counter
from collections import OrderedDict
# from datetime import datetime
from timeit import default_timer as timer
import pandas as pd
from collections import defaultdict
import numpy as np
#from sklearn.feature_extraction.text import CountVectorizer

#import s_e
# s_e unresolved - warum
# muss ich das Paket nicht einbinden - wie findet er dann z.B. write_filelist?
# hier nochmal eingefügt

def write_file_list(liste):
    """
    :param liste:List der Dateinamen im Arbeitsverzeichnis der Werke
    :return: Nichts
    """
    filelist = open("dateinamen.txt","a")
    for x in liste:
        filelist.write(x+"\n")
    filelist.close()
def write_file_list(liste, datei_liste_mit_id=None):
    """schreibt zunächst die Korpus-Dateien (aus einem Verzeichnis) in eine Datei.
    Sie enthält die bis dahin ausgewerteten Dateien in der Verabeitungsreihenfolge
    und erzeugt das dictionary datei_liste_mit_id

    :param liste:Liste der Dateinamen im Arbeitsverzeichnis des Korpus
    datei_liste_mit_id: eine Liste die neben dem Namen der Datei auch die ID als Nummer enthält
    :return: dictionary mit ID-NR und value : Wort
    """

    os.chdir(r"..\result")

    #geht das ? und muss ich das wieder rückgängig machen?
    filelist = open("aa_dateinamen.txt", "a")
    filenumber = 0
    if datei_liste_mit_id is None:
        datei_liste_mit_id={}
    for x in liste:
        filelist.write(str(filenumber) + "," + x + "\n")
        datei_liste_mit_id[filenumber]=x
# Das folgende muss noch als Parameter allgemeingültig verfügbar gemacht werden
os.chdir(r"/Romane")
files=os.listdir()
#print(files)
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
