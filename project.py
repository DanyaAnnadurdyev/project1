import json

with open('operations.json', 'r', encoding='utf-8') as file:
    operation_list = json.load(file)

operation_list = list(operation_list)

sorted_operation_list = sorted(operation_list, key=lambda d: d['date'])

last_operations = sorted_operation_list[-5:]

# for i in last_operations:
#     s = ', '.join(f'i{w}{n}: {i[w][n]}' for w in i for n in i[w])
#     print(s)
for i in last_operations:
    date = i['date'][:10].split('-')
    date = '.'.join(date[::-1])
    # print(date)

    description = i['description']
    # print(description)

    try:
        from_ = i['from'].split(' ')
        if len(from_) == 3:
            from_ = ' '.join(from_[0:1])
        else:
            from_ = from_[0]

    except KeyError:
        from_ = 'наличные'

    try:
        num = i['from'].split(' ')
        num = num[-1]
        if len(num) == 20:
            num = list(num)
            num[0:16] = ['*' * 16]
            num = ''.join(num)
        else:
            num = list(num)
            num[6:12] = ['*' * 6]
            num = ''.join(num)
            num = ' '.join(num[i:i + 4] for i in range(0, len(num), 4))
    except KeyError:
        num = ''
    # print(num)

    to_ = i['to'].split(' ')
    if len(from_) == 3:
        to_ = ' '.join(to_[0:1])
    else:
        to_ = to_[0]
    # print(to_)

    try:
        num2 = i['to'].split(' ')
        num2 = num2[-1]
        if len(num2) == 20:
            num2 = list(num2)
            num2[0:16] = ['*' * 16]
            num2 = ''.join(num2)
        else:
            num2 = list(num2)
            num2[6:12] = ['*' * 6]
            num2 = ''.join(num2)
            num2 = ' '.join(num2[i:i + 4] for i in range(0, len(num2), 4))
    except KeyError:
        num2 = ''

    amount = i['operationAmount']['amount']
    # print(amount)

    currency = i['operationAmount']['currency']['name']
    # print(currency)

    print(date, description, '\n', from_, num, '->', to_, num2, '\n', amount, currency)



# for i in last_operations:
#     print(i)
