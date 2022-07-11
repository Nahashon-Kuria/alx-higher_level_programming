#!/usr/bin/python3
# 6-from_json_string.py
# Nahashon M. Kuria <http://linkedin.com/in/nahashon-kuria-m>
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
