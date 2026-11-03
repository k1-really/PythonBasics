#Функции
import math


def draw_symbol(text, count): # Переменная в функции - совершенно другая что за функцией.
    print(" ".join(text.split(" ") * count))

draw_symbol('Hello', 3)
draw_symbol('Python', 3)
draw_symbol('Python', 10)
print('*' * 5)
print('$' * 10)
print('!' * 5)

def print_ticket(name, film):
    print(f"Билет для {name} для фильма {film}")

print_ticket('Kirill', 'One Piece')

def print_alex():
    birth_year = 34
    print('Alex the great is ', birth_year)
    print(f"Локальная область видимости print_alex(): {locals()}")

print_alex()

king = "Alexander"

def print_birth():
    print(f"King {king}'s birthday is 1992")

print_birth()

def draw_line(symbol, count = 10):
    print(" ".join(symbol.split() * count))

draw_line("Python")
draw_line("Python", 10)
draw_line("Python", 20)

def make_circle(x,y,radius, line_width, fill_color):
    pass
    circumference = 2 * math.pi * radius

make_circle(x=200, y=200, radius = 200, line_width=2.5, fill_color="red") # удобный подход, когда нужно указать много параметров


def get_sum(*args):
    print(args)
    print(set(args))
    print(sum(args))

print(get_sum(1,2))
print(get_sum(1,2,2,4,5))


def calculate_total(price, quantity, has_discount: bool) -> int: #Указываем то, что возвращаем
    total = price * quantity
    if has_discount:
        total -= 10
    return total

total = calculate_total(price = 100, quantity = 2, has_discount = True)
print(total)

name: str = "Kirill"

print(name)

