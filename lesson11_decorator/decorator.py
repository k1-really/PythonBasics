#decorator

import time

def decorator_timer(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Начало исполнения")
        result = func(*args, **kwargs)
        end = time.time()
        print("Конец исполнения")
        print(f"Время исполнения: {end - now}")
        return result
    return wrapper

@decorator_timer
def load_file(seconds):
    print("Загружаю какой то файл")
    time.sleep(seconds)

@decorator_timer
def multiply(a, b):
    print("Вычисляю умножаю")
    time.sleep(1)
    return a * b

load_file(2)
print(multiply(2, 3))

