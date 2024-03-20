from lxml import etree
from pathlib import Path
from typing import List


def read_corpus(dir_path: Path) -> List[Path]:
    """globs corpus xml files in given directory and outputs a list with corresponding file paths"""
    return [file_path for file_path in dir_path.glob("*.xml")]


def return_text(file_list: List[Path]) -> List[str]:
    """takes a list of xml files and outputs a list of their content as a string"""
    generate_str_list = etree.XPath("//text()")  # xpath expression is compiled for multiple application
    return [parse_xml(file_path, generate_str_list) for file_path in file_list]


def parse_xml(file_path: Path, xpath_expression: etree.XPath) -> str:
    """parses a given xml file and outputs corresponding text content as a string by applying given XPath expression"""
    with open(file_path, 'r') as xml_file:
        root = etree.parse(xml_file)  # encoding is decided by built-in parser, default is utf-8.
        text = xpath_expression(root)
    # depending on XPath pattern used, some cases can be expected:
    if type(text) == str:
        return text
    elif type(text) == list:
        return flatten_str_list(text)
    else:
        print(f"attention, encountered unexpected data types in conversion: output of type {type(text)}.")
        return text


def flatten_str_list(text_list: List[str]) -> str:
    """flattens a list of strings to a single string"""
    return " ".join(text_list)


def main() -> List[str]:
    """returns list of strings for use in workflow"""
    dir_path = Path(input("path to corpus files:  "))
    file_list = read_corpus(dir_path)
    text = return_text(file_list)
    return text


if __name__ == "__main__":
    main()
