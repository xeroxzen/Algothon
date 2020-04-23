from datetime import datetime

username = input("Enter your name: ")
current_age = int(input("Enter your age: "))

# age_difference = 100 - current_age
birthday = datetime.now().year - current_age
centenary = birthday + 100 - 1

print("You will be 100 in", centenary)
# print("Your name is", username," and you are", age)