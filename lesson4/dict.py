#Словарь

author = {
    'name': 'Kirill',
    'age': 35,
}

print(author['name'])
print(author.get("surname", 'Zavyalov'))

author['age'] = 24
author['is_mentor'] = False
author.pop("name")

print(author)

autor = {
    'name': 'Kirill',
    'age': 35,
    'is_mentor': False
}

for pair in author:
    print(pair)

for k,v in author.items():
    print(k,v)


user = {
    'name': 'Kirill',
    'age':24,
    'surname':'Zavyalov',
    'is_programmer': True,
    'city': "Ridder",
}

print(user['name'])
print(user.get('surname'))
user['city'] = "Ridder1"
user['learning_python'] = True
user.pop("city")

for k,v in user.items():
    print(f"Ключ {k}: Значение {v}")
