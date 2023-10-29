#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print("{}\n".format(text[i]))
        elif text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue
        else:
            print("{}".format(text[i]), end="")
