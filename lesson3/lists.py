#Списки

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(max(numbers))
print(sum(numbers))

gods = ['Zeus', 'Apollo', 'Ares']

gods.insert(len(gods), 'Hermes')

gods.remove("Apollo")
last = gods.pop(len(gods) - 1)
print(last)
print(gods)

numbers = [4, 7, 10, 15, 18, 21, 24]
for n in numbers:
    print(n)

for i,n in enumerate(numbers):
    if n % 2 == 0:
        print(f'{n} is even and i is {i}')

count = 0

for n in numbers:
    if n > 10:
        count += 1
print(count)

text = input("Enter a string: ")

list = text.split()

result = "-".join(list)

print(result)

