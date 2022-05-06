

request = {
    'question_num': '10'
}

try:
    count = int(request['question_num'])
    print(count)
    print(type(count))
except ValueError:
    print('Невозможно привести к int')
