import pytest
from pathlib import Path
from lxml import etree
from corpuschars.parse_xml_corpus import read_corpus, return_text, parse_xml, flatten_str_list


@pytest.fixture
def return_xml_test_path():
    return Path("./data/xml_test")


def test_read_corpus(return_xml_test_path):
    output = read_corpus(return_xml_test_path)
    expected = [Path(return_xml_test_path / "dat_1.xml"),
                Path(return_xml_test_path / "dat_2.xml"),
                Path(return_xml_test_path / "dat_3.xml")]
    assert sorted(output) == sorted(expected)  # order of elements isn't relevant for this test


def test_return_text():
    pass  # testing functionality not yet implemented


@pytest.fixture
def return_xpath_pattern():
    return etree.XPath("//text()")


def test_parse_xml_0(return_xml_test_path, return_xpath_pattern):
    output = parse_xml(return_xml_test_path / "dat_1.xml", return_xpath_pattern)
    expected = "Hallo Welt!"
    assert output == expected


def test_parse_xml_1(return_xml_test_path, return_xpath_pattern):
    output = parse_xml(return_xml_test_path / "dat_2.xml", return_xpath_pattern)
    expected = "H A L L O Welt!"
    assert output == expected


def test_parse_xml_2(return_xml_test_path, return_xpath_pattern):
    output = parse_xml(return_xml_test_path / "dat_3.xml", return_xpath_pattern)
    expected = "Hallo! Welt!"
    assert output == expected


@pytest.fixture
def generate_test_list():
    return ["A", "", "B", "C", "D ", "."]


def test_flatten_str_list(generate_test_list):
    output = flatten_str_list(generate_test_list)
    expected = "A  B C D  ."
    assert output == expected
