#!/usr/bin/python3
"""
adds all arguments to a Python list
"""
import os.path
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
path = '/usr/local/bin/'

li = []
old = []
if (os.path.isfile("add_item.json")):
    old = load_from_json_file("add_item.json")
for n in old:
    li.append(n)
for i in range(1, len(argv)):
    li.append(argv[i])
save_to_json_file(li, "add_item.json")
