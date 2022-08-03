#!/usr/bin/python3
"""Converts an obj class to dict"""


def class_to_json(obj):
    """Converts an obj class to dict"""
    return obj.__dict__
