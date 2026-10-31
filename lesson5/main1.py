#Множество - неупорядоченная изменяемая структура данных. Выводится через print рандомно. Перезаписывает дубликаты. Нет дубликатов


numbers = {101, 102, 103, 104, 105, 106, 107, 108, 109, 101}
tuple_numbers = tuple(numbers)
print(tuple_numbers)
print(numbers)

languages = ['english', 'french', 'russian', 'french']
print(languages)

print(set(languages))
set_language = set(languages)

languages.remove('english')
languages.remove('french')
print(languages)

set_language.remove('english')
set_language.remove('french')
print(set_language)