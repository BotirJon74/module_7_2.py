import io
from pprint import pprint

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    i = 1
    for string in strings:
        string_positions[i, file.tell()] = string
        file.write(string+'\n')
        i += 1
    file.close()
    return string_positions

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



