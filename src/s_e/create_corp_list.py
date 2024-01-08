import inspect
import sys

import numpy as np
import pandas as pd
from collections import defaultdict
import os
import time
start_time = time.perf_counter()
def create_corpus_liste():
    os.chdir(r"C:\users\Eickelpasch\documents\corpuschars\Romane_test")
    corpus = []
    for filename in os.listdir():
        #with open(filename, 'r') as f:
            corpus.append(filename)
    return corpus
def write_file_list(liste):
    """
    :param liste:List der Dateinamen im Arbeitsverzeichnis der Werke
    :return: Nichts
    """
    filelist = open("dateinamen.txt","a")
    for x in liste:
        filelist.write(x+"\n")
    filelist.close()

files = create_corpus_liste()
write_file_list(files)
print(files)
print (sys.path)
end_time = time.perf_counter()
total_time = end_time - start_time

print(f'Total execution time: {total_time} seconds')