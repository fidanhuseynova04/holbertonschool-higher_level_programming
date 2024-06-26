#!/usr/bin/python3
"""Module for adding arguments to a Python list"""
import json
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    loads = load_from_json_file("add_item.json")
except Exception:
    loads = []

save_to_json_file(loads + sys.argv[1:], "add_item.json")
