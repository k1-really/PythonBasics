#Инкапсуляция

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount >0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

bank = BankAccount(1000)

print(bank.get_balance())

#Полиморфизм

#Наследование
class Developer:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary


