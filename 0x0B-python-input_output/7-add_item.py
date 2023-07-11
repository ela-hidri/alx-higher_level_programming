#!/usr/bin/python3
"""
adds all arguments to a Python list
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import os.path
path = '/usr/local/bin/'

old = []
l = []
if (os.path.isfile("add_item.json")): 
    old = load_from_json_file("add_item.json")
for n in old:
    l.append(n)
for i in range(1, len(argv)):
    l.append(argv[i]);
save_to_json_file(l, "add_item.json")
