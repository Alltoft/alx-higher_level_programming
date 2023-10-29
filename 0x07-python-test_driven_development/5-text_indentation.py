#!/usr/bin/python3
"""a function that prints a text with
2 new lines after each of these characters: ., ? and :
text must be a string, otherwise raise a TypeError
There should be no space at the beginning or at the end of
 each printed line"""


def text_indentation(text):
    """def text_indentation(text): prints a text with
    2 new lines after each of these characters: ., ? and :
    text must be a string
    There should be no space at the beginning or
    at the end of each printed line"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print("{}\n".format(text[i]))
        elif text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue
        else:
            print("{}".format(text[i]), end="")
