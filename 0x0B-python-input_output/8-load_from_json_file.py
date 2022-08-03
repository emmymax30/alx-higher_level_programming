#!/usr/bin/python3
"""load json object from file"""
import json


def load_from_json_file(filename):
    """load json object from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
