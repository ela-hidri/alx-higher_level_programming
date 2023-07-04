#!/usr/bin/python3
# 5-text_indentation
"""
Defines a function that prints paragraph

Attributes:
    text_indentation: prints paragraph with requirements
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text: text of type string

    Raise:
    TypeValue: if text not string

    Returns: nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in ".:?":
        text = (i + "\n\n").join(
                [line.strip(" ") for line in text.split(i)])
    print(text, end="")
