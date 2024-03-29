#!/usr/bin/python3
'''
Module add_item
script that adds all arguments to a Python list
'''
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

# open file
try:
    list_args = load_from_json_file("add_item.json")
except Exception:
    list_args = []

# add args to the lists
list_args += sys.argv[1:]

# save to the file
save_to_json_file(list_args, "add_item.json")
