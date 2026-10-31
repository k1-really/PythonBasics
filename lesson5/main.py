#Кортеж, множество
#Кортеж - аналог списков, но неизменяемый. Задается просто почти как список, только вместо [] - (). Круглые скобки
# Кортеж весит меньше чем список
my_list = ['Kirill', 'Anton', 'Max']

my_tuple = ('Kirill', 'Anton', 'Max')

s = ("list", ) # - строка. Нельзя один элемент сделать кортежем. Будет строкой обычной. Чтобы был кортеж, нужно поставить: ,

print(s)
my_list.append("Kirill")
my_list[0] = 'Dima'
print(my_list)


print(my_tuple)

ALLOWED_IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".gif")

for extension in ALLOWED_IMAGE_EXTENSIONS:


