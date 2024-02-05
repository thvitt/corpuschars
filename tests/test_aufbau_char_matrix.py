from collections import Counter
from pathlib import Path

import pytest

from s_e.aufbau_char_matrix_o import analyze_text, analyze_files


def test_analyze_text():
    output = analyze_text("Das ist ein Test")
    expected = Counter("Das ist ein Test")
    assert output == expected
def test_analyze_text_0():
    output = analyze_text("Otto")
    expected = Counter({"O": 1, "t": 2, "o": 1})
    assert output == expected

def test_analyze_text_1():
    assert analyze_text("") == {}

@pytest.mark.xfail(reason="Not implemented yet")
def test_analyze_text_2():
    emoticon = "\U0001FAF4\U0001F3FF"
    print(emoticon)
    table = analyze_text(emoticon)
    assert len(table) == 1, "emoji should count as one"

@pytest.fixture()
def data_folder():
    return Path(__file__).parent / 'data'

def test_analyze_files(data_folder):
    files = data_folder.joinpath("mini").glob("*.txt")
    result = analyze_files(files)
    assert len(result.index) > 3
    assert len(result.columns) == 3

def test_analyze_many_files(data_folder):
    path = data_folder.joinpath("romane/romane_1")
    print(path)
    files = path.glob("*.txt")
    assert files
    print('Fileliste:', files)
    result = analyze_files(files)
    assert len(result.index) > 3
    assert len(result.columns) == 27    #76
