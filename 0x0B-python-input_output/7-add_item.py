#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then save them to a file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = []
prev_list = ""

prev_list = load_from_json_file("add_item.json")
my_list.append(prev_list)

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")