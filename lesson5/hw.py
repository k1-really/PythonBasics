student = ('Kirill', 24, 'python')

name, age, language = student

print(name)
print(age)
print(language)

words = ['python', 'code', 'list', 'python', 'set', 'code']

print(words)

print(len(set(words)))

for word in words:
    if word == 'tuple':
        print(True)

words.append('loop')

words.remove('list')

print(words)



