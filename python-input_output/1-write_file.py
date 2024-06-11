#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """The write_file function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
