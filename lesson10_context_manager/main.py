#Context manager

file = open("data.txt", "r")
try:
    print(file.read())
finally:
    file.close()

with open("data.txt", "r") as file: #Делает то же самое. Закрывает файл после чтения
    print(file.read())

class FileOpener:
    def __init__(self, file_name:str, mode:str):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileOpener('data.txt', "r") as file:
    print(file.read())