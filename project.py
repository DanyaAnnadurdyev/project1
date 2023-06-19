import json

with open('operations.json', 'r', encoding='utf-8') as file:
    operation_list = json.load(file)

operation_list = list(operation_list)

sorted_operation_list = sorted(operation_list, key=lambda d: d['date'])

last_operations = sorted_operation_list[-5:]

for i in last_operations:
    print(i)