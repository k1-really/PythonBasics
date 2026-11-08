#Инкапсуляция

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

bank = BankAccount(1000)

print(bank.get_balance())

#Полиморфизм
#Общий интерфейс в виде общего метода
class Developer1:
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def work(self):
        print(f"{self.name} is working")


class Designer1:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

#Наследование

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def work(self):
        print(f"{self.__name} is working")


class TesterQA(Employee):
    pass

tester = TesterQA("tester", 100)
tester.work()

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print(f"{self.__name} is working")


class Designer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def work(self):
        print(f"{self.__name} is working")


