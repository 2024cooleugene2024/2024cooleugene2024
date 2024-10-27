def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as f:
        for line_number, line in enumerate(strings, start=1):
            byte_position = f.tell()
            f.write(line + '\n')
            strings_positions[(line_number, byte_position)] = line
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
