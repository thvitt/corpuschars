from collections import Counter
from collections.abc import Iterable
from pathlib import Path

import pandas as pd


def analyze_text(text: str) -> Counter:
    return Counter(text)

def analyze_file(file: Path) -> Counter:
    return analyze_text(file.read_text(encoding='utf-8'))

def analyze_files(corpusfiles: Iterable[Path]) -> pd.DataFrame:
    analyzed_data = {}   # { file : Counter({char : count})}
    for file in corpusfiles:
        analyzed_data[file.stem] = analyze_file(file)
    char_matrix = pd.DataFrame(analyzed_data)

    char_matrix.fillna(0,inplace=True)
    char_matrix['Summe'] = char_matrix.sum(axis=1)
    charmatrix_sorted = char_matrix.sort_values(by='Summe', ascending=True)
    return charmatrix_sorted

def main():
    matrix = analyze_files(Path('/home/tv/git/corpuschars/tests/data/mini').glob('*.txt'))
    print(matrix)

if __name__ == "__main__":
    main()