#!/usr/bin/python3
'''
Module add_item
script that adds all arguments to a Python list
'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:   # load the objects
    list_args = load_from_json_file(filename)
except Exception as error:
    list_args = []

new_args = [arg for arg in sys.argv]   # add elements to the list from args

new_args.remove(sys.argv[0])   # remove first element, the program

list_args.extend(new_args)   # join the lists

save_to_json_file(list_args, filename)   # save to json
