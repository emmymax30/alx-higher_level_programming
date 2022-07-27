#!/usr/bin/python3
"""
   This module prints a text with 2 new lines after each of
   the following characters: '.', '?' and ':'.
   Raises exception if input is not a string
"""


def text_indentation(text):
    """
    text_indentation: indent text after these characters and print
    all text to standard output stream
    Argument:
        text (str): multiline string or single line string
    Raises:
         TypeError: raises error if text is not a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        for i in range(0, len(text)):
            # Ommit spaces after punctuation
            if text[i] == ' ' and (text[i-1] == '?' or text[i-1] == ':'
               or text[i-1] == '.'):
                continue
            print("{}".format(text[i]), end="")
            # Print 2 new line after punctuation
            if text[i] == '?' or text[i] == ':' or text[i] == '.':
                print("\n")
