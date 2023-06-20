import json

from utils.utils import string_format, get_from_file

operation_list = get_from_file('operations.json')

operation_list = list(operation_list)

sorted_operation_list = sorted(operation_list, key=lambda d: d['date'], reverse=True)

last_operations = sorted_operation_list[:5]

print(string_format(last_operations))