#Обработка исключений:

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")


try:
    number = int(input("Enter a number: "))
    print(10/ number)
except Exception as error:
    print("Division by zero", error)
else:
    print("There is no error")
finally:
    print("This text prints everytime")

age = int(input("Enter a name: "))
if age < 0:
    raise ValueError("Random error")


