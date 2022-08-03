#!/usr/bin/python3
"""Saving arguments to a list"""
import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    ls = load_from_json_file("add_item.json")
except:
    ls = []

for i in sys.argv[1:]:
    ls.append(i)
save_to_json_file(ls, "add_item.json")
