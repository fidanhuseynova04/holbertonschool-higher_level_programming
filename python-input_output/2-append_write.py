#!/usr/bin/python3
"""Module containing append_file function"""


def append_write(filename="", text=""):
    """The append_file function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
