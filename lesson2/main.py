#Строки
message = input("Enter a message: ")

message = message.strip()

if len(message) < 1:
    print("Message is empty")
elif "spam" in message:
    print("Blocked")

s = input("Enter a string: ")
i = int(input("Enter an integer: "))

if len(s) < i and s[i] == "a":
    print(s[i])

full_name = input("Enter a full name: ")
full_name = full_name.strip()

full_name = full_name.capitalize()
print(full_name[1])
print(full_name[-1])