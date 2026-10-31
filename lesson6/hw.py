def get_square(number):
    return number * number

square = get_square(5)

def check_age(age):
    if age < 12:
        result = "Ребенок"
    elif age < 18:
        result = "Подросток"
    else:
        result = "Взрослый"
    return result

print(check_age(18))


city = 'Moscow'

def show_city():
    city = "London"
    print(city)
show_city()
print(city)
