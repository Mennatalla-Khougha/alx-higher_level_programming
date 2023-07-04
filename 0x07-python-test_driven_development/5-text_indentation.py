#!/usr/bin/python3
"""
This Module print a text with some modifications
"""


def text_indentation(text):
    """This function prints a text with some modifications

    Args:
        text (str): the text to be indented

    Raises:
        TypeError: when text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
